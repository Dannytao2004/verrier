# Evidence ledger: fc_es_transit_2026_08

- Question: Assume today is 2026-09-11. You know nothing published after this date. Estimate the total number of passengers who used public transport in Spain in August 2026 (urban, interurban and special/discretionary transport combined), as it will be first reported in the provisional data of the National Statistics Institute's (INE) Passenger Transport Statistics (Estadística de Transporte de Personas).
- as_of: 2026-09-11
- Pinned target: Total number of passenger journeys reported by the Instituto Nacional de Estadística (INE) Passenger Transport Statistics (Estadística de Transporte de Personas) for Spain, summing urban, interurban and special/discretionary transport, as first published in the provisional release for August 2026. | unit passenger journeys (viajes de pasajeros) | period 2026-08-01..2026-08-31 | publisher Instituto Nacional de Estadística (INE), Spain

- Official value (scoring only, never shown to the agent): 371,623,271

## Directions and pages

### d1 [own_history] INE monthly statistical series

Hypothesis: The August 2026 ETP total will be close to the August 2025 total adjusted by the 2026 level/trend; the August month-of-year ratio and category mix are stable enough to project from prior Augusts and any 2026 months published before the cutoff.

Queries issued by the searcher: site:ine.es Estadística de Transporte de Personas agosto 2025 viajeros; INE transporte de personas serie mensual 2026 viajeros urbanos interurbanos; ine.es TV0825.pdf "Estadística de Transporte de Viajeros" agosto 2025 datos provisionales 362,4 millones; INEbase estadística transporte de viajeros tabla serie mensual 2021 2022 2023 2024 2025 2026 miles viajeros total nacional

- `https://www.ine.es/dyngs/Prensa/TV0726.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ine.es/dyngs/Prensa/en/TV0825.htm?print=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://apps.fomento.gob.es/BDOTLE/visorBDpop.aspx?i=2024` -> **snapshot** (snapshot 20250414132910); points raw/verified 0/0
- `https://www.ine.es/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176906&idp=1254735576820` -> **snapshot** (snapshot 20260908133509); points raw/verified 8/3
  - p1 Annual variation of total public transport users, Spain, June 2026 vs June 2025 = **2** as written "2,0", value check ok percent (2026-06-01..2026-06-30) [keep: ] quote: "El número de usuarios del transporte público aumentó un 2,0% en junio respecto al mismo mes de 2025."
  - p2 Annual variation of urban transport passengers, Spain, June 2026 vs June 2025 = **3.1** as written "3,1", value check ok percent (2026-06-01..2026-06-30) [keep: ] quote: "El transporte urbano subió un 3,1% en tasa anual y el interurbano cayo un 0,6%."
  - p3 Annual variation of special and discretionary transport passengers, Spain, June  = **3** as written "3,0", value check pending percent (2026-06-01..2026-06-30) [DISCARD: Duplicate of p10 (same June 2026 special/discretionary growth of 3.0%) from the same INE table.] quote: "\| Transporte especial y discrecional \| \| 46.143 \| 3,0 \|"
- dropped by code checks: 5 (scale word 'thousand' not supported by quote or table header: 4; value_as_written not in quote as a whole number: 1)

### d2 [related_series] mode and category decomposition

Hypothesis: The ETP total is the sum of urban, interurban and special/discretionary components, whose August seasonality and 2026 growth differ; component-level recent data can anchor the August 2026 total better than an aggregate trend.

Queries issued by the searcher: INE Estadística de Transporte de Personas viajeros urbanos interurbanos especiales agosto 2025; INE ETP tabla por medio de transporte viajeros 2026; Estadística de Transporte de Viajeros (TV) Julio 2026 datos provisionales INE; INE nota de prensa TV0626 junio 2026 transporte de viajeros millones

- `https://www.ine.es/dyngs/Prensa/TV0726.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ine.es/dyngs/Prensa/en/TV0825.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ine.es/jaxi/Tabla.htm?tpx=78959&L=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ine.es/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176906&idp=1254735576820` -> **snapshot** (snapshot 20260908133509); points raw/verified 11/7
  - p4 Total public transport passengers year-on-year growth, Spain, June 2026 = **2** as written "2,0%", value check pending % (2026-06-01..2026-06-30) [DISCARD: Headline duplicate of p1; same underlying INE release and no additional level value.] quote: "El número de usuarios del transporte público aumentó un 2,0% en junio respecto al mismo mes de 2025."
  - p5 Urban transport passengers year-on-year growth, Spain, June 2026 = **3.1** as written "3,1%", value check pending % (2026-06-01..2026-06-30) [DISCARD: Headline duplicate of p2; same underlying INE release.] quote: "El transporte urbano subió un 3,1% en tasa anual y el interurbano cayo un 0,6%."
  - p6 Interurban transport passengers year-on-year growth, Spain, June 2026 = **0.6** as written "0,6%", value check pending % (2026-06-01..2026-06-30) [DISCARD: Sign error: value is +0.6% but quote says interurban fell and p9 gives -0.6%.] quote: "El transporte urbano subió un 3,1% en tasa anual y el interurbano cayo un 0,6%."
  - p7 Total passengers year-on-year variation, Spain, June 2026 (table) = **2** as written "2,0", value check pending percent (2026-06-01..2026-06-30) [DISCARD: Duplicate of p1 (same June 2026 total ETP growth of 2.0%) from the same INE release.] quote: "\| Total \| \| 506.548 \| 2,0 \|"
  - p8 Urban transport passengers year-on-year variation, Spain, June 2026 (table) = **3.1** as written "3,1", value check pending percent (2026-06-01..2026-06-30) [DISCARD: Duplicate of p2 (same June 2026 urban transport growth of 3.1%) from the same INE release.] quote: "\| Transporte urbano \| \| 314.243 \| 3,1 \|"
  - p9 Interurban transport passengers year-on-year variation, Spain, June 2026 (table) = **-0.6** as written "-0,6", value check ok percent (2026-06-01..2026-06-30) [keep: ] quote: "\| Transporte interurbano \| \| 146.162 \| -0,6 \|"
  - p10 Special and discretionary transport passengers year-on-year variation, Spain, Ju = **3** as written "3,0", value check ok percent (2026-06-01..2026-06-30) [keep: ] quote: "\| Transporte especial y discrecional \| \| 46.143 \| 3,0 \|"
- dropped by code checks: 4 (scale word 'thousand' not supported by quote or table header: 4)

### d3 [related_series] large urban and commuter transport operators

Hypothesis: Monthly passenger counts from major Spanish operators (Metro Madrid, TMB Barcelona, EMT Madrid, Renfe Cercanías, FGC, Metro Bilbao, Valencia/Seville consortia) for August 2026 or July 2026, compared with August 2025, can serve as leading indicators for national urban/interurban ridership after scaling by their national ETP share.

Queries issued by the searcher: Estadística de Transporte de Personas INE viajeros julio 2026; Metro Madrid viajeros julio 2026; INE Estadística de Transporte de Personas agosto 2025 datos provisionales millones de pasajeros; "agosto 2025" INE transporte público viajeros "millones de pasajeros" urbano interurbano especial discrecional; ine.es dyngs Prensa TV0825 Estadística Transporte de Personas agosto 2025; Metro de Madrid viajeros agosto 2026 millones usuarios récord

- `https://www.ine.es/dyngs/Prensa/TV0726.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ine.es/dyngs/Prensa/TV0726.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736176906&idp=1254735576820&menu=ultiDatos&utm_source=chatgpt.com` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ine.es/dyngs/Prensa/en/TV0726.htm?print=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [related_series] tourism and visitor activity

Hypothesis: August public transport demand, especially interurban and urban services in tourist cities, is positively related to tourist overnight stays and airport arrivals; 2026 tourism growth versus 2025 can adjust the August seasonal projection.

Queries issued by the searcher: AENA pasajeros agosto 2026 estadística; INE pernoctaciones hoteleras julio 2026; INE Estadística de Transporte de Personas junio 2026 viajeros nota de prensa; Frontur llegadas turistas julio 2026 INE

- `https://ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736177015&idp=1254735576863` -> **snapshot** (snapshot 20260212165818); points raw/verified 12/11
  - p11 Spain hotel overnight stays year-on-year variation, December 2025 (percent over  = **2.89** as written "2,89", value check pending percent (2025-12-01..2025-12-31) [DISCARD: December 2025 hotel overnight growth, different season; duplicate of p12 and no August transfer without an uncollected s] quote: "\| Pernoctaciones \| \| 18.546.462 \| 2,89 \|"
  - p12 Spain hotel overnight stays year-on-year increase, December 2025 (headline) = **2.9** as written "2,9%", value check pending % (2025-12-01..2025-12-31) [DISCARD: Duplicate December 2025 hotel headline; not directly August passenger evidence.] quote: "Las pernoctaciones en establecimientos hoteleros aumentaron un 2,9% en diciembre respecto al mismo mes de 2024."
  - p13 Spain average hotel stay (estancia media, number of days), December 2025 = **2.67** as written "2,67", value check pending days (2025-12-01..2025-12-31) [DISCARD: December 2025 hotel average stay is outside the August target period and too far from August to calibrate seasonal trans] quote: "\| Estancia media (número de días) \| \| 2,67 \| -2,69 \|"
  - p14 Spain average hotel stay year-on-year variation, December 2025 = **-2.69** as written "-2,69", value check pending percent (2025-12-01..2025-12-31) [DISCARD: Variation of average hotel stay, not a passenger count or August conversion factor.] quote: "\| Estancia media (número de días) \| \| 2,67 \| -2,69 \|"
  - p15 Spain hotel occupancy rate by bed places (grado de ocupación por plaza), Decembe = **49.65** as written "49,65", value check pending percent (2025-12-01..2025-12-31) [DISCARD: December hotel occupancy level, different season; not used without an August tourism bridge.] quote: "\| Grado de ocupación por plaza (porcentaje) \| \| 49,65 \| 1,64 \|"
  - p16 Spain hotel occupancy rate by bed places year-on-year variation, December 2025 = **1.64** as written "1,64", value check pending percent (2025-12-01..2025-12-31) [DISCARD: Variation of December hotel occupancy; not passenger count.] quote: "\| Grado de ocupación por plaza (porcentaje) \| \| 49,65 \| 1,64 \|"
  - p17 Spain average hotel room rate (ADR, tarifa media por habitación ocupada), Decemb = **120** as written "120,31", value check pending euros per occupied room (2025-12-01..2025-12-31) [DISCARD: December hotel ADR level; not passenger count.] quote: "\| Tarifa media por habitación ocupada (euros) \| \| 120,31 \| 2,50 \|"
  - p18 Spain average hotel room rate year-on-year variation, December 2025 = **2.5** as written "2,50", value check pending percent (2025-12-01..2025-12-31) [DISCARD: December hotel ADR growth; not passenger count.] quote: "\| Tarifa media por habitación ocupada (euros) \| \| 120,31 \| 2,50 \|"
  - p19 Spain hotel price index (IPH) level, December 2025 = **151** as written "151,23", value check pending index (2025-12-01..2025-12-31) [DISCARD: December hotel price index; not passenger count.] quote: "\| Precios hoteleros (índice) \| \| 151,23 \| 4,20 \|"
  - p20 Spain hotel price index annual rate, December 2025 = **4.2** as written "4,2%", value check pending % (2025-12-01..2025-12-31) [DISCARD: December hotel price growth; not passenger count.] quote: "El Índice de Precios Hoteleros subió un 4,2% en tasa anual."
  - p21 Spain average hotel revenue per occupied room, December 2025 (headline) = **120** as written "120,3", value check pending euros per occupied room (2025-12-01..2025-12-31) [DISCARD: December hotel revenue per room; not passenger count.] quote: "Los hoteles facturaron 120,3 euros de media por habitación ocupada, un 2,5% más que el mismo mes del año anterior."
- `https://www.ine.es/dyngs/Prensa/es/TV0626.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.aena.es/doc/detalleprensa/260915-pmi-estadisticas-agosto.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ine.es/jaxiT3/Datos.htm?t=20239` -> **snapshot** (snapshot 20260331043326); points raw/verified 1/0
- dropped by code checks: 2 (number: ambiguous separators: '.' used as a thousands separator: 1; scale word 'thousand' not supported by quote or table header: 1)

### d5 [shocks] calendar, weather and policy effects

Hypothesis: August 2026 has a different weekday/weekend composition from August 2025 and may be affected by heat waves, strikes, fare subsidies or service changes; adjusting the historical August ratio for these factors reduces projection error.

Queries issued by the searcher: calendario laboral agosto 2026 España días festivos; Estadística de Transporte de Personas INE agosto 2026 viajeros; accidente Adamuz tren cuándo ocurrió enero 2026 cercanías afectación viajeros; abono transporte 2026 subvención Gobierno precio abonos Renfe Cercanías descuento

- `https://www.ine.es/dyngs/Prensa/TV0826.htm?print=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.eldiario.es/spin/calendario-agosto-2026-festivos-fechas-destacadas_1_13420134.html` -> **snapshot** (snapshot 20260908220023); points raw/verified 7/7
  - p22 Number of days in August 2026 = **31** days (2026-08-01..2026-08-31) [keep: ] quote: "Agosto de 2026 comenzará en sábado y terminará en lunes, con 31 jornadas repartidas a lo largo de cinco fines de semana completos."
  - p23 Number of complete weekends in August 2026 = **5** as written "cinco", value check pending weekends (2026-08-01..2026-08-31) [keep: ] quote: "con 31 jornadas repartidas a lo largo de cinco fines de semana completos"
  - p24 National public holiday in Spain in August 2026 (Asunción de la Virgen), day of  = **15** day of month (2026-08-15..2026-08-15) [keep: ] quote: "El sábado 15 de agosto será festivo en todo el país por la Asunción de la Virgen."
  - p25 Number of national-scope public holidays in August 2026 = **1** as written "única", value check pending national public holidays (2026-08-01..2026-08-31) [keep: ] quote: "La única celebración de alcance nacional caerá en sábado"
  - p26 Descenso Internacional del Sella 2026 route length (km) = **20** kilometres (2026-08-08..2026-08-08) [DISCARD: Local festival route length; no quantitative ridership relation.] quote: "El recorrido cubre unos 20 kilómetros entre Arriondas y Ribadesella"
  - p27 Year Descenso Internacional del Sella recognised as Fiesta de Interés Turístico  = **1,980** year (1980-01-01..1980-12-31) [DISCARD: Recognition year of a local festival; no ridership relation.] quote: "La cita está reconocida como Fiesta de Interés Turístico Internacional desde 1980."
  - p28 Year Día de Cantabria recognised as Fiesta de Interés Turístico Nacional = **1,972** year (1972-01-01..1972-12-31) [DISCARD: Recognition year of a local festival; no ridership relation.] quote: "La celebración de agosto cuenta con la declaración de Fiesta de Interés Turístico Nacional desde 1972."
- `https://www.eldebate.com/economia/20261009/tren-sigue-recuperarse-adamuz-numero-pasajeros-cae-46-agosto_467906.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.europapress.es/economia/laboral-00346/noticia-calendario-2026-cuando-son-proximos-festivos-puentes-mas-largos-20260107111353.html` -> **snapshot** (snapshot 20260304130345); points raw/verified 15/12
  - p29 National common public holidays in Spain, 2025 (count) = **9** as written "nueve", value check pending public holidays (2025-01-01..2025-12-31) [DISCARD: Annual count of national holidays in 2025 does not inform August 2026 passenger journeys.] quote: "El calendario laboral de 2026 incluye nueve festivos nacionales comunes en toda España, la misma cifra que en 2025."
  - p30 National public holiday falling in August 2026 (Assumption of the Virgin, Saturd = **15** day of month (public holiday) (2026-08-15..2026-08-15) [DISCARD: Duplicate of p24: same 15 August national holiday.] quote: "el sábado 15 de agosto (Asunción de la Virgen)"
  - p31 National public holiday falling in August 2026 listed among nationwide holidays  = **15** day of month (public holiday) (2026-08-15..2026-08-15) [DISCARD: Duplicate of p24: same 15 August national holiday.] quote: "En concreto, en 2026 serán fiesta en toda España el viernes 3 de abril (Viernes Santo), el viernes 1 de Mayo (Fiesta del Trabajo), el sábado 15 de agosto (Asunción de la Virgen)"
  - p32 Island-level public holiday in La Palma (Canary Islands), 5 August 2026 = **5** day of month (public holiday) (2026-08-05..2026-08-05) [DISCARD: Island-level holiday in La Palma; negligible national scope and no ridership coefficient.] quote: "el 5 de agosto, en La Palma"
  - p33 Length of Easter bridge in seven communities, 2026 (days) = **5** as written "cinco", value check pending days (2026-04-02..2026-04-06) [DISCARD: Easter bridge length, not an August 2026 calendar factor.] quote: "este puente será de cinco días, puesto que han decidido dar también como festivo el lunes de Pascua (6 de abril)"
  - p34 Length of Easter bridge in communities celebrating Holy Thursday, 2026 (days) = **4** as written "cuatro", value check pending days (2026-04-02..2026-04-05) [DISCARD: Easter bridge length, not an August 2026 calendar factor.] quote: "habrá un puente de cuatro días"
  - p35 Months to wait for next non-working day after 6 January in most communities, 202 = **2** as written "dos", value check pending months (2026-01-06..2026-03-01) [DISCARD: Months between holidays after January; not August.] quote: "en la mayoría de las comunidades, habrá que esperar al menos dos meses para volver a disfrutar de un día no laborable"
  - p36 National public holidays already passed as of article date, 2026 (count) = **2** as written "dos", value check pending public holidays (2026-01-01..2026-01-06) [DISCARD: Count of national holidays passed by early January; not August.] quote: "dos de estos días ya han pasado -el 1 de enero y el 6 de enero, Día de Reyes-"
  - p37 National public holiday in August 2026 (day of month, Assumption) = **15** day of month (public holiday) (2026-08-15..2026-08-15) [DISCARD: Duplicate of p24: same 15 August national holiday.] quote: "15 de agosto, 12 de octubre, 1 de noviembre (es domingo y pasa al 2 de noviembre), y 6 de diciembre (es domingo y pasa al 7 de diciembre), 8 de diciembre y 25 de diciembre."
  - p38 National public holiday in August 2026 listed for Madrid (day of month) = **15** day of month (public holiday) (2026-08-15..2026-08-15) [DISCARD: Duplicate of p24 for Madrid: same 15 August national holiday.] quote: "MADRID 2 de abril, 3 de abril, 1 de mayo, 2 de mayo, 15 de agosto, 12 de octubre"
  - p39 National public holiday in August 2026 listed for Catalonia (day of month) = **15** day of month (public holiday) (2026-08-15..2026-08-15) [DISCARD: Duplicate of p24 for Catalonia: same 15 August national holiday.] quote: "CATALUÑA 3 de abril, 6 de abril, 1 de mayo, 24 de junio, 15 de agosto, 11 de septiembre (Día Nacional de Cataluña)"
  - p40 National public holiday in August 2026 listed for Andalusia (day of month) = **15** day of month (public holiday) (2026-08-15..2026-08-15) [DISCARD: Duplicate of p24 for Andalusia: same 15 August national holiday.] quote: "ANDALUCÍA 28 de febrero (Día de Andalucía), 2 de abril, 3 de abril, 1 de mayo, 15 de agosto, 12 de octubre"
- dropped by code checks: 3 (period_end 2026-12-31 after as_of: 3)

### d6 [administrative] INE metadata and release calendar

Hypothesis: The exact ETP table definitions, mode coverage, and release calendar determine which series must be summed and which comparison periods are available before the cutoff; definitional errors can shift the total by several percent.

Queries issued by the searcher: INE Estadística de Transporte de Personas metodología urbano interurbano especial discrecional; INE calendario publicación Estadística Transporte de Personas 2026; INE "calendario de disponibilidad" estadísticas coyunturales 2026 transporte de personas septiembre; "Estadística de Transporte de Personas" agosto 2025 datos provisionales millones pasajeros

- `http://www.ine.es/daco/daco43/notatvir.pdf` -> **snapshot** (snapshot 20240901060449); points raw/verified 0/0
- `https://www.ine.es/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176906&menu=resultados&secc=1254736195091&idp=1254735576820` -> **snapshot** (snapshot 20230326055513); points raw/verified 6/1
  - p41 Latest data period available in INE Passenger Transport Statistics (ETP) results = **2,023** month (2023-01-01..2023-01-31) [DISCARD: Outdated 2023 snapshot; superseded by 2026 INE evidence.] quote: "Últimos datos Enero 2023 Publicado: 10/03/2023"
- `https://www.ine.es/dyngs/Prensa/TV0726.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ine.es/dyngs/IOE/en/fichaProg.htm?cid=1259946014145` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 5 (number: more than one number in value_as_written: 4; value_as_written not in quote as a whole number: 1)

### d7 [capacity_consumption] transport service supply and occupancy

Hypothesis: Passenger journeys equal provided service (vehicle-km, train-km, scheduled trips) multiplied by average occupancy; August 2026 service schedules and comparable occupancy rates can bound the national total if ridership history is unavailable.

Queries issued by the searcher: INE Estadística de Transporte de Personas viajeros agosto 2025 nota de prensa; EMT Madrid coches-kilómetros 2025 memoria anual viajeros; INE Estadística de Transporte de Viajeros julio 2026 datos provisionales viajeros millones; Renfe trenes-kilómetro 2025 memoria actividad millones de trenes km cercanías

- `https://www.ine.es/dyngs/Prensa/TV0726.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ine.es/dyngs/Prensa/TV0825.htm` -> **snapshot** (snapshot 20251216205557); points raw/verified 15/9
  - p42 Year-on-year change in total public transport passengers, Spain, August 2025 = **2.6** as written "2,6%", value check ok % (2025-08-01..2025-08-31) [keep: ] quote: "El número de usuarios del transporte público aumentó un 2,6% en agosto respecto al mismo mes de 2024."
  - p43 Year-on-year change in urban transport passengers, Spain, August 2025 = **4** as written "4,0%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte urbano subió un 4,0% en tasa anual y el interurbano cayó un 1,4%."
  - p44 Year-on-year change in interurban transport passengers, Spain, August 2025 = **1.4** as written "1,4%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Sign error: value is +1.4% but quote says interurban fell; p58 gives -1.4%.] quote: "El transporte urbano subió un 4,0% en tasa anual y el interurbano cayó un 1,4%."
  - p45 Year-on-year change in metro passengers, Spain, August 2025 = **3.2** as written "3,2%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte por metro aumentó un 3,2% en tasa anual y el transporte urbano por autobús aumentó un 4,5%."
  - p46 Year-on-year change in urban bus passengers, Spain, August 2025 = **4.5** as written "4,5%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte por metro aumentó un 3,2% en tasa anual y el transporte urbano por autobús aumentó un 4,5%."
  - p47 Year-on-year change in interurban bus passengers, Spain, August 2025 = **1.8** as written "1,8%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "Por tipo de transporte, por autobús creció un 1,8%, mientras que el aéreo cayó un 0,3%, el marítimo un 1,6%, y por ferrocarril un 5,9%."
  - p48 Year-on-year change in interurban rail passengers, Spain, August 2025 = **5.9** as written "5,9%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "Por tipo de transporte, por autobús creció un 1,8%, mientras que el aéreo cayó un 0,3%, el marítimo un 1,6%, y por ferrocarril un 5,9%."
  - p49 Year-on-year change in Valencia metro passengers, August 2025 = **16.8** as written "16,8%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte por metro aumentó en todas las ciudades que poseen este tipo de transporte respecto al mismo mes del año anterior, excepto en el de Valencia, en el que disminuyó un 16,8%."
  - p50 Year-on-year change in Palma metro passengers, August 2025 = **56** as written "56,0%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El metro de Palma presentó el mayor incremento, del 56,0%."
- `https://diario.madrid.es/blog/notas-de-prensa/512-millones-de-viajeros-en-bus-y-137-millones-de-viajes-en-bicimad-un-2025-historico-para-emt-madrid/` -> **snapshot** (snapshot 20260112231614); points raw/verified 15/3
  - p51 EMT Madrid bus passenger growth rate vs prior year, full year 2025 = **7.96** as written "7,96 %", value check pending % (2025-01-01..2025-12-31) [keep: ] quote: "lo que supone un incremento del 7,96 %"
  - p52 EMT Madrid zero-emission buses in fleet, 2025 = **462** buses (2025-01-01..2025-12-31) [DISCARD: Zero-emission bus count is fleet capacity, not realised passenger journeys.] quote: "la circulación diaria de los 462 autobuses cero emisiones con los que cuenta en su flota"
  - p53 EMT Madrid new driving staff hired, full year 2025 = **478** professionals (2025-01-01..2025-12-31) [DISCARD: New driver count is staffing input, not realised passenger journeys.] quote: "se contrataron 478 profesionales como nuevo personal de conducción"
- `https://www.viaempresa.cat/es/economia/metro-barcelona-cierra-julio-record-rompe-barrera-40-millones-usuarios_2240239_102.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 18 (scale word 'million' not supported by quote or table header: 6; number: ambiguous separators: '.' used as a thousands separator: 10; value_as_written not in quote as a whole number: 2)

### d8 [base_rates] population and per-capita mobility

Hypothesis: Annual public transport journeys per resident, multiplied by Spain population and an August seasonal share, provides an independent check on the level obtained from time-series projection.

Queries issued by the searcher: INE Estadística de Transporte de Personas viajeros 2025 agosto; población España 2026 INE estimaciones; Estadística Transporte de Viajeros 2025 datos anuales total viajeros millones INE 2026; "transporte público" España 2025 "millones de viajeros" balance anual récord; ine.es dyngs Prensa TV1225.pdf Estadística Transporte de Viajeros diciembre 2025 5.784 millones

- `https://www.ine.es/dyngs/Prensa/TV0825.pdf` -> **snapshot** (snapshot 20251221032913); points raw/verified 14/2
  - p54 Annual growth rate of total public transport passengers, Spain, August 2025 vs A = **2.6** as written "2,6%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Duplicate of p42 August 2025 total growth.] quote: "El número de usuarios del transporte público aumentó un 2,6% en agosto respecto al mismo mes de 2024."
  - p55 Annual growth rate of urban transport passengers, Spain, August 2025 vs August 2 = **4** as written "4,0%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Duplicate of p43 August 2025 urban growth.] quote: "El transporte urbano subió un 4,0% en tasa anual y el interurbano cayó un 1,4%."
- `https://www.ine.es/jaxi/Tabla.htm?tpx=78959&L=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.elindependiente.com/economia/2025/10/10/transporte-publico-espana-viajeros-agosto/` -> **snapshot** (snapshot 20251113205847); points raw/verified 15/6
  - p56 Year-on-year change in total public transport passengers in Spain, August = **2.6** as written "2,6%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Duplicate of p42 August 2025 total growth.] quote: "un incremento del 2,6% respecto al mismo mes de 2024"
  - p57 Year-on-year change in urban transport passengers in Spain, August = **4** % (2025-08-01..2025-08-31) [keep: ] quote: "el transporte urbano creció un 4% (hasta 222,8 millones)"
  - p58 Year-on-year change in interurban transport passengers in Spain, August = **1.4** as written "1,4%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "el interurbano descendió un 1,4% (117,8 millones)"
  - p59 Year-on-year change in special and discretionary transport passengers in Spain,  = **11.7** as written "11,7%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "con más de 21,6 millones de usuarios (11,7% de aumento)"
  - p60 Year-on-year change in rail transport passengers in Spain, August = **5.9** as written "5,9%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Rail growth sign conflicts with p48 and its own quote; unreliable.] quote: "El transporte ferroviario en su conjunto disminuyó un 5,9%."
  - p61 Year-on-year change in urban bus passengers in Spain, August = **4.5** as written "4,5%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Duplicate of p46 August 2025 urban bus growth.] quote: "el crecimiento del 4% se debió principalmente al aumento de usuarios en el autobús urbano (4,5%) y en el metro (3,2%)."
- `https://www.lasprovincias.es/economia/transporte-publico-supera-millones-viajeros-agosto-20251010091507-vi.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 21 (scale word 'million' not supported by quote or table header: 15; scale word 'thousand' not supported by quote or table header: 4; value_as_written not in quote as a whole number: 2)

### b1 [own_history] statistical table values rather than press headlines

Hypothesis: The kept ETP points are mostly growth rates; actual monthly passenger levels for August 2025 and June/July 2026 would replace the per-capita/seasonality assumptions and enable direct yoy_scaling or naive August series. This is the highest-value missing input because the current route must assume the level and August share.

Queries issued by the searcher: Estadística de Transporte de Personas INE viajeros agosto 2025; INE Estadística de Transporte de Personas junio 2026 viajeros urbanos interurbanos; INE Estadística de Transporte de Personas julio 2026 datos provisionales viajeros millones; "Transporte de Personas" INE julio 2026 508 millones viajeros transporte público

- `https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736176906&idp=1254735576820&menu=ultiDatos` -> **snapshot** (snapshot 20260616055709); points raw/verified 11/7
  - p62 Total public transport users year-on-year growth, Spain, April 2026 vs April 202 = **6.1** as written "6,1%", value check pending % (2026-04-01..2026-04-30) [keep: ] quote: "El número de usuarios del transporte público aumentó un 6,1% en abril respecto al mismo mes de 2025."
  - p63 Urban transport year-on-year growth rate, Spain, April 2026 = **8.4** as written "8,4%", value check pending % (2026-04-01..2026-04-30) [keep: ] quote: "El transporte urbano subió un 8,4% en tasa anual y el interurbano un 1,2%."
  - p64 Interurban transport year-on-year growth rate, Spain, April 2026 = **1.2** as written "1,2%", value check pending % (2026-04-01..2026-04-30) [keep: ] quote: "El transporte urbano subió un 8,4% en tasa anual y el interurbano un 1,2%."
  - p65 Total passengers year-on-year variation, Spain, April 2026 (table) = **6.1** as written "6,1", value check pending percent (2026-04-01..2026-04-30) [DISCARD: Duplicate of p62 (April 2026 total ETP growth of 6.1%).] quote: "\| Total \| \| 504.439 \| 6,1 \|"
  - p66 Urban transport year-on-year variation, Spain, April 2026 (table) = **8.4** as written "8,4", value check pending percent (2026-04-01..2026-04-30) [DISCARD: Duplicate of p63 (April 2026 urban transport growth of 8.4%).] quote: "\| Transporte urbano \| \| 318.406 \| 8,4 \|"
  - p67 Interurban transport year-on-year variation, Spain, April 2026 (table) = **1.2** as written "1,2", value check pending percent (2026-04-01..2026-04-30) [DISCARD: Duplicate of p64 (April 2026 interurban transport growth of 1.2%).] quote: "\| Transporte interurbano \| \| 140.433 \| 1,2 \|"
  - p68 Special and discretionary transport year-on-year variation, Spain, April 2026 (t = **6.1** as written "6,1", value check pending percent (2026-04-01..2026-04-30) [keep: ] quote: "\| Transporte especial y discrecional \| \| 45.600 \| 6,1 \|"
- `https://www.ine.es/jaxiT3/Datos.htm?t=20239` -> **snapshot** (snapshot 20260331043326); points raw/verified 1/0
- `https://www.ine.es/dyngs/Prensa/TV0825.htm` -> **snapshot** (snapshot 20251216205557); points raw/verified 15/8
  - p69 Total public transport passengers, Spain, August 2025, annual growth rate = **2.6** as written "2,6%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Duplicate of p42 (August 2025 total public transport growth of 2.6%).] quote: "El número de usuarios del transporte público aumentó un 2,6% en agosto respecto al mismo mes de 2024."
  - p70 Urban transport passengers, Spain, August 2025, annual growth rate = **4** as written "4,0%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Duplicate of p43 (August 2025 urban transport growth of 4.0%).] quote: "El transporte urbano subió un 4,0% en tasa anual y el interurbano cayó un 1,4%."
  - p71 Special and discretionary transport passengers, Spain, August 2025, annual growt = **11.7** as written "11,7%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Duplicate of p59 (August 2025 special/discretionary growth of 11.7%).] quote: "Más de 21,6 millones de usuarios utilizaron transporte especial y discrecional en agosto, lo que supuso un incremento del 11,7% en tasa anual."
  - p72 Interurban bus transport passengers, Spain, August 2025, annual growth rate = **1.8** as written "1,8%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Duplicate of p47 (August 2025 interurban bus growth of 1.8%).] quote: "Dentro del interurbano, destacó el incremento del 1,8% en el transporte por autobús."
  - p73 Metro transport passengers, Spain, August 2025, annual growth rate = **3.2** as written "3,2%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Duplicate of p45 (August 2025 metro growth of 3.2%).] quote: "El transporte por metro aumentó un 3,2% en tasa anual y el transporte urbano por autobús aumentó un 4,5%."
  - p74 Urban bus transport passengers, Spain, August 2025, annual growth rate = **4.5** as written "4,5%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Duplicate of p46 (August 2025 urban bus growth of 4.5%).] quote: "El transporte por metro aumentó un 3,2% en tasa anual y el transporte urbano por autobús aumentó un 4,5%."
  - p75 Special transport passengers, Spain, August 2025, annual growth rate = **15.7** as written "15,7%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El número de pasajeros del transporte especial subió un 15,7% y superó los 5,3 millones de usuarios."
  - p76 Discretionary transport passengers, Spain, August 2025, annual growth rate = **10.4** as written "10,4%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "el transporte discrecional creció un 10,4% respecto al mismo mes del año 2024, con más de 16,3 millones de viajeros."
- `https://www.ine.es/dyngs/Prensa/TV0726.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 12 (scale word 'thousand' not supported by quote or table header: 5; scale word 'million' not supported by quote or table header: 6; value_as_written not in quote as a whole number: 1)

### b2 [related_series] operator-level leading indicators

Hypothesis: Monthly counts for major operators around August 2026 versus August 2025 would validate the 2026 level shift and the August seasonal intensity, reducing reliance on p1 as a June proxy. The current evidence contains only 2025 growth rates for operators.

Queries issued by the searcher: Metro Madrid viajeros agosto 2026; INE Estadística de Transporte de Personas agosto 2026 viajeros; EMT Madrid viajeros agosto 2026 millones de viajeros balance mensual; TMB Barcelona viatgers agost 2026 metro bus demanda

- `https://www.ine.es/dyngs/Prensa/TV0826.htm?print=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.eldiariodemadrid.es/articulo/movilidad/metro-madrid-emt-viajeros-agosto-2026-ine/20261009103223143795.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.viaempresa.cat/es/economia/autobuses-urbanos-ganan-7-5-pasajeros-agosto-catalunya-hasta-23-2-millones_2241738_102.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://transparencia.madrid.es/portales/transparencia/es/Transparencia-por-sectores/Movilidad/Transporte/Uso-del-transporte-gestionado-por-la-socieda` -> **snapshot** (snapshot 20260418031723); points raw/verified 15/0
- dropped by code checks: 15 (scale word 'million' not supported by quote or table header: 15)

### b3 [related_series] tourism and airport demand calibration

Hypothesis: August public transport demand, especially urban/interurban services in tourist cities, is tied to tourist overnight stays and airport arrivals. August 2026 tourism data or a level-to-level August comparison would calibrate the seasonal intensity and tourism-driven part of the estimate.

Queries issued by the searcher: INE Estadística de Transporte de Personas agosto 2026 viajes de pasajeros; Aena pasajeros agosto 2026 aeropuertos España récord; INE Estadística de ocupación hotelera julio 2026 pernoctaciones nota de prensa; Frontur llegadas turistas internacionales julio 2026 INE nota de prensa

- `https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736177015&idp=1254735576863` -> **snapshot** (snapshot 20260212165818); points raw/verified 13/12
  - p77 Spain hotel overnight stays, year-on-year change, December 2025 = **2.89** as written "2,89", value check pending % change vs same month previous year (2025-12-01..2025-12-31) [DISCARD: December 2025 hotel overnight level/growth is outside the August target period and not applicable without a large season] quote: "\| Pernoctaciones \| \| 18.546.462 \| 2,89 \|"
  - p78 Spain hotel overnight stays, year-on-year increase, December 2025 (headline) = **2.9** as written "2,9%", value check pending % (2025-12-01..2025-12-31) [DISCARD: Headline duplicate of p77 and December 2025, not August 2026.] quote: "Las pernoctaciones en establecimientos hoteleros aumentaron un 2,9% en diciembre respecto al mismo mes de 2024."
  - p79 Spain average hotel stay, December 2025 = **2.67** as written "2,67", value check pending days (2025-12-01..2025-12-31) [DISCARD: Duplicate of p13 and December 2025 hotel average stay; not usable for August transport.] quote: "\| Estancia media (número de días) \| \| 2,67 \| -2,69 \|"
  - p80 Spain average hotel stay, year-on-year change, December 2025 = **-2.69** as written "-2,69", value check pending % change vs same month previous year (2025-12-01..2025-12-31) [DISCARD: December 2025 hotel average-stay change; outside target period.] quote: "\| Estancia media (número de días) \| \| 2,67 \| -2,69 \|"
  - p81 Spain hotel occupancy rate by bed places, December 2025 = **49.65** as written "49,65", value check pending % (2025-12-01..2025-12-31) [DISCARD: December 2025 hotel occupancy level; outside target period.] quote: "\| Grado de ocupación por plaza (porcentaje) \| \| 49,65 \| 1,64 \|"
  - p82 Spain hotel occupancy rate by bed places, year-on-year change, December 2025 = **1.64** as written "1,64", value check pending % change vs same month previous year (2025-12-01..2025-12-31) [DISCARD: December 2025 hotel occupancy change; outside target period.] quote: "\| Grado de ocupación por plaza (porcentaje) \| \| 49,65 \| 1,64 \|"
  - p83 Spain average hotel room rate (ADR) per occupied room, December 2025 = **120** as written "120,31", value check pending euros (2025-12-01..2025-12-31) [DISCARD: December 2025 hotel ADR level; price rather than volume and outside target period.] quote: "\| Tarifa media por habitación ocupada (euros) \| \| 120,31 \| 2,50 \|"
  - p84 Spain average hotel room rate (ADR), year-on-year change, December 2025 = **2.5** as written "2,50", value check pending % change vs same month previous year (2025-12-01..2025-12-31) [DISCARD: December 2025 hotel ADR change; price rather than transport demand.] quote: "\| Tarifa media por habitación ocupada (euros) \| \| 120,31 \| 2,50 \|"
  - p85 Spain average hotel revenue per occupied room, December 2025 (headline) = **120** as written "120,3", value check pending euros (2025-12-01..2025-12-31) [DISCARD: December 2025 hotel revenue per room; not a transport demand indicator for August 2026.] quote: "Los hoteles facturaron 120,3 euros de media por habitación ocupada, un 2,5% más que el mismo mes del año anterior."
  - p86 Spain hotel price index (IPH), December 2025 = **151** as written "151,23", value check pending index (2025-12-01..2025-12-31) [DISCARD: December 2025 hotel price index level; outside target period and not a volume measure.] quote: "\| Precios hoteleros (índice) \| \| 151,23 \| 4,20 \|"
  - p87 Spain hotel price index (IPH), year-on-year change, December 2025 = **4.2** as written "4,20", value check pending % change vs same month previous year (2025-12-01..2025-12-31) [DISCARD: December 2025 hotel price index change; not a transport volume measure.] quote: "\| Precios hoteleros (índice) \| \| 151,23 \| 4,20 \|"
  - p88 Spain hotel price index (IPH), annual rate increase, December 2025 (headline) = **4.2** as written "4,2%", value check pending % (2025-12-01..2025-12-31) [DISCARD: Headline duplicate of p87 and December 2025, not August 2026.] quote: "El Índice de Precios Hoteleros subió un 4,2% en tasa anual."
- `https://www.larioja.org/larioja-client/cm/estadistica/images?idMmedia=1750185` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.eldiario.es/canariasahora/turismo/pernoctaciones-hoteleras-aumentaron-3-49-julio-canarias_1_13503556.html` -> **snapshot** (snapshot 20260911171506); points raw/verified 14/9
  - p89 Canary Islands hotel overnight stays year-on-year growth, July 2026 vs July 2025 = **3.49** as written "3,49%", value check pending % (2026-07-01..2026-07-31) [keep: ] quote: "Las pernoctaciones hoteleras aumentaron un 3,49% en julio respecto al mismo mes de 2025 en Canarias"
  - p90 Canary Islands hotel overnight stays increase, July 2026 vs July 2025 = **229** hotel overnight stays (2026-07-01..2026-07-31) [DISCARD: Canary Islands July 2026 overnight-stay increase is regional and its level is not used; p89 already captures the regiona] quote: "con una subida de 228.743 más"
  - p91 Canary Islands hotel travellers, July 2025 = **1,000** travellers (2025-07-01..2025-07-31) [DISCARD: Canary July 2025 traveller count is rounded and regional; not needed for national August 2026 transport.] quote: "que pasaron de 999.568 a 1.058.995 de julio a julio"
  - p92 Canary Islands average hotel stay, July 2026 = **6.4** as written "6,40", value check pending nights per traveller (2026-07-01..2026-07-31) [DISCARD: Canary July 2026 average hotel stay is regional and not used for national transport demand.] quote: "la estancia media de cada uno de ellos apenas cambió, quedando en 6,40 noches, frente a las 6,56 de un año atrás"
  - p93 Canary Islands average hotel stay, July 2025 = **6.56** as written "6,56", value check pending nights per traveller (2025-07-01..2025-07-31) [DISCARD: Canary July 2025 average hotel stay is regional and not used for national transport demand.] quote: "quedando en 6,40 noches, frente a las 6,56 de un año atrás"
  - p94 Canary Islands hotel travellers from abroad, July 2026 = **749** travellers (2026-07-01..2026-07-31) [DISCARD: Canary July 2026 foreign traveller count is regional and not used.] quote: "clientes de hoteles isleños de procedencia extranjera, de 715.913 a 748.524"
  - p95 Canary Islands hotel travellers from abroad, July 2025 = **716** travellers (2025-07-01..2025-07-31) [DISCARD: Canary July 2025 foreign traveller count is regional and not used.] quote: "clientes de hoteles isleños de procedencia extranjera, de 715.913 a 748.524"
  - p96 Canary Islands hotel travellers resident in Spain, July 2026 = **310** travellers (2026-07-01..2026-07-31) [DISCARD: Canary July 2026 resident traveller count is regional and not used.] quote: "como los residentes en España, de 283.655 a 310.471"
  - p97 Canary Islands hotel travellers resident in Spain, July 2025 = **284** travellers (2025-07-01..2025-07-31) [DISCARD: Canary July 2025 resident traveller count is regional and not used.] quote: "como los residentes en España, de 283.655 a 310.471"
- `https://efe.com/economia/2026-08-21/estancias-hoteleras-estancan-julio-precios-siguen-alza/` -> **snapshot** (snapshot 20260822091323); points raw/verified 15/13
  - p98 Spain hotel overnight stays year-on-year change, July 2026 = **0.3** as written "0,3 %", value check pending % (2026-07-01..2026-07-31) [keep: ] quote: "Las pernoctaciones en los hoteles españoles repuntaron un 0,3 % en julio"
  - p99 Spain hotel prices year-on-year change, July 2026 = **5.9** as written "5,9 %", value check pending % (2026-07-01..2026-07-31) [DISCARD: July 2026 hotel price growth is a price indicator, not a transport volume indicator.] quote: "los precios subieron de media un 5,9 % en comparación con el mismo mes de 2025"
  - p100 Spain resident overnight stays year-on-year change, July 2026 = **1.1** as written "1,1 %", value check pending % (2026-07-01..2026-07-31) [keep: ] quote: "un descenso en tasa interanual de las estancias de los residentes españoles (1,1 % menos)"
  - p101 Spain foreign tourist overnight stays year-on-year change, July 2026 = **1.1** as written "1,1 %", value check pending % (2026-07-01..2026-07-31) [keep: ] quote: "frente al ascenso del 1,1 % por parte de los turistas extranjeros"
  - p102 Spain hotel overnight stays year-on-year change, first seven months of 2026 = **1.5** as written "1,5 %", value check pending % (2026-01-01..2026-07-31) [keep: ] quote: "Durante los siete primeros meses del año las estancias hoteleras repuntaron un 1,5 % en tasa interanual"
  - p103 Spain non-resident overnight stays year-on-year change, first seven months of 20 = **1.8** as written "1,8 %", value check pending % (2026-01-01..2026-07-31) [keep: ] quote: "las pernoctaciones de los no residentes en España también crecieron por encima del dato general, un 1,8 % más que en el mismo periodo de 2025"
  - p104 British tourists' share of Spain hotel overnight stays, July 2026 = **25.8** as written "25,8 %", value check pending % (2026-07-01..2026-07-31) [DISCARD: British share of hotel overnight stays does not help estimate total August 2026 public transport journeys.] quote: "los turistas británicos concentraron la cuarta parte de las estancias hoteleras (25,8 % del total)"
  - p105 German guests' share of Spain hotel overnight stays, July 2026 = **14.5** as written "14,5 %", value check pending % (2026-07-01..2026-07-31) [DISCARD: German share of hotel overnight stays does not help estimate total August 2026 public transport journeys.] quote: "seguidos por los huéspedes procedentes de Alemania (14,5 %)"
  - p106 Hotel bed places occupancy rate, Spain, July 2026 = **71.1** as written "71,1 %", value check pending % (2026-07-01..2026-07-31) [keep: ] quote: "En julio se cubrieron el 71,1 % de las plazas ofertadas"
  - p107 Hotel bed places occupancy rate year-on-year change, Spain, July 2026 = **0.9** as written "0,9 %", value check pending % (2026-07-01..2026-07-31) [keep: ] quote: "un 0,9 % más que en el mismo mes del año pasado"
  - p108 Balearic Islands hotel bed places occupancy rate, July 2026 = **87.4** as written "87,4 %", value check pending % (2026-07-01..2026-07-31) [DISCARD: Balearic July 2026 occupancy is regional and not directly transferable to national August transport.] quote: "con Baleares con el mayor grado de ocupación por plazas (87,4 %)"
  - p109 Balearic Islands share of foreign tourists' hotel overnight stays, July 2026 = **33.4** as written "33,4 %", value check pending % (2026-07-01..2026-07-31) [DISCARD: Balearic share of foreign hotel overnight stays is regional and not needed for the national total.] quote: "el principal destino hotelero en julio fue Baleares, con el 33,4 % de los registros"
  - p110 Spain hotel ADR (average daily rate per occupied room), July 2026 = **157** as written "156,9 euros", value check pending euros per occupied room (2026-07-01..2026-07-31) [DISCARD: July 2026 hotel ADR is a price measure, not a transport volume measure.] quote: "la facturación media de los hoteles por cada habitación ocupada (ADR) fue de 156,9 euros en julio"
- dropped by code checks: 8 (number: ambiguous separators: '.' used as a thousands separator: 6; scale word 'million' not supported by quote or table header: 2)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['spain public transport', 'ine passenger transport', 'viajeros agosto 2026']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p4', 'p7'] All three report the same INE June 2026 total public transport change (+2.0%). p4 is a headline duplicate and p7 is the table duplicate; p7's quote also contains the June 2026 total level, but its num
- corroborating: ['p2', 'p5', 'p8'] Same INE June 2026 urban transport change (+3.1%). p5/p8 are duplicates; p8's quote gives the urban June 2026 level but the data value is the growth rate. Not independent.
- corroborating: ['p3', 'p10'] Same INE June 2026 special/discretionary transport change (+3.0%). p10's quote gives the June 2026 special level but the data value is the growth rate. Not independent.
- conflicting: ['p6', 'p9'] p6 gives +0.6% for June 2026 interurban while the quote says it fell and p9 gives -0.6%. p6 is a sign/transcription error; p9 is the coherent table value.
- corroborating: ['p42', 'p54', 'p56'] All report August 2025 total public transport growth of +2.6%. p54 and p56 are repeat/duplicate transmissions of the same INE release, not independent.
- corroborating: ['p43', 'p55', 'p57'] All report August 2025 urban transport growth of +4.0%. p57's quote also gives an urban August 2025 level, but its numeric value is the growth rate; useful only as context. Not independent.
- conflicting: ['p44', 'p58'] p44 gives +1.4% for August 2025 interurban while its quote says interurban fell; p58 gives -1.4%. p44 has a sign error; p58 is coherent with the headline text.
- corroborating: ['p46', 'p61'] Both report August 2025 urban bus growth of +4.5%. p61 is a duplicate transmission.
- conflicting: ['p48', 'p60'] p48 reports rail transport +5.9% in August 2025, while p60's quote says rail decreased 5.9% and its numeric sign is inconsistent with that wording. p60 is unreliable and should not be combined with p4
- contextual: ['p45', 'p49', 'p50'] Metro growth rates for August 2025: national metro +3.2%, Valencia metro +16.8%, Palma metro +56.0%. Different scopes, not contradictory; useful only as mode/city context.
- corroborating: ['p11', 'p12'] December 2025 hotel overnight stays growth +2.9%, same INE release/headline duplicate. It is a different season and cannot transfer to August without a seasonal bridge.
- contextual: ['p13', 'p15', 'p17', 'p19', 'p21'] December 2025 hotel-sector levels: average stay, occupancy, ADR, price index, revenue per room. Only p13 is even potentially a conversion factor; these are not August passenger counts.
- corroborating: ['p22', 'p23', 'p24', 'p25', 'p30', 'p31', 'p37', 'p38', 'p39', 'p40'] Calendar evidence for August 2026: 31 days, five complete weekends, and the national Assumption holiday on Saturday 15 August. Many regional duplicates; they corroborate the same calendar facts.
- contextual: ['p51', 'p52', 'p53'] EMT Madrid full-year 2025 growth and zero-emission fleet/new-driver counts. The fleet and staffing points describe capacity inputs, not realised passenger journeys.
- contextual: ['p41'] Outdated 2023 snapshot saying latest ETP data were January 2023; superseded by the 2026 INE points and not useful for August 2026.
- contextual: ['p59'] Unique August 2025 special/discretionary transport growth (+11.7%); its quote mentions a level above 21.6 million, but the numeric data value is the growth rate and cannot be used as a level input.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p7'] Both report the same INE June 2026 total ETP annual variation of 2.0%; p7 is a duplicate table copy, not an independent measurement.
- corroborating: ['p2', 'p8'] Both report urban transport June 2026 annual growth of 3.1% from the same INE release; duplicate.
- corroborating: ['p3', 'p10'] Both report special/discretionary transport June 2026 annual growth of 3.0% from the same INE release; duplicate.
- corroborating: ['p1', 'p2', 'p9', 'p10'] June 2026 component growth rates imply a weighted total near the reported 2.0%; all are from the same INE table/release and are not independent.
- conflicting: ['p9', 'p6'] p9 reports interurban June 2026 annual change as -0.6%; discarded p6 shows +0.6%, apparently a sign error. The headline/table p9 is authoritative.
- corroborating: ['p42', 'p69'] Both report August 2025 total public transport annual growth of 2.6%; duplicate INE source.
- corroborating: ['p43', 'p70'] Both report August 2025 urban transport annual growth of 4.0%; duplicate INE source.
- conflicting: ['p43', 'p70', 'p44', 'p58'] p43/p70 state interurban August 2025 fell 1.4%; p58 tabulates 1.4 with an ambiguous sign but its quote says 'descendió'. Use only as negative-growth context, not as positive growth.
- corroborating: ['p57', 'p58', 'p59'] Quotes give August 2025 urban ~222.8M, interurban ~117.8M, special ~21.6M, summing to ~362M. Their numeric values are growth rates, not levels; use only to inform August category shares.
- corroborating: ['p62', 'p65'] Both report April 2026 total ETP annual growth of 6.1%; duplicate INE source.
- corroborating: ['p63', 'p66'] Both report April 2026 urban transport annual growth of 8.4%; duplicate INE source.
- corroborating: ['p64', 'p67'] Both report April 2026 interurban transport annual growth of 1.2%; duplicate INE source.
- corroborating: ['p68'] Provides April 2026 special/discretionary growth of 6.1%; no duplicate kept in the main table.
- corroborating: ['p98', 'p100', 'p101', 'p102', 'p107'] July 2026 national hotel data show modest tourism growth: overnight stays +0.3%, resident stays -1.1%, foreign stays +1.1%, first seven months +1.5%, occupancy +0.9%. They consistently suggest a small
- contextual difference: ['p89', 'p98'] Canary Islands July 2026 overnight stays grew 3.49%, stronger than the national +0.3%; this is regional and should not be transferred directly to national August transport demand.
- corroborating: ['p22', 'p23', 'p24', 'p25'] August 2026 has 31 days, five complete weekends, and one national holiday on Saturday 15 August. These calendar facts matter for seasonality but do not provide a clear differential versus August 2025.
- contextual: ['p45', 'p46', 'p47', 'p48', 'p49', 'p50'] August 2025 mode and operator growth rates corroborate urban strength and mixed interurban performance, but they are operator/mode specific, not national passenger levels.
- corroborating: ['p75', 'p76', 'p59'] Special transport +15.7% and discretionary +10.4% are consistent with the combined special/discretionary August 2025 growth of 11.7%.
- irrelevant/older: ['p13', 'p77', 'p78', 'p79', 'p80', 'p81', 'p82', 'p83', 'p84', 'p85', 'p86', 'p87', 'p88'] These are December 2025 hotel statistics, outside the August 2026 target period and not usable for August transport seasonality without a strong transfer assumption.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | Annual ETP passenger journeys per resident, Spain, 2025 | 120 | 90..160 | 84.85..170 (widened) | passenger journeys per resident per year | m1 (m1) | Spain's annual ETP public transport journeys are roughly 5-6 billion with a population near 49 million, implying about 110-125 per resident. The range is widened to cover uncertainty in annual ETP totals, population, and the August seasonal ratio. | Used as the 2025 annual ETP base before applying the 2026 growth proxy. | Official INE annual ETP total implies per-capita annual journeys outside the stated range. |
| a2 | Resident population of Spain, 2026 | 49,000,000 | 48,500,000..50,000,000 | 34,820,971..69,641,941 (widened) | people | m1 (m1), m2 (m2) | Spain's resident population is around 49 million in 2025-2026. The range reflects normal census/projection uncertainty. | Used as the mid-2026 population denominator for per-capita annual journeys. | Official 2026 population estimate falls outside the range. |
| a3 | August 2025 daily ETP journeys relative to 2025 annual average daily journeys | 0.72 | 0.62..0.84 | 0.5103..1.021 (widened) | dimensionless | m1 (m1), m2 (m2) | August 2025 quoted urban level p57 (222.8 million), special/discretionary level p59 (21.6 million), and a typical interurban share around one-third imply an August total near 360 million. A 2025 annual level near 5.9 billion gives an August daily average near 0.72 of the annual average daily rate. T | Used to convert annual average daily journeys into August daily intensity for 2026. | Actual INE August and annual ETP levels imply a ratio outside the range. |
| a6 | Annual ETP passenger journeys per resident, Spain, 2024 | 115 | 85..155 | 81.16..162 (widened) | passenger journeys per resident per year | m2 (m2) | Spain's annual ETP journeys per resident in 2024 were slightly below the 2025 level, consistent with positive 2025 and 2026 ETP growth. The range is wide to cover uncertainty in annual totals, population, and pre-2025 reporting. | Used as the 2024 annual per-capita base in the route that applies reported August 2025 and June 2026 growth to reach August 2026. | Official INE annual ETP totals imply 2024 per-capita journeys outside the stated range. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 368,239,742 | ['p22', 'p1'] / ['a1', 'a2', 'a3'] | [] |  | 0.50 | equal |  |
| m2 | formula_mc | 364,430,676 | ['p22', 'p42', 'p1'] / ['a2', 'a3', 'a6'] | [] |  | 0.50 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target

Result: central **366,330,258** passenger, 80% interval [195,416,387, 686,727,763] passenger, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best estimate for total INE Passenger Transport Statistics journeys in Spain for August 2026 (urban, interurban and special/discretionary combined) is 366,330,258 passenger (80% model-based interval 195,416,387 to 686,727,763 passenger). This combines two aggregate routes: 368,239,742 passenger at weight 50% and 364,430,676 passenger at weight 50%; no backtest error was available, so the weighting reflects the supplied method design rather than demonstrated accuracy.

Observed inputs are the August length 31 days, June 2026 total growth 2 percent, and August 2025 growth 2.6%. The routes rest on assumptions: annual journeys per resident (120, range 84.85 to 170; and 115, range 81.16 to 162), population 49,000,000 (range 34,820,971 to 69,641,941), and August seasonal intensity 0.72 (range 0.5103 to 1.021).

The main risk is that June 2026 growth does not carry into August. The most useful missing evidence would be the actual August 2025 ETP total and any early August 2026 indicators.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 Annual ETP passenger journeys per resident, Spain, 2025: 120 passenger journeys per resident per year, range 84.85 to 170 (range widened by code); used by m1. Overturned by: Official INE annual ETP total implies per-capita annual journeys outside the stated range.
- a2 Resident population of Spain, 2026: 49,000,000 people, range 34,820,971 to 69,641,941 (range widened by code); used by m1, m2. Overturned by: Official 2026 population estimate falls outside the range.
- a3 August 2025 daily ETP journeys relative to 2025 annual average daily journeys: 0.72 dimensionless, range 0.5103 to 1.021 (range widened by code); used by m1, m2. Overturned by: Actual INE August and annual ETP levels imply a ratio outside the range.
- a6 Annual ETP passenger journeys per resident, Spain, 2024: 115 passenger journeys per resident per year, range 81.16 to 162 (range widened by code); used by m2. Overturned by: Official INE annual ETP totals imply 2024 per-capita journeys outside the stated range.

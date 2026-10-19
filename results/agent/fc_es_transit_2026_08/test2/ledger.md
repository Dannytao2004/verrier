# Evidence ledger: fc_es_transit_2026_08

- Question: Assume today is 2026-09-11. You know nothing published after this date. Estimate the total number of passengers who used public transport in Spain in August 2026 (urban, interurban and special/discretionary transport combined), as it will be first reported in the provisional data of the National Statistics Institute's (INE) Passenger Transport Statistics (Estadística de Transporte de Personas).
- as_of: 2026-09-11
- Pinned target: Total number of passengers carried by public transport in Spain (urban, interurban and special/discretionary transport combined) during August 2026, as first reported in INE's Estadística de Transporte de Personas (ETP) provisional data | unit passengers | period 2026-08-01..2026-08-31 | publisher Instituto Nacional de Estadística (INE), Estadística de Transporte de Personas (ETP)

- Official value (scoring only, never shown to the agent): 371,623,271

## Directions and pages

### d1 [own_history] INE ETP time series

Hypothesis: August 2026 total ≈ August 2025 total × (1 + recent YoY growth rate). ETP monthly totals show strong August peaks; the most recent published months (June/July 2026) give the current YoY growth trend to extrapolate one month forward.

Queries issued by the searcher: Estadística de Transporte de Personas INE viajeros agosto 2025; INE Estadística de Transporte de Personas serie mensual viajeros total; "Transporte de Personas" INE junio 2026 viajeros millones tasa anual nota de prensa; INE ETP mayo 2026 transporte público viajeros millones aumento anual

- `https://www.ine.es/dyngs/Prensa/TV0726.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ine.es/dyngs/Prensa/TV0825.htm` -> **snapshot** (snapshot 20251216205557); points raw/verified 15/8
  - p1 Year-on-year growth rate of total public transport passengers in Spain, August 2 = **2.6** as written "2,6%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El número de usuarios del transporte público aumentó un 2,6% en agosto respecto al mismo mes de 2024."
  - p2 Year-on-year growth rate of urban transport passengers in Spain, August 2025 = **4** as written "4,0%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte urbano subió un 4,0% en tasa anual y el interurbano cayó un 1,4%."
  - p3 Year-on-year growth rate of special and discretionary transport passengers in Sp = **11.7** as written "11,7%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "Más de 21,6 millones de usuarios utilizaron transporte especial y discrecional en agosto, lo que supuso un incremento del 11,7% en tasa anual."
  - p4 Year-on-year growth rate of special transport passengers in Spain, August 2025 = **15.7** as written "15,7%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El número de pasajeros del transporte especial subió un 15,7% y superó los 5,3 millones de usuarios."
  - p5 Year-on-year growth rate of discretionary transport passengers in Spain, August  = **10.4** as written "10,4%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "Por su parte, el transporte discrecional creció un 10,4% respecto al mismo mes del año 2024, con más de 16,3 millones de viajeros."
  - p6 Year-on-year growth rate of interurban bus passengers in Spain, August 2025 = **1.8** as written "1,8%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "Dentro del interurbano, destacó el incremento del 1,8% en el transporte por autobús."
  - p7 Year-on-year growth rate of metro passengers in Spain, August 2025 = **3.2** as written "3,2%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte por metro aumentó un 3,2% en tasa anual y el transporte urbano por autobús aumentó un 4,5%."
  - p8 Year-on-year growth rate of urban bus passengers in Spain, August 2025 = **4.5** as written "4,5%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte por metro aumentó un 3,2% en tasa anual y el transporte urbano por autobús aumentó un 4,5%."
- `https://www.ine.es/jaxiT3/Datos.htm?t=20239` -> **snapshot** (snapshot 20260331043326); points raw/verified 1/0
- `https://ebs.publicnow.com/view/CC9E1D0E865D9D0978F20FE565B6085A6B7A8B13` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 8 (scale word 'million' not supported by quote or table header: 6; value_as_written not in quote as a whole number: 1; scale word 'thousand' not supported by quote or table header: 1)

### d2 [related_series] Mode-level decomposition

Hypothesis: Total = sum of urban (metro + bus), interurban (bus + rail + air + sea), and special/discretionary passengers. Each mode has its own August seasonal factor and growth trend; summing mode-level August 2026 estimates constrains the total and reveals which component drives uncertainty.

Queries issued by the searcher: INE Estadística de Transporte de Personas viajeros agosto 2025 metro autobús; Estadística Transporte de Personas INE modos transporte serie viajeros urbanos interurbanos especiales; "Estadística de Transporte de Viajeros" agosto 2025 nota de prensa INE 362,4 millones metro autobús interurbano; Estadística de Transporte de Viajeros julio 2026 INE viajeros transporte público

- `https://ine.es/dyngs/Prensa/TV0825.pdf` -> **dropped** (snapshot fetch failed (http -1); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.elindependiente.com/economia/2025/10/10/transporte-publico-espana-viajeros-agosto/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://195.254.149.130/dynt3/metadatos/es/RespuestaDatos.html?oper=297` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.galiciapress.es/articulo/ultima-hora/2025-10-10/5460974-transporte-urbano-autobus-aumenta-28-agosto-galicia` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] Operator-level data (RENFE, metro systems, EMT, airlines)

Hypothesis: Operator-reported August 2026 passenger counts (RENFE, Madrid/Barcelona metro, EMT Madrid, Aena airport passengers, Puertos del Estado cruise/ferry) can be aggregated and scaled to ETP coverage. Operator data often appears before INE's consolidated release.

Queries issued by the searcher: Aena pasajeros agosto 2026; RENFE viajeros agosto 2026; Metro Madrid viajeros agosto 2026; INE Estadística de Transporte de Personas julio 2026 viajeros millones

- `https://www.aena.es/es/prensa/los-aeropuertos-gallegos-superan-el-medio-millon-de-pasajeros-en-agosto.html&p=1575078740846` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.eldiariodemadrid.es/articulo/movilidad/metro-madrid-emt-viajeros-agosto-2026-ine/20261009103223143795.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://grupo.renfe.com/es/es/sala-de-prensa/noticias/2026/07/renfe-ofrece-1-millones-plazas-operacion-salida-agosto-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.infobae.com/espana/agencias/2026/07/31/otro-agosto-turistico-en-maximos-mas-viajeros-tarifas-mas-altas-y-el-combustible-al-alza/` -> **snapshot** (snapshot 20260801051953); points raw/verified 15/10
  - p9 High-speed, long and medium distance trains circulating Thursday to Sunday (Adif = **4.375** trains (2026-07-30..2026-08-02) [DISCARD: Adif train count for a single long weekend; no conversion to passengers available and too narrow to anchor the total.] quote: "Entre este jueves y el próximo domingo circularán por las vías españolas 4.375 trenes de alta velocidad, larga y media distancia"
  - p10 Aena planned flights across network Friday to Sunday = **22.66** flights (2026-07-31..2026-08-02) [DISCARD: Aena flight count for one weekend; no load-factor/passenger bridge and air is only part of interurban.] quote: "Aena tiene previstos en los aeropuertos de la red entre este viernes y el domingo 22.655 vuelos"
  - p11 Aena year-on-year change in flights for first August weekend = **3** % (2026-07-31..2026-08-02) [keep: Kept as weak directional context for 2026 summer demand; not used as a direct passenger input.] quote: "casi un 3 % más que en el primer fin de semana de agosto del año pasado"
  - p12 Aena average daily flights over first August weekend = **7.5** flights per day (2026-07-31..2026-08-02) [DISCARD: Redundant restatement of p10 (daily average of the same weekend).] quote: "con una media diaria superior a los 7.500 vuelos"
  - p13 Madrid-Barajas scheduled movements Friday to Sunday = **3.716** movements (2026-07-31..2026-08-02) [DISCARD: Single-airport movement count; too narrow and no passenger bridge.] quote: "En Madrid-Barajas están programados 3.716 movimientos, un 7,3 % más que un año antes"
  - p14 Barcelona-El Prat scheduled movements Friday to Sunday = **3.332** movements (2026-07-31..2026-08-02) [DISCARD: Single-airport movement count; too narrow and no passenger bridge.] quote: "en Barcelona-El Prat, 3.332, el 4,7 % más"
  - p15 Palma scheduled flights Friday to Sunday = **3.178** flights (2026-07-31..2026-08-02) [DISCARD: Single-airport flight count; too narrow and no passenger bridge.] quote: "y en Palma, 3.178 vuelos, algo por debajo de los 3.202 del año pasado"
  - p16 Air Europa daily flights in August (lower bound of range) = **220** flights per day (2026-08-01..2026-08-31) [DISCARD: One airline's daily flights; cannot be scaled to national ETP total without a share assumption that is itself unsupporte] quote: "Air Europa mantiene en agosto su operativa habitual, con entre 220 y 225 vuelos diarios"
  - p17 Air Europa daily flights in August (upper bound of range) = **225** flights per day (2026-08-01..2026-08-31) [DISCARD: Upper bound of the same Air Europa range; redundant with p16 and equally unusable for the total.] quote: "Air Europa mantiene en agosto su operativa habitual, con entre 220 y 225 vuelos diarios"
  - p18 Share of Spaniards taking holidays in August (Obervatur) = **36** % (2026-08-01..2026-08-31) [DISCARD: Holiday-share context only; no quantitative bridge to passenger counts.] quote: "según los datos de Obervatur, un 36 % de los españoles toma su descanso en agosto"
- dropped by code checks: 5 (scale word 'million' not supported by quote or table header: 5)

### d4 [physical_flow] Air and rail capacity/throughput

Hypothesis: Air passengers (Aena) and rail passengers (RENFE/AVE) dominate interurban totals; August 2026 air traffic can be estimated from Aena monthly statistics or flight schedules × load factor, then bridged to ETP air passenger count.

Queries issued by the searcher: Aena estadísticas pasajeros agosto 2026; Aena tráfico aeropuertos julio 2026 pasajeros récord; INE Estadística de Transporte de Personas junio 2026 pasajeros transporte aéreo; INE ETP "transporte de personas" 2026 pasajeros millones junio nota de prensa; ine.es TV0826 Estadística de Transporte de Personas agosto 2026 datos provisionales

- `https://www.aena.es/en/press/aena-group-airports-exceed-41-million-passengers-in-august.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://efe.com/economia/2026-09-15/aena-record-pasajeros-espana-agosto-mes/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.aena.es/doc/detalleprensa/260915-aena-estadisticas-agosto.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://aviacionaldia.com/2026/09/aeropuertos-del-grupo-aena-supera-los-41-millones-de-pasajeros-en-agosto.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [base_rates] Seasonality and calendar

Hypothesis: August is the peak month; the August/July and August/annual ratios are stable year to year. Applying historical August seasonal factors to a 2026 annual or July 2026 base yields an August 2026 estimate.

Queries issued by the searcher: INE Estadística de Transporte de Personas viajeros serie mensual agosto 2025; transporte público España agosto máximo anual viajeros INE millones; INE estadística transporte de personas julio 2026 datos provisionales millones de viajeros; INE "transporte de viajeros" serie mensual miles de viajeros 2024 2025 todos los meses tabla; INE transporte de personas 2025 total anual viajeros millones año 2025 acumulado diciembre; "transporte de viajeros" INE agosto 2023 millones de pasajeros agosto 2022

- `https://www.ine.es/dyngs/Prensa/TV0825.pdf` -> **snapshot** (snapshot 20251221032913); points raw/verified 15/6
  - p19 Year-on-year change in total public transport passengers, Spain, August 2025 = **2.6** as written "2,6%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Redundant duplicate of p1 (same INE August 2025 total growth figure); keeping both would double-count the same measureme] quote: "El número de usuarios del transporte público aumentó un 2,6% en agosto respecto al mismo mes de 2024."
  - p20 Year-on-year change in urban transport passengers, Spain, August 2025 = **4** as written "4,0%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Duplicate of p2 (urban 4.0%).] quote: "El transporte urbano subió un 4,0% en tasa anual y el interurbano cayó un 1,4%."
  - p21 Year-on-year change in special and discretionary transport passengers, Spain, Au = **11.7** as written "11,7", value check pending percent (2025-08-01..2025-08-31) [DISCARD: Duplicate of p3 (special+discretionary 11.7%).] quote: "Agosto 4,0 -1,4 11,7"
  - p22 Year-on-year change in urban transport passengers, Spain, July 2025 = **6.2** as written "6,2", value check pending percent (2025-07-01..2025-07-31) [keep: ] quote: "Julio 6,2 -0,2 3,3"
  - p23 Year-on-year change in interurban transport passengers, Spain, July 2025 = **-0.2** as written "-0,2", value check pending percent (2025-07-01..2025-07-31) [keep: ] quote: "Julio 6,2 -0,2 3,3"
  - p24 Year-on-year change in special and discretionary transport passengers, Spain, Ju = **3.3** as written "3,3", value check pending percent (2025-07-01..2025-07-31) [keep: ] quote: "Julio 6,2 -0,2 3,3"
- `https://asetrasegovia.es/wp-content/uploads/2025/11/PRESENTACIN-O-COSTES.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.bolsamania.com/noticias/empresas/video-el-transporte-publico-en-espana-supera-los-362-millones-de-viajeros-en-agosto-impulsado-por-el-ave-` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://laciutat.cat/es/laciutatdebarcelona/metro-barcelona-registra-mejor-agosto-historia-superar-por-primera-vez-30-millones-usuarios_875367_102.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 9 (scale word 'million' not supported by quote or table header: 6; value_as_written not in quote as a whole number: 1; scale word 'thousand' not supported by quote or table header: 2)

### d6 [shocks] Demand drivers and disruptions

Hypothesis: August 2026 demand is affected by tourism arrivals, fuel prices, heatwaves, strikes, and new rail liberalisation (Ouigo/Iryo). Tourism (Frontur arrivals) is a strong leading indicator for interurban and special transport.

Queries issued by the searcher: Frontur llegadas turistas agosto 2026; huelga transporte agosto 2026 España; Frontur julio 2026 datos provisionales INE turistas internacionales julio; Estadística de Transporte de Personas ETP junio 2026 INE viajeros

- `https://www.ine.es/dyngs/Prensa/FRONTUR0726.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.elimparcial.es/imprimir-noticia.asp?noti=68690` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.airhelp.es/noticias-vuelos/huelgas-de-asistencia-en-tierra-en-espana-barcelona-palma-30072026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.elimparcial.es/imprimir-noticia.asp?noti=44869` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d7 [forecasts_markets] Official forecasts and nowcasts

Hypothesis: Ministry of Transport (MITMA) or INE nowcasts/advance indicators, and analyst commentary, may provide an August 2026 transport demand estimate or growth rate usable as a cross-check.

Queries issued by the searcher: MITMA estadísticas transporte agosto 2026 demanda viajeros; INE Estadística de Transporte de Personas ETP 2026 pasajeros; INE nota de prensa Estadística Transporte de Viajeros agosto 2025 datos provisionales millones de pasajeros; Aena tráfico pasajeros agosto 2026 cifras

- `https://www.ine.es/dyngs/Prensa/TV0726.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ine.es/dyngs/Prensa/TV0825.htm` -> **snapshot** (snapshot 20251216205557); points raw/verified 15/6
  - p25 Annual growth rate of total public transport passengers in Spain, August 2025 vs = **2.6** as written "2,6%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Duplicate of p1.] quote: "El número de usuarios del transporte público aumentó un 2,6% en agosto respecto al mismo mes de 2024."
  - p26 Annual growth rate of urban transport passengers in Spain, August 2025 = **4** as written "4,0%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Duplicate of p2.] quote: "El transporte urbano subió un 4,0% en tasa anual y el interurbano cayó un 1,4%."
  - p27 Annual growth rate of metro transport passengers in Spain, August 2025 = **3.2** as written "3,2%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Duplicate of p7.] quote: "El transporte por metro aumentó un 3,2% en tasa anual y el transporte urbano por autobús aumentó un 4,5%."
  - p28 Annual growth rate of urban bus transport passengers in Spain, August 2025 = **4.5** as written "4,5%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Duplicate of p8.] quote: "El transporte por metro aumentó un 3,2% en tasa anual y el transporte urbano por autobús aumentó un 4,5%."
  - p29 Annual growth rate of interurban bus transport passengers in Spain, August 2025 = **1.8** as written "1,8%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "Por tipo de transporte, por autobús creció un 1,8%, mientras que el aéreo cayó un 0,3%, el marítimo un 1,6%, y por ferrocarril un 5,9%."
  - p30 Annual growth rate of special and discretionary transport passengers in Spain, A = **11.7** as written "11,7%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Duplicate of p3.] quote: "Más de 21,6 millones de usuarios utilizaron transporte especial y discrecional en agosto, lo que supuso un incremento del 11,7% en tasa anual."
- `https://apps.fomento.gob.es/BDOTLE/visorBDpop.aspx?i=2024` -> **snapshot** (snapshot 20250414132910); points raw/verified 0/0
- `https://www.elindependiente.com/economia/2025/10/10/transporte-publico-espana-viajeros-agosto/` -> **snapshot** (snapshot 20251113205847); points raw/verified 15/6
  - p31 Year-on-year growth rate of total public transport passengers in Spain, August = **2.6** as written "2,6%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Secondary-outlet duplicate of p1.] quote: "un incremento del 2,6% respecto al mismo mes de 2024"
  - p32 Year-on-year growth rate of urban transport passengers in Spain, August = **4** % (2025-08-01..2025-08-31) [DISCARD: Duplicate of p2 (adds a level but the level is for 2025 urban only, not usable as a 2026 total).] quote: "el transporte urbano creció un 4% (hasta 222,8 millones)"
  - p33 Year-on-year change rate of interurban transport passengers in Spain, August = **1.4** as written "1,4%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Interurban -1.4% August 2025; redundant with p2's statement and not used numerically.] quote: "mientras que el interurbano descendió un 1,4% (117,8 millones)"
  - p34 Year-on-year growth rate of interurban bus passengers in Spain, August = **1.8** as written "1,8%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Duplicate of p6.] quote: "dentro del transporte interurbano, el autobús fue el único medio con crecimiento (1,8%) en tasa anual"
  - p35 Year-on-year change rate of total rail transport passengers in Spain, August = **5.9** as written "5,9%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Conflicts in sign with p29 and is not needed; unreliable secondary reporting.] quote: "El transporte ferroviario en su conjunto disminuyó un 5,9%."
  - p36 Year-on-year growth rate of special and discretionary transport passengers in Sp = **11.7** as written "11,7%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Duplicate of p3.] quote: "con más de 21,6 millones de usuarios (11,7% de aumento)"
- dropped by code checks: 18 (scale word 'million' not supported by quote or table header: 15; value_as_written not in quote as a whole number: 3)

### b1 [own_history] d1

Hypothesis: The single most valuable missing input is the actual ETP total passenger level for a recent month (e.g. July 2026 or August 2025 in absolute passengers, not just growth rates). With a level plus the 2.6% August 2025 growth and the recent monthly trend, a yoy_scaling route becomes executable and would dominate the current growth-only extrapolation.

Queries issued by the searcher: INE Estadística de Transporte de Personas millones de viajeros agosto 2025; Estadística de Transporte de Personas ETP julio 2026 viajeros; "362.4 millones" agosto 2025 INE transporte viajeros miles total nacional tabla; INE jaxiT3 "Viajeros transportados" total transporte urbano interurbano especial mensual miles 2026

- `https://www.ine.es/dyngs/Prensa/TV0726.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ine.es/dyngs/Prensa/TV0825.htm` -> **snapshot** (snapshot 20251216205557); points raw/verified 15/6
  - p37 Year-on-year growth rate of total public transport passengers, August 2025 vs Au = **2.6** as written "2,6%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El número de usuarios del transporte público aumentó un 2,6% en agosto respecto al mismo mes de 2024."
  - p38 Year-on-year growth rate of urban transport passengers, August 2025 = **4** as written "4,0%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte urbano subió un 4,0% en tasa anual y el interurbano cayó un 1,4%."
  - p39 Year-on-year growth rate of special and discretionary transport passengers, Augu = **11.7** as written "11,7%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "Más de 21,6 millones de usuarios utilizaron transporte especial y discrecional en agosto, lo que supuso un incremento del 11,7% en tasa anual."
  - p40 Year-on-year growth rate of interurban bus passengers, August 2025 = **1.8** as written "1,8%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "Dentro del interurbano, destacó el incremento del 1,8% en el transporte por autobús."
  - p41 Year-on-year growth rate of metro passengers, August 2025 = **3.2** as written "3,2%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte por metro aumentó un 3,2% en tasa anual y el transporte urbano por autobús aumentó un 4,5%."
  - p42 Year-on-year growth rate of urban bus passengers, August 2025 = **4.5** as written "4,5%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte por metro aumentó un 3,2% en tasa anual y el transporte urbano por autobús aumentó un 4,5%."
- `https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736176906&idp=1254735576820&menu=ultiDatos` -> **snapshot** (snapshot 20260616055709); points raw/verified 8/4
  - p43 Year-on-year variation of total public transport passengers in Spain, April 2026 = **6.1** as written "6,1", value check pending percent (2026-04-01..2026-04-30) [keep: ] quote: "El número de usuarios del transporte público aumentó un 6,1% en abril respecto al mismo mes de 2025."
  - p44 Year-on-year variation of urban transport passengers in Spain, April 2026 (perce = **8.4** as written "8,4", value check pending percent (2026-04-01..2026-04-30) [keep: ] quote: "El transporte urbano subió un 8,4% en tasa anual y el interurbano un 1,2%."
  - p45 Year-on-year variation of interurban transport passengers in Spain, April 2026 ( = **1.2** as written "1,2", value check pending percent (2026-04-01..2026-04-30) [keep: ] quote: "El transporte urbano subió un 8,4% en tasa anual y el interurbano un 1,2%."
  - p46 Year-on-year variation of special and discretionary transport passengers in Spai = **6.1** as written "6,1", value check pending percent (2026-04-01..2026-04-30) [keep: ] quote: "\| Transporte especial y discrecional \| \| 45.600 \| 6,1 \|"
- `https://confebus.org/publicaciones/ver/5025/ine-estadistica-transporte-de-viajeros-agosto-2025` -> **snapshot** (snapshot 20260511143144); points raw/verified 15/5
  - p47 Year-on-year growth of total public transport passengers in Spain, August = **2.6** as written "2,6%", value check ok % (2025-08-01..2025-08-31) [keep: ] quote: "más de 362,4 millones de pasajeros utilizaron el transporte público en agosto, un 2,6% más que en el mismo mes del año 2024."
  - p48 Year-on-year growth of urban transport passengers in Spain, August = **4** as written "4,0%", value check ok % (2025-08-01..2025-08-31) [keep: ] quote: "el transporte urbano fue utilizado por más de 222,8 millones de viajeros en agosto, un 4,0% más que en el mismo mes del año 2024."
  - p49 Year-on-year growth of special and discretionary transport passengers in Spain,  = **11.7** as written "11,7%", value check ok % (2025-08-01..2025-08-31) [keep: ] quote: "más de 21,6 millones de usuarios utilizaron transporte especial y discrecional en agosto, lo que supuso un incremento del 11,7% en tasa anual."
  - p50 Year-on-year growth of bus transport passengers in Spain, August = **7.8** as written "7,8%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte en autobús sigue al alza: un 7,8% más de viajeros en agosto"
  - p51 Year-on-year growth of cumulative bus transport passengers in Spain, January to  = **5.66** as written "5,66%", value check pending % (2025-01-01..2025-08-31) [keep: ] quote: "En cuanto al acumulado de los ocho primeros meses del año, el incremento ha sido del 5,66%, con respecto a los mismos meses de 2024"
- dropped by code checks: 23 (scale word 'million' not supported by quote or table header: 15; value_as_written not in quote as a whole number: 4; scale word 'thousand' not supported by quote or table header: 4)

### b2 [related_series] d2

Hypothesis: Mode-level absolute August 2025 levels (urban 222.8M, interurban 117.8M, special/discretionary 21.6M) sum to a total that, grown by recent YoY rates, gives a bottom-up August 2026 estimate. This unlocks a sum-coverage method and cross-checks the top-down growth route.

Queries issued by the searcher: INE Estadística de Transporte de Personas agosto 2025 viajeros transporte urbano interurbano especial 222,8 117,8 21,6; INE ETP agosto 2025 transporte de personas más de 456 millones viajeros; INE Estadística de Transporte de Personas agosto 2026 datos provisionales; site:ine.es TV0826 Estadística de Transporte de Personas agosto 2026; "agosto 2026" "transporte urbano" viajeros INE

- `https://www.ine.es/dyngs/Prensa/TV0726.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ine.es/dyngs/Prensa/TV0825.htm` -> **snapshot** (snapshot 20251216205557); points raw/verified 15/8
  - p52 Year-on-year growth rate of total public transport passengers in Spain, August 2 = **2.6** as written "2,6%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El número de usuarios del transporte público aumentó un 2,6% en agosto respecto al mismo mes de 2024."
  - p53 Year-on-year growth rate of urban transport passengers in Spain, August 2025 vs  = **4** as written "4,0%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte urbano subió un 4,0% en tasa anual y el interurbano cayó un 1,4%."
  - p54 Year-on-year growth rate of special and discretionary transport passengers in Sp = **11.7** as written "11,7%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "Más de 21,6 millones de usuarios utilizaron transporte especial y discrecional en agosto, lo que supuso un incremento del 11,7% en tasa anual."
  - p55 Year-on-year growth rate of special transport passengers in Spain, August 2025 v = **15.7** as written "15,7%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El número de pasajeros del transporte especial subió un 15,7% y superó los 5,3 millones de usuarios."
  - p56 Year-on-year growth rate of discretionary transport passengers in Spain, August  = **10.4** as written "10,4%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "el transporte discrecional creció un 10,4% respecto al mismo mes del año 2024, con más de 16,3 millones de viajeros."
  - p57 Year-on-year growth rate of interurban bus passengers in Spain, August 2025 vs A = **1.8** as written "1,8%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "Dentro del interurbano, destacó el incremento del 1,8% en el transporte por autobús."
  - p58 Year-on-year growth rate of urban metro passengers in Spain, August 2025 vs Augu = **3.2** as written "3,2%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte por metro aumentó un 3,2% en tasa anual y el transporte urbano por autobús aumentó un 4,5%."
  - p59 Year-on-year growth rate of urban bus passengers in Spain, August 2025 vs August = **4.5** as written "4,5%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte por metro aumentó un 3,2% en tasa anual y el transporte urbano por autobús aumentó un 4,5%."
- `https://confebus.org/publicaciones/ver/5025/ine-estadistica-transporte-de-viajeros-agosto-2025` -> **snapshot** (snapshot 20260511143144); points raw/verified 16/7
  - p60 Total public transport passengers YoY growth rate, August = **2.6** as written "2,6%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "más de 362,4 millones de pasajeros utilizaron el transporte público en agosto, un 2,6% más que en el mismo mes del año 2024."
  - p61 Urban transport passengers YoY growth rate, August = **4** as written "4,0%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "el transporte urbano fue utilizado por más de 222,8 millones de viajeros en agosto, un 4,0% más que en el mismo mes del año 2024."
  - p62 Special and discretionary transport passengers YoY growth rate, August = **11.7** as written "11,7%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "más de 21,6 millones de usuarios utilizaron transporte especial y discrecional en agosto, lo que supuso un incremento del 11,7% en tasa anual."
  - p63 Special transport passengers YoY growth rate, August = **15.7** as written "15,7%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El número de pasajeros del transporte especial subió un 15,7% y superó los 5,3 millones de usuarios."
  - p64 Discretionary transport passengers YoY growth rate, August = **10.4** as written "10,4%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "el transporte discrecional creció un 10,4% respecto al mismo mes del año 2024, con más de 16,3 millones de viajeros."
  - p65 Bus transport passengers YoY growth rate, August = **7.8** as written "7,8%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "cuya media, con más de 226 millones de viajeros, se situó un 7,8% por encima de la del mismo mes de 2024."
  - p66 Bus transport passengers cumulative January-August YoY growth rate = **5.66** as written "5,66%", value check pending % (2025-01-01..2025-08-31) [keep: ] quote: "En cuanto al acumulado de los ocho primeros meses del año, el incremento ha sido del 5,66%, con respecto a los mismos meses de 2024"
- `https://www.ine.es/dyngs/INEbase/operacion.htm?c=Estadistica_C&cid=1254736176906&menu=resultados&secc=1254736195091&idp=1254735576820` -> **snapshot** (snapshot 20230326055513); points raw/verified 0/0
- dropped by code checks: 16 (scale word 'million' not supported by quote or table header: 14; value_as_written not in quote as a whole number: 2)

### b3 [forecasts_markets] d7

Hypothesis: A published 2026 transport-demand nowcast or MITMA monthly mobility statistic for summer 2026 would resolve whether the 2025 growth trend (~2.6%) persisted, shrank, or accelerated into August 2026 — the assumption contributing the largest uncertainty.

Queries issued by the searcher: INE Estadística de Transporte de Personas ETP pasajeros 2026; MITMA movilidad transporte público pasajeros julio 2026; INE "transporte de viajeros" julio 2026 datos provisionales fecha publicación agosto 2026; INE transporte de viajeros agosto 2025 "millones de pasajeros" agosto 2025 un 3,0%

- `https://www.ine.es/dyngs/Prensa/TV0726.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ine.es/dyngs/Prensa/TV0726.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://apps.fomento.gob.es/BDOTLE/visorBDpop.aspx?i=2024` -> **snapshot** (snapshot 20250414132910); points raw/verified 0/0
- `https://www.viaempresa.cat/es/economia/metro-barcelona-cierra-julio-record-rompe-barrera-40-millones-usuarios_2240239_102.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['spain transport passengers', 'ine etp august', 'spain public transport']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p19', 'p25', 'p31'] All report the same INE August 2025 total-public-transport YoY growth of 2.6%; p19 is the INE release, p31 a secondary outlet repeating it. Same underlying measurement, not independent.
- corroborating: ['p2', 'p20', 'p26', 'p32'] Urban transport August 2025 YoY growth of 4.0% (p32 adds the level 222.8 million). Same INE source.
- corroborating: ['p3', 'p21', 'p30', 'p36'] Special+discretionary August 2025 growth 11.7% with level >21.6 million; same INE figure repeated.
- corroborating: ['p4', 'p5'] Special (15.7%, >5.3M) and discretionary (10.4%, >16.3M) subcomponents sum consistently to the 11.7% / 21.6M combined figure.
- corroborating: ['p6', 'p29', 'p34'] Interurban bus August 2025 growth 1.8%; p29/p34 add that air fell 0.3%, sea 1.6%, rail rose 5.9% (note p35 states rail 'disminuyó 5.9%' which conflicts in sign with p29's 'ferrocarril un 5.9%' growth)
- conflicting: ['p29', 'p35'] p29 lists rail +5.9% while p35 says rail fell 5.9%; sign ambiguity in secondary reporting. Neither is used numerically for the target.
- corroborating: ['p7', 'p8', 'p27', 'p28'] Metro 3.2% and urban bus 4.5% August 2025, consistent with the 4.0% urban aggregate.
- corroborating: ['p22', 'p23', 'p24'] July 2025 urban 6.2%, interurban -0.2%, special/discretionary 3.3% — same INE table, different month; useful for trend context only.
- corroborating: ['p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15'] Early-August 2026 operational indicators (Adif trains, Aena flights, airport movements) all point to a modestly positive early-August travel season (~3% more flights than 2025).
- corroborating: ['p16', 'p17'] Air Europa August 2026 daily flights 220-225, a range point; consistent with normal August operations.
- corroborating: ['p18'] 36% of Spaniards holidaying in August supports August being a peak month, but is contextual only.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p37', 'p47', 'p52', 'p60'] All state the same INE August 2025 total public transport YoY growth of 2.6%; p47/p60 (Confebus) reproduce the INE release, so they are not independent measurements.
- corroborating: ['p2', 'p38', 'p48', 'p53', 'p61'] Same INE August 2025 urban transport growth of 4.0%, repeated across INE and Confebus restatements; one underlying measurement.
- corroborating: ['p3', 'p39', 'p49', 'p54', 'p62'] Same INE August 2025 special+discretionary growth of 11.7% and level of 21.6 million; repeated copies.
- corroborating: ['p4', 'p55', 'p63'] Special transport August 2025: +15.7%, >5.3 million; same INE source.
- corroborating: ['p5', 'p56', 'p64'] Discretionary transport August 2025: +10.4%, >16.3 million; same INE source.
- corroborating: ['p6', 'p29', 'p40', 'p57'] Interurban bus August 2025 +1.8%; p29 also gives air -0.3%, sea -1.6%, rail +5.9% for the same month.
- corroborating: ['p7', 'p41', 'p58'] Metro August 2025 +3.2%; same INE release.
- corroborating: ['p8', 'p42', 'p59'] Urban bus August 2025 +4.5%; same INE release.
- corroborating: ['p22', 'p23', 'p24'] July 2025 INE table row: urban +6.2%, interurban -0.2%, special/discretionary +3.3%; a different month, useful as a seasonal/trend analogue, not a contradiction of August figures.
- corroborating: ['p43', 'p44', 'p45', 'p46'] April 2026 INE release: total +6.1%, urban +8.4%, interurban +1.2%, special/discretionary +6.1%; the most recent kept growth evidence and the basis for the 2026 growth factor.
- corroborating: ['p50', 'p51', 'p65', 'p66'] Confebus bus aggregates: August 2025 bus +7.8% (mean >226 million) and Jan-Aug cumulative +5.66%; consistent with INE bus components but a derived aggregate, not independent.
- contextual: ['p11'] Aena first-August-weekend 2026 flights +3% YoY is a weak leading indicator for air passengers; flights are not passengers and only cover one weekend, so it can only inform the direction of the 2026 gr

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | August 2026 vs August 2025 growth factor for total public transport passengers | 1.045 | 0.99..1.1 | 0.9334..1.167 (widened) | ratio | unused | Anchored on the April 2026 INE total growth of +6.1% (p43) and the August 2025 total growth of +2.6% (p1). August is a tourism-peak month with historically lower growth than spring, so the factor sits between the two, slightly below the April rate. Aena's +3% first-weekend flights (p11) supports con | The 2026 monthly growth trend observed in April persists through August with normal August seasonality. | A published June/July 2026 ETP total showing growth well below 2% or above 8%, or a major transport disruption in August 2026. |
| a3 | August 2026 vs August 2025 growth factor for urban transport passengers | 1.06 | 1..1.13 | 0.9508..1.188 (widened) | ratio | unused | Urban transport grew 8.4% in April 2026 (p44) and 4.0% in August 2025 (p2); August urban growth is typically lower than spring, so the factor is set between them, closer to the August 2025 rate. | Urban metro/bus demand growth in August 2026 is between the August 2025 and April 2026 rates. | Operator data (Madrid/Barcelona metro, EMT) showing urban ridership flat or falling in August 2026. |
| a4 | August 2026 vs August 2025 growth factor for interurban transport passengers | 1.02 | 0.97..1.07 | 0.9112..1.139 (widened) | ratio | unused | Interurban grew only 1.2% in April 2026 (p45) and fell 1.4% in August 2025 (p38); rail liberalisation and tourism support modest growth, so the factor is set slightly above 1. | Interurban demand grows modestly in August 2026, consistent with the April 2026 trend. | Aena/RENFE August 2026 data showing interurban passenger declines. |
| a5 | August 2026 vs August 2025 growth factor for special and discretionary transport passengers | 1.07 | 1..1.15 | 0.9592..1.199 (widened) | ratio | unused | Special/discretionary grew 6.1% in April 2026 (p46) and 11.7% in August 2025 (p3); August is the peak discretionary month, so the factor is set between the two rates. | Discretionary/tourism-linked transport continues to grow in August 2026 at a rate between the April 2026 and August 2025 rates. | Tourism arrival data (Frontur) showing a summer 2026 decline, or operator reports of weaker coach/charter demand. |
| a6 | Interurban share of August 2025 total public transport passengers | 0.325 | 0.3..0.35 | 0.2291..0.4583 (widened) | ratio | unused | Derived from the August 2025 INE/Confebus levels: total 'more than 362.4M' (p47), urban 'more than 222.8M' (p48), special/discretionary 'more than 21.6M' (p49). Residual interurban ≈ 362.4 − 222.8 − 21.6 = 118.0M, i.e. ≈0.326 of the total. Range reflects the 'more than' rounding and possible small c | The August 2025 component split is representative of the interurban share of the ETP total. | A revised August 2025 release with materially different component levels, or evidence that interurban's share shifted sharply in 2026. |

Rejected by code:

- a10 August 2025 total public transport passengers in Spain, millions (level anchor): target-like: a level of the target quantity (unit or name matches the target, no ratio wording)
- a11 August 2025 urban transport passengers in Spain, millions (level anchor): target-like: a level of the target quantity (unit or name matches the target, no ratio wording)
- a12 August 2025 special and discretionary transport passengers in Spain, millions (l: target-like: a level of the target quantity (unit or name matches the target, no ratio wording)

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | n/a |  | [] |  | 0.00 |  | input a10: assumption a10 was rejected (target-like: a level of the target quantity (unit or name matches the target, no ratio wording)) |
| m2 | formula_mc | n/a |  | [] |  | 0.00 |  | input a11: assumption a11 was rejected (target-like: a level of the target quantity (unit or name matches the target, no ratio wording)) |

- m1 coverage: the whole target
- m2 coverage: sum over channel of urban, interurban, special_discretionary

Result: central **n/a** person, 80% interval [n/a, n/a] person, basis no_method (no method produced an estimate, so there is no interval), weight rule None, weight on methods that use assumptions 0.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

No estimate: no estimation method could be computed from the verified evidence.

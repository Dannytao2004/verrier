# Evidence ledger: fc_es_transit_2026_08

- Question: Assume today is 2026-09-11. You know nothing published after this date. Estimate the total number of passengers who used public transport in Spain in August 2026 (urban, interurban and special/discretionary transport combined), as it will be first reported in the provisional data of the National Statistics Institute's (INE) Passenger Transport Statistics (Estadística de Transporte de Personas).
- as_of: 2026-09-11
- Pinned target: Total passengers carried by public transport in Spain (urban, interurban, and special/discretionary transport combined) during August 2026, as first reported in INE's Estadística de Transporte de Personas (Passenger Transport Statistics) provisional data; counted as passenger journeys/trips (each bo | unit passengers (journeys) | period 2026-08-01..2026-08-31 | publisher Instituto Nacional de Estadística (INE), Estadística de Transporte de Personas (ETP)

- Official value (scoring only, never shown to the agent): 371,623,271

## Directions and pages

### d1 [own_history] INE ETP time series

Hypothesis: August 2026 total passengers can be projected from the ETP monthly series: August 2025 level plus trend growth plus any August-specific seasonal factor. The ETP publishes monthly totals by transport class; the August value in prior years anchors the level and the July-to-August seasonal ratio anchors the shape.

Queries issued by the searcher: Estadística de Transporte de Personas INE viajeros agosto 2025; INE ETP serie mensual viajeros transporte urbano interurbano especial; Estadística de Transporte de Viajeros agosto 2024 datos provisionales millones de pasajeros transporte público; Estadística de Transporte de Personas julio 2026 INE 449,0 millones viajeros datos provisionales

- `https://www.ine.es/dyngs/Prensa/TV0825.pdf` -> **snapshot** (snapshot 20251221032913); points raw/verified 15/9
  - p1 Annual growth rate of total public transport passengers, Spain, August 2025 vs A = **2.6** as written "2,6%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El número de usuarios del transporte público aumentó un 2,6% en agosto respecto al mismo mes de 2024."
  - p2 Urban transport annual growth rate, Spain, August 2025 = **4** as written "4,0%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte urbano subió un 4,0% en tasa anual y el interurbano cayó un 1,4%."
  - p3 Special and discretionary transport annual growth rate, Spain, August 2025 = **11.7** as written "11,7%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "Más de 21,6 millones de usuarios utilizaron transporte especial y discrecional en agosto, lo que supuso un incremento del 11,7% en tasa anual."
  - p4 Urban transport annual growth rate, Spain, August 2024 = **5.8** as written "5,8", value check pending percent (2024-08-01..2024-08-31) [DISCARD: Superseded vintage of August 2024 urban growth (5.8%); the later INE vintage p114 gives 5.3%, corroborated by Confebus p] quote: "2024 Agosto 5,8 7,1 -1,1"
  - p5 Interurban transport annual growth rate, Spain, August 2024 = **7.1** as written "7,1", value check pending percent (2024-08-01..2024-08-31) [DISCARD: Superseded vintage of August 2024 interurban growth (7.1%); later vintage p115 gives 3.4%, corroborated by Confebus p12.] quote: "2024 Agosto 5,8 7,1 -1,1"
  - p6 Special and discretionary transport annual growth rate, Spain, August 2024 = **-1.1** as written "-1,1", value check pending percent (2024-08-01..2024-08-31) [DISCARD: Superseded vintage of August 2024 special growth (-1.1%); later vintage p116 gives -10.7%.] quote: "2024 Agosto 5,8 7,1 -1,1"
  - p7 Urban transport annual growth rate, Spain, July 2025 = **6.2** as written "6,2", value check pending percent (2025-07-01..2025-07-31) [keep: ] quote: "Julio 6,2 -0,2 3,3"
  - p8 Interurban transport annual growth rate, Spain, July 2025 = **-0.2** as written "-0,2", value check pending percent (2025-07-01..2025-07-31) [keep: ] quote: "Julio 6,2 -0,2 3,3"
  - p9 Special and discretionary transport annual growth rate, Spain, July 2025 = **3.3** as written "3,3", value check pending percent (2025-07-01..2025-07-31) [keep: ] quote: "Julio 6,2 -0,2 3,3"
- `https://www.ine.es/dyngs/Prensa/TV0726.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://confebus.org/publicaciones/ver/4668/ine-estadistica-transporte-de-viajeros-agosto-2024` -> **snapshot** (snapshot 20260606190408); points raw/verified 15/7
  - p10 Year-on-year growth rate of total public transport passengers in Spain, August 2 = **3.7** as written "3,7%", value check pending % (2024-08-01..2024-08-31) [DISCARD: Already discarded in round 1; August 2024 total growth 3.7% conflicts with the later-vintage component-consistent pictur] quote: "más de 346,3 millones de pasajeros utilizaron el transporte público en agosto, un 3,7% más que en el mismo mes del año 2023."
  - p11 Year-on-year growth rate of urban transport passengers in Spain, August 2024 vs  = **5.3** as written "5,3%", value check pending % (2024-08-01..2024-08-31) [keep: ] quote: "El transporte urbano fue utilizado por más de 213,4 millones de viajeros en agosto, un 5,3% más que en el mismo mes del año 2023."
  - p12 Year-on-year growth rate of interurban transport passengers in Spain, August 202 = **3.4** as written "3,4%", value check pending % (2024-08-01..2024-08-31) [keep: ] quote: "más de 115,3 millones de viajeros utilizaron el transporte interurbano en agosto, lo que supuso un incremento del 3,4% respecto al mismo mes de 2023."
  - p13 Total public transport passengers in Spain, August 2024 vs August 2019 growth ra = **9.6** as written "9,6%", value check pending % (2024-08-01..2024-08-31) [DISCARD: Already discarded; 2019 comparison not needed for a 2025-to-2026 projection.] quote: "Respecto a agosto de 2019, el incremento de viajeros ha sido un 9,6%, así como de casi un 3% superior al de 2023, año de cifras récord."
  - p14 Total public transport passengers in Spain, August 2024 vs August 2023 growth ra = **2.8** as written "2,8%", value check pending % (2024-08-01..2024-08-31) [DISCARD: Already discarded; duplicate/conflicting August 2024 total growth.] quote: "siendo la media un 9,6% superior a la de agosto de 2019 y situándose un 2,8% por encima de la del mismo mes de 2023."
  - p15 Cumulative total public transport passengers in Spain, first eight months of 202 = **7.44** as written "7,44%", value check pending % (2024-01-01..2024-08-31) [DISCARD: Already discarded; cumulative 8-month 2024 figure not aligned to the August target period.] quote: "En cuanto al acumulado de los ocho primeros meses de 2024, con respecto a los mismos meses de 2019, el crecimiento has sido del 7,44%."
  - p16 Urban transport passengers in Spain, August 2024 vs August 2019 growth rate = **15** % (2024-08-01..2024-08-31) [DISCARD: Already discarded; 2019 comparison not needed.] quote: "En el transporte urbano la demanda de agosto de 2024 se situó casi un 15% por encima de la de 2019"
- `https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736176906&idp=1254735576820` -> **snapshot** (snapshot 20260421011958); points raw/verified 8/2
  - p17 Year-on-year change in urban transport passengers, Spain, February 2026 = **2** as written "2,0", value check pending percent (2026-02-01..2026-02-28) [keep: ] quote: "El transporte urbano subió un 2,0% en tasa anual y el interurbano cayó un 4,2%."
  - p18 Year-on-year change in special and discretionary transport passengers, Spain, Fe = **-1.4** as written "-1,4", value check pending percent (2026-02-01..2026-02-28) [keep: ] quote: "\| Transporte especial y discrecional \| \| 41.125 \| -1,4 \|"
- dropped by code checks: 20 (number: scale word 'millones' is not English or CJK (not supported): 4; value_as_written not in quote as a whole number: 5; scale word 'thousand' not supported by quote or table header: 5; scale word 'million' not supported by quote or table header: 6)

### d2 [related_series] Component decomposition by transport class

Hypothesis: Total = urban + interurban + special/discretionary passengers. Each component has its own trend and seasonality; summing separately estimated components reduces error versus a single aggregate projection. Urban and interurban are dominated by bus and metro; special/discretionary is dominated by bus charter and school/works services (seasonally low in August).

Queries issued by the searcher: INE Estadística de Transporte de Personas viajeros agosto 2025 urbano interurbano especial discrecional; INE ETP viajeros transporte urbano interurbano especial discrecional agosto 2024 autobús metro; INE Estadística de Transporte de Viajeros julio 2026 viajeros transporte público; "transporte de viajeros" INE 2026 millones de pasajeros transporte urbano interurbano junio

- `https://www.ine.es/dyngs/Prensa/TV0726.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ine.es/dyngs/Prensa/TV0825.pdf` -> **snapshot** (snapshot 20251221032913); points raw/verified 15/6
  - p19 Total public transport passengers, Spain, annual growth rate, August 2025 vs Aug = **2.6** as written "2,6%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El número de usuarios del transporte público aumentó un 2,6% en agosto respecto al mismo mes de 2024."
  - p20 Urban transport passengers, Spain, annual growth rate, August 2025 vs August 202 = **4** as written "4,0%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte urbano subió un 4,0% en tasa anual y el interurbano cayó un 1,4%."
  - p21 Special and discretionary transport passengers, Spain, annual growth rate, Augus = **11.7** as written "11,7%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "Más de 21,6 millones de usuarios utilizaron transporte especial y discrecional en agosto, lo que supuso un incremento del 11,7% en tasa anual."
  - p22 Urban metro passengers, Spain, annual growth rate, August 2025 vs August 2024 = **3.2** as written "3,2%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte por metro aumentó un 3,2% en tasa anual y el transporte urbano por autobús aumentó un 4,5%."
  - p23 Urban bus passengers, Spain, annual growth rate, August 2025 vs August 2024 = **4.5** as written "4,5%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte por metro aumentó un 3,2% en tasa anual y el transporte urbano por autobús aumentó un 4,5%."
  - p24 Special and discretionary transport annual growth rate, Spain, August 2024 vs Au = **-1.1** as written "-1,1", value check pending percent (2024-08-01..2024-08-31) [DISCARD: Already discarded; superseded August 2024 special vintage.] quote: "Agosto 5,8 7,1 -1,1"
- `https://anetra-informa.es/noticias/el-regular-especial-y-el-discrecional-suman-viajeros-en-agosto-un-157-y-un-104-respectivamente/` -> **snapshot** (snapshot 20260215133242); points raw/verified 0/0
- `https://www.ine.es/jaxi/Tabla.htm?tpx=78959&L=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 9 (number: scale word 'millones' is not English or CJK (not supported): 6; value_as_written not in quote as a whole number: 1; scale word 'thousand' not supported by quote or table header: 2)

### d3 [base_rates] Seasonal index and growth-rate transfer

Hypothesis: The August share of annual ETP passengers and the year-over-year August growth rate are stable enough to transfer from 2023-2025 to 2026. Total_Aug_2026 ≈ Total_Aug_2025 × (1 + g), where g is the recent 12-month growth rate adjusted for August-specific seasonality.

Queries issued by the searcher: INE Estadística de Transporte de Personas viajeros anual 2025 total; transporte público España crecimiento viajeros 2026 INE; "Estadística de Transporte de Viajeros" agosto 2025 datos provisionales millones de pasajeros INE nota de prensa; INE transporte de viajeros junio 2026 datos provisionales pasajeros aumento anual

- `https://www.ine.es/dyngs/Prensa/TV0825.pdf` -> **snapshot** (snapshot 20251221032913); points raw/verified 15/9
  - p25 Total public transport passengers year-over-year growth rate, August 2025 vs Aug = **2.6** as written "2,6%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El número de usuarios del transporte público aumentó un 2,6% en agosto respecto al mismo mes de 2024."
  - p26 Urban transport year-over-year growth rate, August 2025 = **4** as written "4,0%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte urbano subió un 4,0% en tasa anual y el interurbano cayó un 1,4%."
  - p27 Special and discretionary transport year-over-year growth rate, August 2025 = **11.7** as written "11,7%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "Más de 21,6 millones de usuarios utilizaron transporte especial y discrecional en agosto, lo que supuso un incremento del 11,7% en tasa anual."
  - p28 Urban transport year-over-year growth rate, July 2025 = **6.2** as written "6,2", value check pending percent (2025-07-01..2025-07-31) [DISCARD: Already discarded; duplicate of p7.] quote: "Julio 6,2 -0,2 3,3"
  - p29 Interurban transport year-over-year growth rate, July 2025 = **-0.2** as written "-0,2", value check pending percent (2025-07-01..2025-07-31) [DISCARD: Already discarded; duplicate of p8.] quote: "Julio 6,2 -0,2 3,3"
  - p30 Special and discretionary transport year-over-year growth rate, July 2025 = **3.3** as written "3,3", value check pending percent (2025-07-01..2025-07-31) [DISCARD: Already discarded; duplicate of p9.] quote: "Julio 6,2 -0,2 3,3"
  - p31 Urban transport year-over-year growth rate, June 2025 = **6.8** as written "6,8", value check pending percent (2025-06-01..2025-06-30) [keep: ] quote: "Junio 6,8 9,7 2,0"
  - p32 Interurban transport year-over-year growth rate, June 2025 = **9.7** as written "9,7", value check pending percent (2025-06-01..2025-06-30) [keep: ] quote: "Junio 6,8 9,7 2,0"
  - p33 Special and discretionary transport year-over-year growth rate, June 2025 = **2** as written "2,0", value check pending percent (2025-06-01..2025-06-30) [keep: ] quote: "Junio 6,8 9,7 2,0"
- `https://ine.es/dyngs/INEbase/en/operacion.htm?c=Estadistica_C&cid=1254736176906&idp=1254735576820` -> **snapshot** (snapshot 20260122225509); points raw/verified 11/7
  - p34 Total passengers transported YoY variation, November 2025 vs November 2024 (%) = **4.5** percent (2025-11-01..2025-11-30) [keep: ] quote: "\| Total \| \| 508,701 \| 4.5 \|"
  - p35 City transport passengers YoY variation, November 2025 vs November 2024 (%) = **6.8** percent (2025-11-01..2025-11-30) [keep: ] quote: "\| City transport \| \| 318,771 \| 6.8 \|"
  - p36 Inter-city transport passengers YoY variation, November 2025 vs November 2024 (% = **1.2** percent (2025-11-01..2025-11-30) [keep: ] quote: "\| Inter-city transport \| \| 143,569 \| 1.2 \|"
  - p37 Special and unscheduled transport passengers YoY variation, November 2025 vs Nov = **-0.6** percent (2025-11-01..2025-11-30) [keep: ] quote: "\| Special and unscheduled transport \| \| 46,361 \| -0.6 \|"
  - p38 Total public transport passengers YoY increase, October (vs October 2024) (%) = **4.4** % (2025-10-01..2025-10-31) [keep: ] quote: "The number of passengers using public transport increased by 4.4% in October, as compared with the same month of 2024."
  - p39 City transport passengers annual rate increase, October (%) = **5.4** % (2025-10-01..2025-10-31) [keep: ] quote: "The annual rate for city transport increased by 5.4% and for inter-city transport by 3.6%."
  - p40 Inter-city transport passengers annual rate increase, October (%) = **3.6** % (2025-10-01..2025-10-31) [keep: ] quote: "The annual rate for city transport increased by 5.4% and for inter-city transport by 3.6%."
- `https://ine.es/dyngs/Prensa/TV1225.htm?print=1` -> **snapshot** (snapshot 20260210090821); points raw/verified 15/6
  - p41 Annual growth rate of total public transport passengers, 2025 vs 2024 = **3.7** as written "3,7%", value check pending % (2025-01-01..2025-12-31) [keep: ] quote: "En el conjunto del año 2025 el número de usuarios se incrementó un 3,7%."
  - p42 Total public transport passengers, December 2025 vs December 2024, annual growth = **3.6** as written "3,6%", value check pending % (2025-12-01..2025-12-31) [keep: ] quote: "El número de usuarios del transporte público aumentó un 3,6% en diciembre respecto al mismo mes de 2024."
  - p43 Special and discretionary transport passengers, December 2025 vs December 2024,  = **4.6** as written "4,6%", value check pending % (2025-12-01..2025-12-31) [keep: ] quote: "Más de 37,3 millones de usuarios utilizaron transporte especial y discrecional en diciembre, lo que supuso un incremento del 4,6% en tasa anual."
  - p44 Urban transport passengers, December 2025 vs December 2024, annual growth rate = **3.4** as written "3,4%", value check pending % (2025-12-01..2025-12-31) [keep: ] quote: "El transporte urbano subió un 3,4% en tasa anual y el interurbano un 3,6%."
  - p45 Interurban transport passengers, December 2025 vs December 2024, annual growth r = **3.6** as written "3,6%", value check pending % (2025-12-01..2025-12-31) [keep: ] quote: "El transporte urbano subió un 3,4% en tasa anual y el interurbano un 3,6%."
  - p46 Interurban bus passengers, December 2025 vs December 2024, annual growth rate = **6.8** as written "6,8%", value check pending % (2025-12-01..2025-12-31) [keep: ] quote: "Dentro del interurbano, destacó el incremento del 6,8% en el transporte por autobús."
- `https://www.ine.es/dyngs/Prensa/TV0526.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 19 (number: scale word 'millones' is not English or CJK (not supported): 9; value_as_written not in quote as a whole number: 1; scale word 'thousand' not supported by quote or table header: 5; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 4)

### d4 [related_series] Metro and large-city operator statistics

Hypothesis: Metro Madrid, Metro Barcelona, EMT Madrid, TMB Barcelona and other large operators publish monthly passenger counts that are the dominant urban component. Aggregating major operator August 2026 (or August 2025 with growth) figures and scaling to national urban total via their historical share constrains the urban component.

Queries issued by the searcher: Metro Madrid viajeros agosto 2025; TMB Barcelona viatgers agost 2025 metro bus; INE Estadística de Transporte de Viajeros agosto 2025 nota de prensa 362,4 millones; EMT Madrid viajeros agosto 2025 millones autobuses municipales

- `https://www.ine.es/dyngs/Prensa/TV0825.htm?print=1` -> **snapshot** (snapshot 20251227114854); points raw/verified 15/7
  - p47 Annual growth rate of total public transport passengers in Spain, August 2025 vs = **2.6** as written "2,6%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El número de usuarios del transporte público aumentó un 2,6% en agosto respecto al mismo mes de 2024."
  - p48 Annual growth rate of urban transport passengers in Spain, August 2025 vs August = **4** as written "4,0%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte urbano subió un 4,0% en tasa anual y el interurbano cayó un 1,4%."
  - p49 Annual growth rate of metro transport passengers in Spain, August 2025 vs August = **3.2** as written "3,2%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte por metro aumentó un 3,2% en tasa anual y el transporte urbano por autobús aumentó un 4,5%."
  - p50 Annual growth rate of urban bus transport passengers in Spain, August 2025 vs Au = **4.5** as written "4,5%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte por metro aumentó un 3,2% en tasa anual y el transporte urbano por autobús aumentó un 4,5%."
  - p51 Annual growth rate of bus transport passengers in Comunidad de Madrid, August 20 = **11.8** as written "11,8%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El número de viajeros en el transporte por autobús presentó las mayores subidas en Comunidad de Madrid (11,8%), Extremadura (10,7%) y País Vasco (6,9%)."
  - p52 Annual growth rate of bus transport passengers in Cataluña, August 2025 vs Augus = **-0.5** as written "-0,5%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El único descenso en el transporte por autobús se dio en Cataluña (-0,5%)."
  - p53 Annual change rate of metro passengers in Palma, August 2025 vs August 2024 (lar = **56** as written "56,0%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El metro de Palma presentó el mayor incremento, del 56,0%."
- `https://www.europapress.es/madrid/noticia-usuarios-emt-aumentaron-139-agosto-subieron-37-viajeros-metro-20251010091105.html` -> **snapshot** (snapshot 20251010071243); points raw/verified 11/8
  - p54 EMT Madrid bus passengers year-on-year growth, August = **13.9** as written "13,9%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "los autobuses de la Empresa Municipal de Transporte (EMT) para desplazarse en la ciudad de Madrid subieron un 13,9% en agosto"
  - p55 Metro de Madrid passengers year-on-year growth, August = **3.7** as written "3,7%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "los que se decantaron por el Metro crecieron un 3,7% con respecto al mismo mes del año anterior"
  - p56 Comunidad de Madrid urban bus passengers year-on-year growth, August = **11.8** as written "11,8%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "lo que supone un 11,8% más que en el mismo mes del año anterior"
  - p57 National urban bus passengers year-on-year growth, August = **4.5** as written "4,5", value check pending percent (2025-08-01..2025-08-31) [keep: ] quote: "frente a un aumento del 4,5 a nivel nacional"
  - p58 Comunidad de Madrid urban transport average growth year-to-date = **5.6** as written "5,6%", value check pending % (2025-01-01..2025-08-31) [keep: ] quote: "En lo que va de año, la media de crecimiento del transporte urbano en la región ha crecido un 5,6%."
  - p59 Extremadura urban bus passengers year-on-year growth, August = **10.7** as written "10,7%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "con Madrid (+11,8%), Extremadura (+10,7%) y País Vasco (+6,9%) a la cabeza"
  - p60 País Vasco urban bus passengers year-on-year growth, August = **6.9** as written "6,9%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "con Madrid (+11,8%), Extremadura (+10,7%) y País Vasco (+6,9%) a la cabeza"
  - p61 Cataluña urban bus passengers year-on-year change, August = **0.5** as written "0,5%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "excepto en Cataluña en donde cayó un 0,5%"
- `https://www.viaempresa.cat/economia/metro-barcelona-maxims-historics-agost_2220532_102.html` -> **snapshot** (snapshot 20260212070716); points raw/verified 15/6
  - p62 Metro Barcelona year-on-year growth in passengers, August = **6** % (2025-08-01..2025-08-31) [keep: ] quote: "El vuitè mes de l'any va registrar 30,3 milions de persones, un 6% més respecte al mateix període de l'any passat."
  - p63 Urban bus passengers in Catalonia, August (year-on-year change) = **0.5** as written "0,5%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "Pel que fa al transport per autobús urbà a Catalunya es va reduir un 0,5% a l'agost en comparació amb el mateix període de l'any passat"
  - p64 Urban bus passengers in Barcelona, August (year-on-year growth) = **0.6** as written "0,6%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "La primera vegada que assoleix aquesta xifra i es tracta d'un 0,6% més que el vuitè mes del 2024 (14,9 milions)."
  - p65 Total public transport passengers in Spain, August (year-on-year growth) = **2.6** as written "2,6%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "Al conjunt de l'Estat, el nombre d'usuaris del transport públic a l'agost van superar els 362,4 milions, un 2,6% interanual més."
  - p66 Urban transport passengers in Spain, August (year-on-year growth) = **4** % (2025-08-01..2025-08-31) [keep: ] quote: "L'INE destaca l'augment d'un 4% del transport urbà, fins a 222,8 milions"
  - p67 Interurban transport passengers in Spain, August (year-on-year change) = **1.4** as written "1,4%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "mentre que l'interurbà va recular un 1,4%, vorejant els 118 milions"
- `https://www.cronicabalear.es/mallorca/2025-10-10/el-autobus-de-palma-alcanza-los-431-millones-de-pasajeros-hasta-agosto/` -> **snapshot** (snapshot 20251010085851); points raw/verified 15/7
  - p68 Metro Palma passengers, August 2025 = **91** passengers (2025-08-01..2025-08-31) [DISCARD: Already discarded; Metro Palma level not needed.] quote: "El metro de Palma, con unos 91.000 pasajeros, es el que más ha crecido en usuarios en agosto de todos los suburbanos del país, un 56 %"
  - p69 Metro Sevilla passengers, August 2025 = **919** passengers (2025-08-01..2025-08-31) [keep: ] quote: "lejos del siguiente que es el de Sevilla, con 919.000 viajeros en agosto"
  - p70 Metro Palma passengers, January-August 2025 cumulative = **56** passengers (2025-01-01..2025-08-31) [DISCARD: Already discarded; cumulative figure not aligned to August.] quote: "En lo que va de año ha transportado a 56.000 viajeros, un 16,4 % más."
  - p71 Year-on-year growth of total public transport passengers in Spain, August 2025 = **2.6** as written "2,6 %", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "el transporte público en general fue utilizado por más de 362,4 millones de pasajeros en agosto, un 2,6 % más que en el mismo mes de 2024."
  - p72 Year-on-year growth of urban transport passengers in Spain, August 2025 = **4** % (2025-08-01..2025-08-31) [keep: ] quote: "el transporte urbano fue utilizado por más de 222,8 millones de viajeros en agosto, el citado 4 % más"
  - p73 Year-on-year growth of metro transport passengers in Spain, August 2025 = **3.2** as written "3,2 %", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "el transporte por metro aumentó un 3,2 % en tasa anual y el transporte urbano por autobús, un 4,5 %."
  - p74 Year-on-year growth of urban bus transport passengers in Spain, August 2025 = **4.5** as written "4,5 %", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "el transporte por metro aumentó un 3,2 % en tasa anual y el transporte urbano por autobús, un 4,5 %."
- dropped by code checks: 28 (number: scale word 'millones' is not English or CJK (not supported): 17; value_as_written not in quote as a whole number: 2; number: scale word 'milions' is not English or CJK (not supported): 8; scale word 'million' not supported by quote or table header: 1)

### d5 [related_series] Renfe and rail operator statistics

Hypothesis: Renfe Cercanías, Media Distancia and Avant passenger counts are the rail interurban/urban component of ETP. Renfe publishes monthly or quarterly passenger numbers; August 2025 plus growth gives the rail component, which is a smaller but non-trivial share of the total.

Queries issued by the searcher: Renfe viajeros cercanías agosto 2025; Renfe pasajeros mensuales 2025 cercanías media distancia estadística; INE Estadística de Transporte de Viajeros julio 2026 millones de viajeros transporte público; "transporte público" viajeros julio 2026 INE cercanías media distancia datos

- `https://www.ine.es/dyngs/Prensa/en/TV0726.htm?print=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.europapress.es/economia/transportes-00343/noticia-transporte-publico-supera-362-millones-viajeros-agosto-impulsado-ave-autobus-20251010093` -> **dropped** (snapshot fetch failed (http -1); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://cnmc.es/sites/default/files/6291881.pdf` -> **snapshot** (snapshot 20251211072642); points raw/verified 15/1
  - p75 Year-on-year change in MD AV passengers, Spain, Q3 2025 vs Q3 2024 = **10** % (2025-07-01..2025-09-30) [keep: ] quote: "y en MD AV, donde no ha habido cambio en las ayudas, un 10%."
- `https://www.abc.es/economia/renfe-pierde-viajeros-servicios-subvencionados-estado-puertas-20260717200357-nt.html` -> **snapshot** (snapshot 20260910110746); points raw/verified 15/8
  - p76 Renfe Media Distancia conventional passengers, Spain, year-on-year change 2025 = **-10.8** as written "-10,8%", value check pending % (2025-01-01..2025-12-31) [keep: ] quote: "Media Distancia convencional cayendo a plomo un -10,8% en pasajeros durante 2025"
  - p77 Renfe Media Distancia conventional seats offered, Spain, year-on-year change 202 = **0.7** as written "0,7%", value check pending % (2025-01-01..2025-12-31) [keep: ] quote: "pese a haber incrementado las plazas un 0,7%, según el Informe Anual Ferroviario publicado este viernes por la CNMC"
  - p78 Renfe Avant passengers, Spain, year-on-year change 2025 = **0.7** as written "0,7%", value check pending % (2025-01-01..2025-12-31) [keep: ] quote: "los conocidos como Avant, la caída de viajeros fue del 0,7% pese a que el alza de asientos ofrecidos fue del 0,7%"
  - p79 Renfe Avant seats offered, Spain, year-on-year change 2025 = **0.7** as written "0,7%", value check pending % (2025-01-01..2025-12-31) [keep: ] quote: "la caída de viajeros fue del 0,7% pese a que el alza de asientos ofrecidos fue del 0,7%"
  - p80 Renfe Cercanías passengers, Spain, year-on-year change 2025 = **0.4** as written "0,4%", value check pending % (2025-01-01..2025-12-31) [keep: ] quote: "también cayó en número de tickets un 0,4% cuando las plazas ofertadas habían crecido un 0,6%"
  - p81 Renfe Cercanías seats offered, Spain, year-on-year change 2025 = **0.6** as written "0,6%", value check pending % (2025-01-01..2025-12-31) [keep: ] quote: "también cayó en número de tickets un 0,4% cuando las plazas ofertadas habían crecido un 0,6%"
  - p82 All Renfe OSP services passengers, Spain, year-on-year change 2025 = **1.2** as written "1,2%", value check pending % (2025-01-01..2025-12-31) [keep: ] quote: "Sumando todas las OSP se perdieron un 1,2% de viajeros"
  - p83 High-speed passengers, Madrid-Barcelona corridor, year-on-year change 2025 = **-1.7** as written "-1,7 %", value check pending % (2025-01-01..2025-12-31) [keep: ] quote: "solo se perdió en el Madrid-Barcelona, donde disminuyeron por primera vez desde la liberalización (-1,7 %)"
- dropped by code checks: 21 (number: scale word 'millones' is not English or CJK (not supported): 7; number: ambiguous separators: '.' used as a thousands separator: 12; value_as_written not in quote as a whole number: 1; number: low/high given but value_as_written is not a range: 1)

### d6 [forecasts_markets] Official and analyst forecasts

Hypothesis: Published forecasts or early indicators (e.g., INE advance indicators, ministry transport statistics, operator guidance) for summer 2026 passenger volumes can anchor the level and growth rate, reducing reliance on extrapolation.

Queries issued by the searcher: INE Estadística de Transporte de Personas viajeros 2026 avance; previsión demanda transporte público 2026 España viajeros; INE Estadística de Transporte de Viajeros agosto 2025 datos provisionales millones de pasajeros; INEbase estadística transporte de personas tabla total viajeros mensual serie 2025 2026

- `https://www.ine.es/dyngs/Prensa/TV0726.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ine.es/dyngs/Prensa/TV0825.htm` -> **snapshot** (snapshot 20251216205557); points raw/verified 15/6
  - p84 Annual growth rate of total public transport passengers, Spain, August 2025 vs A = **2.6** as written "2,6%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El número de usuarios del transporte público aumentó un 2,6% en agosto respecto al mismo mes de 2024."
  - p85 Annual growth rate of urban transport passengers, Spain, August 2025 = **4** as written "4,0%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte urbano subió un 4,0% en tasa anual y el interurbano cayó un 1,4%."
  - p86 Annual growth rate of metro passengers, Spain, August 2025 = **3.2** as written "3,2%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte por metro aumentó un 3,2% en tasa anual y el transporte urbano por autobús aumentó un 4,5%."
  - p87 Annual growth rate of urban bus passengers, Spain, August 2025 = **4.5** as written "4,5%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte por metro aumentó un 3,2% en tasa anual y el transporte urbano por autobús aumentó un 4,5%."
  - p88 Annual growth rate of interurban bus passengers, Spain, August 2025 = **1.8** as written "1,8%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "Por tipo de transporte, por autobús creció un 1,8%, mientras que el aéreo cayó un 0,3%, el marítimo un 1,6%, y por ferrocarril un 5,9%."
  - p89 Annual growth rate of special and discretionary transport passengers, Spain, Aug = **11.7** as written "11,7%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "Más de 21,6 millones de usuarios utilizaron transporte especial y discrecional en agosto, lo que supuso un incremento del 11,7% en tasa anual."
- `https://nexotrans.com/el-autobus-movera-al-29-de-los-viajeros-durante-el-verano-de-2026/` -> **snapshot** (snapshot 20260722003508); points raw/verified 12/4
  - p90 Share of July 2026 displacements by bus (bus share of total displacements) = **29** % (2026-07-01..2026-07-31) [DISCARD: Already discarded; bus share of displacements is a different quantity from passenger journeys.] quote: "De ellos, el 29% corresponderá a viajeros que optarán por el autobús"
  - p91 Average tourist satisfaction with Spain, ESTI 2025 survey (out of 10) = **9.3** as written "9,3", value check pending points out of 10 (2025-01-01..2025-12-31) [DISCARD: Already discarded; tourist satisfaction irrelevant to passenger counts.] quote: "La satisfacción media de los turistas con España alcanzó una nota de 9,3 sobre 10 según la encuesta ESTI 2025 de Turespaña"
  - p92 Bus vs car pollution factor, lower bound (times less polluting) = **4** as written "cuatro", value check pending times less polluting than car (not stated (page dated 2026-06-30)) [DISCARD: Already discarded; pollution factor irrelevant.] quote: "viajar en autobús es entre cuatro y seis veces menos contaminante que hacerlo en coche particular"
  - p93 Bus vs car pollution factor, upper bound (times less polluting) = **6** as written "seis", value check pending times less polluting than car (not stated (page dated 2026-06-30)) [DISCARD: Already discarded; pollution factor irrelevant.] quote: "viajar en autobús es entre cuatro y seis veces menos contaminante que hacerlo en coche particular"
- `https://anetra-informa.es/noticias/la-demanda-del-transporte-en-autobus-crece-un-25-hasta-mayo-apenas-un-05-en-el-caso-del-regular-de-uso-especial-y-d` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 17 (scale word 'million' not supported by quote or table header: 6; value_as_written not in quote as a whole number: 3; number: scale word 'millones' is not English or CJK (not supported): 4; period_end 2026-09-30 after as_of: 4)

### d7 [physical_flow] Population and trip-rate base rate

Hypothesis: Total passengers ≈ resident population × average public-transport trips per person per month, adjusted for August tourism (visitors add trips) and August seasonality (commuting drops, leisure rises). Spain population ~48-49 million; average monthly trips per capita from ETP history gives a cross-check on the aggregate.

Queries issued by the searcher: INE Estadística de Transporte de Personas viajeros por habitante 2024; INE padrón población España 1 enero 2026; Frontur llegadas turistas internacionales agosto 2025 INE; Estadística de Transporte de Personas agosto 2025 viajeros transporte público INE

- `https://www.ine.es/dyngs/Prensa/TV1224.pdf` -> **dropped** (snapshot fetch failed (http -1); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://efe.com/espana/2026-02-12/espana-habitantes-1-enero-2026/` -> **dropped** (snapshot fetch failed (http -1); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://asetrasegovia.es/wp-content/uploads/2025/03/Presentacion_Observatorio_Costes_Viajeros_2025.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ine.es/dyngs/Prensa/FRONTUR0825.htm?print=1` -> **snapshot** (snapshot 20251002185237); points raw/verified 15/6
  - p94 Year-on-year change in international tourists, August 2025 = **2.9** as written "2,9", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "España recibió 11,3 millones de turistas internacionales en agosto, un 2,9% más que en el mismo mes de 2024."
  - p95 Share of international tourists with Illes Balears as main destination, August 2 = **22.5** as written "22,5%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "Illes Balears fue el primer destino principal de los turistas en agosto, con el 22,5% del total."
  - p96 Share of international tourists with Cataluña as main destination, August 2025 = **19.4** as written "19,4%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "Le siguieron Cataluña (19,4%) y Andalucía (15,3%)."
  - p97 Share of international tourists with Andalucía as main destination, August 2025 = **15.3** as written "15,3%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "Le siguieron Cataluña (19,4%) y Andalucía (15,3%)."
  - p98 Year-on-year change in excursionists (same-day visitors without overnight stay), = **7.5** as written "7,5%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El número de visitantes se incrementó un 7,5% entre los que no pernoctan (excursionistas), mientras que descendió un 0,8% entre los turistas con mayor duración (más de 15 noches)."
  - p99 Theoretical annual FRONTUR sample size (surveys) = **450** surveys per year (2025-01-01..2025-12-31) [DISCARD: Already discarded; FRONTUR sample size irrelevant.] quote: "el tamaño muestral teórico anual de FRONTUR supera las 450.000 encuestas"
- dropped by code checks: 9 (number: scale word 'millones' is not English or CJK (not supported): 7; number: ambiguous separators: '.' used as a thousands separator: 1; value_as_written not in quote as a whole number: 1)

### d8 [shocks] Calendar, weather, and disruption effects

Hypothesis: August 2026 passenger totals are affected by calendar (number of weekdays vs weekends), heatwaves, wildfire disruptions, strikes, and fare policies (e.g., free/reduced Renfe Cercanías passes, subsidised bus fares). These shift the August 2025-to-2026 growth rate away from trend.

Queries issued by the searcher: Estadística de Transporte de Personas INE agosto 2026 viajeros; gratuidad cercanías abono 2026 España transporte público subvención; huelga transporte público agosto 2026 España autobús metro tren paro; ola de calor agosto 2026 España incendios transporte carreteras cortadas

- `https://www.ine.es/dyngs/Prensa/TV0826.htm?print=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.transportes.gob.es/transporte-terrestre/bonificaciones-transporte-publico/medidas-vigentes-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.elperiodicodeceuta.es/operacion-salida-de-agosto-caos-de-trafico-huelga-de-renfe-carreteras-cortadas-y-rutas-alternativas-para-evitar-atas` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://quieroviajarporelmundo.com/noticias-viajes-espana-29-julio-2026/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [own_history] INE ETP monthly series

Hypothesis: Obtaining the actual INE ETP monthly total passenger levels (not just growth rates) for August 2023, 2024, 2025 and the 2026 monthly run-rate would let us anchor the level directly and apply a trend growth, replacing the need to reconstruct levels from growth rates. This is the single most valuable missing input.

Queries issued by the searcher: INE Estadística de Transporte de Personas agosto 2025 362,4 millones viajeros; INE ETP table 2026 monthly viajeros transporte público millones; Estadística de Transporte de Personas serie mensual millones viajeros agosto 2024; INE Estadística de Transporte de Personas julio 2026 datos provisionales millones pasajeros; site:ine.es "Transporte de Personas" "Julio 2026"; INE TV0726 pdf pasajeros transporte público julio 2026

- `https://www.ine.es/dyngs/Prensa/TV0825.pdf` -> **snapshot** (snapshot 20251221032913); points raw/verified 15/3
  - p100 Year-on-year growth of total public transport passengers in Spain, August 2025 = **2.6** as written "2,6%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El número de usuarios del transporte público aumentó un 2,6% en agosto respecto al mismo mes de 2024."
  - p101 Year-on-year growth of urban transport passengers in Spain, August 2025 = **4** as written "4,0%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte urbano subió un 4,0% en tasa anual y el interurbano cayó un 1,4%."
  - p102 Year-on-year growth of urban transport passengers in Spain, August 2024 = **5.8** as written "5,8", value check pending percent (year-on-year) (2024-08-01..2024-08-31) [DISCARD: Duplicate of the superseded August 2024 urban vintage (5.8%); redundant with discarded p4.] quote: "2024 Agosto 5,8 7,1 -1,1"
- `https://www.ine.es/dyngs/Prensa/TV0824.htm?print=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ine.es/dyngs/Prensa/TV0526.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://apps.fomento.gob.es/BDOTLE/visorBDpop.aspx?i=2024` -> **snapshot** (snapshot 20250414132910); points raw/verified 0/0
- dropped by code checks: 12 (scale word 'million' not supported by quote or table header: 6; scale word 'thousand' not supported by quote or table header: 4; value_as_written not in quote as a whole number: 2)

### b2 [related_series] 2026 growth trajectory

Hypothesis: The February 2026 INE data (p17, p18) show urban +2.0% and interurban -4.2%, much weaker than 2025. Finding the most recent 2026 monthly INE ETP growth rates (March-July 2026) would pin the 2026 growth rate to apply to the August 2025 level, resolving the largest uncertainty in the projection.

Queries issued by the searcher: INE Estadística de Transporte de Personas junio 2026 viajeros tasa anual; INE transporte público 2026 crecimiento mensual viajeros

- `https://www.ine.es/dyngs/Prensa/TV0726.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ine.es/dyngs/Prensa/TV0726.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ine.es/dyngs/Prensa/es/TV0626.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ine.es/jaxiT3/Datos.htm?t=20239` -> **snapshot** (snapshot 20260331043326); points raw/verified 1/0
- dropped by code checks: 1 (scale word 'thousand' not supported by quote or table header: 1)

### b3 [base_rates] August seasonality

Hypothesis: The July-to-August ratio of total ETP passengers (August level relative to July level) is needed to convert a July 2026 run-rate into an August 2026 estimate. Finding historical July and August monthly totals would supply this seasonal factor.

Queries issued by the searcher: INE Estadística de Transporte de Personas más de 400 millones viajeros agosto 2024; transporte público España agosto 2025 millones viajeros INE julio comparación; INE "Estadística de Transporte de Viajeros" agosto 2024 millones pasajeros transporte público "agosto"; ine.es TV0825 prensa agosto 2025 362,4 millones porcentaje julio

- `https://ine.es/dyngs/INEbase/en/operacion.htm?c=Estadistica_C&cid=1254736176906&idp=1254735576820` -> **snapshot** (snapshot 20260122225509); points raw/verified 11/7
  - p103 Total public transport passengers year-on-year variation, October (percent) = **4.4** % (not stated (page dated 2026-01-12)) [keep: ] quote: "The number of passengers using public transport increased by 4.4% in October, as compared with the same month of 2024."
  - p104 City transport passengers year-on-year variation, October (percent) = **5.4** % (not stated (page dated 2026-01-12)) [keep: ] quote: "The annual rate for city transport increased by 5.4% and for inter-city transport by 3.6%."
  - p105 Inter-city transport passengers year-on-year variation, October (percent) = **3.6** % (not stated (page dated 2026-01-12)) [keep: ] quote: "The annual rate for city transport increased by 5.4% and for inter-city transport by 3.6%."
  - p106 Total passengers year-on-year variation, November 2025 (percent) = **4.5** percent (2025-11-01..2025-11-30) [keep: ] quote: "\| Total \| \| 508,701 \| 4.5 \|"
  - p107 City transport passengers year-on-year variation, November 2025 (percent) = **6.8** percent (2025-11-01..2025-11-30) [keep: ] quote: "\| City transport \| \| 318,771 \| 6.8 \|"
  - p108 Inter-city transport passengers year-on-year variation, November 2025 (percent) = **1.2** percent (2025-11-01..2025-11-30) [keep: ] quote: "\| Inter-city transport \| \| 143,569 \| 1.2 \|"
  - p109 Special and unscheduled transport passengers year-on-year variation, November 20 = **-0.6** percent (2025-11-01..2025-11-30) [keep: ] quote: "\| Special and unscheduled transport \| \| 46,361 \| -0.6 \|"
- `https://www.ine.es/dyngs/Prensa/TV0725.pdf` -> **snapshot** (snapshot 20251009203316); points raw/verified 15/10
  - p110 Annual growth rate of total public transport passengers, July 2025 vs July 2024 = **3.9** as written "3,9%", value check pending % (2025-07-01..2025-07-31) [keep: ] quote: "El número de usuarios del transporte público aumentó un 3,9% en julio respecto al mismo mes de"
  - p111 Annual growth rate of urban transport passengers, July 2025 = **6.2** as written "6,2%", value check pending % (2025-07-01..2025-07-31) [keep: ] quote: "El transporte urbano subió un 6,2% en tasa anual, mientras que el interurbano bajó un 0,2%."
  - p112 Annual growth rate of interurban transport passengers, July 2025 = **0.2** as written "0,2%", value check pending % (2025-07-01..2025-07-31) [keep: ] quote: "El transporte urbano subió un 6,2% en tasa anual, mientras que el interurbano bajó un 0,2%."
  - p113 Annual growth rate of special and discretionary transport passengers, July 2025 = **3.3** as written "3,3%", value check pending % (2025-07-01..2025-07-31) [keep: ] quote: "Más de 25,9 millones de usuarios utilizaron transporte especial y discrecional en julio, lo que supuso un incremento del 3,3% en tasa anual."
  - p114 Annual growth rate of urban transport passengers, August 2024 = **5.3** as written "5,3", value check pending % (2024-08-01..2024-08-31) [keep: ] quote: "Agosto 5,3 3,4 -10,7"
  - p115 Annual growth rate of interurban transport passengers, August 2024 = **3.4** as written "3,4", value check pending % (2024-08-01..2024-08-31) [keep: ] quote: "Agosto 5,3 3,4 -10,7"
  - p116 Annual growth rate of special and discretionary transport passengers, August 202 = **-10.7** as written "-10,7", value check pending % (2024-08-01..2024-08-31) [keep: ] quote: "Agosto 5,3 3,4 -10,7"
  - p117 Annual growth rate of urban transport passengers, July 2024 = **8.7** as written "8,7", value check pending % (2024-07-01..2024-07-31) [keep: ] quote: "Julio 8,7 12,3 4,5"
  - p118 Annual growth rate of interurban transport passengers, July 2024 = **12.3** as written "12,3", value check pending % (2024-07-01..2024-07-31) [keep: ] quote: "Julio 8,7 12,3 4,5"
  - p119 Annual growth rate of special and discretionary transport passengers, July 2024 = **4.5** as written "4,5", value check pending % (2024-07-01..2024-07-31) [keep: ] quote: "Julio 8,7 12,3 4,5"
- `https://www.ine.es/dyngs/Prensa/TV0824.htm?print=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.elindependiente.com/economia/2025/10/10/transporte-publico-espana-viajeros-agosto/` -> **snapshot** (snapshot 20251113205847); points raw/verified 15/6
  - p120 Year-on-year change in total public transport passengers in Spain, August = **2.6** as written "2,6%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "un incremento del 2,6% respecto al mismo mes de 2024"
  - p121 Year-on-year change in urban transport passengers in Spain, August = **4** % (2025-08-01..2025-08-31) [keep: ] quote: "el transporte urbano creció un 4% (hasta 222,8 millones)"
  - p122 Year-on-year change in interurban transport passengers in Spain, August = **1.4** as written "1,4%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "el interurbano descendió un 1,4% (117,8 millones)"
  - p123 Year-on-year change in special and discretionary transport passengers in Spain,  = **11.7** as written "11,7%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "con más de 21,6 millones de usuarios (11,7% de aumento)"
  - p124 Year-on-year change in rail transport passengers in Spain, August = **5.9** as written "5,9%", value check pending % (2025-08-01..2025-08-31) [DISCARD: States rail transport 'disminució un 5,9%' while p88 says rail 'creció un 5,9%' — sign contradiction in the same article] quote: "El transporte ferroviario en su conjunto disminuyó un 5,9%."
  - p125 Year-on-year change in urban bus passengers in Spain, August = **4.5** as written "4,5%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "el crecimiento del 4% se debió principalmente al aumento de usuarios en el autobús urbano (4,5%) y en el metro (3,2%)."
- dropped by code checks: 18 (scale word 'thousand' not supported by quote or table header: 5; scale word 'million' not supported by quote or table header: 4; number: scale word 'millones' is not English or CJK (not supported): 9)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['spain passenger transport', 'ine etp august', 'public transport passengers']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p19', 'p25', 'p47', 'p65', 'p71', 'p84'] All report the same INE August 2025 total growth of 2.6% (2.6% vs Aug 2024); they are copies of one INE press release, not independent measurements.
- corroborating: ['p2', 'p20', 'p26', 'p48', 'p66', 'p72', 'p85'] Same INE urban growth figure of 4.0% for August 2025, repeated across outlets; single underlying source.
- corroborating: ['p3', 'p21', 'p27', 'p89'] Same INE special/discretionary August 2025 growth of 11.7% and level of 21.6 million; one source.
- corroborating: ['p22', 'p49', 'p73', 'p86'] Metro growth 3.2% August 2025, repeated INE figure.
- corroborating: ['p23', 'p50', 'p57', 'p74', 'p87'] Urban bus growth 4.5% August 2025, repeated INE figure.
- corroborating: ['p4', 'p5', 'p6', 'p24'] Same INE August 2024 table row (urban 5.8, interurban 7.1, special -1.1); p24 duplicates p6.
- corroborating: ['p7', 'p8', 'p9', 'p28', 'p29', 'p30'] Same INE July 2025 table row (6.2, -0.2, 3.3); duplicates.
- conflicting: ['p10', 'p14'] Both Confebus August 2024 vs August 2023 growth but give 3.7% and 2.8%; likely different vintages/definitions of the same release. Not usable as a precise growth rate.
- corroborating: ['p11', 'p16'] Confebus urban August 2024: 5.3% vs 2023 and ~15% vs 2019; consistent recovery narrative.
- corroborating: ['p51', 'p56', 'p59', 'p60'] Same INE regional bus growth figures (Madrid 11.8, Extremadura 10.7, País Vasco 6.9) repeated by Europapress.
- corroborating: ['p52', 'p61', 'p63'] Catalonia urban bus -0.5% August 2025, repeated across outlets.
- corroborating: ['p54', 'p55'] EMT Madrid +13.9% and Metro Madrid +3.7% August 2025; operator-level, distinct from INE national aggregates but same month.
- corroborating: ['p62', 'p64'] Metro Barcelona 30.3M (+6%) and Barcelona urban bus 14.9M (+0.6%) August 2025; operator-level.
- conflicting: ['p68', 'p70'] Palma metro: 91,000 in August 2025 vs 56,000 cumulative Jan-Aug 2025 — inconsistent (monthly > cumulative); likely unit/typo issues, treat with caution.
- corroborating: ['p34', 'p35', 'p36', 'p37'] November 2025 INE table: total 508.7M (+4.5%), urban 318.8M (+6.8%), interurban 143.6M (+1.2%), special 46.4M (-0.6%). Consistent internal decomposition.
- corroborating: ['p38', 'p39', 'p40'] October 2025 INE: total +4.4%, urban +5.4%, interurban +3.6%.
- corroborating: ['p41', 'p42', 'p43', 'p44', 'p45', 'p46'] 2025 annual +3.7%; December 2025 total +3.6%, urban +3.4%, interurban +3.6%, special +4.6%, interurban bus +6.8%.
- corroborating: ['p17', 'p18'] February 2026 INE: urban +2.0%, interurban -4.2%, special -1.4% — shows 2026 growth has slowed versus 2025.
- corroborating: ['p75', 'p76', 'p78', 'p80', 'p82'] Rail passenger trends 2025: MD AV +10% Q3, MD conventional -10.8%, Avant -0.7%, Cercanías -0.4%, all OSP -1.2% — rail is a small, mixed component.
- corroborating: ['p94', 'p95', 'p96', 'p97', 'p98'] August 2025 tourism: 11.3M international tourists (+2.9%), excursionists +7.5%, destination shares — supports August tourism-driven transport demand.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p19', 'p25', 'p47', 'p65', 'p71', 'p84', 'p100', 'p120'] All report the same INE ETP August 2025 headline: total public transport passengers +2.6% year-on-year. They are repeated republications of one INE measurement, not independent confirmations.
- corroborating: ['p2', 'p20', 'p26', 'p48', 'p72', 'p85', 'p101', 'p121'] Same INE August 2025 urban growth figure (+4.0%), repeated across outlets. Single underlying measurement.
- corroborating: ['p3', 'p21', 'p27', 'p89', 'p123'] Same INE August 2025 special/discretionary figure: 21.6 million passengers, +11.7%. Repeated copies.
- corroborating: ['p65', 'p66', 'p67', 'p71', 'p72', 'p121', 'p122'] These give the August 2025 component levels: total 362.4 million, urban 222.8 million, interurban ~117.8-118 million, special 21.6 million. They are internally consistent (222.8 + 117.8 + 21.6 ≈ 362.2
- conflicting: ['p4', 'p5', 'p6', 'p102', 'p114', 'p115', 'p116'] Two different vintages of the August 2024 growth table disagree: p4-p6 give urban 5.8 / interurban 7.1 / special -1.1, while p114-p116 give urban 5.3 / interurban 3.4 / special -10.7. These are revisi
- conflicting: ['p11', 'p12', 'p114', 'p115'] Confebus (p11, p12) reports August 2024 urban +5.3% and interurban +3.4%, matching the later INE vintage p114/p115, not the earlier p4/p5. Supports using p114-p116 as the August 2024 reference.
- corroborating: ['p7', 'p8', 'p9', 'p110', 'p111', 'p112', 'p113'] July 2025 growth figures (urban 6.2, interurban -0.2, special 3.3, total 3.9) are consistent across vintages and give the July-to-August seasonal shape.
- corroborating: ['p17', 'p18'] February 2026 INE data show urban +2.0% and interurban -4.2%, special -1.4% — a marked slowdown versus 2025. This is the most recent 2026 evidence and should pull the August 2026 growth assumption bel
- corroborating: ['p34', 'p35', 'p36', 'p37', 'p106', 'p107', 'p108', 'p109'] November 2025 INE data: total +4.5%, urban +6.8%, interurban +1.2%, special -0.6%. Consistent across duplicate copies; shows strong late-2025 urban growth.
- corroborating: ['p38', 'p39', 'p40', 'p103', 'p104', 'p105'] October 2025 INE data: total +4.4%, urban +5.4%, interurban +3.6%. Consistent duplicates.
- corroborating: ['p41', 'p42', 'p43', 'p44', 'p45', 'p46'] Full-year 2025 total +3.7%, December 2025 total +3.6%, urban +3.4%, interurban +3.6%, special +4.6%, interurban bus +6.8%. Coherent INE 2025 picture.
- corroborating: ['p51', 'p52', 'p54', 'p55', 'p56', 'p57', 'p59', 'p60', 'p61', 'p62', 'p63', 'p64'] Regional and operator August 2025 growth figures (Madrid bus +11.8%, EMT Madrid +13.9%, Metro Madrid +3.7%, Metro Barcelona +6%, Catalonia bus -0.5%) are consistent with the national urban +4.0% and m
- corroborating: ['p75', 'p76', 'p77', 'p78', 'p79', 'p80', 'p81', 'p82', 'p83'] Renfe/CNMC 2025 rail data: Cercanías -0.4%, MD conventional -10.8%, Avant -0.7%, all OSP -1.2%, Madrid-Barcelona -1.7%. These are annual figures for a sub-component (rail) of the interurban/urban tota
- corroborating: ['p94', 'p95', 'p96', 'p97', 'p98'] August 2025 tourism: 11.3 million international tourists +2.9%, excursionists +7.5%, with Balearics/Catalonia/Andalucía shares. Contextual driver of August public transport demand, not a direct measur
- corroborating: ['p69', 'p53'] Metro Sevilla 919,000 passengers and Metro Palma +56% in August 2025 are small metro sub-components consistent with the national metro +3.2%.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | August 2026 YoY growth factor of total public transport passengers vs August 2025 | 1.015 | 0.99..1.04 | 0.9076..1.134 (widened) | ratio | unused | 2025 monthly total growth ran 3.6-4.5% (p34, p38, p41, p42), but the only 2026 evidence (p17, p18, February 2026) shows a sharp slowdown: urban +2.0%, interurban -4.2%, special -1.4%. August 2025 itself was only +2.6% (p1). A modest positive August 2026 growth of ~1.5% is consistent with a decelerat | The 2026 slowdown seen in February persists through August and no major fare/strike shock occurs. | March-July 2026 INE ETP growth returning to 4%+ or turning negative. |
| a2 | August 2025 total public transport passengers level (millions) | 362 | 355..370 | 256..513 (widened) | millions of passengers | unused | Anchored on the reported August 2025 total of 'more than 362.4 million' (p65, p71); range reflects rounding and possible revision. | The August 2025 level is not materially revised before the August 2026 release. | A revised August 2025 total outside 355-370 million. |
| a3 | Urban share of total public transport passengers, August | 0.615 | 0.58..0.65 | 0.4342..0.8683 (widened) | share | unused | Derived from August 2025 levels: urban 222.8M / total 362.4M ≈ 0.615 (p66, p65). Range reflects seasonal and revision uncertainty. | The urban/interurban/special mix in August 2026 resembles August 2025. | A large shift in urban vs interurban ridership mix. |
| a4 | Interurban share of total public transport passengers, August | 0.325 | 0.3..0.35 | 0.2291..0.4583 (widened) | share | unused | August 2025 interurban ~117.8M / total 362.4M ≈ 0.325 (p122, p65). | Interurban mix stable year-on-year. | Interurban ridership diverging sharply from urban. |
| a5 | Special/discretionary share of total public transport passengers, August | 0.06 | 0.05..0.07 | 0.04183..0.08367 (widened) | share | unused | August 2025 special 21.6M / total 362.4M ≈ 0.06 (p3, p65). | Special/discretionary mix stable. | Large swing in school/charter services. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | n/a | [] / ['a1', 'a2'] | [] |  | 0.00 |  | formula_mc must use at least one kept observed data point (a formula made only of assumptions is rejected) |
| m2 | formula_mc | n/a | [] / ['a1', 'a2', 'a3', 'a4', 'a5'] | [] |  | 0.00 |  | formula_mc must use at least one kept observed data point (a formula made only of assumptions is rejected) |

- m1 coverage: the whole target
- m2 coverage: the whole target

Result: central **n/a** passenger, 80% interval [n/a, n/a] passenger, basis no_method (no method produced an estimate, so there is no interval), weight rule None, weight on methods that use assumptions 0.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

No estimate: no estimation method could be computed from the verified evidence.

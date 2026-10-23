# Evidence ledger: fc_es_transit_2026_08

- Question: Assume today is 2026-09-11. You know nothing published after this date. Estimate the total number of passengers who used public transport in Spain in August 2026 (urban, interurban and special/discretionary transport combined), as it will be first reported in the provisional data of the National Statistics Institute's (INE) Passenger Transport Statistics (Estadística de Transporte de Personas).
- as_of: 2026-09-11
- Pinned target: Total passengers carried by public transport in Spain (urban, interurban, and special/discretionary transport combined) during August 2026, as first reported in INE's Estadística de Transporte de Personas (Passenger Transport Statistics) provisional data; measured as passenger journeys (boardings/tr | unit passenger journeys | period 2026-08-01..2026-08-31 | publisher Instituto Nacional de Estadística (INE), Estadística de Transporte de Personas (ETP)

- Official value (scoring only, never shown to the agent): 371,623,271

## Directions and pages

### d1 [own_history] INE ETP time series

Hypothesis: August 2026 total passengers will follow the historical August level and recent year-on-year growth trend of the ETP total series; the target equals the most recent August value scaled by observed YoY growth.

Queries issued by the searcher: Estadística de Transporte de Personas INE agosto 2025 viajeros; INE transporte de personas serie mensual viajeros total; INE TV1004 serie viajeros total agosto 2024 2023 miles viajeros transporte público; "agosto 2026" transporte público viajeros INE Estadística de Transporte de Personas

- `https://www.ine.es/dyngs/Prensa/TV0726.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ine.es/consul/serie.do?d=true&s=TV1004&c=2&nult=15&L=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ine.es/dyngs/Prensa/TV0825.htm` -> **snapshot** (snapshot 20251216205557); points raw/verified 15/6
  - p1 Year-on-year growth rate of total public transport passengers, Spain, August 202 = **2.6** as written "2,6%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El número de usuarios del transporte público aumentó un 2,6% en agosto respecto al mismo mes de 2024."
  - p2 Year-on-year growth rate of urban transport passengers, Spain, August 2025 = **4** as written "4,0%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte urbano subió un 4,0% en tasa anual y el interurbano cayó un 1,4%."
  - p3 Year-on-year growth rate of special and discretionary transport passengers, Spai = **11.7** as written "11,7%", value check ok % (2025-08-01..2025-08-31) [keep: ] quote: "Más de 21,6 millones de usuarios utilizaron transporte especial y discrecional en agosto, lo que supuso un incremento del 11,7% en tasa anual."
  - p4 Year-on-year growth rate of interurban bus transport passengers, Spain, August 2 = **1.8** as written "1,8%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "Dentro del interurbano, destacó el incremento del 1,8% en el transporte por autobús."
  - p5 Year-on-year growth rate of metro transport passengers, Spain, August 2025 = **3.2** as written "3,2%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte por metro aumentó un 3,2% en tasa anual y el transporte urbano por autobús aumentó un 4,5%."
  - p6 Year-on-year growth rate of urban bus transport passengers, Spain, August 2025 = **4.5** as written "4,5%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte por metro aumentó un 3,2% en tasa anual y el transporte urbano por autobús aumentó un 4,5%."
- `https://apitropia.com/viajeros` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 9 (scale word 'million' not supported by quote or table header: 6; value_as_written not in quote as a whole number: 3)

### d2 [related_series] Mode-level ETP components

Hypothesis: Total = urban + interurban + special/discretionary. Each component has its own seasonal August pattern; summing component-level August estimates (each from its own history and growth) gives the total with better structure than a single aggregate trend.

Queries issued by the searcher: INE Estadística de Transporte de Personas viajeros agosto 2025 urbano interurbano especial; INE viajeros transporte público urbano interurbano discrecional agosto 2025 datos; Estadística de Transporte de Personas INE 2026 viajeros datos provisionales junio 2026; "transporte de personas" INE julio 2026 viajeros urbano interurbano

- `https://www.ine.es/dyngs/Prensa/TV0825.pdf` -> **snapshot** (snapshot 20251221032913); points raw/verified 15/8
  - p7 Urban transport YoY growth rate, Spain, August 2025 = **4** as written "4,0", value check pending percent (2025-08-01..2025-08-31) [keep: ] quote: "El transporte urbano subió un 4,0% en tasa anual y el interurbano cayó un 1,4%."
  - p8 Special and discretionary transport YoY growth rate, Spain, August 2025 = **11.7** as written "11,7", value check pending percent (2025-08-01..2025-08-31) [keep: ] quote: "Agosto 4,0 -1,4 11,7"
  - p9 Urban transport YoY growth rate, Spain, July 2025 = **6.2** as written "6,2", value check pending percent (2025-07-01..2025-07-31) [DISCARD: Duplicate of p75 (July 2025 urban growth 6.2%); redundant copy.] quote: "Julio 6,2 -0,2 3,3"
  - p10 Interurban transport YoY growth rate, Spain, July 2025 = **-0.2** as written "-0,2", value check pending percent (2025-07-01..2025-07-31) [DISCARD: Duplicate of p76 (July 2025 interurban -0.2%); redundant copy.] quote: "Julio 6,2 -0,2 3,3"
  - p11 Special and discretionary transport YoY growth rate, Spain, July 2025 = **3.3** as written "3,3", value check pending percent (2025-07-01..2025-07-31) [DISCARD: Duplicate of p77 (July 2025 special 3.3%); redundant copy.] quote: "Julio 6,2 -0,2 3,3"
  - p12 Urban transport YoY growth rate, Spain, August 2024 = **5.8** as written "5,8", value check pending percent (2024-08-01..2024-08-31) [DISCARD: August 2024 urban growth; superseded by the August 2025 baseline and not needed for the target period.] quote: "Agosto 5,8 7,1 -1,1"
  - p13 Interurban transport YoY growth rate, Spain, August 2024 = **7.1** as written "7,1", value check pending percent (2024-08-01..2024-08-31) [DISCARD: August 2024 interurban growth; superseded by the August 2025 baseline.] quote: "Agosto 5,8 7,1 -1,1"
  - p14 Special and discretionary transport YoY growth rate, Spain, August 2024 = **-1.1** as written "-1,1", value check pending percent (2024-08-01..2024-08-31) [DISCARD: August 2024 special growth; superseded by the August 2025 baseline.] quote: "Agosto 5,8 7,1 -1,1"
- `https://www.ine.es/dyngs/Prensa/es/TV0626.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ine.es/jaxiT3/Datos.htm?t=20239` -> **snapshot** (snapshot 20260331043326); points raw/verified 1/0
- `https://anetra-informa.es/noticias/la-demanda-del-transporte-en-autobus-crece-un-25-hasta-junio-apenas-un-09-en-el-caso-del-regular-de-uso-especial-y-` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 8 (scale word 'million' not supported by quote or table header: 6; value_as_written not in quote as a whole number: 1; scale word 'thousand' not supported by quote or table header: 1)

### d3 [related_series] Regional/modal breakdown (autonomous communities, metro systems)

Hypothesis: Large metro and regional operators (Madrid EMT/Metro, Barcelona TMB, etc.) publish their own ridership; aggregating major operators plus a residual share can cross-check or build the total. August tourism boosts coastal and city systems.

Queries issued by the searcher: Metro Madrid viajeros agosto 2025; TMB Barcelona viatgers agost 2025 metro; INE Estadística de Transporte de Personas agosto 2025 millones de viajeros total urbano interurbano; Metro Madrid viajeros junio 2026

- `https://www.elindependiente.com/economia/2025/10/10/transporte-publico-espana-viajeros-agosto/` -> **snapshot** (snapshot 20251113205847); points raw/verified 15/6
  - p15 Year-on-year growth of total public transport passengers in Spain, August = **2.6** as written "2,6%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "un incremento del 2,6% respecto al mismo mes de 2024"
  - p16 Year-on-year growth of urban transport passengers in Spain, August = **4** % (2025-08-01..2025-08-31) [keep: ] quote: "el transporte urbano creció un 4% (hasta 222,8 millones)"
  - p17 Year-on-year growth of urban bus passengers in Spain, August = **4.5** as written "4,5%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "el crecimiento del 4% se debió principalmente al aumento de usuarios en el autobús urbano (4,5%) y en el metro (3,2%)."
  - p18 Year-on-year growth of metro passengers in Spain, August = **3.2** as written "3,2%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "el crecimiento del 4% se debió principalmente al aumento de usuarios en el autobús urbano (4,5%) y en el metro (3,2%)."
  - p19 Year-on-year change of metro passengers in Valencia, August = **-16.8** as written "-16,8%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Valencia metro -16.8% is a local operator anomaly (likely DANA-related) that does not transfer to the national August 20] quote: "En cuanto al metro, aumentó en todas las ciudades excepto en Valencia (-16,8%)."
  - p20 Year-on-year growth of urban bus passengers in Comunidad de Madrid, August = **11.8** as written "11,8%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "el autobús presentó las mayores subidas en Comunidad de Madrid (11,8%), Extremadura (10,7%) y País Vasco (6,9%)."
- `https://www.europapress.es/madrid/noticia-usuarios-emt-aumentaron-139-agosto-subieron-37-viajeros-metro-20251010091105.html` -> **snapshot** (snapshot 20251010071243); points raw/verified 11/8
  - p21 EMT Madrid bus passenger growth, August year-on-year = **13.9** as written "13,9%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "los autobuses de la Empresa Municipal de Transporte (EMT) para desplazarse en la ciudad de Madrid subieron un 13,9% en agosto"
  - p22 Metro de Madrid passenger growth, August year-on-year = **3.7** as written "3,7%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "los que se decantaron por el Metro crecieron un 3,7% con respecto al mismo mes del año anterior"
  - p23 Comunidad de Madrid urban bus passenger growth, August year-on-year = **11.8** as written "11,8%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "lo que supone un 11,8% más que en el mismo mes del año anterior"
  - p24 National urban bus passenger growth, August year-on-year = **4.5** as written "4,5", value check pending percent (2025-08-01..2025-08-31) [DISCARD: Duplicate of p6/p37 (national urban bus +4.5%); redundant copy.] quote: "frente a un aumento del 4,5 a nivel nacional"
  - p25 Comunidad de Madrid urban transport average growth year-to-date = **5.6** as written "5,6%", value check pending % (2025-01-01..2025-08-31) [DISCARD: Comunidad de Madrid YTD average growth; regional context not needed and not a national signal.] quote: "En lo que va de año, la media de crecimiento del transporte urbano en la región ha crecido un 5,6%."
  - p26 Extremadura urban bus passenger growth, August year-on-year = **10.7** as written "10,7%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Extremadura urban bus +10.7%; regional detail already covered by p97 for 2026 and not needed for the national estimate.] quote: "con Madrid (+11,8%), Extremadura (+10,7%) y País Vasco (+6,9%) a la cabeza"
  - p27 País Vasco urban bus passenger growth, August year-on-year = **6.9** as written "6,9%", value check pending % (2025-08-01..2025-08-31) [DISCARD: País Vasco urban bus +6.9%; regional detail already covered by p100 for 2026.] quote: "País Vasco (+6,9%) a la cabeza"
  - p28 Cataluña urban bus passenger change, August year-on-year = **0.5** as written "0,5%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "excepto en Cataluña en donde cayó un 0,5%"
- `https://www.viaempresa.cat/economia/metro-barcelona-maxims-historics-agost_2220532_102.html` -> **snapshot** (snapshot 20260212070716); points raw/verified 15/6
  - p29 Barcelona metro passengers, August 2025, year-on-year change = **6** % (2025-08-01..2025-08-31) [keep: ] quote: "El vuitè mes de l'any va registrar 30,3 milions de persones, un 6% més respecte al mateix període de l'any passat."
  - p30 Urban bus passengers in Catalonia, August 2025, year-on-year change = **0.5** as written "0,5%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "Pel que fa al transport per autobús urbà a Catalunya es va reduir un 0,5% a l'agost en comparació amb el mateix període de l'any passat"
  - p31 Barcelona urban bus passengers, August 2025, year-on-year change = **0.6** as written "0,6%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "es tracta d'un 0,6% més que el vuitè mes del 2024 (14,9 milions)"
  - p32 Total public transport passengers in Spain, August 2025, year-on-year change = **2.6** as written "2,6%", value check ok % (2025-08-01..2025-08-31) [keep: ] quote: "van superar els 362,4 milions, un 2,6% interanual més"
  - p33 Urban transport passengers in Spain, August 2025, year-on-year change = **4** % (2025-08-01..2025-08-31) [keep: ] quote: "L'INE destaca l'augment d'un 4% del transport urbà, fins a 222,8 milions"
  - p34 Interurban transport passengers in Spain, August 2025, year-on-year change = **1.4** as written "1,4%", value check ok % (2025-08-01..2025-08-31) [keep: ] quote: "mentre que l'interurbà va recular un 1,4%, vorejant els 118 milions"
- `https://confebus.org/publicaciones/ver/5025/ine-estadistica-transporte-de-viajeros-agosto-2025` -> **snapshot** (snapshot 20260511143144); points raw/verified 15/4
  - p35 Year-on-year growth of total public transport passengers in Spain, August = **2.6** as written "2,6%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "más de 362,4 millones de pasajeros utilizaron el transporte público en agosto, un 2,6% más que en el mismo mes del año 2024."
  - p36 Year-on-year growth of metro passengers in Spain, August = **3.2** as written "3,2%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte por metro aumentó un 3,2% en tasa anual y el transporte urbano por autobús aumentó un 4,5%."
  - p37 Year-on-year growth of urban bus passengers in Spain, August = **4.5** as written "4,5%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte por metro aumentó un 3,2% en tasa anual y el transporte urbano por autobús aumentó un 4,5%."
  - p38 Year-on-year growth of bus passengers in Comunidad de Madrid, August = **11.8** as written "11,8%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "el número de viajeros en el transporte por autobús presentó las mayores subidas en Comunidad de Madrid (11,8%), Extremadura (10,7%) y País Vasco (6,9%)."
- dropped by code checks: 32 (number: scale word 'millones' is not English or CJK (not supported): 19; scale word 'million' not supported by quote or table header: 10; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 3)

### d4 [physical_flow] Tourism and population exposure

Hypothesis: August public transport demand is driven by resident commuting (lower in August) plus tourist trips (higher in August). National tourism arrivals/night stays in August, combined with per-tourist public-transport trip rates, can constrain the special/interurban component.

Queries issued by the searcher: INE llegadas turistas agosto 2025 España; pernoctaciones agosto 2025 España turismo INE; uso transporte público turistas España viajes por turista; Estadística de Transporte de Personas INE agosto 2025 viajeros transporte público

- `https://www.ine.es/dyngs/Prensa/FRONTUR0825.htm?print=1` -> **snapshot** (snapshot 20251002185237); points raw/verified 15/5
  - p39 Annual variation of international tourist arrivals to Spain, August 2025 vs Augu = **2.9** as written "2,9", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "España recibió 11,3 millones de turistas internacionales en agosto, un 2,9% más que en el mismo mes de 2024."
  - p40 Share of total international tourists with Illes Balears as main destination, Au = **22.5** as written "22,5%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Balearic destination share; tourism composition detail not needed for the ridership estimate.] quote: "Illes Balears fue el primer destino principal de los turistas en agosto, con el 22,5% del total."
  - p41 Share of total international tourists with Cataluña as main destination, August  = **19.4** as written "19,4%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Cataluña destination share; tourism composition detail not needed.] quote: "Le siguieron Cataluña (19,4%) y Andalucía (15,3%)."
  - p42 Share of total international tourists with Andalucía as main destination, August = **15.3** as written "15,3%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Andalucía destination share; tourism composition detail not needed.] quote: "Le siguieron Cataluña (19,4%) y Andalucía (15,3%)."
  - p43 Annual variation of excursionists (same-day visitors without overnight stay), Au = **7.5** as written "7,5%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El número de visitantes se incrementó un 7,5% entre los que no pernoctan (excursionistas), mientras que descendió un 0,8% entre los turistas con mayor duración (más de 15 noches)."
- `https://www.europapress.es/economia/noticia-pernoctaciones-hoteles-aumentan-09-agosto-pese-encarecerse-precios-58-20250923091134.html` -> **snapshot** (snapshot 20251025025609); points raw/verified 15/13
  - p44 Year-on-year change in hotel overnight stays in Spain, August = **0.9** as written "0,9%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "registraron en agosto un incremento interanual del 0,9% en las pernoctaciones"
  - p45 Year-on-year change in overnight stays by international travellers in Spain, Aug = **1.7** as written "1,7%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El número de pernoctaciones se ha visto impulsado por los viajeros internacionales, que incrementaron un 1,7% sus estancias."
  - p46 Year-on-year change in hotel overnight stays by Spain residents, August = **0.5** as written "0,5%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "los residentes en España recortaron sus pernoctaciones hoteleras un 0,5% interanual en el octavo mes del año"
  - p47 Hotel bed occupancy rate (places offered covered), Spain, August = **75** % (2025-08-01..2025-08-31) [DISCARD: Hotel bed occupancy rate; not a ridership driver with a usable conversion.] quote: "En total, ante el octavo mes del año se cubrió el 75% de las plazas ofertadas, mismo valor que un año antes."
  - p48 Weekend occupancy rate by places, Spain, August = **76.5** as written "76,5%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Weekend occupancy rate; not a ridership driver with a usable conversion.] quote: "El grado de ocupación por plazas en fin de semana creció un 0,3% y se situó en el 76,5%."
  - p49 Share of non-resident overnight stays from United Kingdom travellers, Spain, Aug = **25.4** as written "25,4%", value check pending % (2025-08-01..2025-08-31) [DISCARD: UK share of non-resident overnight stays; tourism composition detail not needed.] quote: "los viajeros de Reino Unido y Alemania concentraron el 25,4% y el 15,1%, respectivamente, del total de pernoctaciones de no residentes en agosto."
  - p50 Share of non-resident overnight stays from Germany travellers, Spain, August = **15.1** as written "15,1%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Germany share of non-resident overnight stays; tourism composition detail not needed.] quote: "los viajeros de Reino Unido y Alemania concentraron el 25,4% y el 15,1%, respectivamente, del total de pernoctaciones de no residentes en agosto."
  - p51 Share of non-resident overnight stays from France travellers, Spain, August = **11.8** as written "11,8%", value check pending % (2025-08-01..2025-08-31) [DISCARD: France share of non-resident overnight stays; tourism composition detail not needed.] quote: "Las pernoctaciones de viajeros procedentes de Francia, Italia y Países Bajos (los siguientes mercados emisores) representaron el 11,8%, 6,1% y 4,9% del total, respectivamente."
  - p52 Share of non-resident overnight stays from Italy travellers, Spain, August = **6.1** as written "6,1%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Italy share of non-resident overnight stays; tourism composition detail not needed.] quote: "Las pernoctaciones de viajeros procedentes de Francia, Italia y Países Bajos (los siguientes mercados emisores) representaron el 11,8%, 6,1% y 4,9% del total, respectivamente."
  - p53 Share of non-resident overnight stays from Netherlands travellers, Spain, August = **4.9** as written "4,9%", value check pending % (2025-08-01..2025-08-31) [DISCARD: Netherlands share of non-resident overnight stays; tourism composition detail not needed.] quote: "Las pernoctaciones de viajeros procedentes de Francia, Italia y Países Bajos (los siguientes mercados emisores) representaron el 11,8%, 6,1% y 4,9% del total, respectivamente."
  - p54 Year-on-year change in cumulative hotel overnight stays, Spain, first eight mont = **0.7** as written "0,7%", value check pending % (2025-01-01..2025-08-31) [DISCARD: Cumulative first-eight-months overnight stays; not needed for the August ridership estimate.] quote: "con 254,16 millones y un crecimiento global de las pernoctaciones fue del 0,7%, con una leve caída del 0,4% en las pernoctaciones nacionales y un alza del 1,3% en las internacionales."
  - p55 Year-on-year change in cumulative overnight stays by Spain residents, first eigh = **0.4** as written "0,4%", value check pending % (2025-01-01..2025-08-31) [DISCARD: Cumulative resident overnight stays; not needed.] quote: "con una leve caída del 0,4% en las pernoctaciones nacionales y un alza del 1,3% en las internacionales."
  - p56 Year-on-year change in cumulative overnight stays by international travellers, f = **1.3** as written "1,3%", value check pending % (2025-01-01..2025-08-31) [DISCARD: Cumulative international overnight stays; not needed.] quote: "con una leve caída del 0,4% en las pernoctaciones nacionales y un alza del 1,3% en las internacionales."
- `https://efe.com/economia/2025-12-19/viajes-espanoles-bajan-verano-gasto-sube/` -> **snapshot** (snapshot 20260302102436); points raw/verified 15/0
- `https://www.ine.es/dyngs/Prensa/EOAT0825.htm?print=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 27 (number: scale word 'millones' is not English or CJK (not supported): 10; number: ambiguous separators: '.' used as a thousands separator: 5; period year 2026 does not appear in the page text or URL (likely mis-dated): 1; period_end 2026-09-30 after as_of: 11)

### d5 [forecasts_markets] Official and analyst forecasts

Hypothesis: Any published forecast or nowcast of Spanish public transport ridership for 2026 (government transport ministry, operator guidance, EU statistics) can anchor the level and growth rate for August 2026.

Queries issued by the searcher: INE Estadística de Transporte de Personas viajeros agosto 2025 dato provisional; MITMA movilidad 2026 viajeros previsión transporte público; INE Estadística de Transporte de Viajeros junio 2026 datos provisionales viajeros; transporte público España 2026 crecimiento viajeros previsión

- `https://www.ine.es/dyngs/Prensa/en/TV0626.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ine.es/dyngs/Prensa/TV0825.pdf` -> **snapshot** (snapshot 20251221032913); points raw/verified 15/4
  - p57 Total public transport passengers, Spain, August 2025, annual growth rate = **2.6** as written "2,6%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El número de usuarios del transporte público aumentó un 2,6% en agosto respecto al mismo mes de 2024."
  - p58 Urban transport passengers, Spain, August 2025, annual growth rate = **4** as written "4,0%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte urbano subió un 4,0% en tasa anual y el interurbano cayó un 1,4%."
  - p59 Special and discretionary transport passengers, Spain, August 2025, annual growt = **11.7** as written "11,7%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "Más de 21,6 millones de usuarios utilizaron transporte especial y discrecional en agosto, lo que supuso un incremento del 11,7% en tasa anual."
  - p60 Urban transport annual growth rate, Spain, August 2025 (table row) = **4** as written "4,0", value check pending % annual change (2025-08-01..2025-08-31) [keep: ] quote: "Agosto 4,0 -1,4 11,7"
- `https://www.ine.es/jaxiT3/Datos.htm?t=20239` -> **snapshot** (snapshot 20260331043326); points raw/verified 1/0
- `https://confebus.org/publicaciones/ver/5304/ine-estadistica-transporte-de-viajeros-junio-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 12 (number: scale word 'millones' is not English or CJK (not supported): 6; value_as_written not in quote as a whole number: 1; scale word 'thousand' not supported by quote or table header: 5)

### d6 [shocks] Calendar and disruption effects

Hypothesis: August 2026 calendar (weekday composition, holiday timing) and any strikes, heatwaves, or service disruptions affect ridership relative to August 2025; adjusting the historical August baseline for these effects narrows the estimate.

Queries issued by the searcher: huelga transporte público España agosto 2026; ola de calor España agosto 2026 movilidad; calendario laboral agosto 2026 España festivos; Estadística de Transporte de Personas INE agosto 2026 viajeros

- `https://www.eldiario.es/spin/calendario-agosto-2026-festivos-fechas-destacadas_1_13420134.html` -> **snapshot** (snapshot 20260908220023); points raw/verified 6/6
  - p61 Days in August 2026 = **31** days (2026-08-01..2026-08-31) [keep: ] quote: "Agosto de 2026 comenzará en sábado y terminará en lunes, con 31 jornadas repartidas a lo largo de cinco fines de semana completos."
  - p62 Complete weekends in August 2026 = **5** as written "cinco", value check pending weekends (2026-08-01..2026-08-31) [keep: ] quote: "con 31 jornadas repartidas a lo largo de cinco fines de semana completos"
  - p63 Nationally applicable public holidays in August 2026 (Assumption, 15 August) = **15** day of month (2026-08-15..2026-08-15) [keep: ] quote: "El sábado 15 de agosto será festivo en todo el país por la Asunción de la Virgen."
  - p64 Descenso Internacional del Sella 2026 date (Saturday) = **8** day of month (2026-08-08..2026-08-08) [DISCARD: Sella descent date; local event detail with no usable ridership conversion.] quote: "La prueba tendrá lugar el sábado 8, de acuerdo con la tradición de disputarla en el primer sábado posterior al 2 de agosto."
  - p65 Descenso Internacional del Sella course length (Arriondas to Ribadesella) = **20** kilometres (2026-08-08..2026-08-08) [DISCARD: Sella descent course length; irrelevant to ridership.] quote: "El recorrido cubre unos 20 kilómetros entre Arriondas y Ribadesella"
  - p66 Día de Cantabria 2026 date (second Sunday, 9 August) = **9** day of month (2026-08-09..2026-08-09) [DISCARD: Día de Cantabria date; local event detail with no usable ridership conversion.] quote: "Un día después, el domingo 9, se celebrará el Día de Cantabria, conocido también como Día de la Montaña."
- `https://administracion.gob.es/pag_Home/en/dam/jcr:06b4b4ab-b5fa-4d05-badf-a763eb094c3d/Calendario_Laboral2026.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://elpais.com/sociedad/2026-08-11/el-gobierno-preve-hasta-15-millones-de-desplazamientos-adicionales-por-carretera-por-el-eclipse.html` -> **snapshot** (snapshot 20260812152946); points raw/verified 11/6
  - p67 Additional foreign visitors to Spain forecast from the eclipse, 10-16 August = **164** visitors (2026-08-10..2026-08-16) [keep: ] quote: "El Gobierno prevé que el eclipse genere 164.000 visitantes extranjeros adicionales a España entre el 10 y el 16 de agosto."
  - p68 Share of people with eclipse plans travelling to a province other than their res = **8.4** as written "8,4%", value check pending % (2026-08-12..2026-08-12) [DISCARD: Share of eclipse travellers going to another province; too indirect to convert to journeys.] quote: "Un 8,4% de las personas con planes para ver el eclipse tiene previsto desplazarse a una provincia distinta de la de su residencia"
  - p69 Increase in scheduled airplane seats for eclipse week vs same period 2025 = **7.9** as written "7,9%", value check pending % (2026-08-10..2026-08-16) [keep: ] quote: "se prevé un aumento del 7,9% en los asientos de avión programados para la semana del eclipse respecto al mismo periodo de 2025"
  - p70 Increase in hotel bookings for August 2026 vs August 2025 = **17.8** as written "17,8%", value check pending % (2026-08-01..2026-08-31) [keep: ] quote: "un incremento del 17,8% en las reservas hoteleras para agosto de 2026 en comparación con agosto de 2025"
  - p71 Peak time of the eclipse (local time) = **20.3** hour of day (2026-08-12..2026-08-12) [DISCARD: Eclipse peak local time; irrelevant to ridership totals.] quote: "que tendrá su momento álgido a las 20.30 horas"
  - p72 Temperatures forecast around eclipse travel (Valencia warning) = **30** degrees Celsius (2026-08-12..2026-08-12) [DISCARD: Forecast temperatures; irrelevant to ridership totals.] quote: "en ciertas vías con temperaturas que pueden rondar los 30 grados"
- `https://www.elnortedecastilla.es/segovia/junta-fija-servicios-minimos-huelga-transporte-viajeros-20260605124255-nt.html` -> **snapshot** (snapshot 20260714182621); points raw/verified 15/0
- dropped by code checks: 20 (number: scale word 'millones' is not English or CJK (not supported): 5; number: more than one number in value_as_written: 4; period_end 2026-09-30 after as_of: 11)

### b1 [own_history] d1

Hypothesis: The August 2025 ETP total level (~362.4 million, p32/p35) is the base for a YoY-scaling route; a published August 2026 YoY growth estimate (or a 2026 year-to-date ETP growth rate) would let us scale it. Without a 2026 growth signal the route relies on an assumption.

Queries issued by the searcher: INE Estadística de Transporte de Personas 2026 viajeros millones; INE transporte de personas agosto 2025 362 millones viajeros

- `https://www.ine.es/dyngs/Prensa/TV0726.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ine.es/dyngs/Prensa/TV0825.pdf` -> **snapshot** (snapshot 20251221032913); points raw/verified 15/8
  - p73 Total public transport passengers YoY growth rate, Spain, August 2025 = **2.6** as written "2,6%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El número de usuarios del transporte público aumentó un 2,6% en agosto respecto al mismo mes de 2024."
  - p74 Urban transport YoY growth rate, Spain, August 2025 = **4** as written "4,0%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte urbano subió un 4,0% en tasa anual y el interurbano cayó un 1,4%."
  - p75 Urban transport YoY growth rate, Spain, July 2025 = **6.2** as written "6,2", value check pending % year-on-year (2025-07-01..2025-07-31) [keep: ] quote: "Julio 6,2 -0,2 3,3"
  - p76 Interurban transport YoY growth rate, Spain, July 2025 = **-0.2** as written "-0,2", value check pending % year-on-year (2025-07-01..2025-07-31) [keep: ] quote: "Julio 6,2 -0,2 3,3"
  - p77 Special and discretionary transport YoY growth rate, Spain, July 2025 = **3.3** as written "3,3", value check pending % year-on-year (2025-07-01..2025-07-31) [keep: ] quote: "Julio 6,2 -0,2 3,3"
  - p78 Urban transport YoY growth rate, Spain, June 2025 = **6.8** as written "6,8", value check pending % year-on-year (2025-06-01..2025-06-30) [keep: ] quote: "Junio 6,8 9,7 2,0"
  - p79 Interurban transport YoY growth rate, Spain, June 2025 = **9.7** as written "9,7", value check pending % year-on-year (2025-06-01..2025-06-30) [keep: ] quote: "Junio 6,8 9,7 2,0"
  - p80 Special and discretionary transport YoY growth rate, Spain, June 2025 = **2** as written "2,0", value check pending % year-on-year (2025-06-01..2025-06-30) [keep: ] quote: "Junio 6,8 9,7 2,0"
- `https://www.informacion.es/economia/2026/06/11/tren-alta-velocidad-baja-abril-incidencias-131272796.html` -> **snapshot** (snapshot 20260711182757); points raw/verified 15/9
  - p81 Year-on-year growth of total public transport passengers in Spain, April 2026 = **6.1** as written "6,1%", value check pending % (2026-04-01..2026-04-30) [keep: ] quote: "lo que supuso un incremento interanual del 6,1%, el segundo mes consecutivo al alza"
  - p82 Average year-on-year growth of total public transport passengers in Spain, Jan-A = **1.9** as written "1,9%", value check pending % (2026-01-01..2026-04-30) [keep: ] quote: "la cifra de usuarios del transporte público español aumentó de media un 1,9% frente al mismo periodo del año pasado"
  - p83 Year-on-year growth of urban transport passengers in Spain, Jan-Apr 2026 = **3.8** as written "3,8%", value check pending % (2026-01-01..2026-04-30) [keep: ] quote: "apoyado en el transporte urbano, que creció un 3,8%"
  - p84 Year-on-year growth of special/discretionary transport passengers in Spain, Jan- = **0.7** as written "0,7%", value check pending % (2026-01-01..2026-04-30) [keep: ] quote: "mientras que el especial creció apenas un 0,7%"
  - p85 Year-on-year growth of interurban transport passengers in Spain, Jan-Apr 2026 = **1.8** as written "1,8%", value check pending % (2026-01-01..2026-04-30) [keep: ] quote: "y el interurbano bajó un 1,8%"
  - p86 Year-on-year growth of urban transport passengers in Spain, April 2026 = **8.4** as written "8,4%", value check pending % (2026-04-01..2026-04-30) [keep: ] quote: "El transporte urbano fue utilizado por más de 318,4 millones de viajeros en abril, un 8,4% más que un año atrás"
  - p87 Year-on-year growth of interurban transport passengers in Spain, April 2026 = **1.2** as written "1,2%", value check pending % (2026-04-01..2026-04-30) [keep: ] quote: "el uso del transporte interurbano aumentó un 1,2% en abril, hasta superar los 140,4 millones de viajeros"
  - p88 Year-on-year growth of special and discretionary transport passengers in Spain,  = **6.1** as written "6,1%", value check pending % (2026-04-01..2026-04-30) [keep: ] quote: "Más de 45,6 millones de personas utilizaron transporte especial (escolar y laboral) y discrecional (para eventos concretos) en abril, lo que se tradujo en un incremento del 6,1% en tasa anual."
  - p89 Year-on-year decline of high-speed rail passengers in Spain, Jan-Apr 2026 = **19.6** as written "19,6%", value check pending % (2026-01-01..2026-04-30) [keep: ] quote: "La cifra de usuarios de la alta velocidad ferroviaria, que incluye Ave, Ouigo, Iryo y Avlo, cayó un 19,6% en comparación interanual en los cuatro primeros meses del año"
- `https://www.elnortedecastilla.es/castillayleon/bus-urbano-crece-castilla-leon-alcanza-millones-20260807110831-nt.html` -> **snapshot** (snapshot 20260808143900); points raw/verified 15/12
  - p90 National total public transport passengers YoY growth, Spain, June = **2** % (2026-06-01..2026-06-30) [keep: ] quote: "A nivel nacional, más de 506,5 millones de pasajeros utilizaron el transporte público en junio, un 2% más que en el mismo mes del año 2025."
  - p91 Urban bus passengers YoY growth, Spain, June = **1.6** as written "1,6%", value check pending % (2026-06-01..2026-06-30) [keep: ] quote: "En España, los usuarios de este servicio aumentaron un 1,6% y alcanzaron los 187,7 millones de viajeros"
  - p92 Urban transport passengers YoY growth, Spain, June = **3.1** as written "3,1%", value check pending % (2026-06-01..2026-06-30) [keep: ] quote: "El transporte urbano aumentó un 3,1% en tasa anual y el interurbano disminuyó un 0,6%."
  - p93 Interurban transport passengers YoY growth, Spain, June = **0.6** as written "0,6%", value check pending % (2026-06-01..2026-06-30) [keep: ] quote: "El transporte urbano aumentó un 3,1% en tasa anual y el interurbano disminuyó un 0,6%."
  - p94 Rail transport passengers YoY decline within interurban, Spain, June = **8.3** as written "8,3%", value check pending % (2026-06-01..2026-06-30) [keep: ] quote: "Dentro del interurbano, destacó el descenso del 8,3% en el transporte por ferrocarril."
  - p95 Urban bus passengers YoY growth, Castilla y León, June = **7.6** as written "7,6%", value check pending % (2026-06-01..2026-06-30) [keep: ] quote: "El número de usuarios de transporte urbano por autobús en Castilla y León aumentó un 7,6% en junio con respecto al mismo mes del ... año pasado, hasta los 7,3 millones de viajeros."
  - p96 Urban bus passengers YoY growth, Murcia, June = **12** % (2026-06-01..2026-06-30) [keep: ] quote: "solo por detrás del 12% registrado en Murcia, el 10% de Extremadura y el 8,6% de Asturias"
  - p97 Urban bus passengers YoY growth, Extremadura, June = **10** % (2026-06-01..2026-06-30) [keep: ] quote: "solo por detrás del 12% registrado en Murcia, el 10% de Extremadura y el 8,6% de Asturias"
  - p98 Urban bus passengers YoY growth, Asturias, June = **8.6** as written "8,6%", value check pending % (2026-06-01..2026-06-30) [keep: ] quote: "solo por detrás del 12% registrado en Murcia, el 10% de Extremadura y el 8,6% de Asturias"
  - p99 Urban bus passengers YoY growth, Cataluña, June = **7.5** as written "7,5%", value check pending % (2026-06-01..2026-06-30) [keep: ] quote: "mientras que aumentó un 7,5% en Cataluña, un 6% en País Vasco, un 4,3% en Canarias, un 4,1% en Castilla-La Mancha y Andalucía"
  - p100 Urban bus passengers YoY growth, País Vasco, June = **6** % (2026-06-01..2026-06-30) [keep: ] quote: "mientras que aumentó un 7,5% en Cataluña, un 6% en País Vasco, un 4,3% en Canarias, un 4,1% en Castilla-La Mancha y Andalucía"
  - p101 Urban bus passengers YoY growth, Canarias, June = **4.3** as written "4,3%", value check pending % (2026-06-01..2026-06-30) [keep: ] quote: "mientras que aumentó un 7,5% en Cataluña, un 6% en País Vasco, un 4,3% en Canarias, un 4,1% en Castilla-La Mancha y Andalucía"
- dropped by code checks: 16 (number: scale word 'millones' is not English or CJK (not supported): 10; value_as_written not in quote as a whole number: 2; scale word 'thousand' not supported by quote or table header: 1; scale word 'million' not supported by quote or table header: 3)

### b2 [related_series] d2

Hypothesis: Component-level August 2025 levels (urban 222.8M, interurban ~118M, special ~21.6M) plus 2026 component growth signals would let us sum a structured estimate. A 2026 urban/interurban/special growth signal is the missing input.

Queries issued by the searcher: INE Estadística de Transporte de Personas 2026 viajeros urbanos interurbanos especial; EMT Madrid viajeros 2026 millones autobús; TMB Barcelona viatgers 2026 metro bus augment juliol; "transporte de viajeros" INE julio 2026 datos provisionales 449 millones anexo tablas

- `https://www.ine.es/dyngs/Prensa/TV0726.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://anetra-informa.es/noticias/la-demanda-del-transporte-en-autobus-crece-un-25-hasta-mayo-apenas-un-05-en-el-caso-del-regular-de-uso-especial-y-d` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ine.es/dyngs/Prensa/TV0126.htm?print=1` -> **snapshot** (snapshot 20260510124115); points raw/verified 15/9
  - p102 Total public transport passengers, Spain, January 2026, annual growth rate = **1.8** as written "1,8%", value check pending % (2026-01-01..2026-01-31) [keep: ] quote: "El número de usuarios del transporte público disminuyó un 1,8% en enero respecto al mismo mes de 2025."
  - p103 Urban transport passengers, Spain, January 2026, annual growth rate = **0.2** as written "0,2%", value check pending % (2026-01-01..2026-01-31) [keep: ] quote: "El transporte urbano bajó un 0,2% en tasa anual y el interurbano un 4,7%."
  - p104 Interurban transport passengers, Spain, January 2026, annual growth rate = **4.7** as written "4,7%", value check pending % (2026-01-01..2026-01-31) [keep: ] quote: "El transporte urbano bajó un 0,2% en tasa anual y el interurbano un 4,7%."
  - p105 Special and discretionary transport passengers, Spain, January 2026, annual grow = **4.4** as written "4,4%", value check pending % (2026-01-01..2026-01-31) [keep: ] quote: "Más de 36,9 millones de usuarios utilizaron transporte especial y discrecional en enero, lo que supuso un descenso del 4,4% en tasa anual."
  - p106 Special transport passengers, Spain, January 2026, annual growth rate = **6.8** as written "6,8%", value check pending % (2026-01-01..2026-01-31) [keep: ] quote: "El número de pasajeros del transporte especial bajó un 6,8% y superó los 25,7 millones de usuarios."
  - p107 Discretionary transport passengers, Spain, January 2026, annual growth rate = **1.8** as written "1,8%", value check pending % (2026-01-01..2026-01-31) [keep: ] quote: "Por su parte, el transporte discrecional creció un 1,8% respecto al mismo mes del año 2025, con más de 11,1 millones de viajeros."
  - p108 Interurban bus transport passengers, Spain, January 2026, annual growth rate = **0.3** as written "0,3%", value check pending % (2026-01-01..2026-01-31) [keep: ] quote: "Dentro del interurbano, destacó el incremento del 0,3% en el transporte por autobús."
  - p109 Metro transport passengers, Spain, January 2026, annual growth rate = **1.3** as written "1,3%", value check pending % (2026-01-01..2026-01-31) [keep: ] quote: "El transporte por metro aumentó un 1,3% en tasa anual, mientras que el transporte urbano por autobús disminuyó un 1,2%."
  - p110 Urban bus transport passengers, Spain, January 2026, annual growth rate = **1.2** as written "1,2%", value check pending % (2026-01-01..2026-01-31) [keep: ] quote: "El transporte por metro aumentó un 1,3% en tasa anual, mientras que el transporte urbano por autobús disminuyó un 1,2%."
- `https://laciutat.cat/laciutatdebarcelona/metro-barcelona-tanca-juliol-record-supera-primera-vegada-40-milions-usuaris_900245_102.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 6 (scale word 'million' not supported by quote or table header: 6)

### b3 [base_rates] d4

Hypothesis: The eclipse and tourism surge (p67, p69, p70) could materially lift August 2026 special/discretionary and interurban ridership; a per-tourist public-transport trip rate would convert the extra visitors into journeys and bound the tourism contribution.

Queries issued by the searcher: INE Estadística de Transporte de Personas viajeros agosto 2025 transporte discrecional; share of tourist trips made by public transport Spain survey EGATUR mode of transport; "turistas" "transporte público" porcentaje desplazamientos España estudio movilidad turística reparto modal; INE "Estadística de Transporte de Personas" agosto 2026 viajeros; "Encuesta de Satisfacción de los Turistas Internacionales" 2025 Turespaña transporte público 69%; "desplazamientos por turista" "al día" movilidad turística España estudio número viajes turista destino

- `https://www.ine.es/dyngs/Prensa/TV0825.pdf` -> **snapshot** (snapshot 20251221032913); points raw/verified 15/3
  - p111 Annual change in total public transport passengers, Spain, August 2025 vs August = **2.6** as written "2,6%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El número de usuarios del transporte público aumentó un 2,6% en agosto respecto al mismo mes de 2024."
  - p112 Annual change in urban transport passengers, Spain, August 2025 vs August 2024 = **4** as written "4,0%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte urbano subió un 4,0% en tasa anual y el interurbano cayó un 1,4%."
  - p113 Annual change in interurban bus passengers, Spain, August 2025 vs August 2024 = **1.8** as written "1,8%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "Dentro del interurbano, destacó el incremento del 1,8% en el transporte por autobús."
- `https://www.autobusesyautocares.com/texto-diario/mostrar/5461933/transporte-especial-discrecional-crece-11-agosto` -> **snapshot** (snapshot 20251013182634); points raw/verified 15/8
  - p114 Year-on-year growth rate of special and discretionary transport passengers in Sp = **11.7** as written "11,7%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "lo que supone un incremento del 11,7% en tasa anual"
  - p115 Year-on-year growth of special transport passengers in Spain, August = **15.7** as written "15,7%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "el número de pasajeros del transporte especial subió un 15,7%"
  - p116 Year-on-year growth of school transport demand in Spain, August = **14** % (2025-08-01..2025-08-31) [keep: ] quote: "la demanda del transporte escolar aumentó un 14%"
  - p117 Year-on-year growth of worker transport demand in Spain, August = **15.7** as written "15,7%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "el de trabajadores un 15,7%"
  - p118 Year-on-year growth of discretionary transport passengers in Spain, August = **10.4** as written "10,4%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "el uso del transporte discrecional creció un 10,4% respecto al mismo mes del año 2024"
  - p119 Year-on-year growth of interurban transport passenger volume in Spain, August = **1.8** as written "1,8%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "el crecimiento del volumen de pasajeros fue del 1,8%"
  - p120 Year-on-year growth of long-distance coach passengers in Spain, August = **12.2** as written "12,2%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "los servicios de autocares de larga distancia registraron una afluencia de 2,4 millones de usuarios, con un alza del 12,2%"
  - p121 Year-on-year growth of medium-distance coach passengers in Spain, August = **6.6** as written "6,6%", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "los de media distancia acogieron a 22,6 millones de viajeros, con una subida del 6,6%"
- `https://www.infobae.com/espana/agencias/2025/10/10/el-transporte-interurbano-de-viajeros-por-tren-se-redujo-en-agosto-casi-un-6-interanual/` -> **snapshot** (snapshot 20251010091723); points raw/verified 15/8
  - p122 Year-on-year growth of total public transport passengers in Spain, August = **2.6** as written "2,6 %", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "un 2,6 % más que en el mismo mes de 2024."
  - p123 Year-on-year growth of special transport passengers in Spain, August = **11.7** as written "11,7 %", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte especial (destinado a grupos específicos como escolares o trabajadores) fue el que más creció en agosto, un 11,7 %"
  - p124 Year-on-year growth of urban transport passengers in Spain, August = **4** % (2025-08-01..2025-08-31) [keep: ] quote: "en tanto que el urbano aumentó un 4 % y el interurbano se redujo un 1,4 %."
  - p125 Year-on-year growth of discretionary transport passengers in Spain, August = **10.4** as written "10,4 %", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "el transporte discrecional creció un 10,4 % respecto al mismo mes del año 2024"
  - p126 Year-on-year growth of interurban rail passengers in Spain, August = **5.9** as written "5,9 %", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "El transporte interurbano de viajeros por ferrocarril se redujo un 5,9 % interanual el pasado mes de agosto"
  - p127 Year-on-year decline of medium-distance rail passengers in Spain, August = **24.4** as written "24,4 %", value check pending % (2025-08-01..2025-08-31) [keep: ] quote: "lastrado especialmente por el recorte del 24,4 % registrado por los trayectos de media distancia"
  - p128 Average year-on-year growth of public transport passengers in Spain, first eight = **3.1** as written "3,1 %", value check pending % (2025-01-01..2025-08-31) [keep: ] quote: "En los ocho primeros meses de 2025, el número de usuarios del transporte público aumentó de media un 3,1 %."
  - p129 Year-on-year growth of interurban transport passengers in Spain, first eight mon = **2.4** as written "2,4 %", value check pending % (2025-01-01..2025-08-31) [keep: ] quote: "El transporte urbano fue el que más creció, un 3,7 %, en tanto que el interurbano lo hizo en un 2,4 % y el especial, en un 1 %."
- `https://anetra-informa.es/noticias/el-regular-especial-y-el-discrecional-suman-viajeros-en-agosto-un-157-y-un-104-respectivamente/` -> **snapshot** (snapshot 20260215133242); points raw/verified 0/0
- dropped by code checks: 26 (number: scale word 'millones' is not English or CJK (not supported): 18; scale word 'thousand' not supported by quote or table header: 4; value_as_written not in quote as a whole number: 4)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['spain passengers', 'ine transport', 'public transport spain']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p15', 'p32', 'p35', 'p57'] All report the same INE August 2025 headline: total public transport passengers +2.6% YoY, ~362.4 million. They are not independent measurements; the news outlets (elindependiente, viaempresa, confebu
- corroborating: ['p2', 'p7', 'p16', 'p33', 'p58', 'p60'] Same INE August 2025 urban transport +4.0% figure repeated across outlets and the INE table row. Single underlying measurement.
- corroborating: ['p3', 'p8', 'p59'] Special/discretionary +11.7% in August 2025, same INE source; p3 additionally gives the level (>21.6 million).
- corroborating: ['p5', 'p6', 'p17', 'p18', 'p36', 'p37'] Metro +3.2% and urban bus +4.5% for August 2025, all from the same INE release.
- corroborating: ['p4', 'p34'] Interurban bus +1.8% (p4) and interurban total -1.4% (p34) are consistent: bus grew while the interurban aggregate fell, implying weakness in other interurban modes (rail/coastal). Different sub-scope
- corroborating: ['p20', 'p23', 'p38'] Comunidad de Madrid urban bus +11.8% in August 2025, repeated across outlets from the same INE regional breakdown.
- corroborating: ['p21', 'p22'] EMT Madrid bus +13.9% and Metro de Madrid +3.7% are operator-level figures consistent with the regional/national pattern (Madrid bus growth above national 4.5%).
- corroborating: ['p29', 'p31'] Barcelona metro +6% (30.3 million) and Barcelona urban bus +0.6% (14.9 million) are operator-level August 2025 figures; consistent with Catalonia urban bus -0.5% (p28/p30) being dragged by non-Barcelo
- corroborating: ['p28', 'p30'] Catalonia urban bus -0.5% appears in both Europapress and viaempresa, same INE regional data.
- corroborating: ['p39', 'p43', 'p44', 'p45', 'p46'] August 2025 tourism signals: international arrivals +2.9%, excursionists +7.5%, hotel overnight stays +0.9% (international +1.7%, residents -0.5%). Together they describe a modestly growing August tou
- corroborating: ['p61', 'p62', 'p63'] August 2026 calendar: 31 days, starts Saturday, ends Monday, five complete weekends, 15 August national holiday falling on a Saturday. Consistent calendar facts.
- corroborating: ['p67', 'p69', 'p70'] Eclipse-related August 2026 demand signals: 164k additional foreign visitors, +7.9% scheduled seats in eclipse week, +17.8% hotel bookings for August 2026 vs 2025. All point to elevated August 2026 to
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p15', 'p32', 'p35', 'p57', 'p73', 'p111', 'p122'] All report the same INE August 2025 headline: total public transport passengers +2.6% YoY, with 362.4 million in August 2025. These are multiple media/agency republications of one INE measurement, not
- corroborating: ['p2', 'p7', 'p16', 'p33', 'p58', 'p60', 'p74', 'p112', 'p124'] Same INE August 2025 urban transport figure: +4.0% YoY, 222.8 million passengers. Shared underlying source; corroborates the urban component level and growth.
- corroborating: ['p3', 'p8', 'p59', 'p114', 'p123'] Same INE August 2025 special/discretionary figure: >21.6 million passengers, +11.7% YoY. Shared source; usable as the special/discretionary component level.
- corroborating: ['p34', 'p119'] Interurban August 2025 level ~118 million, with the interurban total down 1.4% YoY while interurban bus rose 1.8%. Consistent with the INE release; the 1.8% refers to the bus subcomponent, not the who
- corroborating: ['p4', 'p113'] Interurban bus +1.8% in August 2025; same INE subcomponent figure repeated. Not a total-interurban growth rate.
- corroborating: ['p5', 'p6', 'p17', 'p18', 'p36', 'p37'] Metro +3.2% and urban bus +4.5% in August 2025; same INE subcomponent figures repeated across outlets.
- corroborating: ['p20', 'p23', 'p38'] Comunidad de Madrid urban bus +11.8% in August 2025; same regional figure repeated. Regional detail, not national.
- corroborating: ['p21', 'p22'] EMT Madrid bus +13.9% and Metro de Madrid +3.7% in August 2025; operator-level detail consistent with the strong Madrid urban bus growth reported nationally.
- corroborating: ['p28', 'p30'] Cataluña urban bus -0.5% in August 2025; same regional figure repeated.
- corroborating: ['p29', 'p31'] Barcelona metro +6% (30.3M) and Barcelona urban bus +0.6% (14.9M) in August 2025; operator-level detail.
- corroborating: ['p39', 'p43', 'p44', 'p45', 'p46'] August 2025 tourism context: international arrivals +2.9% (11.3M), excursionists +7.5%, hotel overnight stays +0.9% (international +1.7%, residents -0.5%). These describe the tourism backdrop that dri
- corroborating: ['p61', 'p62', 'p63'] August 2026 calendar: 31 days, starts Saturday, ends Monday, five complete weekends, 15 August a national holiday falling on a Saturday. Calendar context for seasonal adjustment; the Saturday holiday 
- corroborating: ['p67', 'p69', 'p70'] Eclipse/tourism surge signals for August 2026: 164,000 additional foreign visitors 10-16 August, +7.9% scheduled airplane seats that week, +17.8% hotel bookings for August 2026 vs 2025. These are fore
- corroborating: ['p81', 'p82', 'p83', 'p84', 'p85', 'p86', 'p87', 'p88', 'p89'] 2026 year-to-date INE-based figures: Jan-Apr average total +1.9%, urban +3.8%, special +0.7%, interurban -1.8%; April total +6.1%, urban +8.4%, interurban +1.2%, special +6.1%; high-speed rail -19.6% 
- corroborating: ['p90', 'p91', 'p92', 'p93', 'p94'] June 2026 INE release: total 506.5M, +2.0% YoY; urban +3.1%, interurban -0.6%, urban bus +1.6% (187.7M), interurban rail -8.3%. Most recent pre-cutoff national growth signal; note the text says interu
- corroborating: ['p95', 'p96', 'p97', 'p98', 'p99', 'p100', 'p101'] June 2026 regional urban bus growth: Murcia +12%, Extremadura +10%, Asturias +8.6%, Castilla y León +7.6%, Cataluña +7.5%, País Vasco +6%, Canarias +4.3%, Castilla-La Mancha/Andalucía +4.1%. Regional 
- corroborating: ['p102', 'p103', 'p104', 'p105', 'p106', 'p107', 'p108', 'p109', 'p110'] January 2026 INE release: total -1.8%, urban -0.2%, interurban -4.7%, special -4.4% (special transport -6.8%, discretionary +1.8%), interurban bus +0.3%, metro +1.3%, urban bus -1.2%. Note the text fo
- corroborating: ['p75', 'p76', 'p77', 'p78', 'p79', 'p80'] Mid-2025 monthly component growth (June/July 2025) showing urban growth 6-7%, interurban volatile, special 2-3%. Historical context for the 2025 baseline; not directly the target period.
- corroborating: ['p115', 'p116', 'p117', 'p118', 'p120', 'p121', 'p126', 'p127'] August 2025 subcomponent detail: special transport +15.7% (school +14%, workers +15.7%), discretionary +10.4%, long-distance coach +12.2% (2.4M), medium-distance coach +6.6% (22.6M), interurban rail -
- corroborating: ['p128', 'p129'] First eight months of 2025: total +3.1%, urban +3.7%, interurban +2.4%, special +1.0%. Historical context for the 2025 baseline.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | August 2026 YoY growth factor for total public transport passengers | 1.025 | 0.98..1.07 | 0.9159..1.145 (widened) | ratio | unused | Anchored on the 2026 growth regime: Jan-Apr 2026 average +1.9% (p82), April +6.1% (p81), June +2.0% (p90), January -1.8% (p102). August 2025 itself grew 2.6% (p1). August 2026 has a tourism surge (eclipse, +17.8% hotel bookings p70, +164k visitors p67) but also a Saturday 15 August holiday (p63) and | The 2026 national growth regime continues into August and the eclipse tourism boost roughly offsets the weaker resident-commuting month. | A published July or August 2026 ETP release showing total growth outside the 0.98-1.07 range, or evidence the eclipse surge was much larger/smaller than bookings suggest. |
| a2 | August 2026 special/discretionary growth factor relative to August 2025 | 1.08 | 0.95..1.25 | 0.95..1.25 | ratio | unused | Special/discretionary grew 11.7% in August 2025 (p3) but only 0.7% Jan-Apr 2026 (p84) and 6.1% in April 2026 (p88); the eclipse and tourism surge (p67, p70) should lift discretionary travel in August 2026. Central ~+8%, wide range. | The eclipse/tourism surge lifts discretionary transport while special (school/worker) transport stays near its 2026 trend. | Evidence that August 2026 special/discretionary growth was near zero or negative, or that the eclipse surge did not materialise in transport demand. |
| a3 | August 2026 urban transport growth factor relative to August 2025 | 1.03 | 0.98..1.08 | 0.9202..1.15 (widened) | ratio | unused | Urban transport grew 4.0% in August 2025 (p2), 3.8% Jan-Apr 2026 (p83), 8.4% in April 2026 (p86), and 3.1% in June 2026 (p92). August 2026 tourism boosts city systems but resident commuting is lower; central ~+3%. | Urban ridership continues its 2026 trend with a modest tourism uplift. | A 2026 urban growth signal outside the 0.98-1.08 range. |
| a4 | August 2026 interurban transport growth factor relative to August 2025 | 1 | 0.94..1.06 | 0.8928..1.116 (widened) | ratio | unused | Interurban fell 1.4% in August 2025 (p34), fell 1.8% Jan-Apr 2026 (p85), rose 1.2% in April 2026 (p87), and was around -0.6% in June 2026 (p93). High-speed rail is down sharply (p89, p94). Central ~flat, wide range. | Interurban ridership stays near its 2025 level with offsetting rail decline and coach/tourism growth. | A 2026 interurban growth signal outside the 0.94-1.06 range. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | n/a | ['p32'] / ['a1'] | [] |  | 0.00 |  | formula_mc needs at least one input that is a quantity (not a share, ratio or %); a product of ratios cannot produce the target. Inputs: p32 = p32 (unit "%", name "Total public transport passengers in |
| m2 | formula_mc | n/a | ['p33', 'p34', 'p3'] / ['a2', 'a3', 'a4'] | [] |  | 0.00 |  | formula_mc needs at least one input that is a quantity (not a share, ratio or %); a product of ratios cannot produce the target. Inputs: p33 = p33 (unit "%", name "Urban transport passengers in Spain, |

- m1 coverage: the whole target
- m2 coverage: sum over channel of urban, interurban, special/discretionary

Result: central **n/a** passenger, 80% interval [n/a, n/a] passenger, basis no_method (no method produced an estimate, so there is no interval), weight rule None, weight on methods that use assumptions 0.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

No estimate: no estimation method could be computed from the verified evidence.

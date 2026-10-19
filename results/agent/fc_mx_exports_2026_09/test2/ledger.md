# Evidence ledger: fc_mx_exports_2026_09

- Question: Assume today is 2026-10-19. You know nothing published after this date. Estimate Mexico's total merchandise exports in September 2026, in US dollars (original figures, not seasonally adjusted), as they will be first reported in INEGI's timely trade balance bulletin (Balanza Comercial de Mercancías de México, información oportuna).
- as_of: 2026-10-19
- Pinned target: Total value of Mexico's merchandise exports (all commodities, f.o.b.) for the calendar month of September 2026, as first published in INEGI's timely merchandise trade balance bulletin (Balanza Comercial de Mercancías de México, información oportuna), original (not seasonally adjusted) figures, in cu | unit USD | period 2026-09-01..2026-09-30 | publisher INEGI (Instituto Nacional de Estadística y Geografía), with SAT/ANAM customs data; timely bulletin 'Balanza Comercial de Mercancías de México, información oportuna'

## Directions and pages

### d1 [own_history] INEGI timely bulletin time series

Hypothesis: September exports follow a recurring seasonal pattern relative to August and to the same month of prior years; the most recent published months (July/August 2026) anchor the level, and the September/August ratio from prior years transfers the seasonal step.

Queries issued by the searcher: INEGI balanza comercial mercancías información oportuna exportaciones agosto 2026; México exportaciones totales mensuales 2026 INEGI balanza comercial oportuna julio; INEGI balanza comercial septiembre 2025 exportaciones totales mdd información oportuna; "septiembre de 2024" balanza comercial exportaciones totales INEGI millones de dólares

- `https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/comext_o/balcom_o2026_09.pdf` -> **live_dated** (page date 2026-09-01); points raw/verified 15/3
  - p1 Mexico total merchandise exports, original, August 2026 annual variation (%) = **40.4** percent (2026-08-01..2026-08-31) [DISCARD: August 2026 y/y growth; the seasonal route uses the September 2025 level (p35) times a September/August ratio, so August] quote: "Aumentaron las exportaciones 40.4 %"
  - p2 Mexico total merchandise exports, original, January-August 2026 annual variation = **29.3** percent (2026-01-01..2026-08-31) [DISCARD: Cumulative Jan-Aug growth; not a September level and not needed for the seasonal route.] quote: "En el periodo enero-agosto de 2026, el valor de las exportaciones totales sumó 549 398 mdd, lo que significó un crecimiento anual de 29.3 por ciento."
  - p3 Mexico total merchandise exports, seasonally adjusted, August 2026 monthly varia = **1.23** percent (2026-08-01..2026-08-31) [DISCARD: Seasonally adjusted monthly growth; the target is original (not seasonally adjusted), so this cannot be applied to an or] quote: "En el mes que se reporta, en términos desestacionalizados, las exportaciones totales registraron un avance mensual de 1.23 por ciento."
- `https://200.33.109.5/app/saladeprensa/noticia/10282` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/comext_o/balcom_o2025_10.pdf` -> **live_dated** (page date 2025-10-01); points raw/verified 15/2
  - p4 Mexico total merchandise exports, September 2025, annual percentage change = **13.8** % (2025-09-01..2025-09-30) [DISCARD: Redundant copy of p35 (same release, no USD level).] quote: "Incrementaron las exportaciones 13.8 % y las importaciones, 15.2 % a tasa anual, en septiembre de 2025"
  - p5 Mexico total merchandise exports, September 2025, seasonally adjusted monthly pe = **1.33** % (2025-09-01..2025-09-30) [DISCARD: Seasonally adjusted September 2025 change; not applicable to original figures.] quote: "las exportaciones totales registraron una caída mensual de 1.33 por ciento"
- `https://www.inegi.org.mx/app/saladeprensa/noticia/11149` -> **dropped** (live page has no readable date); points raw/verified -/-
- dropped by code checks: 25 (scale word 'million' not supported by quote or table header: 25)

### d2 [related_series] US Census/BEA US imports from Mexico

Hypothesis: The large majority of Mexico's exports go to the US; US goods imports from Mexico for September 2026 (Census FT900 advance or BEA) track Mexico's exports with a stable ratio, allowing a bridge: Mexico exports ≈ US imports from Mexico / US share.

Queries issued by the searcher: US Census advance goods trade balance September 2026 imports from Mexico; Census FT900 US imports from Mexico August 2026; INEGI balanza comercial de mercancías información oportuna agosto 2026 exportaciones totales; "advance" goods trade balance September 2026 Census Bureau release date imports; census.gov press release August 2026 goods and services trade deficit Mexico imports $60.6 billion; inegi.org.mx balcom_o2026_08.pdf exportaciones septiembre 2025 55 mil millones balanza comercial oportuna

- `https://www.liderempresarial.com/exportaciones-de-mexico-a-estados-unidos-rompen-record-en-agosto-2026/` -> **live_dated** (page date 2026-10-07); points raw/verified 15/0
- `https://www.excelsior.com.mx/finanzas/exportaciones-mexicanas-eu-marcan-record-reporte-agosto` -> **live_dated** (page date 2026-10-06); points raw/verified 15/13
  - p6 Year-over-year growth of US goods imports from Mexico, August 2026 = **34.2** % (2026-08-01..2026-08-31) [DISCARD: US import growth from Mexico; the US-import bridge is not used (different concept, no stable ratio), so this is not need] quote: "lo que representó un aumento de 34.2% a tasa anual"
  - p7 Mexico share of total US goods imports, August 2026 (historical) = **18** % (2026-08-01..2026-08-31) [DISCARD: Mexico share of US imports; a share, not a level, and the US-import bridge is not used because the US import concept dif] quote: "con una participación histórica de 18.0% en las importaciones totales de la Unión Americana"
  - p8 Mexico share of total US goods imports, August 2026 (Banco Base figure) = **18.04** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of p7.] quote: ""En agosto, las compras desde México representaron el 18.04% de las compras totales de Estados Unidos"
  - p9 Mexico share of total US goods imports, cumulative January-August 2026 = **17.36** % (2026-01-01..2026-08-31) [DISCARD: Cumulative share; not a level driver.] quote: "representando el 17.36% de las compras totales de Estados Unidos"
  - p10 Canada share of total US goods imports, cumulative January-August 2026 (second p = **11.16** % (2026-01-01..2026-08-31) [DISCARD: Canada share of US imports; irrelevant to Mexico export level.] quote: "En segundo lugar, se ubica Canadá con 11.16%"
  - p11 China share of total US goods imports, cumulative January-August 2026 (third pla = **7.6** % (2026-01-01..2026-08-31) [DISCARD: China share; irrelevant.] quote: "China en tercero con 7.60%"
  - p12 Taiwan share of total US goods imports, cumulative January-August 2026 (fourth p = **7.74** % (2026-01-01..2026-08-31) [DISCARD: Taiwan share; irrelevant.] quote: "Taiwán en cuarto con 7.74% de las compras totales"
  - p13 Mexico share of total US trade deficit, cumulative January-August 2026 = **20.09** % (2026-01-01..2026-08-31) [DISCARD: Mexico share of US trade deficit; not a level driver for exports.] quote: "al representar 20.09% del desequilibrio total"
  - p14 Vietnam share of total US trade deficit, cumulative January-August 2026 (first p = **21.13** % (2026-01-01..2026-08-31) [DISCARD: Vietnam deficit share; irrelevant.] quote: "Vietnam ocupó el primer lugar, con 21.13%"
  - p15 Taiwan share of total US trade deficit, cumulative January-August 2026 (third pl = **19.04** percent (2026-01-01..2026-08-31) [DISCARD: Taiwan deficit share; irrelevant.] quote: "Taiwán se mantuvo en el tercer lugar con 19.04 por ciento"
  - p16 Average effective US tariff rate on all imports, August 2026 = **6.76** % (2026-08-01..2026-08-31) [DISCARD: Average US tariff on all imports; not specific to Mexico exports.] quote: "Estados Unidos cobró un arancel efectivo promedio de 6.76%"
  - p17 Average effective US tariff rate on all imports, July 2026 = **6.36** % (2026-07-01..2026-07-31) [DISCARD: Average US tariff July; not specific to Mexico.] quote: "Este porcentaje aumentó respecto al 6.36% observado en julio"
  - p18 Average effective US tariff rate on imports from Mexico, August 2026 = **3.19** % (2026-08-01..2026-08-31) [DISCARD: Effective tariff rate; no established elasticity to convert a tariff level into a September export value change.] quote: "México tuvo un arancel efectivo promedio de 3.19%, aumentando desde el 2.90% registrado en julio"
- `https://www.emerics.org:446/issueDetail.es?brdctsNo=402714&mid=a10200000000&search_option=&search_keyword=&search_year=&search_month=&search_tagkeywor` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://heraldodemexico.com.mx/economia/2026/10/7/mexico-mantiene-su-liderazgo-comercial-con-estados-unidos-903100.html` -> **live_dated** (page date 2026-10-07); points raw/verified 15/10
  - p19 Mexico share of total US goods imports, August 2026 = **18** % of total US goods imports (2026-08-01..2026-08-31) [DISCARD: Redundant copy of p7.] quote: "registraron una participación histórica dentro de su comercio de bienes totales, al alcanzar una tasa de 18 por ciento en agosto de este año"
  - p20 US goods imports from Mexico, nominal annual growth, August 2026 = **34.3** % year-over-year (2026-08-01..2026-08-31) [DISCARD: Redundant copy of p6.] quote: "Monto que representó un crecimiento nominal de 34.3 por ciento anual"
  - p21 US goods imports from Mexico, monthly growth, August 2026 vs July 2026 = **0.15** % month-over-month (2026-08-01..2026-08-31) [DISCARD: US imports from Mexico m/m; not used.] quote: "y un avance de 0.15 por ciento mensual"
  - p22 US goods exports to Mexico, annual growth, August 2026 = **15.3** % year-over-year (2026-08-01..2026-08-31) [DISCARD: US exports to Mexico; opposite direction, not used.] quote: "lo que significó un aumento de 15.3 por ciento anual"
  - p23 Mexico share of total US goods exports, August 2026 = **16.4** % of total US goods exports (2026-08-01..2026-08-31) [DISCARD: Mexico share of US exports; not used.] quote: "equivalentes al 16.4 por ciento de las ventas de bienes totales al exterior de la Unión Americana"
  - p24 US goods imports from Mexico, cumulative January-August 2026, annual growth = **18.2** % year-over-year (2026-01-01..2026-08-31) [DISCARD: US imports from Mexico cumulative growth; redundant with monthly p6/p20.] quote: "el dinamismo de enero a agosto en las importaciones de EU con un alza de 18.2 por ciento anual"
  - p25 US goods exports to Mexico, cumulative January-August 2026, annual growth = **16.4** % year-over-year (2026-01-01..2026-08-31) [DISCARD: US exports to Mexico growth; not used.] quote: "y exportaciones con un avance de 16.4 por ciento anual"
  - p26 Mexico share of total US trade, cumulative January-August 2026 = **16.84** % of total US trade (2026-01-01..2026-08-31) [DISCARD: Mexico share of total US trade; not a level driver.] quote: "De enero a agosto de este año México se mantuvo como el principal socio comercial con una participación de mercado de 16.84 por ciento"
  - p27 Share of US imports from Mexico complying with T-MEC, August 2026 = **85.4** % of US imports from Mexico (2026-08-01..2026-08-31) [DISCARD: T-MEC compliance share; contextual, not a level driver.] quote: "En agosto, de las importaciones hechas desde México, 85.40 por ciento cumplió con el T-MEC"
  - p28 US tariff rate collected on imports from Mexico, August 2026 = **3.19** % of imports from Mexico (2026-08-01..2026-08-31) [DISCARD: Redundant copy of p18.] quote: "pero volvió a subir a 3.19 por ciento en agosto, ubicándose en la posición 28 entre 35 países con los que EU más importa"
- dropped by code checks: 22 (scale word 'million' not supported by quote or table header: 19; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1; number: unknown scale word 'mil millones': 1; number: unknown scale word 'millones': 1)

### d3 [related_series] Banxico/INEGI export component breakdown

Hypothesis: Total exports = oil exports (Pemex) + non-oil exports (manufacturing, auto, agriculture); estimating each component from its own recent trend and summing gives the total.

Queries issued by the searcher: Pemex exportaciones crudo valor mensual 2026; exportaciones manufactureras México 2026 INEGI balanza comercial oportuna; INEGI exportaciones septiembre 2025 valor total millones de dólares balanza comercial oportuna; INEGI balanza comercial septiembre 2025 exportaciones manufactureras automotrices 78 mil millones

- `https://www.infobae.com/mexico/2026/09/28/boom-de-exportaciones-lleva-a-mexico-a-superavit-comercial-de-605-mdd-en-agosto/` -> **live_dated** (page date 2026-09-28); points raw/verified 15/5
  - p29 Mexico total merchandise exports, annual growth rate, August 2026 = **40.4** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of p1 with the August level; the level is not used because the seasonal route anchors on September 2025.] quote: "Las exportaciones totales sumaron 78,010 mdd, un aumento anual de 40.4 %."
  - p30 Mexico manufacturing exports, annual growth rate, August 2026 = **42.6** % (2026-08-01..2026-08-31) [DISCARD: Manufacturing export growth; redundant with the total growth p1 for the seasonal route.] quote: "Las exportaciones manufactureras alcanzaron 73,619 mdd, con un avance anual de 42.6 %."
  - p31 Mexico electrical and electronic equipment exports, annual growth rate, August 2 = **122** % (2026-08-01..2026-08-31) [DISCARD: Electrical equipment growth; sub-component, not used.] quote: "Equipos y aparatos eléctricos y electrónicos: 122.3 %"
  - p32 Mexico automotive exports, annual growth rate, August 2026 = **2.2** % (2026-08-01..2026-08-31) [DISCARD: Auto export growth; the September auto signal is better captured by p140/p70.] quote: "Las exportaciones automotrices cayeron 2.2 % anual: 1.0 % las dirigidas a Estados Unidos y 7.8 % las enviadas a otros mercados."
  - p33 Average price of Mexican crude mix (mezcla mexicana), August 2026, USD per barre = **75.98** USD per barrel (2026-08-01..2026-08-31) [DISCARD: Crude price August 2026; oil is small share and no volume bridge to value.] quote: "El precio promedio de la mezcla mexicana fue de 75.98 dólares por barril, 13.64 dólares más que en agosto de 2025."
- `https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/comext_o/balcom_o2025_10.pdf` -> **live_dated** (page date 2025-10-01); points raw/verified 15/1
  - p34 Mexican crude export blend average price, September 2025 (USD per barrel) = **62.45** USD per barrel (2025-09-01..2025-09-30) [DISCARD: Crude price September 2025; no volume bridge.] quote: "el precio promedio de la mezcla mexicana de crudo de exportación se situó en 62.45 dólares por barril"
- `https://www.jornada.com.mx/noticia/2026/09/30/economia/exportaciones-de-crudo-de-pemex-se-desplomaron-4480-anual-en-agosto` -> **dropped** (live http 403); points raw/verified -/-
- `https://www.banxico.org.mx/dyn/publicaciones-y-prensa/informacion-oportuna-de-comercio-exterior/%7BDF3A0ACE-EC72-EFE8-4837-DAD6D24F5777%7D.pdf` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- dropped by code checks: 24 (scale word 'million' not supported by quote or table header: 19; scale word 'thousand' not supported by quote or table header: 5)

### d4 [base_rates] Seasonal ratio base rates

Hypothesis: The September-to-August export ratio and September year-over-year growth have stable historical distributions; use these base rates applied to the latest known monthly level.

Queries issued by the searcher: Mexico merchandise exports monthly historical series INEGI 2015 2025 original figures; exportaciones México septiembre serie histórica INEGI balanza comercial mensual; INEGI BIE exportaciones totales mensuales millones de dólares 2015 2025 tabla septiembre agosto; "exportaciones" "septiembre" "agosto" millones de dólares 2019 2020 2021 México balanza comercial cifras originales mensuales tabla histórica

- `https://www.inegi.org.mx/app/tabulados/?nc=452&idrt=1099&opc=p&rn=2` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://www.banxico.org.mx/dyn/publicaciones-y-prensa/informacion-revisada-de-comercio-exterior/informacion-revisada-comercio.html` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/comext_o/balcom_o2025_10.pdf` -> **live_dated** (page date 2025-10-01); points raw/verified 15/6
  - p35 Mexico total merchandise exports, September 2025, annual percentage change (orig = **13.8** percent (2025-09-01..2025-09-30) [keep: Kept: the only September 2025 USD level (56,487.9 mdd), the anchor for the seasonal route.] quote: "Exportaciones totales 56 487.9 13.8 481 642.0 5.7"
  - p36 Mexico total merchandise exports, January-September 2025 cumulative, annual perc = **5.7** percent (2025-01-01..2025-09-30) [DISCARD: Cumulative Jan-Sep 2025 growth; not a monthly level.] quote: "Exportaciones totales 56 487.9 13.8 481 642.0 5.7"
  - p37 Mexico non-oil merchandise exports, September 2025, annual percentage change = **14.8** percent (2025-09-01..2025-09-30) [DISCARD: Non-oil growth Sept 2025; redundant with total p35 for level.] quote: "No petroleras 54 821.3 14.8 465 284.7 7.1"
  - p38 Mexico oil merchandise exports, September 2025, annual percentage change = **-11.8** percent (2025-09-01..2025-09-30) [DISCARD: Oil exports growth Sept 2025; oil is ~3% of total, negligible for level.] quote: "Petroleras 1 666.6 -11.8 16 357.3 -23.6"
  - p39 Mexico total merchandise exports, September 2025, seasonally adjusted monthly pe = **1.33** percent (2025-09-01..2025-09-30) [DISCARD: Redundant copy of p5.] quote: "las exportaciones totales registraron una caída mensual de 1.33 por ciento"
  - p40 Mexico total merchandise exports, September 2025, annual percentage change (head = **13.8** percent (2025-09-01..2025-09-30) [DISCARD: Redundant copy of p35.] quote: "monto superior en 13.8 % al del mismo mes de 2024"
- `https://trendonify.com/mexico/exports-yoy` -> **dropped** (live http 403); points raw/verified -/-
- dropped by code checks: 9 (scale word 'million' not supported by quote or table header: 9)

### d5 [forecasts_markets] Analyst and official forecasts

Hypothesis: Published forecasts or nowcasts of Mexico's September 2026 trade balance/exports (e.g., Banxico, private analysts, IMF Article IV) constrain the level; treat as forecast, not realization.

Queries issued by the searcher: pronóstico balanza comercial México septiembre 2026 exportaciones; Mexico exports forecast September 2026 trade balance analysts; Banorte previa balanza comercial septiembre 2026 exportaciones; "balanza comercial" septiembre 2026 México "se espera" superávit exportaciones octubre 2026

- `https://www.eluniversal.com.mx/cartera/exportaciones-se-encaminan-a-su-mejor-ano-en-la-historia/` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.jornada.com.mx/noticia/2026/10/12/columnas/mexico-pronosticos-economicos-202627-sep-2026-reporte-economico` -> **dropped** (live http 403); points raw/verified -/-
- `https://heraldodemexico.com.mx/edicion-impresa/2026/10/16/proyectan-avance-de-26-en-exportacion-de-mexico-para-2026-909646.html` -> **live_dated** (page date 2026-10-16); points raw/verified 12/2
  - p41 Mexico's share of US merchandise imports in 2024 = **15.5** % (2024-01-01..2024-12-31) [DISCARD: 2024 share; superseded by 2025/2026 shares.] quote: "con una participación de 15.5 por ciento en 2024 y de 15.7 por ciento en 2025 en las importaciones estadounidenses"
  - p42 Mexico's share of US merchandise imports in 2025 = **15.7** % (2025-01-01..2025-12-31) [DISCARD: 2025 share; superseded by August 2026 share for the bridge.] quote: "con una participación de 15.5 por ciento en 2024 y de 15.7 por ciento en 2025 en las importaciones estadounidenses"
- `https://www.scotiabank.com/content/dam/scotiabank/sub-brands/scotiabank-economics/english/documents/latam-daily/latamdaily20260928.pdf` -> **live_dated** (page date 2026-09-28); points raw/verified 15/15
  - p43 Mexico total merchandise exports, August 2026 (monthly, USD) = **78,000,000,000** USD (2026-08-01..2026-08-31) [DISCARD: Rounded restatement of INEGI's August level; p35 plus p1 gives the same anchor more precisely, and p43 is a rounded $78b] quote: "with exports totaling $78 billion and imports reaching $77.4 billion (chart 1)"
  - p44 Mexico total merchandise imports, August 2026 (monthly, USD) = **77,400,000,000** USD (2026-08-01..2026-08-31) [DISCARD: Imports level; not used in any export route.] quote: "imports reaching $77.4 billion (chart 1), resulting in a trade surplus of $605.4 million."
  - p45 Mexico merchandise trade surplus, August 2026 (monthly, USD) = **605,400,000** USD (2026-08-01..2026-08-31) [DISCARD: Trade surplus; not used in any export route.] quote: "resulting in a trade surplus of $605.4 million."
  - p46 Mexico total exports year-over-year growth, August 2026 = **40.4** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of p1.] quote: "Exports grew by 40.4% year over year, led by non-automotive manufacturing exports"
  - p47 Mexico non-automotive manufacturing exports year-over-year growth, August 2026 = **63.2** % (2026-08-01..2026-08-31) [DISCARD: Non-automotive manufacturing growth; redundant with p30 for the total-export route.] quote: "led by non-automotive manufacturing exports (63.2%) and non-oil extractive exports (45.9%)"
  - p48 Mexico non-oil extractive exports year-over-year growth, August 2026 = **45.9** % (2026-08-01..2026-08-31) [DISCARD: Non-oil extractive growth; small component, not used.] quote: "non-oil extractive exports (45.9%), while automotive, oil, and agricultural exports declined"
  - p49 Mexico automotive exports year-over-year change, August 2026 = **-2.2** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of p32.] quote: "while automotive, oil, and agricultural exports declined (-2.2%, -2.8%, and -2.2%, respectively)."
  - p50 Mexico oil exports year-over-year change, August 2026 = **-2.8** % (2026-08-01..2026-08-31) [DISCARD: Oil exports change; small component, not used.] quote: "while automotive, oil, and agricultural exports declined (-2.2%, -2.8%, and -2.2%, respectively)."
  - p51 Mexico agricultural exports year-over-year change, August 2026 = **-2.2** % (2026-08-01..2026-08-31) [DISCARD: Agricultural exports change; small component, not used.] quote: "while automotive, oil, and agricultural exports declined (-2.2%, -2.8%, and -2.2%, respectively)."
  - p52 Mexico total imports year-over-year growth, August 2026 = **34.2** % (2026-08-01..2026-08-31) [DISCARD: Imports growth; not used in export route.] quote: "Imports also showed strong momentum, rising by 34.2% year over year."
  - p53 Mexico intermediate goods imports year-over-year growth, August 2026 = **41.9** % (2026-08-01..2026-08-31) [DISCARD: Imports component; not used.] quote: "Intermediate goods led the increase (41.9%), consumer goods posted a more moderate gain (8.9%)"
  - p54 Mexico consumer goods imports year-over-year growth, August 2026 = **8.9** % (2026-08-01..2026-08-31) [DISCARD: Imports component; not used.] quote: "consumer goods posted a more moderate gain (8.9%), and capital goods rose by only 6.9%."
  - p55 Mexico capital goods imports year-over-year growth, August 2026 = **6.9** % (2026-08-01..2026-08-31) [DISCARD: Imports component; not used.] quote: "and capital goods rose by only 6.9%."
  - p56 Mexico cumulative exports annual growth, first half of 2026 = **29.3** % (2026-01-01..2026-06-30) [DISCARD: Mislabels Jan-Aug cumulative 29.3% as first-half; redundant with p2/p94 and period label is wrong.] quote: "during the first half of the year, exports maintained annual growth of 29.3%, while imports increased by 26.8%"
  - p57 Mexico cumulative imports annual growth, first half of 2026 = **26.8** % (2026-01-01..2026-06-30) [DISCARD: Imports figure, not needed for export target and period label inconsistent.] quote: "while imports increased by 26.8%, resulting in a surplus of $9.8603 billion."
- dropped by code checks: 10 (period_end 2026-12-31 after as_of: 9; scale word 'million' not supported by quote or table header: 1)

### d6 [shocks] Trade policy and tariff environment

Hypothesis: US tariff actions, USMCA review, or auto-sector disruptions in 2026 shift the level and seasonal ratio of Mexican exports; quantify exposure to adjust the historical seasonal route.

Queries issued by the searcher: US tariffs Mexico 2026 exports impact auto sector; Mexico merchandise exports 2026 INEGI balanza comercial oportuna; INEGI exportaciones septiembre 2025 balanza comercial oportuna 2025_09 mdd; "balcom_o2026_08" inegi exportaciones agosto 2026 pdf

- `https://www.liderempresarial.com/aumentan-las-exportaciones-en-mexico-en-agosto-2026-cual-fue-la-balanza-comercial/` -> **live_dated** (page date 2026-09-28); points raw/verified 15/8
  - p58 Mexico total merchandise exports, August 2026, year-on-year growth rate = **40.4** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of p1.] quote: "las exportaciones alcanzaron 78 mil 10.5 millones de dólares (mdd), un incremento anual de 40.4%"
  - p59 Mexico total merchandise exports, August 2026, month-on-month change, seasonally = **1.23** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of p3.] quote: "En agosto, las exportaciones totales aumentaron 1.23% mensual en términos desestacionalizados."
  - p60 Manufactured goods share of total Mexican exports, January-August 2026 = **92.1** % (2026-01-01..2026-08-31) [DISCARD: Manufacturing share; not needed for total level.] quote: "los bienes manufacturados representaron 92.1% de la estructura total de las exportaciones"
  - p61 US share of Mexico's non-oil exports, January-August 2026 = **84.69** % (2026-01-01..2026-08-31) [DISCARD: US share of non-oil exports; not needed for total level.] quote: "Durante enero-agosto, Estados Unidos concentró 84.69% de las exportaciones no petroleras de México."
  - p62 Mexico automotive exports to the United States, August 2026, year-on-year change = **1** % (2026-08-01..2026-08-31) [DISCARD: US-bound auto export change; sub-segment of p32, redundant.] quote: "Las exportaciones automotrices hacia Estados Unidos disminuyeron 1% en agosto"
  - p63 Mexico total automotive exports, August 2026, year-on-year change = **2.2** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of p32.] quote: "En contraste, las exportaciones automotrices disminuyeron 2.2% anual."
  - p64 Mexico automotive manufacturing exports, August 2026, month-on-month change, sea = **1.63** % (2026-08-01..2026-08-31) [DISCARD: Automotive m/m change; small component, not used.] quote: "Manufactureras automotrices: -1.63%."
  - p65 Mexico non-automotive manufacturing exports, August 2026, month-on-month change, = **3.06** % (2026-08-01..2026-08-31) [DISCARD: Non-auto manufacturing m/m; not used directly.] quote: "Manufactureras no automotrices: +3.06%."
- `https://inegi.org.mx/app/saladeprensa/noticia/10282` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://www.usatoday.com/story/business/autos/2026/10/08/trump-tariffs-take-toll-on-mexican-auto-exports/92150817007/` -> **dropped** (live http 402); points raw/verified -/-
- `https://www.infobae.com/america/agencias/2026/10/16/mexico-niega-estancamiento-en-negociaciones-con-eeuu-e-insiste-en-bajar-arancel-automotriz/` -> **live_dated** (page date 2026-10-16); points raw/verified 15/15
  - p66 Proposed reduction of US tariff on Mexican automobiles (target rate, from 25%) = **15** % (2026-10-16..2026-10-16) [DISCARD: Proposed tariff target; a policy proposal, not a realized September flow.] quote: "insistió en su objetivo de bajar del 25 % al 15 % el gravamen a automóviles"
  - p67 Current US tariff on Mexican automobiles (rate to be reduced) = **25** % (2026-10-16..2026-10-16) [DISCARD: Current auto tariff level; background only, no conversion to September value.] quote: "oposición a rebajas sustanciales del 25 % a los automóviles mexicanos y del 50 % al acero y aluminio"
  - p68 US tariff on Mexican steel and aluminium (rate) = **50** % (2026-10-16..2026-10-16) [DISCARD: Steel/aluminium tariff; background only.] quote: "oposición a rebajas sustanciales del 25 % a los automóviles mexicanos y del 50 % al acero y aluminio"
  - p69 Mexico-proposed tariff parity rate with South Korea for automobiles = **15** % (2026-10-16..2026-10-16) [DISCARD: Proposed tariff parity; background only.] quote: "México propone igualar el arancel del 15 % concedido a Corea del Sur, independientemente del contenido regional"
  - p70 Mexico light vehicle exports, September 2026, year-on-year change = **11.9** as written "11,9 %", value check pending % (2026-09-01..2026-09-30) [keep: Kept: corroborates p140 (-11.9%).] quote: "Las exportaciones mexicanas de vehículos ligeros cayeron un 11,9 % interanual en septiembre, a 277.369 unidades"
  - p71 Mexico light vehicle exports, September 2026, units = **277** vehicles (2026-09-01..2026-09-30) [DISCARD: Redundant copy of p138/p161.] quote: "Las exportaciones mexicanas de vehículos ligeros cayeron un 11,9 % interanual en septiembre, a 277.369 unidades"
  - p72 Mexico light vehicle production, September 2026, year-on-year change = **15.1** as written "15,1 %", value check pending % (2026-09-01..2026-09-30) [keep: Kept: corroborates p137.] quote: "y la producción un 15,1 %, a 301.803, según cifras oficiales"
  - p73 Mexico light vehicle production, September 2026, units = **302** vehicles (2026-09-01..2026-09-30) [DISCARD: Redundant copy of p135.] quote: "y la producción un 15,1 %, a 301.803, según cifras oficiales"
  - p74 Mexico domestic vehicle sales, September 2026, year-on-year change = **7.9** as written "7,9 %", value check pending % (2026-09-01..2026-09-30) [DISCARD: Domestic vehicle sales; not exports.] quote: "Las ventas internas aumentaron un 7,9 %, hasta 129.274 vehículos"
  - p75 Mexico domestic vehicle sales, September 2026, units = **129** vehicles (2026-09-01..2026-09-30) [DISCARD: Domestic vehicle sales units; not exports.] quote: "Las ventas internas aumentaron un 7,9 %, hasta 129.274 vehículos"
  - p76 Share of Mexico's exported vehicles received by the United States, January-Septe = **76** % (2026-01-01..2026-09-30) [DISCARD: US share of exported vehicles; not a level driver.] quote: "Estados Unidos recibió alrededor del 76 % de los vehículos exportados entre enero y septiembre"
  - p77 Canacero steel exports to the United States, 2025, decline = **49** % (2025-01-01..2025-12-31) [DISCARD: Steel exports decline 2025; too indirect and small relative to total.] quote: "La Cámara Nacional de la Industria del Hierro y del Acero (Canacero) reportó una caída del 49 % en sus exportaciones a Estados Unidos durante 2025"
  - p78 Canacero installed capacity utilisation (upper bound, below) = **60** % (2025-01-01..2025-12-31) [DISCARD: Steel capacity utilisation; not used.] quote: "una utilización inferior al 60 % de la capacidad instalada"
  - p79 Reduction in entries of certain imported vehicles under Mexican tariffs (up to,  = **70** % (2026-10-16..2026-10-16) [DISCARD: Imported vehicle entries under Mexican tariffs; import side, not used.] quote: "redujeron sus entradas hasta un 70 % en algunos casos sin elevar los precios"
  - p80 Share of Mexico's trade with the United States remaining tariff-free = **80** % (2026-10-16..2026-10-16) [DISCARD: Tariff-free share; contextual, not a level driver.] quote: "cerca del 80 % del comercio mexicano con Estados Unidos permanece libre de aranceles, con una tasa efectiva media del 3,2 % sobre las exportaciones"
- dropped by code checks: 7 (number: unknown scale word 'millones': 1; number: unknown scale word 'mil': 6)

### d7 [physical_flow] Cross-border truck/rail freight and port throughput

Hypothesis: Physical throughput at key border crossings (Laredo, El Paso) and ports (Lázaro Cárdenas, Manzanillo) plus auto rail shipments scales with export value via a value-per-unit factor.

Queries issued by the searcher: Laredo border crossings truck volume September 2026; Mexico port container throughput September 2026 Manzanillo Lázaro Cárdenas; Mexico merchandise exports August 2026 INEGI balanza comercial oportuna billion dollars; Laredo World Trade Bridge value of trade per truck crossing average US imports Mexico

- `https://elmanana.com.mx/nuevo-laredo/2026/10/16/sistema-de-puentes-internacionales-de-laredo-tiene-record-historico-182664.html` -> **live_dated** (page date 2026-10-16); points raw/verified 15/12
  - p81 Laredo International Bridges System cumulative revenue, fiscal year 2025-2026 (1 = **84,176,999** as written "84 millones 176 mil 999 dólares", value check pending USD (2025-10-01..2026-09-30) [DISCARD: FY bridge revenue; superseded by September-specific p82.] quote: "los ingresos alcanzaron los 84 millones 176 mil 999 dólares"
  - p82 Laredo International Bridges System revenue, September 2026 = **7,089,607** as written "7 millones 089 mil 607 dólares", value check pending USD (2026-09-01..2026-09-30) [DISCARD: Laredo bridge revenue is a toll-revenue proxy, not export value; no stable revenue-to-value conversion exists, so it can] quote: "Solo en septiembre ingresos por 7 millones 089 mil 607 dólares, un 3.1% superior al mismo mes del año previo"
  - p83 Laredo commercial truck crossings, fiscal year 2025-2026 (12 months) = **3,005,832** as written "3 millones 005 mil 832 camiones de carga", value check pending trucks (2025-10-01..2026-09-30) [DISCARD: FY truck crossings; annual total, not a September flow.] quote: "Laredo cerró el año fiscal con 3 millones 005 mil 832 camiones de carga contabilizados durante los 12 meses del ejercicio"
  - p84 Laredo commercial truck crossings, year-over-year change, September 2026 = **4.6** % (2026-09-01..2026-09-30) [DISCARD: Truck crossings growth; no value-per-truck bridge to total exports.] quote: "un alza del 4.6% en comparación con septiembre de 2025"
  - p85 Laredo commercial truck crossings, additional units vs prior fiscal year = **23,504** as written "23 mil 504 unidades adicionales", value check pending trucks (2025-10-01..2026-09-30) [DISCARD: FY truck crossing increment; redundant with p86 growth.] quote: "superando por 0.8% el volumen registrado en el periodo anterior (23 mil 504 unidades adicionales)"
  - p86 Laredo commercial truck crossings, year-over-year growth, fiscal year 2025-2026 = **0.8** % (2025-10-01..2026-09-30) [DISCARD: FY truck crossing growth; annual, not September-specific.] quote: "superando por 0.8% el volumen registrado en el periodo anterior"
  - p87 Laredo private vehicle crossings, fiscal year 2025-2026 (12 months) = **5,297,675** as written "5 millones 297 mil 675 cruces", value check pending crossings (2025-10-01..2026-09-30) [DISCARD: Private vehicle crossings; passenger traffic, not freight value.] quote: "El tránsito de vehículos particulares concluyó el periodo fiscal con 5 millones 297 mil 675 cruces acumulados"
  - p88 Laredo International Bridges System revenue, fiscal year 2025-2026, shortfall vs = **2,523,596** as written "2 millones 523 mil 596 dólares", value check pending USD (2025-10-01..2026-09-30) [DISCARD: Budget shortfall; not a level driver.] quote: "La cifra deja un saldo desfavorable de 2 millones 523 mil 596 dólares frente a la proyección presupuestal interna de 86.70 millones de dólares."
  - p89 Laredo International Bridges System revenue, year-over-year change, fiscal year  = **1.4** % (2025-10-01..2026-09-30) [DISCARD: FY revenue growth; superseded by September-specific p82/p90.] quote: "lo que representa un incremento del 1.4% (+1.15 millones de dólares) en comparación con el ejercicio anterior"
  - p90 Laredo International Bridges System revenue, September 2026, year-over-year chan = **3.1** % (2026-09-01..2026-09-30) [DISCARD: Laredo revenue growth; same unusable proxy as p82.] quote: "Solo en septiembre ingresos por 7 millones 089 mil 607 dólares, un 3.1% superior al mismo mes del año previo"
  - p91 Laredo International Bridges System revenue, August shortfall vs budget = **545,676** as written "545 mil 676 dólares", value check pending USD (2026-08-01..2026-08-31) [DISCARD: August budget shortfall; not a level driver.] quote: "meses clave como agosto (-545 mil 676 dólares), noviembre (-475 mil 242 dólares) y enero (-370 mil 716 dólares)"
  - p92 Laredo private vehicle crossings, year-over-year growth, fiscal year 2025-2026 = **4.2** % (2025-10-01..2026-09-30) [DISCARD: Private vehicle crossings growth; not freight.] quote: "lo que equivale a un crecimiento del 4.2% respecto al ciclo previo"
- `https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/comext_o/balcom_o2026_09.pdf` -> **live_dated** (page date 2026-09-01); points raw/verified 15/4
  - p93 Mexico total merchandise exports, August 2026, annual percentage change = **40.4** percent (2026-08-01..2026-08-31) [DISCARD: Redundant copy of p1.] quote: "Aumentaron las exportaciones 40.4 %"
  - p94 Mexico total merchandise exports, January-August 2026 cumulative, annual percent = **29.3** percent (2026-01-01..2026-08-31) [DISCARD: Redundant copy of p2.] quote: "Exportaciones totales 78 010.5 40.4 549 397.6 29.3"
  - p95 Mexico non-oil exports to United States, share of non-oil exports, January-Augus = **84.69** percent (2026-01-01..2026-08-31) [DISCARD: Duplicate of p61.] quote: "Estados Unidos 84.69 8.7 35.9 49.8 45.2 31.6"
  - p96 Mexico non-oil exports to United States, August 2026 annual percentage change = **45.2** percent (2026-08-01..2026-08-31) [DISCARD: US-directed non-oil growth; redundant with total.] quote: "se presentaron incrementos anuales de 45.2 % en las dirigidas a Estados Unidos y de 23.5 % en las canalizadas al resto"
- `https://www.cityoflaredo.com/departments/bridge-system/-sortn-SPhone` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.tyt.com.mx/nota/crece-movimiento-de-contenedores-en-puertos-hacia-agosto-alcanza-6-5-millones-de-teus` -> **live_dated** (page date 2026-09-17); points raw/verified 15/1
  - p97 Container movement at Pacific coast ports, January–August 2025 cumulative (TEUs) = **4,673,118** as written "4 millones 673 mil 118", value check pending TEUs (2025-01-01..2025-08-31) [DISCARD: Pacific port TEUs 2025; no September 2026 counterpart and no value-per-TEU bridge.] quote: "comparado con los 4 millones 673 mil 118 TEUs del mismo periodo de 2025"
- dropped by code checks: 28 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1; scale word 'million' not supported by quote or table header: 12; scale word 'thousand' not supported by quote or table header: 1; period year 2026 does not appear in the page text or URL (likely mis-dated): 13; value_as_written not in quote as a whole number: 1)

### b1 [related_series] US Census FT900 advance goods imports from Mexico, September 2026

Hypothesis: US imports from Mexico for September 2026 (released ~Oct 2026) would let the d2 bridge (Mexico exports ≈ US imports from Mexico / US share) be applied to the target month directly, resolving the August-to-September step that the seasonal route must otherwise assume.

Queries issued by the searcher: Census Bureau advance economic indicators September 2026 advance goods trade imports from Mexico; census.gov foreign-trade Press-Release current_press_release FT900 August 2026 goods imports Mexico; August 2026 U.S. goods imports from Mexico Census Bureau FT900 country detail billion; INEGI balanza comercial de mercancías información oportuna agosto 2026 exportaciones

- `https://t21.com.mx/mexico-mantiene-ruta-comercial-con-eu-rompe-record-de-exportaciones-en-agosto/` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://www.liderempresarial.com/exportaciones-de-mexico-a-estados-unidos-rompen-record-en-agosto-2026/` -> **live_dated** (page date 2026-10-07); points raw/verified 15/0
- `https://www.excelsior.com.mx/finanzas/exportaciones-mexicanas-eu-marcan-record-reporte-agosto` -> **live_dated** (page date 2026-10-06); points raw/verified 15/12
  - p98 US goods imports from Mexico, August 2026, year-over-year increase (%) = **34.2** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of p6.] quote: "lo que representó un aumento de 34.2% a tasa anual"
  - p99 Mexico share of total US imports, August 2026 (numerator: US imports from Mexico = **18** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of p7.] quote: "con una participación histórica de 18.0% en las importaciones totales de la Unión Americana"
  - p100 Mexico share of total US imports, August 2026, Banco Base figure (numerator: US  = **18.04** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of p8.] quote: "En agosto, las compras desde México representaron el 18.04% de las compras totales de Estados Unidos"
  - p101 US goods exports to Mexico, August 2026, year-over-year increase (%) = **15.3** % (2026-08-01..2026-08-31) [DISCARD: US goods exports to Mexico; the target is Mexican exports, so this is the wrong direction of flow.] quote: "un alza de 15.3% anual, equivalentes a 16.4% de las importaciones totales"
  - p102 Mexico share of total US imports, January-August 2026 cumulative (numerator: US  = **17.36** % (2026-01-01..2026-08-31) [DISCARD: Cumulative Mexico share of US imports; redundant with the August share points.] quote: "representando el 17.36% de las compras totales de Estados Unidos"
  - p103 Canada share of total US imports, January-August 2026 cumulative = **11.16** % (2026-01-01..2026-08-31) [DISCARD: Canada share of US imports; irrelevant to Mexico's export level.] quote: "En segundo lugar, se ubica Canadá con 11.16%, China en tercero con 7.60% y Taiwán en cuarto con 7.74% de las compras totales."
  - p104 China share of total US imports, January-August 2026 cumulative = **7.6** % (2026-01-01..2026-08-31) [DISCARD: China share of US imports; irrelevant.] quote: "China en tercero con 7.60% y Taiwán en cuarto con 7.74% de las compras totales."
  - p105 Taiwan share of total US imports, January-August 2026 cumulative = **7.74** % (2026-01-01..2026-08-31) [DISCARD: Taiwan share of US imports; irrelevant.] quote: "Taiwán en cuarto con 7.74% de las compras totales."
  - p106 Mexico share of total US trade deficit, January-August 2026 cumulative = **20.09** % (2026-01-01..2026-08-31) [DISCARD: Mexico share of US trade deficit; not an export level.] quote: "al representar 20.09% del desequilibrio total"
  - p107 Average effective US tariff rate on all imports, August 2026 = **6.76** % (2026-08-01..2026-08-31) [DISCARD: Average US tariff on all imports; the Mexico-specific rate (p18) is the relevant one.] quote: "Estados Unidos cobró un arancel efectivo promedio de 6.76%"
  - p108 Average effective US tariff rate on imports from Mexico, August 2026 = **3.19** % (2026-08-01..2026-08-31) [DISCARD: Redundant copy of p18.] quote: "México tuvo un arancel efectivo promedio de 3.19%, aumentando desde el 2.90% registrado en julio"
  - p109 Average effective US tariff rate on imports from Mexico, July 2026 = **2.9** % (2026-07-01..2026-07-31) [DISCARD: July 2026 Mexico tariff rate; superseded by August p18 for the target period.] quote: "México tuvo un arancel efectivo promedio de 3.19%, aumentando desde el 2.90% registrado en julio"
- `https://www.indexbox.io/blog/mexico-remains-top-us-trading-partner-in-august-2026/` -> **live_dated** (page date 2026-10-07); points raw/verified 15/15
  - p110 US goods imports from Mexico, August 2026 (monthly, USD) = **60,640,000,000** USD (2026-08-01..2026-08-31) [DISCARD: US imports from Mexico in August 2026 is a different concept (US customs, c.i.f.-ish, US-bound only) from Mexico's f.o.b] quote: "goods coming from Mexico climbed 34.3% to $60.64 billion"
  - p111 US goods imports from Mexico, August 2026, year-over-year percent change = **34.3** % (2026-08-01..2026-08-31) [DISCARD: Redundant with p6/p20 on the same US import growth.] quote: "goods coming from Mexico climbed 34.3% to $60.64 billion"
  - p112 US goods exports to Mexico, August 2026 (monthly, USD) = **33,660,000,000** USD (2026-08-01..2026-08-31) [DISCARD: US goods exports to Mexico; wrong direction of flow for the target.] quote: "U.S. shipments to Mexico grew 15.1% year over year to $33.66 billion"
  - p113 US-Mexico two-way merchandise trade, August 2026 (monthly, USD) = **94,290,000,000** USD (2026-08-01..2026-08-31) [DISCARD: Two-way trade; mixes exports and imports, not the target.] quote: "Two-way commerce between the two nations amounted to $94.29 billion for the month"
  - p114 US-Mexico two-way merchandise trade, August 2025 (monthly, USD) = **74,400,000,000** USD (2025-08-01..2025-08-31) [DISCARD: August 2025 two-way trade; only a comparison base, redundant with p113.] quote: "marking a 26.75% gain from $74.4 billion in August 2025"
  - p115 Mexico share of total US international trade, August 2026 = **17.4** % (2026-08-01..2026-08-31) [DISCARD: Mexico share of total US trade; a share, not a level, and redundant with p7/p8.] quote: "Mexico made up 17.4% of all U.S. international trade during August."
  - p116 Total US international trade, August 2026 (monthly, USD) = **540,920,000,000** USD (2026-08-01..2026-08-31) [DISCARD: Total US international trade; only useful as a denominator already implied by p117.] quote: "Total U.S. international trade came to $540.92 billion in August"
  - p117 Total US goods imports, August 2026 (monthly, USD) = **336,170,000,000** USD (2026-08-01..2026-08-31) [DISCARD: Total US goods imports; only a denominator, redundant with p110/p7.] quote: "comprising $204.75 billion in exports and $336.17 billion in imports"
  - p118 Total US goods exports, August 2026 (monthly, USD) = **204,750,000,000** USD (2026-08-01..2026-08-31) [DISCARD: Total US goods exports; not a Mexican export quantity.] quote: "comprising $204.75 billion in exports and $336.17 billion in imports"
  - p119 US-Mexico two-way merchandise trade, cumulative January-August 2026 (USD) = **682,820,000,000** USD (2026-01-01..2026-08-31) [DISCARD: Cumulative two-way trade; not a monthly export level.] quote: "Over the first eight months of 2026, U.S.-Mexico commerce hit $682.82 billion"
  - p120 US-Mexico two-way merchandise trade, cumulative January-August 2026, year-over-y = **17.5** % (2026-01-01..2026-08-31) [DISCARD: Cumulative two-way trade growth; not a monthly export level.] quote: "a 17.5% rise from the same stretch a year earlier"
  - p121 US goods imports through Port Laredo, August 2026 (monthly, USD) = **26,230,000,000** USD (2026-08-01..2026-08-31) [DISCARD: Laredo US imports from Mexico; a sub-national port figure, not the national total, and not convertible without a stable ] quote: "Imports passing through Laredo reached $26.23 billion, up 33.9%"
  - p122 US-Mexico commerce through Port Laredo, August 2026 (monthly, USD) = **37,620,000,000** USD (2026-08-01..2026-08-31) [DISCARD: Laredo two-way Mexico commerce; sub-national and two-way, not the national export total.] quote: "Commerce with Mexico accounted for $37.62 billion, roughly 97.6%, of Laredo's total August trade."
  - p123 Mexico share of Port Laredo total trade, August 2026 = **97.6** % (2026-08-01..2026-08-31) [DISCARD: Laredo Mexico share; redundant with p122 level.] quote: "Commerce with Mexico accounted for $37.62 billion, roughly 97.6%, of Laredo's total August trade."
  - p124 Port Laredo total two-way trade, August 2026 (monthly, USD) = **38,560,000,000** USD (2026-08-01..2026-08-31) [DISCARD: Laredo total two-way trade; redundant with p122 Mexico-specific figure.] quote: "Port Laredo stayed the nation's busiest international trade gateway in August, moving $38.56 billion in two-way commerce"
- dropped by code checks: 18 (scale word 'million' not supported by quote or table header: 15; number: unknown scale word 'mil millones': 2; number: unknown scale word 'millones': 1)

### b2 [own_history] INEGI September/August original export ratio in prior years

Hypothesis: The September-to-August original (not seasonally adjusted) ratio from 2022-2025 would convert the known August 2026 level (p43/p94) into a September 2026 estimate via the d1 seasonal route, which currently lacks the ratio series.

Queries issued by the searcher: INEGI Balanza Comercial de Mercancías de México septiembre 2025 exportaciones agosto serie original; INEGI balanza comercial exportaciones mensuales originales 2022 2023 2024 2025 agosto septiembre; "septiembre de 2024" exportaciones 49 626 agosto 2024 INEGI balanza comercial; "septiembre de 2023" exportaciones "millones de dólares" INEGI agosto 2023 balanza comercial; "septiembre de 2022" exportaciones totales mercancías INEGI agosto 2022 balanza comercial original

- `https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/comext_o/balcom_o2025_10.pdf` -> **live_dated** (page date 2025-10-01); points raw/verified 15/5
  - p125 Mexico total merchandise exports, original, September 2025 annual variation (%) = **13.8** percent (2025-09-01..2025-09-30) [DISCARD: Redundant copy of p35.] quote: "Exportaciones totales 56 487.9 13.8 481 642.0 5.7"
  - p126 Mexico total merchandise exports, original, January-September 2025 annual variat = **5.7** percent (2025-01-01..2025-09-30) [DISCARD: Cumulative Jan-Sep 2025 growth; not a September level.] quote: "Exportaciones totales 56 487.9 13.8 481 642.0 5.7"
  - p127 Mexico total merchandise exports, original, September 2025 annual variation (%) = **13.8** % (2025-09-01..2025-09-30) [DISCARD: Redundant copy of p4.] quote: "Incrementaron las exportaciones 13.8 % y las importaciones, 15.2 % a tasa anual, en septiembre de 2025"
  - p128 Mexico total merchandise exports, original, January-September 2025 annual variat = **5.7** percent (2025-01-01..2025-09-30) [DISCARD: Redundant copy of p126.] quote: "lo que significó un incremento anual de 5.7 por ciento"
  - p129 Mexico total merchandise exports, original, September 2025 annual variation (%) = **13.8** percent (2025-09-01..2025-09-30) [DISCARD: Redundant copy of p4.] quote: "monto superior en 13.8 % al del mismo mes de 2024"
- `https://www.gslb.inegi.org.mx/contenidos/saladeprensa/boletines/2024/balcom_o/balcom_o2024_10.docx` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2023/balcom_o/balcom_o2023_10.pdf` -> **live_dated** (page date 2023-10-01); points raw/verified 12/2
  - p130 Mexico total merchandise exports, original, September 2022 (annual comparison ba = **5.1** percent annual change (2023-09-01..2023-09-30) [DISCARD: Mislabeled: the quote is the September 2023 release (non-oil 46,212 mdd, oil 3,446 mdd) but the name/period say Septembe] quote: "por 46 212 millones de dólares de exportaciones no petroleras y por 3 446 millones de dólares de petroleras. Así, en el mes de referencia, las exportaciones totales observaron una caída anual de 5.1 %"
  - p131 Mexico total merchandise exports, original, January-September 2023 annual change = **2.7** percent annual change (2023-01-01..2023-09-30) [DISCARD: Cumulative 2023 growth; not a September level.] quote: "En los primeros nueve meses de 2023, el valor de las exportaciones totales sumó 441 537 millones de dólares, lo que significó un incremento anual de 2.7 por ciento."
- `https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2022/balcom_o/balcom_o2022_10.pdf` -> **live_dated** (page date 2022-10-01); points raw/verified 15/3
  - p132 Mexico total merchandise exports, original, September 2022 annual percent change = **25.4** % (2022-09-01..2022-09-30) [DISCARD: September 2022 y/y change; a single old growth rate, not a level, and not needed once p35 anchors the level.] quote: "Exportaciones totales 52 338.0 25.4 430 283.9 19.7"
  - p133 Mexico total merchandise exports, original, January-September 2022 annual percen = **19.7** % (2022-01-01..2022-09-30) [DISCARD: Cumulative 2022 growth; not a September level.] quote: "Exportaciones totales 52 338.0 25.4 430 283.9 19.7"
  - p134 Mexico total merchandise exports, seasonally adjusted, September 2022 monthly pe = **4.98** % (2022-09-01..2022-09-30) [DISCARD: Seasonally adjusted September 2022 change; not applicable to original figures.] quote: "las exportaciones totales de mercancías registraron un avance mensual de 4.98 %"
- dropped by code checks: 32 (scale word 'million' not supported by quote or table header: 32)

### b3 [shocks] September 2026 manufacturing/auto export momentum

Hypothesis: The -11.9% September light-vehicle export decline (p70) conflicts with August's +40.4% total growth; a September manufacturing or auto export nowcast would resolve whether the September total growth collapsed toward zero or stayed strong, the largest uncertainty in the seasonal route.

Queries issued by the searcher: IMEF indicador manufacturero septiembre 2026; Banxico encuesta expectativas exportaciones septiembre 2026; exportaciones automotrices septiembre 2026 México caída vehículos ligeros; INEGI balanza comercial mercancías septiembre 2026 información oportuna exportaciones

- `https://www.eleconomista.com.mx/empresas/produccion-autos-mexico-frena-15-septiembre-exportaciones-derrapan-20261007-837350.html` -> **live_dated** (page date 2026-10-07); points raw/verified 15/11
  - p135 Mexico light-vehicle production, September 2026 (INEGI) = **301,803** vehicles (2026-09-01..2026-09-30) [keep: Kept: September 2026 production units, corroborates the auto slowdown.] quote: "México fabricó 301,803 vehículos durante septiembre del 2026"
  - p136 Mexico light-vehicle production, September 2025 (comparison base) = **355,589** vehicles (2025-09-01..2025-09-30) [DISCARD: 2025 production base; redundant with p137 change.] quote: "disminución de 15.3% contra las 355,589 unidades del año pasado"
  - p137 Mexico light-vehicle production year-on-year change, September 2026 = **15.3** % (2026-09-01..2026-09-30) [keep: Kept: September 2026 production change, corroborates the auto slowdown.] quote: "que representa disminución de 15.3% contra las 355,589 unidades del año pasado"
  - p138 Mexico light-vehicle exports, September 2026 (INEGI) = **277,369** vehicles (2026-09-01..2026-09-30) [keep: Kept: September 2026 vehicle export units, corroborates p140.] quote: "Las exportaciones de autos se redujeron 11.85% durante el noveno mes del 2026, al enviar 277,369 unidades"
  - p139 Mexico light-vehicle exports, September 2025 (comparison base) = **314,656** vehicles (2025-09-01..2025-09-30) [DISCARD: 2025 export base; redundant with p163 change.] quote: "comparado con los 314,656 vehículos enviados al mundo en 2025"
  - p140 Mexico light-vehicle exports year-on-year change, September 2026 = **11.85** % (2026-09-01..2026-09-30) [keep: Kept: September 2026 light-vehicle export change (-11.85%), the key shock signal for the September/August ratio.] quote: "Las exportaciones de autos se redujeron 11.85% durante el noveno mes del 2026"
  - p141 Mexico light-vehicle production year-on-year change, cumulative January-Septembe = **2.42** % (2026-01-01..2026-09-30) [DISCARD: Cumulative production change; September monthly production change (p137) is the relevant signal.] quote: "con reducción de 2.42% frente a las 3 millones 20,006 unidades ensambladas"
  - p142 Mexico light-vehicle exports year-on-year change, cumulative January-September 2 = **1.5** % (2026-01-01..2026-09-30) [DISCARD: Cumulative export change; redundant with monthly p163.] quote: "con descenso del 1.50% en comparación con el periodo enero-septiembre de 2025"
  - p143 General Motors Mexico light-vehicle production change, September 2026 = **27.1** % (2026-09-01..2026-09-30) [DISCARD: Single-firm (GM) production change; too narrow to enter a total-export formula and redundant with the aggregate auto-exp] quote: "General Motors que disminuyó su ensamble 27.1%"
  - p144 Nissan Mexico light-vehicle production change, September 2026 = **26.3** % (2026-09-01..2026-09-30) [DISCARD: Single-firm (Nissan) production change; too narrow and redundant with aggregate auto-export points.] quote: "seguido de Nissan con una baja de 26.3%"
  - p145 US auto market growth, September 2026 = **7** % (2026-09-01..2026-09-30) [DISCARD: US auto market growth is a demand-side context point with no established conversion to Mexican export value; not usable ] quote: "aunque el mercado de autos estadounidense creció 7% en septiembre"
- `https://www.imef.org.mx/descargas/2026/octubre/resultados-indicador-imef-septiembre-2026.pdf` -> **live_dated** (page date 2026-10-01); points raw/verified 15/15
  - p146 IMEF Manufacturing Index general, September 2026 (seasonally adjusted, diffusion = **50** index points (2026-09-01..2026-09-30) [keep: Kept: IMEF manufacturing index ~50 in September 2026, a broad activity signal for the September/August ratio.] quote: "el índice general mostró una ligera mejora al pasar de 49.9 a 50.0 puntos, alcanzando el umbral de neutralidad"
  - p147 IMEF Manufacturing Index general, August 2026 (prior month level) = **49.9** index points (2026-08-01..2026-08-31) [DISCARD: August IMEF level; only a comparison base for p146.] quote: "el índice general mostró una ligera mejora al pasar de 49.9 a 50.0 puntos, alcanzando el umbral de neutralidad"
  - p148 IMEF Manufacturing trend-cycle series, September 2026 = **49.9** index points (2026-09-01..2026-09-30) [DISCARD: Trend-cycle level; redundant with p146.] quote: "La serie tendencia-ciclo también avanzó 0.3 puntos hasta ubicarse en 49.9 unidades"
  - p149 IMEF Manufacturing trend-cycle change, September 2026 (points) = **0.3** index points (2026-09-01..2026-09-30) [DISCARD: Trend-cycle point change; redundant with p148 level.] quote: "La serie tendencia-ciclo también avanzó 0.3 puntos hasta ubicarse en 49.9 unidades"
  - p150 IMEF Manufacturing size-adjusted subindex, September 2026 = **51.9** index points (2026-09-01..2026-09-30) [DISCARD: Size-adjusted manufacturing subindex; redundant with the general index and not convertible to value.] quote: "el subíndice ajustado por tamaño de empresa retrocedió (-) 0.6 puntos hasta 51.9 unidades"
  - p151 IMEF Manufacturing New Orders component, September 2026 = **50.2** index points (2026-09-01..2026-09-30) [DISCARD: New orders component; redundant with p146 general index.] quote: "Nuevos pedidos retrocedió (-) 1.2 puntos hasta 50.2 unidades, aunque se mantuvo en zona de expansión"
  - p152 IMEF Manufacturing Production component, September 2026 = **47.7** index points (2026-09-01..2026-09-30) [DISCARD: Production component; redundant with p146 general index.] quote: "Producción disminuyó (-) 2.1 puntos hasta 47.7 unidades, profundizando su trayectoria contractiva"
  - p153 IMEF Manufacturing Employment component, September 2026 = **50.2** index points (2026-09-01..2026-09-30) [DISCARD: Employment component; redundant with the general manufacturing index for a value estimate.] quote: "el Empleo avanzó 0.6 puntos hasta 50.2 unidades, ingresando en terreno expansivo"
  - p154 IMEF Manufacturing Product Deliveries component, September 2026 = **49.5** index points (2026-09-01..2026-09-30) [DISCARD: Deliveries component; redundant with the general manufacturing index.] quote: "Entrega de Productos mostró una recuperación significativa de 3.5 puntos hasta 49.5 unidades"
  - p155 IMEF Manufacturing Inventories component, September 2026 = **52.4** index points (2026-09-01..2026-09-30) [DISCARD: Inventories component; redundant with the general manufacturing index.] quote: "Inventarios permaneció sin cambios en 52.4 unidades, consolidándose en zona de expansión"
  - p156 IMEF Non-Manufacturing Index general, September 2026 = **49.2** index points (2026-09-01..2026-09-30) [DISCARD: Non-manufacturing IMEF index; exports are overwhelmingly manufactured goods, so this adds no signal.] quote: "el índice general, que pasó de 49.0 a 49.2 puntos, un avance de 0.2 unidades respecto a agosto"
  - p157 IMEF Non-Manufacturing trend-cycle series, September 2026 = **49** index points (2026-09-01..2026-09-30) [DISCARD: Non-manufacturing trend-cycle; irrelevant to merchandise export value.] quote: "la serie tendencia-ciclo disminuyó marginalmente (-) 0.1 puntos hasta ubicarse en 49.0 unidades"
  - p158 IMEF Non-Manufacturing size-adjusted subindex, September 2026 = **48.5** index points (2026-09-01..2026-09-30) [DISCARD: Non-manufacturing size-adjusted subindex; irrelevant.] quote: "la medición ajustada por tamaño de empresa retrocedió (-) 1.2 puntos hasta 48.5 unidades"
  - p159 IMEF Non-Manufacturing Production component, September 2026 = **48.2** index points (2026-09-01..2026-09-30) [DISCARD: Non-manufacturing production component; irrelevant.] quote: "Producción avanzó 0.3 puntos hasta 48.2 unidades, moderando su ritmo de contracción"
  - p160 IMEF Non-Manufacturing New Orders component, September 2026 = **49.3** index points (2026-09-01..2026-09-30) [DISCARD: Non-manufacturing new orders; irrelevant.] quote: "Nuevos pedidos retrocedió ligeramente (-) 0.1 puntos hasta 49.3 unidades"
- `https://www.liderempresarial.com/exportaciones-automotrices-de-mexico-caen-12-los-datos-de-la-industria-en-2026/` -> **live_dated** (page date 2026-10-09); points raw/verified 15/12
  - p161 Mexico light-vehicle exports, September 2026 (units) = **277,369** as written "277 mil 369", value check pending vehicles (2026-09-01..2026-09-30) [DISCARD: Redundant copy of p138.] quote: "durante septiembre se exportaron 277 mil 369 unidades"
  - p162 Mexico light-vehicle exports, September 2025 (units) = **314,656** as written "314 mil 656", value check pending vehicles (2025-09-01..2025-09-30) [DISCARD: Redundant copy of p139.] quote: "frente a las 314 mil 656 enviadas al extranjero en el mismo mes de 2025"
  - p163 Mexico light-vehicle exports, September 2026 annual change (percent) = **11.85** % (2026-09-01..2026-09-30) [DISCARD: Redundant copy of p140.] quote: "Esto representó una disminución de 11.85%"
  - p164 Mexico light-vehicle exports, September 2026 annual decline (vehicles) = **37,287** as written "37 mil 287", value check pending vehicles (2026-09-01..2026-09-30) [DISCARD: Redundant with p163 percentage change.] quote: "equivalente a 37 mil 287 vehículos menos"
  - p165 Mexico light-vehicle exports, January-September 2026 cumulative annual change (p = **1.5** % (2026-01-01..2026-09-30) [DISCARD: Cumulative Jan-Sep vehicle export change; the September monthly change (p163) is the relevant signal.] quote: "2 millones 528 mil 623 vehículos ligeros, 1.5% menos que en el mismo periodo de 2025"
  - p166 Mexico light-vehicle exports, January-September cumulative difference 2026 vs 20 = **38,549** as written "38 mil 549", value check pending vehicles (2026-01-01..2026-09-30) [DISCARD: Cumulative vehicle difference; redundant with p163/p164.] quote: "la diferencia acumulada fue de 38 mil 549 vehículos"
  - p167 United States share of Mexico light-vehicle exports, January-September 2026 (per = **76.4** % (2026-01-01..2026-09-30) [DISCARD: US share of vehicle exports; not needed for a total-export level estimate.] quote: "equivalentes al 76.4% de las exportaciones"
  - p168 Canada share of Mexico light-vehicle exports, January-September 2026 (percent) = **12.4** % (2026-01-01..2026-09-30) [DISCARD: Canada share of vehicle exports; not needed.] quote: "Canadá concentró 12.4% de los envíos"
  - p169 Mexico light-vehicle exports to Canada, January-September 2026 cumulative (units = **314,185** as written "314 mil 185", value check pending vehicles (2026-01-01..2026-09-30) [DISCARD: Canada-bound vehicle units; sub-segment detail not needed for the total-export route.] quote: "con 314 mil 185 vehículos"
  - p170 Mexico light-vehicle exports to Germany, January-September 2026 cumulative (unit = **64,963** as written "64 mil 963", value check pending vehicles (2026-01-01..2026-09-30) [DISCARD: Germany-bound vehicle units; sub-segment detail not needed.] quote: "Alemania recibió 64 mil 963 unidades"
  - p171 Mexico light-vehicle exports to Brazil, January-September 2026 cumulative (units = **43,821** as written "43 mil 821", value check pending vehicles (2026-01-01..2026-09-30) [DISCARD: Brazil-bound vehicle units; sub-segment detail not needed.] quote: "y Brasil 43 mil 821"
  - p172 Nissan Mexico light-vehicle exports, January-September 2026 cumulative annual ch = **29.5** % (2026-01-01..2026-09-30) [DISCARD: Nissan cumulative export change; single-firm detail, redundant.] quote: "Así, acumuló una caída de 29.5%"
- `https://enfoquenoticias.com.mx/noticias/imef-recuperacion-economica-debil-mexico-2026` -> **live_dated** (page date 2026-10-01); points raw/verified 2/1
  - p173 Average annual GDP growth of Mexico through 2018 (comparison benchmark) = **2.2** % (..2018-12-31) [DISCARD: Historical average GDP growth benchmark, irrelevant to September 2026 export level.] quote: "una cifra que permanece por debajo del crecimiento promedio anual de 2.2% que registraba el PIB hasta 2018"
- dropped by code checks: 8 (scale word 'million' not supported by quote or table header: 6; period_end missing or unparseable: 1; period_end 2026-12-31 after as_of: 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['mexico exports', 'mexico trade balance', 'inegi exports']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p29', 'p46', 'p58', 'p93'] All report August 2026 total export growth of 40.4% y/y; same INEGI release echoed by multiple outlets, so one underlying measurement, not independent confirmation.
- corroborating: ['p2', 'p56', 'p94'] January-August 2026 cumulative exports 549,397.6 mdd and 29.3% growth; p56 mislabels it as first-half but the 29.3% figure matches the Jan-Aug cumulative, so treat as same INEGI datum.
- corroborating: ['p3', 'p59'] August 2026 seasonally adjusted monthly export growth 1.23%; same INEGI figure repeated.
- corroborating: ['p4', 'p35', 'p40'] September 2025 total exports 56,487.9 mdd, +13.8% y/y; consistent across INEGI table and headline.
- corroborating: ['p5', 'p39'] September 2025 seasonally adjusted monthly change -1.33%; duplicate of same INEGI figure.
- corroborating: ['p6', 'p20'] US goods imports from Mexico August 2026 y/y growth ~34.2-34.3%; same Census-based measurement reported by two outlets.
- corroborating: ['p7', 'p8', 'p19'] Mexico share of US goods imports August 2026 ~18.0-18.04%; same underlying Census data.
- corroborating: ['p18', 'p28'] Effective US tariff on Mexican imports August 2026 3.19%; duplicate.
- corroborating: ['p43', 'p44', 'p45'] August 2026 exports 78.0 bn, imports 77.4 bn, surplus 0.605 bn; internally consistent (78.0-77.4=0.6).
- corroborating: ['p30', 'p47'] Manufacturing exports strong in August 2026; p30 gives 42.6% manufacturing growth, p47 attributes leadership to non-automotive manufacturing (63.2%).
- corroborating: ['p32', 'p49', 'p62', 'p63'] Automotive exports declined ~2.2% y/y in August 2026 (1.0% to US); consistent across sources.
- corroborating: ['p70', 'p71', 'p72', 'p73'] September 2026 light vehicle exports 277,369 units (-11.9%) and production 301,803 (-15.1%); same AMIA/INEGI official figures.
- corroborating: ['p66', 'p67', 'p68', 'p69'] Tariff negotiation context: current 25% autos, 50% steel/aluminium, proposed 15% parity; contextual, not a level input.
- corroborating: ['p82', 'p90'] Laredo bridge revenue September 2026 7.09 mUSD, +3.1% y/y; duplicate of same figure.
- corroborating: ['p83', 'p85', 'p86'] Laredo FY2025-26 truck crossings 3,005,832, +0.8% (+23,504); internally consistent.
- conflicting: ['p1', 'p70'] August total exports +40.4% y/y but September light-vehicle exports -11.9% y/y; suggests September total growth likely well below August's, a material tension for the seasonal route.
- conflicting: ['p41', 'p42', 'p7'] Mexico share of US imports 15.5% (2024), 15.7% (2025) vs 18.0% (Aug 2026); the jump is large and may reflect a definitional or base-period difference, so treat the 18% cautiously.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p29', 'p46', 'p58', 'p93'] All report the same INEGI August 2026 total export figure (78,010.5 mdd) and +40.4% y/y; they share one underlying INEGI release, so this is one measurement echoed by several outlets, not independent 
- corroborating: ['p2', 'p94'] Same INEGI January-August 2026 cumulative total (549,397.6 mdd) and +29.3% y/y; identical source.
- corroborating: ['p3', 'p59'] Same seasonally adjusted August 2026 monthly growth (+1.23%); one INEGI measurement.
- corroborating: ['p4', 'p35', 'p40', 'p125', 'p127', 'p129'] All the September 2025 INEGI release: 56,487.9 mdd, +13.8% y/y. p35 is the only one carrying the USD level, which is what the seasonal route needs.
- corroborating: ['p5', 'p39'] Same September 2025 seasonally adjusted monthly change (-1.33%); one measurement.
- corroborating: ['p6', 'p20', 'p98', 'p111'] US goods imports from Mexico August 2026 up ~34.2-34.3% y/y; same US Census underlying data reported by several outlets.
- corroborating: ['p7', 'p8', 'p19', 'p99', 'p100'] Mexico's ~18% share of US goods imports in August 2026; same Census denominator, minor rounding differences.
- corroborating: ['p18', 'p28', 'p108'] Same 3.19% effective US tariff rate on Mexican imports in August 2026; one measurement.
- corroborating: ['p110', 'p113', 'p114', 'p117', 'p121', 'p122', 'p124'] IndexBox August 2026 US-Mexico trade block: $60.64bn US imports from Mexico, $94.29bn two-way, $336.17bn total US imports, Laredo $26.23bn imports. Internally consistent (60.64/336.17 ≈ 18.0%), so it 
- corroborating: ['p43', 'p29', 'p58'] Scotiabank's $78bn August export figure matches INEGI's 78,010.5 mdd; p43 is a rounded restatement, usable as a level anchor.
- corroborating: ['p30', 'p47'] Manufacturing exports +42.6% and non-automotive manufacturing +63.2% in August 2026; consistent decomposition of the +40.4% total.
- corroborating: ['p32', 'p49', 'p62', 'p63'] Automotive exports fell ~2.2% y/y in August 2026 (US-bound -1%); one INEGI auto-export measurement.
- corroborating: ['p70', 'p71', 'p138', 'p139', 'p140', 'p161', 'p162', 'p163', 'p164'] September 2026 light-vehicle exports 277,369 units, -11.85% y/y vs 314,656; consistent across outlets and with the 37,287-unit decline.
- corroborating: ['p72', 'p73', 'p135', 'p136', 'p137'] September 2026 light-vehicle production 301,803 units, -15.1/-15.3% y/y; minor rounding difference between outlets on the same INEGI figure.
- conflicting: ['p70', 'p1'] September 2026 light-vehicle exports fell ~12% y/y while August total exports rose 40.4%; the auto channel is a drag, so September total growth should be well below August's. This is the central uncer
- corroborating: ['p146', 'p147', 'p148', 'p151', 'p152'] IMEF manufacturing index ~50 in September 2026 (new orders 50.2, production 47.7): manufacturing roughly flat, consistent with a sharp slowdown from August's surge.
- corroborating: ['p82', 'p90', 'p83', 'p85', 'p86'] Laredo bridge revenue +3.1% y/y in September 2026 and truck crossings +0.8% for FY2025-26: border physical flow roughly flat, arguing against a September collapse but also against August-like growth.
- corroborating: ['p66', 'p67', 'p68', 'p69'] US tariff context: 25% auto tariff with a proposed cut to 15%, 50% steel/aluminium; these are policy levels, not September flow outcomes, and enter only as background for the shock adjustment.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | September/August original export ratio, adjusted for the September 2026 auto slowdown | 0.97 | 0.88..1.06 | 0.6829..1.366 (widened) | ratio | unused | Historically September original exports are close to August (roughly 0.95-1.00 in recent years), but September 2026 light-vehicle exports fell ~12% y/y while August total exports surged 40.4%, and the IMEF manufacturing index sat at ~50, so the September/August step should be at or slightly below th | The September 2026 seasonal step resembles recent Septembers but is pulled down by the auto-export decline. | A September 2026 total export print far above August (ratio > 1.1) or far below (ratio < 0.85). |
| a2 | September 2026 y/y growth factor relative to August 2026 growth | 0.5 | 0.2..0.9 | 0.2..0.9 | ratio | unused | August 2026 total exports grew 40.4% y/y, an exceptional surge; September 2026 light-vehicle exports fell ~12% y/y and manufacturing activity was flat, so September total growth should be well below August's but still positive. A factor of 0.5 (i.e., ~20% y/y growth) with a wide range captures the u | September 2026 total export growth is a fraction of August's exceptional growth, consistent with the auto drag. | September 2026 total exports growing at or above August's 40.4% rate, or falling outright. |
| a3 | Mexico-reported exports to US-reported imports from Mexico ratio (f.o.b./customs basis) | 1.29 | 1.15..1.45 | 0.9131..1.826 (widened) | ratio | unused | Mexico's August 2026 exports (78.0 bn) exceed US-reported imports from Mexico (60.64 bn) by a factor of ~1.29, reflecting f.o.b. vs customs-value and origin-rule differences. This ratio is used to convert US imports into Mexico exports for the d2 bridge. | The Mexico/US measurement-basis ratio observed in August 2026 carries into September 2026. | A September 2026 Mexico/US ratio outside 1.1-1.5. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | n/a |  | [] |  | 0.00 |  | input p43: id p43 unknown or discarded |
| m2 | formula_mc | n/a |  | [] |  | 0.00 |  | input p1: id p1 unknown or discarded |
| m3 | formula_mc | n/a |  | [] |  | 0.00 |  | input p43: id p43 unknown or discarded |
| m4 | formula_mc | n/a |  | [] |  | 0.00 |  | input p110: id p110 unknown or discarded |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target
- m4 coverage: the whole target

Result: central **n/a** USD, 80% interval [n/a, n/a] USD, basis no_method (no method produced an estimate, so there is no interval), weight rule None, weight on methods that use assumptions 0.00

## Published-value check (live use only)

Status: **not_confirmed**. 2 candidate(s); entity terms ['mexico']; measure stems ['expor', 'merch', 'mexic', 'usd']
Early checks while the sub-agents were running: 3 (not_confirmed); details in state.json -> published_early.

| id | name | value | unit | period | source | verdict | reason |
|---|---|---|---|---|---|---|---|
| p138 | Mexico light-vehicle exports, September 2026 (INEGI) | 277,369 | vehicles | 2026-09-01..2026-09-30 | www.eleconomista.com.mx | different | Light-vehicle exports are only a segment of total merchandise exports, not the all-commodities total; also unit is vehicles, not USD. |
| p135 | Mexico light-vehicle production, September 2026 (INEGI) | 301,803 | vehicles | 2026-09-01..2026-09-30 | www.eleconomista.com.mx | different | Light-vehicle production is a different measure (production, not exports) and only a segment; unit is vehicles, not USD. |


## Final answer

No estimate: no estimation method could be computed from the verified evidence.

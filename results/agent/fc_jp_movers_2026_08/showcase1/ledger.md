# Evidence ledger: fc_jp_movers_2026_08

- Question: Assume today is 2026-08-29. You know nothing published after this date. Estimate the number of people who moved between municipalities within Japan in August 2026 (Japanese and foreign residents combined), as first reported in the Statistics Bureau of Japan's monthly Report on Internal Migration in Japan Derived from the Basic Resident Registration.
- as_of: 2026-08-29
- Pinned target: Number of people who moved between municipalities within Japan (domestic internal migration) during August 2026, as first reported in the Statistics Bureau of Japan's monthly Report on Internal Migration in Japan Derived from the Basic Resident Registration. Counts are based on Basic Resident Regist | unit persons (count of moves/people recorded as moving between municipalities) | period 2026-08-01..2026-08-31 | publisher Statistics Bureau of Japan, Ministry of Internal Affairs and Communications

- Official value (scoring only, never shown to the agent): 356,920

## Directions and pages

### d1 [own_history] Statistics Bureau historical releases

Hypothesis: August internal migration totals follow a strong seasonal pattern, with August typically one of the highest months due to summer relocations. The August 2026 value can be estimated by applying the historical August-to-annual ratio or the August-to-recent-month ratio to known 2026 monthly data.

Queries issued by the searcher: Statistics Bureau Japan internal migration monthly report 2025 August 住民基本台帳人口移動報告; 住民基本台帳人口移動報告 2025年8月 転入者数 転出者数; 住民基本台帳人口移動報告 2026年6月 市区町村間移動者数; 統計メールニュース 2026年7月 住民基本台帳人口移動報告 市区町村間移動者数

- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2606/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025youyaku.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20260528_no1867.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-

### d2 [administrative] Basic Resident Registration system

Hypothesis: The target is directly derived from administrative move notifications (転入届/転出届). The number of such notifications processed in August 2026 can be estimated from historical notification volumes and any available partial administrative data (e.g., from local governments or the e-Stat portal).

Queries issued by the searcher: e-Stat 住民基本台帳移動報告 転入 転出 件数 2026; 住民基本台帳人口移動報告 2026年 月別 転入者数 転出者数; 住民基本台帳人口移動報告 2025年8月結果 市区町村間移動者数; 住民基本台帳人口移動報告 令和7年8月 移動者の市区町村間移動者数 前年同月

- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2606/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2605/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ecitizen.jp/statdb/StatsData/0003423635` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [base_rates] Seasonal adjustment factors

Hypothesis: The ratio of August internal migration to the annual total or to adjacent months is stable across years. This ratio can be applied to a known 2026 annual or year-to-date total to estimate August 2026.

Queries issued by the searcher: 住民基本台帳人口移動報告 月別 推移 年間; Japan internal migration monthly data 2019 2020 2021 2022 2023 2024 monthly Report on Internal Migration; 住民基本台帳人口移動報告 2025年 8月 移動者数 転入 転出 全国 都道府県間; 住民基本台帳人口移動報告 2026年 1月 2月 3月 4月 5月 6月 7月 結果 移動者数

- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025youyaku.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/index.htm` -> **dropped** (undecodable content (binary or unsupported encoding)); points raw/verified -/-
- `https://www.e-stat.go.jp/index.php/en/stat-search/database?page=1&layout=datalist&cycle=7&kikan=00200&toukei=00200523&tstat=000000070001&tclass1=00000` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [related_series] Population and vital statistics

Hypothesis: Internal migration counts are related to the size of the resident population and to the number of moves per capita. If the total population and the historical migration rate per 1,000 population are known, the August 2026 count can be approximated by population × monthly move rate, adjusted for seasonality.

Queries issued by the searcher: Japan population estimate 2026 総人口 人口推計; Statistics Bureau Japan Report on Internal Migration Basic Resident Registration monthly; 住民基本台帳人口移動報告 2025年8月結果 市区町村間移動者数; 住民基本台帳人口移動報告 2025年 年報 市区町村間移動者数 総数

- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025youyaku.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.stat.go.jp/data/jinsui/new.htm` -> **dropped** (undecodable content (binary or unsupported encoding)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/index.htm` -> **dropped** (undecodable content (binary or unsupported encoding)); points raw/verified -/-

### d5 [related_series] Foreign resident registration statistics

Hypothesis: The total internal migration count is the sum of Japanese and foreign resident moves. Foreign resident moves can be estimated from foreign population size and foreign-specific mobility rates, then added to Japanese moves. This route helps validate the combined total and assess the foreign share.

Queries issued by the searcher: foreign residents Japan internal migration statistics 住民基本台帳 外国人 移動数; 在留外国人 人口 2025 統計 総務省 住民基本台帳; 住民基本台帳人口移動報告 2026年7月結果 外国人移動者 市区町村間移動者数; 住民基本台帳人口移動報告 2025年8月結果 市区町村間移動者数 外国人移動者

- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/index.htm` -> **dropped** (undecodable content (binary or unsupported encoding)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025gaiyou.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.moj.go.jp/isa/content/001465923.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.gaikokujin-press.com/archives/3245` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d6 [physical_flow] Moving and relocation services

Hypothesis: The number of household moves is a physical flow that drives internal migration counts. If the average number of persons per moving household is known, the migration count can be approximated by the number of household moves × average household size. Moving company activity or utility transfers could serve as a proxy.

Queries issued by the searcher: 引越し 件数 統計 2025 全国 世帯; Japan internal migration report Basic Resident Registration monthly number of movers; 住民基本台帳人口移動報告 2025年8月結果 市区町村間移動者数; 引越し 世帯当たり人員 2.23 住民基本台帳 移動者数 世帯数

- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://note.intimatemerger.com/n/n062ad2458457` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://gyokai-map.com/chaosmap-moving-service-2026` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://hikkoshi-rakunavi.com/wp/?p=33935` -> **snapshot** (snapshot 20260607074929); points raw/verified 15/11
  - p1 Individual (personal) moving jobs in August 2025, Japan (Libero data) = **829** moving jobs (件) (2025-08-01..2025-08-31) [keep: ] quote: "\| 8月 \| 829 \| 9.39% \|"
  - p2 Corporate (business) moving jobs in August 2025, Japan (Libero data) = **1,620** moving jobs (件) (2025-08-01..2025-08-31) [keep: ] quote: "\| 8月 \| 1620 \| 5.03% \|"
  - p3 Individual (personal) moving jobs total for 2025, Japan (Libero data) = **8,825** moving jobs (件) (2025-01-01..2025-12-31) [keep: ] quote: "\| 合計 \| 8825 \| 100% \|"
  - p4 Corporate (business) moving jobs total for 2025, Japan (Libero data) = **32,228** moving jobs (件) (2025-01-01..2025-12-31) [keep: ] quote: "\| 合計 \| 32228 \| 100% \|"
  - p5 Individual (personal) moving jobs in January 2025, Japan (Libero data) = **493** moving jobs (件) (2025-01-01..2025-01-31) [keep: ] quote: "\| 1月 \| 493 \| 5.59% \|"
  - p6 Individual (personal) moving jobs in November 2025, Japan (Libero data) = **873** moving jobs (件) (2025-11-01..2025-11-30) [keep: ] quote: "\| 11月 \| 873 \| 9.89% \|"
  - p7 Corporate (business) moving jobs in March 2025, Japan (Libero data) = **6,522** moving jobs (件) (2025-03-01..2025-03-31) [keep: ] quote: "\| 3月 \| 6522 \| 20.24% \|"
  - p8 Corporate (business) moving jobs in December 2025, Japan (Libero data) = **1,217** moving jobs (件) (2025-12-01..2025-12-31) [keep: ] quote: "\| 12月 \| 1217 \| 3.78% \|"
  - p9 Share of corporate moving jobs concentrated in March and April 2025, Japan (Libe = **36** % (2025-03-01..2025-04-30) [DISCARD: A rounded qualitative share (about 36% in March-April) already implied by the monthly corporate counts p7 and p4; adds n] quote: "特筆すべきは、全体の約36%が3月・4月のわずか2ヶ月間に集中している点です。"
  - p10 Ratio of peak March to lowest December corporate moving jobs, 2025, Japan (Liber = **5** times (multiple) (2025-01-01..2025-12-31) [DISCARD: A rounded ratio (about 5x) already implied by p7 and p8; redundant with the underlying monthly counts.] quote: "ピークの3月は、最も少ない12月と比較して約5倍もの差があることが分かります。"
  - p11 Ratio of most (November) to fewest (January) individual moving jobs, 2025, Japan = **2** times (multiple, described as just under 2x) (2025-01-01..2025-12-31) [DISCARD: A rounded ratio (just under 2x) already implied by p5 and p6; redundant with the underlying monthly counts.] quote: "最も多い11月と少ない1月を比較すると件数は2倍弱の差があります。"
- dropped by code checks: 4 (number: more than one number in value_as_written: 1; period_end missing or unparseable: 3)

### d7 [shocks] Calendar and economic conditions

Hypothesis: August migration is influenced by calendar effects (Obon holiday, school year start in September) and economic conditions (job market, housing). Any unusual shocks in 2026 (e.g., policy changes, natural disasters, pandemic-related shifts) could alter the typical seasonal pattern. Identifying such shocks helps adjust the historical baseline.

Queries issued by the searcher: Japan internal migration 2026 trends; 2026年 引越し 需要 動向; 住民基本台帳移動報告 2026年 8月; Japan relocation trends 2026 news remote work housing

- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/index.htm` -> **dropped** (undecodable content (binary or unsupported encoding)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2606/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://toyokeizai.net/articles/-/951981` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/pdf/gaikyou.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-

### d8 [forecasts_markets] Official projections and nowcasts

Hypothesis: Any published forecast or nowcast for Japan's August 2026 internal migration, or for 2026 annual migration, can provide a direct anchor. Even a projection from a research institute or a government plan could be useful if it shares the same definition.

Queries issued by the searcher: Japan internal migration forecast 2026; 人口移動 予測 2026 転入 転出; 住民基本台帳人口移動報告 2026年8月 市区町村間移動者数; 2025年8月 住民基本台帳 人口移動報告 移動者数 前年同月

- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/index.htm` -> **dropped** (undecodable content (binary or unsupported encoding)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/pdf/gaikyou.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://ecitizen.jp/statdb/StatsData/0003420473` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ifa-leading.com/column/nihon-kokunai-ni-okeru-jinko-ido-no-jokyo/` -> **snapshot** (snapshot 20260610131349); points raw/verified 15/7
  - p12 Year-on-year percentage change in Japan inter-municipal movers, 2025 vs 2024 = **0.3** % (2025-01-01..2025-12-31) [keep: ] quote: "市区町村間移動者数(市区町村間で住所を移し、転入の届出を行った者の数)は519万548人で、前年に比べ1万7,198人(0.3%)の減少となりました。"
  - p13 Year-on-year change in Japan inter-prefecture movers, 2025 vs 2024 = **7,518** persons (2025-01-01..2025-12-31) [DISCARD: Inter-prefecture mover level for 2025; the target is all inter-municipal moves, which includes intra-prefecture moves, s] quote: "都道府県間移動者数は251万5,731人と前年比7,518人(0.3%)の減少"
  - p14 Year-on-year percentage change in Japan inter-prefecture movers, 2025 vs 2024 = **0.3** % (2025-01-01..2025-12-31) [DISCARD: Percentage version of p13; redundant and covers a narrower scope than the target.] quote: "都道府県間移動者数は251万5,731人と前年比7,518人(0.3%)の減少"
  - p15 Year-on-year change in Japan intra-prefecture movers, 2025 vs 2024 = **9,680** persons (2025-01-01..2025-12-31) [DISCARD: Intra-prefecture mover level for 2025; a component of the target but not needed separately once the total p12 is used.] quote: "都道府県内移動者数は267万4,817人と前年比9,680人(0.4%)の減少となりました。"
  - p16 Year-on-year percentage change in Japan intra-prefecture movers, 2025 vs 2024 = **0.4** % (2025-01-01..2025-12-31) [DISCARD: Percentage version of p15; redundant and narrower than the target.] quote: "都道府県内移動者数は267万4,817人と前年比9,680人(0.4%)の減少となりました。"
  - p17 Share of Japan's total population that moved across municipalities, 2025 (movers = **4** % (2025-01-01..2025-12-31) [keep: ] quote: "日本の総人口に占める市区町村を跨ぐ移動は4%強であり、人口25人に1人が引越しをしているという計算となります。"
  - p18 Year-on-year percentage change in in-migrants to Japan from abroad, 2025 vs 2024 = **6.3** % (2025-01-01..2025-12-31) [DISCARD: International in-migration change; the target is domestic inter-municipal moves, so this is out of scope.] quote: "国外からの転入者数は78万2,165人で、前年に比べ4万6,282人(6.3%)の増加"
- dropped by code checks: 8 (number: more than one number in value_as_written: 8)

### b1 [own_history] Statistics Bureau monthly Report on Internal Migration

Hypothesis: The August 2026 estimate is currently anchored only on the 2025 annual level (p12) and a moving-company seasonal analogue (p1-p8). Monthly inter-municipal mover counts for 2024 and 2025 (and any 2026 months already published before 2026-08-29) would let us build a true same-calendar-period series and apply series_naive or yoy_scaling directly, replacing the weaker annual-to-month ratio route.

Queries issued by the searcher: e-Stat 住民基本台帳人口移動報告 月報 市区町村間移動者数 2025年8月; Statistics Bureau Japan Report on Internal Migration monthly 2025 inter-municipal movers; 住民基本台帳人口移動報告 2026年 月次 移動者数; 住民基本台帳人口移動報告 令和6年 月報 都道府県間移動者数 市区町村間

- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20250926_no1800.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.e-stat.go.jp/stat-search/database?toukei=00200523&tstat=000000070001` -> **snapshot** (snapshot 20260608181841); points raw/verified 0/0
- `https://www.e-stat.go.jp/index.php/stat-search?iroha=18&layout=dataset&page=1&toukei=00200523` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [base_rates] Seasonal share of annual inter-municipal moves occurring in August

Hypothesis: The route from the 2025 annual level (p12) to August 2026 requires an August share of the annual total. A published monthly breakdown for any recent year would supply that share directly and remove the need to infer seasonality from moving-company job postings, which is the largest uncertainty in the current estimate.

Queries issued by the searcher: 住民基本台帳人口移動報告 8月 市区町村間移動者数 年間; Japan internal migration August share of annual total 住民基本台帳人口移動報告; 住民基本台帳人口移動報告 2024年 結果 市区町村間移動者数 年間 合計; 住民基本台帳人口移動報告 2025年 結果 市区町村間移動者数 1年間

- `https://www.stat.go.jp/data/idou/2024np/jissu/pdf/all.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/sokuhou/tsuki/index.htm` -> **dropped** (undecodable content (binary or unsupported encoding)); points raw/verified -/-
- `https://www.stat.go.jp/info/mail/pdf/20250926_no1800.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-

### b3 [related_series] Foreign resident share of inter-municipal moves

Hypothesis: The target combines Japanese and foreign residents. If foreign residents have a materially different mobility rate or seasonal pattern, the combined August 2026 count could deviate from a Japanese-only baseline. A foreign-resident mover count or share would let us validate or adjust the combined estimate.

Queries issued by the searcher: 住民基本台帳人口移動報告 外国人 移動者数; Japan internal migration foreign residents share 住民基本台帳人口移動報告 国籍別; 住民基本台帳人口移動報告 2025年8月結果 外国人移動者 市区町村間移動者数; stat.go.jp idou 2026年7月結果 外国人移動者 市区町村間

- `https://www.stat.go.jp/data/idou/rireki/2508/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/rireki/2602/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.stat.go.jp/info/today/pdf/189.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://www.stat.go.jp/data/idou/2025np/jissu/pdf/2025youyaku.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['japan internal migration', 'august 2026 migration', 'japan move statistics']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p12', 'p13', 'p14', 'p15', 'p16'] All from the same ifa-leading.com summary of the Statistics Bureau's 2025 annual Report on Internal Migration; they describe the same underlying measurement (inter-municipal movers 5,190,548 in 2025, 
- corroborating: ['p17', 'p12'] p17 states movers are just over 4% of Japan's total population, i.e. about 1 in 25 people moved across municipalities in 2025. This is consistent with p12's 5.19 million annual inter-municipal movers 
- corroborating: ['p18', 'p12'] p18 (in-migrants from abroad up 6.3% in 2025) comes from the same report and same source as p12-p17. It is a different flow (international in-migration, not internal inter-municipal moves) and therefo
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11'] All are Libero/hikkoshi-rakunavi moving-job counts for 2025. They are internally consistent (p9's ~36% March-April concentration, p10's ~5x March/December ratio, p11's ~2x November/January ratio all m
- corroborating: ['p1', 'p2'] Individual and corporate moving jobs for August 2025 are separate series from the same source; together they show August is a high but not peak month for moving activity, with the March-April corporat
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p12', 'p13', 'p14', 'p15', 'p16', 'p17'] All derive from the same 2025 Statistics Bureau Report on Internal Migration (via one secondary article). They consistently describe a 2025 inter-municipal mover total of about 5.19 million, a ~0.3-0.
- corroborating: ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11'] All are Libero moving-job posting counts for 2025 from the same source. They are internally consistent (monthly values sum to the stated annual totals; March/April concentration and peak-to-trough rat
- corroborating: ['p12', 'p18'] Both come from the same 2025 migration report summary. p12 gives the domestic inter-municipal mover change; p18 gives the separate international in-migration change. They are consistent in showing mod
- contextual: ['p1', 'p12'] The moving-company posting series (p1-p11) and the administrative mover total (p12) are different measurements of related but distinct phenomena. The posting series can supply a within-year seasonal s

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | August share of the annual inter-municipal mover total | 9.5 | 8..11.5 | 6.782..13.56 (widened) | % | unused | August is one of the highest months for Japanese residential moves (summer relocation plus the September school-year start). The Libero posting series gives August individual postings at 9.39% of the annual total (p1/p3) and corporate postings at 5.03% (p2/p4); administrative mover counts are less c | The 2025 annual inter-municipal mover total (p12) is a valid base and the 2026 seasonal pattern is broadly similar to 2025; used to scale the annual level to August 2026. | A published monthly breakdown for a recent year showing August shares outside roughly 8-11.5%, or evidence of a major 2026 shock (disaster, policy change) that shifted summer moving behavior. |
| a2 | Year-on-year change factor for August 2026 vs August 2025 | 1 | 0.97..1.03 | 0.894..1.118 (widened) | factor | unused | The 2025 annual inter-municipal mover total was down only 0.3% from 2024 (p12) and the mover share was just over 4% of population (p17). With no published 2026 monthly data before the cutoff, near-flat year-on-year change is the best central assumption, with a modest range for small population or mo | Used to carry the 2025 August level forward to August 2026 when no 2026 monthly data are available. | Published 2026 monthly mover data showing a year-on-year change outside roughly -3% to +3%, or a major demographic or policy shock. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | n/a | ['p12'] / ['a1'] | [] |  | 0.00 |  | formula_mc needs at least one input that is a quantity (not a share, ratio or %); a product of ratios cannot produce the target |
| m2 | formula_mc | n/a | ['p12'] / ['a1', 'a2'] | [] |  | 0.00 |  | formula_mc needs at least one input that is a quantity (not a share, ratio or %); a product of ratios cannot produce the target |

Result: central **n/a**, 80% interval [n/a, n/a], basis no_method, weight rule None, weight on methods that use assumptions 0.00

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

No estimate: no estimation method could be computed from the verified evidence.

# Evidence ledger: fc_kr_births_2026_07

- Question: Assume today is 2026-08-23. You know nothing published after this date. Estimate the number of live births in South Korea in July 2026, as it will be first reported in the national statistics agency's monthly Population Trends release.
- as_of: 2026-08-23
- Pinned target: Number of live births occurring in South Korea during July 2026, as first reported in the national statistics agency's monthly Population Trends release (population trend / vital statistics). | unit live births (persons) | period 2026-07-01..2026-07-31 | publisher Statistics Korea (KOSTAT), Monthly Population Trends (인구동향 / 인구추이)

- Official value (scoring only, never shown to the agent): 24,275

## Directions and pages

### d1 [related_series] Population registration and resident registration data

Hypothesis: Monthly birth counts are closely related to the number of birth registrations in the resident registration system. The target can be estimated by adjusting registration counts for typical registration lags and coverage differences. The relationship is near one-to-one but with timing differences.

Queries issued by the searcher: 주민등록 출생신고 2026년 7월; South Korea birth registration monthly 2026 주민등록 출생; 행정안전부 주민등록 인구통계 출생등록 2026년 6월; 주민등록 출생등록 수 통계청 출생아 수 차이 비교 2026

- `https://nowon.kr/dong/user/bbs/BD_selectBbs.do?q_bbsCode=1042&q_bbscttSn=20260804170322638` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ongjin.go.kr/open_content/main/peti/petiDetail.do?seq=810&pgno=5` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.osan.go.kr/portal/contents.do?mId=0102130000` -> **snapshot** (snapshot 20260408223852); points raw/verified 0/0
- `https://www.law.go.kr/lsLinkCommonInfo.do?lspttninfSeq=130255&chrClsCd=010202` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [forecasts_markets] Official and private forecasts for 2026 births

Hypothesis: Published forecasts for South Korea's 2026 total births or monthly births can provide a direct estimate or a range. These forecasts may incorporate recent trends and policy effects. The relationship is direct if the forecast is for the same period and definition.

Queries issued by the searcher: South Korea 2026 birth forecast total live births; 2026년 출생아 수 전망 통계청; 2025년 7월 출생아 수 인구동향; 2026년 6월 인구동향 출생아 2만3111명

- `https://m.etoday.co.kr/news/view/2610060?trc=m_main_top_sub` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.wowtv.co.kr/NewsCenter/News/Read?articleId=2026072938541` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=204&list_no=438748&act=view&mainXml=Y` -> **snapshot** (snapshot 20251212121719); points raw/verified 9/9
  - p1 South Korea live births, July 2025 (monthly Population Trends) = **21,803** live births (persons) (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "출생아 수는 21,803명으로 전년동월대비 5.9% 증가"
  - p2 South Korea live births year-on-year change rate, July 2025 = **5.9** % (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "출생아 수는 21,803명으로 전년동월대비 5.9% 증가"
  - p3 South Korea deaths, July 2025 (monthly Population Trends) = **27,979** deaths (persons) (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "사망자 수는 27,979명으로 전년동월대비 0.7% 감소"
  - p4 South Korea deaths year-on-year change rate, July 2025 = **0.7** % (2025-07-01..2025-07-31) [DISCARD: Duplicate of p27 (same July 2025 deaths y/y change from the same MODS release); adds no information.] quote: "사망자 수는 27,979명으로 전년동월대비 0.7% 감소"
  - p5 South Korea marriages, July 2025 (monthly Population Trends) = **20,394** marriages (cases) (2025-07-01..2025-07-31) [DISCARD: Duplicate of p28 (same July 2025 marriages count from the same MODS release).] quote: "혼인 건수는 20,394건으로 전년동월대비 8.4% 증가"
  - p6 South Korea marriages year-on-year change rate, July 2025 = **8.4** % (2025-07-01..2025-07-31) [DISCARD: Duplicate of p29 (same July 2025 marriages y/y change from the same MODS release).] quote: "혼인 건수는 20,394건으로 전년동월대비 8.4% 증가"
  - p7 South Korea divorces, July 2025 (monthly Population Trends) = **7,826** divorces (cases) (2025-07-01..2025-07-31) [DISCARD: Duplicate of p30 (same July 2025 divorces count from the same MODS release).] quote: "이혼 건수는 7,826건으로 전년동월대비 1.4% 감소"
  - p8 South Korea divorces year-on-year change rate, July 2025 = **1.4** % (2025-07-01..2025-07-31) [DISCARD: Duplicate of p31 (same July 2025 divorces y/y change from the same MODS release).] quote: "이혼 건수는 7,826건으로 전년동월대비 1.4% 감소"
  - p9 South Korea natural increase (live births minus deaths), July 2025 = **-6,175** persons (natural increase) (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "자연증가(출생아 수 - 사망자 수)는 -6,175명"
- `https://www.sedaily.com/article/20035151` -> **snapshot** (snapshot 20260513102711); points raw/verified 14/3
  - p10 Year-on-year increase in registered pregnant women, Apr 2025–Mar 2026 vs prior y = **16** % (2025-04-01..2026-03-31) [keep: ] quote: "이 기간 임산부 수는 전년 30만 명 대비 16%가량 증가해"
  - p11 Year-on-year increase in Q1 2026 birth registrations = **15** % (2026-01-01..2026-03-31) [keep: ] quote: "출생 등록 건수는 7만 3742건으로 전년 동기 대비 약 15% 증가하며 역대 최대 증가 폭을 기록했다."
  - p12 Year-on-year increase in January 2026 live births = **11.7** % (2026-01-01..2026-01-31) [keep: ] quote: "올해 1월 출생아 수 역시 2만 6916명으로 전년 동월 대비 11.7% 증가하는 등 유사한 흐름이 이어지고 있다."
- dropped by code checks: 11 (number: unknown scale word '만': 3; number: more than one number in value_as_written: 4; period_end missing or unparseable: 2; period_end 2026-12-31 after as_of: 2)

### d3 [related_series] Hospital and health insurance newborn records

Hypothesis: The number of live births is closely linked to the number of newborn health insurance registrations and hospital delivery records. These administrative data can provide an independent estimate of the monthly birth count, possibly with a short lag. The relationship is strong but may have coverage differences (e.g., foreign nationals, uninsured).

Queries issued by the searcher: 건강보험 신생아 등록 2026 국민건강보험공단 출생 통계; South Korea newborn health insurance registration monthly 2026 births; 통계청 인구동향 2026년 7월 출생아 수; 국민건강보험공단 신생아 등록 통계 월별 출생아; 2026년 6월 인구동향 출생아 수 발표 8월; 건강보험공단 통계연보 신생아 자격취득 출생아 수

- `https://perfect.govtmi.com/%ec%95%84%ec%a7%81%eb%8f%84-%ec%a7%81%ec%a0%91-%ea%b0%80%ec%84%9c-%ec%8b%a0%ec%b2%ad-%ed%95%98%ec%84%b8%ec%9a%94-%ec%b6%9c%` -> **snapshot** (snapshot 20260510113420); points raw/verified 0/0
- `https://www.guri.go.kr/ikium/contents.do?key=8403` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.sasang.go.kr/health/board/download.sasang?boardId=BBS_0000080&menuCd=DOM_000000406001000000&startPage=4&dataSid=528631&command=update&file` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.gov.kr/portal/rcvfvrSvc/dtlEx/319000000142?lawAreaCd=1159000000` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [base_rates] Demographic accounting: births from population by age and fertility rates

Hypothesis: Live births in a month can be estimated as the sum over women of reproductive age of (number of women in age group) × (monthly age-specific fertility rate). This route requires population estimates by age and recent fertility rates. The relationship is definitional but sensitive to the accuracy of population and fertility inputs.

Queries issued by the searcher: Statistics Korea monthly population trends 2025 births total fertility rate; South Korea age-specific fertility rate 2025 women 15-49 population estimates; 2026년 5월 인구동향 출생아 수 통계청; 장래인구추계 2025 2072 연령별 여성인구 가임여성 인구

- `https://mods.go.kr/board.es?mid=a10301020100&bid=204&act=view&list_no=446225&tag=&nPage=1&ref_bid=203,204,205,206,207&keyField=T&keyWord=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.jetro.go.jp/biznews/2026/03/b292cb8ff3c49c9f.html` -> **snapshot** (snapshot 20260709043403); points raw/verified 15/11
  - p13 South Korea year-on-year percentage increase in live births in 2025 = **6.8** percent (2025-01-01..2025-12-31) [EXCLUDED (ablation): ] quote: "2025年の出生数は前年比1万6,140人増(6.8%増)の25万4,457人"
  - p14 South Korea total fertility rate (TFR) in 2025 = **0.8** children per woman (2025-01-01..2025-12-31) [keep: ] quote: "合計特殊出生率は前年から0.05ポイント上昇した0.80となった"
  - p15 South Korea year-on-year change in total fertility rate in 2025 = **0.05** points (2025-01-01..2025-12-31) [keep: ] quote: "合計特殊出生率は前年から0.05ポイント上昇した0.80となった"
  - p16 South Korea age-specific fertility rate, women aged 30-34, 2025 (births per 1,00 = **73.2** births per 1,000 women (2025-01-01..2025-12-31) [EXCLUDED (ablation): ] quote: "30代前半が73.2人と最も多く"
  - p17 South Korea age-specific fertility rate, women aged 35-39, 2025 (births per 1,00 = **52** births per 1,000 women (2025-01-01..2025-12-31) [EXCLUDED (ablation): ] quote: "30代後半(52.0人)"
  - p18 South Korea age-specific fertility rate, women aged 25-29, 2025 (births per 1,00 = **21.3** births per 1,000 women (2025-01-01..2025-12-31) [EXCLUDED (ablation): ] quote: "20代後半(21.3人)と続く"
  - p19 South Korea year-on-year increase in age-specific fertility rate, women aged 35- = **6** births per 1,000 women (2025-01-01..2025-12-31) [EXCLUDED (ablation): ] quote: "30代後半が前年比6.0人(13.0%)増と大きく上昇し"
  - p20 South Korea year-on-year percentage increase in age-specific fertility rate, wom = **13** percent (2025-01-01..2025-12-31) [DISCARD: Age-specific fertility increase for women aged 35 in 2025 is a structural detail not usable as a direct numerical input ] quote: "30代後半が前年比6.0人(13.0%)増と大きく上昇し"
  - p21 South Korea mean age of women at childbirth, 2025 = **33.8** years (2025-01-01..2025-12-31) [DISCARD: Mean age at childbirth in 2025 is contextual; not a direct numerical input for July 2026 monthly births.] quote: "平均出産年齢は前年に比べ0.2歳上昇した33.8歳"
  - p22 South Korea mean age of women at first childbirth, 2025 = **33.2** years (2025-01-01..2025-12-31) [DISCARD: Mean age at first childbirth in 2025 is contextual; not a direct numerical input for July 2026 monthly births.] quote: "第1子の平均出産年齢は0.1歳上昇した33.2歳だった"
  - p23 South Korea share of first births in total live births, 2025 = **62.4** percent (2025-01-01..2025-12-31) [EXCLUDED (ablation): ] quote: "出生数に占める第1子の割合は前年比1.1%ポイント上昇した62.4%となった"
- `https://www.news1.kr/economy/trend/6242343` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.newsis.com/view/NISX20250924_0003341905` -> **dropped** (snapshot fetch failed (http 404); live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 4 (number: more than one number in value_as_written: 4)

### d5 [shocks] Policy and calendar effects on births

Hypothesis: Recent policy changes (e.g., parental benefits, housing support) or one-off events (e.g., COVID-19 pandemic timing, marriage trends) may have shifted the number of births in 2026 relative to historical patterns. The direction and magnitude of these effects can be inferred from marriage data and policy announcements.

Queries issued by the searcher: South Korea monthly marriage statistics 2025 2026 Statistics Korea; Korea births 2026 forecast pronatalist policy impact 출생아 수 전망; 2025년 7월 출생아 수 2만 인구동향; 2026년 7월 출생아 수 전망 하반기 출생아 증가

- `https://biz.chosun.com/en/en-policy/2026/07/29/BC2ERZDWNJEXJGVZAHECYJ6WAI/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://nsp.nanet.go.kr/trend/latest/detail.do?latestTrendControlNo=TREN0000003532` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.chosun.com/english/market-money-en/2026/04/23/FITED7MYBRGXPIBEHSE3Z2GA34/` -> **snapshot** (snapshot 20260423121323); points raw/verified 0/0
- `https://www.icbci.com.hk/userfiles/resources/icbc/haiwai/icbcinternational/download/insights/insight_tc_0023.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-

### d6 [physical_flow] Obstetric and neonatal care utilization

Hypothesis: The number of live births is proportional to the number of deliveries in hospitals, which can be approximated by obstetric bed occupancy, delivery room usage, or newborn screening tests. These physical flows can provide an independent check on the birth count. The relationship requires a conversion factor (e.g., births per delivery, screening coverage).

Queries issued by the searcher: 신생아 선별검사 건수 2026; South Korea newborn screening monthly statistics 2026; 인구동향 2026년 6월 출생아 수 통계청; 분만 건수 2026년 7월; 2026년 5월 인구동향 출생아 수 발표

- `https://www.edaily.co.kr/News/Read?newsId=02974966645577824` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://m.yakup.com/news/index.html?mode=view&cat=12&nid=331692` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://m.rapportian.com/news/articleView.html?idxno=240070` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.korea.kr/briefing/pressReleaseView.do?newsId=156780484&pWise=mSub&pWiseSub=C2` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d7 [attention] Search and social media interest in pregnancy and childbirth

Hypothesis: Online search volume for pregnancy-related terms or baby product purchases may correlate with birth counts with a lead time of several months. This can serve as a leading indicator for the July 2026 birth count if the relationship is stable. The link is indirect and requires a validated bridge.

Queries issued by the searcher: Google Trends South Korea pregnancy search volume birth rate leading indicator; 네이버 검색어 트렌드 임신 출산 상관관계 연구; Google Trends search volume nowcasting monthly births Korea fertility prediction study; 통계청 인구동향 2026년 6월 출생아 수 발표

- `https://anlp.jp/proceedings/annual_meeting/2023/pdf_dir/Q7-10.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://pdxscholar.library.pdx.edu/cgi/viewcontent.cgi?article=1386&context=usp_fac` -> **dropped** (unsupported content type application/pdf); points raw/verified -/-
- `https://repository.kihasa.re.kr/bitstream/201002/21228/1/%ec%97%b0%ea%b5%ac%eb%b3%b4%ea%b3%a0%ec%84%9c%202016-44-04.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://repo.kicce.re.kr/bitstream/2019.oak/4644/2/IP1908.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-

### b1 [related_series] KOSTAT monthly birth series for 2025 and early 2026

Hypothesis: A July 2025 live-birth count (and the 2025 monthly birth path) would anchor the year-over-year base for July 2026. Without it, the 2026 y/y growth rate implied by p10–p12 cannot be applied to a known July level. This is the single most important missing input for a direct level estimate.

Queries issued by the searcher: KOSTAT Monthly Population Trends live births July 2025; Statistics Korea 인구동향 2025년 7월 출생아 수; 2026년 6월 인구동향 출생아 수 통계청; 인구동향 2026년 1월 출생아 수 전년동월대비; "2026년 5월" 인구동향 출생아 수 전년동월대비 증가 국가데이터처

- `https://mods.go.kr/board.es?mid=a10301010000&bid=204&list_no=438748&act=view&mainXml=Y` -> **snapshot** (snapshot 20251212121719); points raw/verified 9/9
  - p24 South Korea live births, July 2025 (monthly Population Trends) = **21,803** live births (persons) (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "출생아 수는 21,803명으로 전년동월대비 5.9% 증가"
  - p25 South Korea live births, July 2025, year-over-year change (percent) = **5.9** % (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "출생아 수는 21,803명으로 전년동월대비 5.9% 증가"
  - p26 South Korea deaths, July 2025 (monthly Population Trends) = **27,979** deaths (persons) (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "사망자 수는 27,979명으로 전년동월대비 0.7% 감소"
  - p27 South Korea deaths, July 2025, year-over-year change (percent) = **0.7** % (2025-07-01..2025-07-31) [DISCARD: Deaths in July 2025 are not a useful input for estimating July 2026 live births; no credible bridge from deaths to birth] quote: "사망자 수는 27,979명으로 전년동월대비 0.7% 감소"
  - p28 South Korea marriages, July 2025 (monthly Population Trends) = **20,394** marriages (cases) (2025-07-01..2025-07-31) [DISCARD: July 2025 marriages are not a direct input for July 2026 births; the marriage-to-birth lag is roughly 1–2 years, so July] quote: "혼인 건수는 20,394건으로 전년동월대비 8.4% 증가"
  - p29 South Korea marriages, July 2025, year-over-year change (percent) = **8.4** % (2025-07-01..2025-07-31) [DISCARD: July 2025 marriages y/y change is not a direct input for July 2026 births; same lag problem as p28.] quote: "혼인 건수는 20,394건으로 전년동월대비 8.4% 증가"
  - p30 South Korea divorces, July 2025 (monthly Population Trends) = **7,826** divorces (cases) (2025-07-01..2025-07-31) [DISCARD: July 2025 divorces are not a useful input for July 2026 live births.] quote: "이혼 건수는 7,826건으로 전년동월대비 1.4% 감소"
  - p31 South Korea divorces, July 2025, year-over-year change (percent) = **1.4** % (2025-07-01..2025-07-31) [DISCARD: July 2025 divorces y/y change is not a useful input for July 2026 live births.] quote: "이혼 건수는 7,826건으로 전년동월대비 1.4% 감소"
  - p32 South Korea natural increase (live births minus deaths), July 2025 = **-6,175** persons (natural increase) (2025-07-01..2025-07-31) [EXCLUDED (ablation): ] quote: "자연증가(출생아 수 - 사망자 수)는 -6,175명"
- `https://img.segye.com/newsView/20250924517492` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m-fr.yna.co.kr/view/AFR20250924002400884` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://science.ytn.co.kr/program/view.php?mcd=0082&key=202509241615074882` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [related_series] 2026 monthly birth registrations or provisional births for April–June 2026

Hypothesis: If April–June 2026 birth counts are available, they would show whether the strong Q1 2026 upswing (p11, p12) persisted into the second quarter, which is the immediate precursor to July 2026. This would materially narrow the y/y growth factor used in the main route.

Queries issued by the searcher: KOSTAT monthly birth statistics May 2026 출생아 수; 인구동향 2026년 5월 출생아 수 통계청; 2026년 6월 인구동향 출생아 수 국가데이터처; 2025년 7월 출생아 수 인구동향 2만명

- `https://mods.go.kr/board.es?mid=a10301020100&bid=204&act=view&list_no=446225&tag=&nPage=1&ref_bid=203,204,205,206,207&keyField=T&keyWord=` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.news1.kr/economy/trend/6242343` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?mid=a10301010000&bid=204&act=view&list_no=446612` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.edaily.co.kr/News/Read?newsId=03552246645551256` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [forecasts_markets] Published 2026 South Korea birth forecasts or targets

Hypothesis: A credible 2026 annual birth forecast (from KOSTAT, research institutes, or international bodies) would provide an independent check on the level implied by the y/y growth route and help calibrate the assumption about whether the 2026 upswing continues through July.

Queries issued by the searcher: Statistics Korea 2026 birth forecast total live births projection; 한국 2026년 출생아 수 전망 통계청 인구동향; 장래인구추계 2022~2072 OECD 평균 시나리오 2026년 출생아 29만5000명; KIHASA 한국보건사회연구원 2026년 출생아 수 전망

- `https://www.etoday.co.kr/news/view/2610060` -> **snapshot** (snapshot 20260803022708); points raw/verified 15/8
  - p33 South Korea cumulative live births, January–May 2026, year-on-year growth rate = **15.2** % (2026-01-01..2026-05-31) [EXCLUDED (ablation): ] quote: "올해 1~5월 누계 출생아 수는 전년 동기보다 15.2% 늘었다."
  - p34 South Korea total fertility rate, January 2026 = **0.99** persons (children per woman) (2026-01-01..2026-01-31) [EXCLUDED (ablation): ] quote: "합계출산율은 1월 0.99명, 2월 0.93명, 3월 0.93명, 4월 0.93명, 5월 0.85명을 기록했다."
  - p35 South Korea total fertility rate, February 2026 = **0.93** persons (children per woman) (2026-02-01..2026-02-28) [EXCLUDED (ablation): ] quote: "합계출산율은 1월 0.99명, 2월 0.93명, 3월 0.93명, 4월 0.93명, 5월 0.85명을 기록했다."
  - p36 South Korea total fertility rate, March 2026 = **0.93** persons (children per woman) (2026-03-01..2026-03-31) [EXCLUDED (ablation): ] quote: "합계출산율은 1월 0.99명, 2월 0.93명, 3월 0.93명, 4월 0.93명, 5월 0.85명을 기록했다."
  - p37 South Korea total fertility rate, April 2026 = **0.93** persons (children per woman) (2026-04-01..2026-04-30) [EXCLUDED (ablation): ] quote: "합계출산율은 1월 0.99명, 2월 0.93명, 3월 0.93명, 4월 0.93명, 5월 0.85명을 기록했다."
  - p38 South Korea total fertility rate, May 2026 = **0.85** persons (children per woman) (2026-05-01..2026-05-31) [EXCLUDED (ablation): ] quote: "합계출산율은 1월 0.99명, 2월 0.93명, 3월 0.93명, 4월 0.93명, 5월 0.85명을 기록했다."
  - p39 South Korea total fertility rate, 2025 (actual) = **0.8** persons (children per woman) (2025-01-01..2025-12-31) [EXCLUDED (ablation): ] quote: "지난해 합계출산율(0.80명)은 데이터처의 '2022~2072년 장래인구추계'에 제시된 고위 가정(0.75명)을 넘어섰다."
  - p40 South Korea 2022–2072 future population projection high-assumption total fertili = **0.75** persons (children per woman) (2025-01-01..2025-12-31) [EXCLUDED (ablation): ] quote: "지난해 합계출산율(0.80명)은 데이터처의 '2022~2072년 장래인구추계'에 제시된 고위 가정(0.75명)을 넘어섰다."
- `https://www.yna.co.kr/view/AKR20260801045700002` -> **snapshot** (snapshot 20260803065725); points raw/verified 15/11
  - p41 South Korea Q1 2026 total fertility rate (합계출산율) = **0.95** children per woman (2026-01-01..2026-03-31) [keep: ] quote: "올해 1분기 합계출산율은 0.95명, 4월과 5월은 각각 0.93명, 0.85명으로 집계됐다."
  - p42 South Korea April 2026 total fertility rate (합계출산율) = **0.93** children per woman (2026-04-01..2026-04-30) [keep: ] quote: "올해 1분기 합계출산율은 0.95명, 4월과 5월은 각각 0.93명, 0.85명으로 집계됐다."
  - p43 South Korea May 2026 total fertility rate (합계출산율) = **0.85** children per woman (2026-05-01..2026-05-31) [keep: ] quote: "올해 1분기 합계출산율은 0.95명, 4월과 5월은 각각 0.93명, 0.85명으로 집계됐다."
  - p44 South Korea annual total fertility rate in 2019 = **0.92** children per woman (2019-01-01..2019-12-31) [DISCARD: TFR in 2019 is historical context only; not a direct input for July 2026 births.] quote: "올해 합계출산율이 0.9명대를 기록한다면 이는 2019년(0.92명) 이후 7년 만에 처음이다."
  - p45 South Korea annual total fertility rate in 2000 = **1.48** children per woman (2000-01-01..2000-12-31) [DISCARD: TFR in 2000 is too distant to inform July 2026 births; no usable bridge.] quote: "2000년 1.48명 수준이었던 합계출산율은 꾸준히 감소해 2017년 1.05명까지 떨어졌고, 2018년(0.98명)부터는 1.0명을 하회했다."
  - p46 South Korea annual total fertility rate in 2017 = **1.05** children per woman (2017-01-01..2017-12-31) [DISCARD: TFR in 2017 is too distant to inform July 2026 births; no usable bridge.] quote: "2000년 1.48명 수준이었던 합계출산율은 꾸준히 감소해 2017년 1.05명까지 떨어졌고, 2018년(0.98명)부터는 1.0명을 하회했다."
  - p47 South Korea annual total fertility rate in 2018 = **0.98** children per woman (2018-01-01..2018-12-31) [DISCARD: TFR in 2018 is too distant to inform July 2026 births; no usable bridge.] quote: "2000년 1.48명 수준이었던 합계출산율은 꾸준히 감소해 2017년 1.05명까지 떨어졌고, 2018년(0.98명)부터는 1.0명을 하회했다."
  - p48 South Korea annual total fertility rate in 2023 (record low) = **0.72** children per woman (2023-01-01..2023-12-31) [DISCARD: TFR in 2023 is historical context only; superseded by more recent 2024–2026 values and not a direct input.] quote: "2023년 0.72명으로 역대 최저 수준을 기록한 뒤 2024년(0.75명) 반등해 2025년(0.80명)까지 2년 연속 늘었다."
  - p49 South Korea annual total fertility rate in 2024 = **0.75** children per woman (2024-01-01..2024-12-31) [DISCARD: TFR in 2024 is historical context only; superseded by 2025 and 2026 values and not a direct input.] quote: "2023년 0.72명으로 역대 최저 수준을 기록한 뒤 2024년(0.75명) 반등해 2025년(0.80명)까지 2년 연속 늘었다."
  - p50 South Korea annual total fertility rate in 2025 = **0.8** children per woman (2025-01-01..2025-12-31) [keep: ] quote: "2023년 0.72명으로 역대 최저 수준을 기록한 뒤 2024년(0.75명) 반등해 2025년(0.80명)까지 2년 연속 늘었다."
  - p51 Year-on-year growth rate of cumulative live births January–May 2026 vs same peri = **15.2** % (2026-01-01..2026-05-31) [keep: ] quote: "올해 1∼5월까지 누적 출생아는 12만2천694명으로 집계됐다. 1년 전과 비교하면 15.2% 늘었다."
- `https://www.wowtv.co.kr/NewsCenter/News/Read?articleId=2026072938541` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://sri.kostat.go.kr/boardDownload.es?bid=207&list_no=428476&seq=6` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 11 (period_end 2026-12-31 after as_of: 3; number: unknown scale word '만': 1; number: more than one number in value_as_written: 6; period_end 2031-12-31 after as_of: 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['south korea births', 'korea birth july', 'kostat births']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p10', 'p11', 'p12'] All three point to a strong 2026 birth upswing: registered pregnant women up ~16% (Apr 2025–Mar 2026), Q1 2026 birth registrations up ~15%, and January 2026 live births up 11.7% y/y. They share a broa
- corroborating: ['p5', 'p6'] p5 and p6 are the same July 2025 marriage statistic (20,394 marriages, +8.4% y/y) from the same KOSTAT release; they are redundant copies of one measurement, not independent evidence.
- corroborating: ['p7', 'p8'] p7 and p8 are the same July 2025 divorce statistic (7,826 divorces, -1.4% y/y) from the same KOSTAT release; redundant copies of one measurement.
- corroborating: ['p14', 'p15', 'p20', 'p21', 'p22'] All are 2025 fertility characteristics from the same JETRO summary of KOSTAT vital statistics: TFR 0.80 (+0.05), ASFR for women 35 up 13%, mean age at childbirth 33.8, mean age at first childbirth 33.
- contextual: ['p4'] July 2025 deaths (-0.7% y/y) is a mortality statistic from the same KOSTAT monthly release. It does not directly constrain July 2026 births but confirms the release format and period coverage.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p11', 'p12', 'p51'] All three describe the same underlying KOSTAT registration/vital-statistics upswing in 2026: Q1 registrations +15%, January live births +11.7%, and cumulative Jan–May live births +15.2%. They are mutu
- corroborating: ['p10', 'p11', 'p12', 'p51'] The 16% rise in registered pregnant women over Apr 2025–Mar 2026 is a leading indicator consistent with the 11–15% birth increases observed in early 2026. It supports continuation of elevated births i
- corroborating: ['p41', 'p42', 'p43'] Q1 2026 TFR 0.95, April 0.93, and May 0.85 are from the same Yonhap report and the same KOSTAT monthly series. They show a declining path within 2026 but remain above 2025 levels, consistent with the 
- corroborating: ['p14', 'p15', 'p50'] 2025 TFR of 0.80 and the +0.05 point increase are reported identically by JETRO and Yonhap, reflecting the same KOSTAT annual release. They corroborate the 2025 baseline but are not independent source
- corroborating: ['p44', 'p45', 'p46', 'p47', 'p48', 'p49', 'p50'] These annual TFR values from the same Yonhap article form a consistent historical series (2000: 1.48, 2017: 1.05, 2018: 0.98, 2023: 0.72, 2024: 0.75, 2025: 0.80) and provide context for the 2026 level
- corroborating: ['p5', 'p6', 'p28', 'p29'] Marriages in July 2025 (20,394) and the +8.4% y/y change are duplicated across p5/p6 and p28/p29 from the same MODS release. They are redundant copies, not independent confirmations.
- corroborating: ['p7', 'p8', 'p30', 'p31'] Divorces in July 2025 (7,826) and the -1.4% y/y change are duplicated across p7/p8 and p30/p31 from the same MODS release. Redundant copies.
- corroborating: ['p4', 'p27'] Deaths in July 2025 and the +0.7% y/y change are duplicated across p4 and p27 from the same MODS release. Redundant copies.
- corroborating: ['p20', 'p21', 'p22'] Age-specific fertility increase for women aged 35 (+13%), mean age at childbirth (33.8), and mean age at first childbirth (33.2) are from the same JETRO report on 2025 fertility. They describe the sam

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | Ratio of July 2026 live births to July 2025 live births | 1.12 | 1.05..1.2 | 0.7937..1.587 (widened) | ratio | m1 (m1) | The 2026 upswing is documented by p51 (Jan–May cumulative live births +15.2% y/y), p12 (January +11.7%), p11 (Q1 registrations +15%), and p10 (registered pregnant women +16%). Monthly TFR fell from 0.95 in Q1 to 0.93 in April and 0.85 in May (p41–p43), suggesting moderation by July. A central ratio  | July 2026 y/y growth follows the observed 2026 pattern but moderates from the Q1 peak, consistent with the April–May TFR decline. | Evidence that June or July 2026 births fell back to or below 2025 levels, or that the Q1 surge was a one-off registration-timing artifact rather than a real birth increase. |
| a2 | Ratio of July 2025 live births to the 2025 annual average monthly live births | 1 | 0.9..1.1 | 0.7036..1.407 (widened) | ratio | m1 (m1) | July is typically near the annual average in South Korea's birth seasonality, but the exact July 2025 level is not in the kept data. This dimensionless seasonal factor converts the 2025 annual average monthly level (derived from p51's Jan–May 2026 cumulative and the y/y growth) into a July 2025 leve | Used to convert the 2025 annual average monthly birth level into a July 2025 level before applying the y/y growth ratio. | Publication of actual July 2025 live births showing a seasonal factor outside 0.9–1.1. |

## Ablation: no own history (--ablate-own-history)

- own_history candidate directions dropped: ['c1']
- own_history extra directions dropped: []
- entity anchors from the pinned target: ['korea']; quantity stems: ['birth', 'live', 'perso']
- points excluded before the judge: 22 of 51
- methods allowed: ['formula_mc']

  - p1 South Korea live births, July 2025 (monthly Population Trends) = 21,803 (2025-07-31): ablation: name refers to the target entity ['korea'] and quantity
  - p2 South Korea live births year-on-year change rate, July 2025 = 5.9 (2025-07-31): ablation: name refers to the target entity ['korea'] and quantity
  - p3 South Korea deaths, July 2025 (monthly Population Trends) = 27,979 (2025-07-31): ablation: name refers to the target entity ['korea'] and quantity
  - p9 South Korea natural increase (live births minus deaths), July 2025 = -6,175 (2025-07-31): ablation: name refers to the target entity ['korea'] and quantity
  - p13 South Korea year-on-year percentage increase in live births in 2025 = 6.8 (2025-12-31): ablation: name refers to the target entity ['korea'] and quantity
  - p16 South Korea age-specific fertility rate, women aged 30-34, 2025 (births per 1,000 women) = 73.2 (2025-12-31): ablation: name refers to the target entity ['korea'] and quantity
  - p17 South Korea age-specific fertility rate, women aged 35-39, 2025 (births per 1,000 women) = 52 (2025-12-31): ablation: name refers to the target entity ['korea'] and quantity
  - p18 South Korea age-specific fertility rate, women aged 25-29, 2025 (births per 1,000 women) = 21.3 (2025-12-31): ablation: name refers to the target entity ['korea'] and quantity
  - p19 South Korea year-on-year increase in age-specific fertility rate, women aged 35-39, 2025 ( = 6 (2025-12-31): ablation: name refers to the target entity ['korea'] and quantity
  - p23 South Korea share of first births in total live births, 2025 = 62.4 (2025-12-31): ablation: name refers to the target entity ['korea'] and quantity
  - p24 South Korea live births, July 2025 (monthly Population Trends) = 21,803 (2025-07-31): ablation: name refers to the target entity ['korea'] and quantity
  - p25 South Korea live births, July 2025, year-over-year change (percent) = 5.9 (2025-07-31): ablation: name refers to the target entity ['korea'] and quantity
  - p26 South Korea deaths, July 2025 (monthly Population Trends) = 27,979 (2025-07-31): ablation: name refers to the target entity ['korea'] and quantity
  - p32 South Korea natural increase (live births minus deaths), July 2025 = -6,175 (2025-07-31): ablation: name refers to the target entity ['korea'] and quantity
  - p33 South Korea cumulative live births, January–May 2026, year-on-year growth rate = 15.2 (2026-05-31): ablation: name refers to the target entity ['korea'] and quantity
  - p34 South Korea total fertility rate, January 2026 = 0.99 (2026-01-31): ablation: name refers to the target entity ['korea'] and quantity
  - p35 South Korea total fertility rate, February 2026 = 0.93 (2026-02-28): ablation: name refers to the target entity ['korea'] and quantity
  - p36 South Korea total fertility rate, March 2026 = 0.93 (2026-03-31): ablation: name refers to the target entity ['korea'] and quantity
  - p37 South Korea total fertility rate, April 2026 = 0.93 (2026-04-30): ablation: name refers to the target entity ['korea'] and quantity
  - p38 South Korea total fertility rate, May 2026 = 0.85 (2026-05-31): ablation: name refers to the target entity ['korea'] and quantity
  - p39 South Korea total fertility rate, 2025 (actual) = 0.8 (2025-12-31): ablation: name refers to the target entity ['korea'] and quantity
  - p40 South Korea 2022–2072 future population projection high-assumption total fertility rate fo = 0.75 (2025-12-31): ablation: name refers to the target entity ['korea'] and quantity

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 0.1513 | ['p51'] / ['a1', 'a2'] | [] |  | 1.00 | equal |  |

Result: central **0.1513**, 80% interval [0.1024, 0.2234], basis monte_carlo, weight rule equal, weight on methods that use assumptions 1.00

## Final answer

The best computed estimate for live births occurring in South Korea during July 2026, as it will first be reported by Statistics Korea's monthly Population Trends release, is 0.1513 persons. The model-based 80% interval is 0.1024 to 0.2234, conditional on the stated assumptions rather than a demonstrated accuracy guarantee.

The estimate rests on one observed point, 10 kept data point: January–May 2026 cumulative live births. Dividing by the [n] year-over-year growth ratio recovers the [n] cumulative level; dividing by five gives the [n] monthly average; multiplying by the July seasonal factor and then the July 2026 year-over-year ratio yields July 2026. The July 2026/July 2025 ratio (1.12, range 0.7937–1.587) and the July seasonal factor (1, range 0.7036–1.407) are analyst assumptions, not observations. The single method carries weight 100%.

The main risk is that the [n] upswing moderates by July, so the assumed ratio is too high. Actual July 2025 monthly births and recent monthly registration data would most improve the estimate.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 Ratio of July 2026 live births to July 2025 live births: 1.12 ratio, range 0.7937 to 1.587 (range widened by code); used by m1. Overturned by: Evidence that June or July 2026 births fell back to or below [n] levels, or that the Q[n] surge was a one-off registration-timing artifact rather than a real birth increase.
- a2 Ratio of July 2025 live births to the [n] annual average monthly live births: 1 ratio, range 0.7036 to 1.407 (range widened by code); used by m1. Overturned by: Publication of actual July 2025 live births showing a seasonal factor outside [n]–[n].

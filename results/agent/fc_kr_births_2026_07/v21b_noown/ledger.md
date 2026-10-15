# Evidence ledger: fc_kr_births_2026_07

- Question: Assume today is 2026-08-23. You know nothing published after this date. Estimate the number of live births in South Korea in July 2026, as it will be first reported in the national statistics agency's monthly Population Trends release.
- as_of: 2026-08-23
- Pinned target: Number of live births occurring in South Korea during July 2026, as first reported in the national statistics agency's monthly Population Trends release | unit live births (persons) | period 2026-07-01..2026-07-31 | publisher Statistics Korea (KOSTAT), Monthly Population Trends (인구동향)

- Official value (scoring only, never shown to the agent): 24,275

## Directions and pages

### d1 [related_series] Population registration and resident registration data

Hypothesis: Monthly birth counts from KOSTAT are closely correlated with birth registrations in the resident registration system, though with a lag. If July 2026 registration data are available (e.g., from Ministry of Interior and Safety), they can serve as a leading indicator or cross-check for the KOSTAT figure.

Queries issued by the searcher: 주민등록 출생신고 2026년 7월; South Korea birth registration statistics July 2026 resident registration; 행정안전부 주민등록 인구통계 출생신고 2026년 7월 출생자 수; 2026년 6월 인구동향 출생아 수 발표; 주민등록 인구통계 출생등록 2026년 6월 전국 출생아; 행정안전부 주민등록 출생신고 코스타 출생아 수 차이 비율

- `https://nowon.kr/dong/user/bbs/BD_selectBbs.do?q_bbsCode=1042&q_bbscttSn=20260804170322638` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ongjin.go.kr/open_content/main/peti/petiDetail.do?seq=810&pgno=5` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.yangcheon.go.kr/site/yangcheon/ex/seol/seolContentDeailView.do?not_ancmt_mgt_no=47438` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.osan.go.kr/portal/contents.do?mId=0102130000` -> **snapshot** (snapshot 20260408223852); points raw/verified 0/0

### d2 [base_rates] Seasonality and trend decomposition

Hypothesis: The monthly birth series exhibits seasonality (e.g., higher births in certain months) and a long-term downward trend. A seasonal index and trend can be estimated from historical data to project July 2026 from a recent 12-month total or year-to-date total.

Queries issued by the searcher: South Korea monthly live births 2025 Statistics Korea monthly population trends; 월별 출생아 수 2021 2022 2023 2024 2025 통계청 인구동향; 2026년 6월 인구동향 출생아 수 상반기 누계; 2026년 5월 인구동향 출생아 수 통계청

- `https://www.yna.co.kr/view/PYH20260826116300013` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.korea.kr/common/download.do?fileId=198368729` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://nsp.nanet.go.kr/trend/latest/detail.do?latestTrendControlNo=TREN0000003532` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://namu.wiki/w/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD/%EC%B6%9C%EC%82%B0%EC%9C%A8/%EC%83%81%EC%84%B8%20%ED%86%B5%EA%B3%84` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d3 [related_series] Hospital and health insurance claims for deliveries

Hypothesis: The number of live births is strongly related to the number of delivery-related hospital admissions or health insurance claims for childbirth. National Health Insurance Service (NHIS) data on delivery claims can provide an independent estimate, adjusted for multiple births and coverage.

Queries issued by the searcher: 건강보험 분만 청구 2026년 월별; NHIS delivery claims South Korea monthly statistics; 국민건강보험공단 분만실적 월별 분만건수 2025; Statistics Korea Monthly Population Trends July 2026 live births; 인구동향 2026년 7월 출생아 수

- `https://www.nhis.or.kr/_custom/nhis/_common/board/index/725.do?mode=download&articleNo=11008252&attachNo=365025` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://kha.or.kr/kha_home/notice_list.do?mode=download&articleNo=46661&attachNo=424913` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.bokjiro.go.kr/ssis-tem/cms/mob/common/download/2026%20%EB%82%98%EC%97%90%EA%B2%8C%20%ED%9E%98%EC%9D%B4%20%EB%90%98%EB%8A%94%20%EB%B3%B5%EC%A` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://workingmom.or.kr/wp-content/plugins/bbang-cpboard/lib/download.php?att_id=29710` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d4 [forecasts_markets] Official projections and expert forecasts

Hypothesis: Statistics Korea or other institutions may publish monthly or quarterly birth projections that include July 2026. These can serve as a direct estimate or a benchmark.

Queries issued by the searcher: Statistics Korea birth projection 2026 monthly live births; 장래인구추계 2026 출생아 수 전망; South Korea monthly birth forecast 2026 KOSTAT 인구동향; 한국은행 출생아 수 전망 2026

- `https://chosun-chosun-prod.cdn.arcpublishing.com/economy/economy_general/2026/09/23/4336WE6G4BBALOXOVOQM7RBNKE/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://namu.wiki/w/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD/%EC%B6%9C%EC%82%B0%EC%9C%A8/%EC%83%81%EC%84%B8%20%ED%86%B5%EA%B3%84` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://m.etoday.co.kr/news/view/2610060?trc=m_main_top_sub` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.newsworks.co.kr/news/articleView.html?idxno=848723` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d5 [related_series] Marriage and fertility intentions

Hypothesis: Births in July 2026 are largely determined by conceptions around October 2025, which may correlate with marriage counts and fertility intentions. Marriage data from late 2025 and early 2026 can provide a leading indicator.

Queries issued by the searcher: South Korea monthly marriage statistics 2025 KOSTAT 혼인건수; Statistics Korea Monthly Population Trends 2026 births marriage; 2025년 월별 혼인건수 10월 11월 12월 인구동향; 2026년 6월 인구동향 출생아 수 혼인건수 국가데이터처

- `https://www.etoday.co.kr/news/view/2550201?trc=sub_list_news` -> **snapshot** (snapshot 20260210001709); points raw/verified 15/11
  - p1 Year-on-year growth rate of South Korea live births in November 2025 = **3.1** % (2025-11-01..2025-11-30) [EXCLUDED (ablation): ] quote: "지난해 11월 출생아 수가 2만710명으로 전년 동월보다 3.1% 증가했다고 밝혔다."
  - p2 Year-on-year growth rate of South Korea live births in October 2025 = **2.5** % (2025-10-01..2025-10-31) [EXCLUDED (ablation): ] quote: "10월에는 2024년 6월 이후 16개월 만에 가장 낮은 증가율(2.5%)을 기록했고"
  - p3 Year-on-year growth rate of South Korea marriages in November 2025 = **2.7** % (2025-11-01..2025-11-30) [keep: ] quote: "11월 혼인 건수는 1만9079건으로 전년 동월보다 2.7% 증가했다."
  - p4 Year-on-year growth rate of South Korea marriages in October 2025 = **0.2** % (2025-10-01..2025-10-31) [keep: ] quote: "10월에는 증가율(0.2%)이 2024년 3월 이후 19개월 만에 최저치를 기록했고"
  - p5 South Korea annual total fertility rate forecast for 2025 (lower bound) = **0.78** children per woman (total fertility rate) (2025-01-01..2025-12-31) [DISCARD: Annual TFR forecast lower bound; TFR is a period fertility intensity measure, not a monthly birth count, and the target ] quote: "연간 합계출산율은 0.78~0.80명을 기록할 것으로 보인다."
  - p6 South Korea annual total fertility rate forecast for 2025 (upper bound) = **0.8** children per woman (total fertility rate) (2025-01-01..2025-12-31) [DISCARD: Annual TFR forecast upper bound; same ineligibility as p5. Redundant with p5 as the other endpoint of the same forecast.] quote: "연간 합계출산율은 0.78~0.80명을 기록할 것으로 보인다."
  - p7 South Korea annual live births threshold expected to be exceeded in 2025 (250 th = **25** live births (persons) (2025-01-01..2025-12-31) [EXCLUDED (ablation): ] quote: "12월 출생아가 전년 수준만 기록해도 연간 출생아 수는 2021년 이후 4년 만에 25만 명을 넘어서게 된다."
  - p8 Year-on-year growth rate of cumulative live births in Seoul, January–November 20 = **8.7** % (2025-01-01..2025-11-30) [keep: ] quote: "서울은 8.7%, 인천은 8.4%, 경기는 6.8% 늘었으나"
  - p9 Year-on-year growth rate of cumulative live births in Incheon, January–November  = **8.4** % (2025-01-01..2025-11-30) [keep: ] quote: "서울은 8.7%, 인천은 8.4%, 경기는 6.8% 늘었으나"
  - p10 Year-on-year growth rate of cumulative live births in Gyeonggi, January–November = **6.8** % (2025-01-01..2025-11-30) [keep: ] quote: "서울은 8.7%, 인천은 8.4%, 경기는 6.8% 늘었으나"
  - p11 Year-on-year growth rate of cumulative marriages in Seoul, January–November 2025 = **15.8** % (2025-01-01..2025-11-30) [keep: ] quote: "1~11월 누계로는 서울에서 15.8%, 경기에서 8.1% 늘었지만"
- `https://chosun-chosun-prod.cdn.arcpublishing.com/economy/economy_general/2026/04/22/DMBJ2HALXRADPCZV3ZFUGFIKXQ/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://en.sedaily.com/finance/2026/06/24/koreas-birth-rate-rises-to-093-but-population-shrinks-for` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mhdata.or.kr/mailing/Numbers325_260303_B1_Part.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- dropped by code checks: 4 (number: more than one number in value_as_written: 4)

### d6 [physical_flow] Obstetric service utilization

Hypothesis: Births can be estimated from the capacity and utilization of obstetric wards: number of obstetric beds, average length of stay, and occupancy rates. This route requires assumptions about the share of births in hospitals versus other settings, but can provide a lower-bound check.

Queries issued by the searcher: South Korea obstetric beds occupancy rate 2025 분만실 병상 가동률; OECD obstetric beds Korea per 1000 births; OECD health at a glance Korea length of stay normal delivery days; 산부인과 병상 가동률 2025 분만 병상 평균 재원일수 제왕절개 자연분만

- `https://www.hkn24.com/news/articleView.html?idxno=345602` -> **snapshot** (snapshot 20250724174330); points raw/verified 15/13
  - p12 South Korea newborn nursery beds, Q1 2021 = **6,925** beds (2021-01-01..2021-03-31) [keep: ] quote: "신생아실의 경우, 병상수는 2021년 6925개에서 2025년 6292개로 9.1%(633개) 줄었고"
  - p13 South Korea newborn nursery beds, Q1 2025 = **6,292** beds (2025-01-01..2025-03-31) [keep: ] quote: "신생아실의 경우, 병상수는 2021년 6925개에서 2025년 6292개로 9.1%(633개) 줄었고"
  - p14 South Korea newborn nursery rooms, Q1 2021 = **656** rooms (2021-01-01..2021-03-31) [keep: ] quote: "병실 수는 656실에서 538실로 18%(118실) 감소했다."
  - p15 South Korea newborn nursery rooms, Q1 2025 = **538** rooms (2025-01-01..2025-03-31) [keep: ] quote: "병실 수는 656실에서 538실로 18%(118실) 감소했다."
  - p16 South Korea delivery (분만) facility beds, Q1 2021 = **2,060** beds (2021-01-01..2021-03-31) [keep: ] quote: "같은 기간 분만 시설도 감소세를 보였다. 병상수는 2060개에서 1721개로 16.5%(339개)"
  - p17 South Korea delivery (분만) facility beds, Q1 2025 = **1,721** beds (2025-01-01..2025-03-31) [keep: ] quote: "병상수는 2060개에서 1721개로 16.5%(339개), 병실 수는 1328실에서 1176실로 11.5%(152실) 줄었다."
  - p18 South Korea delivery (분만) facility rooms, Q1 2021 = **1,328** rooms (2021-01-01..2021-03-31) [keep: ] quote: "병실 수는 1328실에서 1176실로 11.5%(152실) 줄었다."
  - p19 South Korea delivery (분만) facility rooms, Q1 2025 = **1,176** rooms (2025-01-01..2025-03-31) [keep: ] quote: "병실 수는 1328실에서 1176실로 11.5%(152실) 줄었다."
  - p20 South Korea mother-and-baby rooming-in (모자동실) rooms, 2021 = **268** rooms (2021-01-01..2021-12-31) [DISCARD: Mother-and-baby rooming-in rooms are a post-delivery amenity count, not a delivery-capacity measure; no defensible conve] quote: "모자동실은 2021년 268개에서 2025년 251개로 6.3%(17개) 줄었다."
  - p21 South Korea mother-and-baby rooming-in (모자동실) rooms, 2025 = **251** rooms (2025-01-01..2025-12-31) [DISCARD: Mother-and-baby rooming-in rooms (2025); same ineligibility as p20.] quote: "모자동실은 2021년 268개에서 2025년 251개로 6.3%(17개) 줄었다."
  - p22 South Korea operating room beds, Q1 2021 = **8,751** beds (2021-01-01..2021-03-31) [DISCARD: Operating room beds are not delivery-specific capacity and have no defined conversion to births; irrelevant to the targe] quote: "수술실 병상수는 2021년 8751개에서 2025년 9151개로 약 4.6%(400개)"
  - p23 South Korea operating room beds, Q1 2025 = **9,151** beds (2025-01-01..2025-03-31) [DISCARD: Operating room beds (2025) are not delivery-specific capacity; irrelevant to the target.] quote: "수술실 병상수는 2021년 8751개에서 2025년 9151개로 약 4.6%(400개)"
  - p24 South Korea emergency room beds, Q1 2021 = **8,948** beds (2021-01-01..2021-03-31) [DISCARD: Emergency room beds are not delivery-specific capacity; irrelevant to the target.] quote: "응급실의 병상수는 8948개에서 8938개로 거의 변화가 없었지만"
- `https://mhlw-grants.niph.go.jp/system/files/download_pdf/2022/202205006B.pdf` -> **dropped** (binary file type not supported in MVP); points raw/verified -/-
- `https://hnews.kr/news/view.php?no=66910` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.medicalworldnews.co.kr/news/view.php?idx=1510969077` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 2 (number: more than one number in value_as_written: 2)

### d7 [shocks] Policy and calendar effects

Hypothesis: Recent policy changes (e.g., parental benefits, housing support) or calendar effects (e.g., number of weekends, holidays) may have influenced births in July 2026. Quantifying these effects can adjust a baseline estimate.

Queries issued by the searcher: Statistics Korea monthly population trends July 2026 live births; South Korea births 2026 policy parental benefits housing support; 2026년 5월 인구동향 출생아 수 통계청; 2026년 7월 달력 공휴일 주말 일수

- `https://www.gov.kr/portal/ntnadmNews/4866340?srchOrgCd=1241000&pageIndex=1&hideurl=N` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://admin.korea.kr/briefing/pressReleaseView.do?newsId=156783095&pWise=mSub&pWiseSub=C3` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.kbs.co.kr/news/pc/view/view.do?ncd=8670306` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://busan.fnnews.com/news/202609231201183232` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b1 [related_series] d1

Hypothesis: Monthly resident-registration birth counts (Ministry of Interior and Safety 주민등록 인구통계) for June and July 2026 would provide a near-contemporaneous level and year-on-year change for the target month, anchoring the level that the KOSTAT occurrence-based series should land near after allowing for the registration lag. This is the single most valuable missing input because it converts the whole estimate from a growth-rate extrapolation into a level-plus-adjustment calculation.

Queries issued by the searcher: 주민등록 인구통계 월별 출생자 수 2026년 7월; 행정안전부 주민등록 인구통계 2026년 6월 출생아 수; 주민등록 인구통계 2026년 7월 출생 24,000명 월간; 행정안전부 주민등록 인구통계 2026년 7월말 출생아 등록

- `https://mods.go.kr/board.es?mid=a10301010000&bid=204&list_no=447111&act=view&mainXml=Y` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://mods.go.kr/board.es?act=view&bid=204&list_no=446612&mid=a10301020300` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.hani.co.kr/arti/economy/economy_general/1274698.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://gwangyang.go.kr/boardDownload.es?bid=0092&list_no=200423&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b2 [base_rates] d2

Hypothesis: A complete monthly KOSTAT live-birth series for 2024 and 2025 (levels, not just growth rates) would let us fit a level-plus-seasonal-plus-trend projection to July 2026 directly, replacing the need to chain a growth rate onto an assumed base level. It also supplies the July seasonal factor and the recent level that the current evidence lacks.

Queries issued by the searcher: KOSTAT monthly live births 2024 2025 인구동향 출생아 수; Statistics Korea Monthly Population Trends live births 2025 monthly series; 2026년 5월 인구동향 출생아 수 명; "2026년 6월 인구동향" 출생아 수; kosis DT_1B8000G 월별 출생아 수 2024 2025 인구동향 월간

- `https://kostat.go.kr/boardDownload.es?bid=11749&list_no=435971&seq=2` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.kostat.go.kr/boardDownload.es?bid=11749&list_no=439522&seq=3` -> **dropped** (unsupported content type application/pdf); points raw/verified -/-
- `https://mods.go.kr/boardDownload.es?bid=204&list_no=447111&seq=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.kostat.go.kr/boardDownload.es?bid=204&list_no=439018&seq=3` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### b3 [related_series] d3

Hypothesis: NHIS delivery-related health-insurance claim counts for July 2026 (or the latest available month) would give an independent, near-complete count of hospital deliveries, which can be scaled to live births using the hospital-delivery share and multiple-birth adjustment. This would resolve whether the marriage-led rebound is actually showing up in deliveries.

Queries issued by the searcher: 국민건강보험공단 분만 진료비 청구 통계 2026; 건강보험심사평가원 분만 건수 통계 월별 2026; 심평원 분만 통계 2026년 6월 분만 건수 월별; 보건의료빅데이터개방시스템 분만 통계 다운로드 시군구별 연령군별

- `https://www.donga.com/news/article/all/20260805/134422454/1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.medicaltimes.com/Users/News/NewsView.html?ID=11413` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.data.go.kr/data/15118813/fileData.do` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www.drshingangnamclinic.co.kr/page/cboard_view.asp?idx=1475&page=3&gu=2` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['south korea births', 'korea birth july', 'kostat births']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p3', 'p4'] Both are KOSTAT-derived monthly marriage growth rates for adjacent months (Oct and Nov 2025) from the same underlying registration series; they jointly indicate a modest but positive marriage uptick i
- corroborating: ['p8', 'p9', 'p10'] Seoul, Incheon and Gyeonggi cumulative Jan-Nov 2025 live-birth growth rates (8.7%, 8.4%, 6.8%) are all positive and mutually consistent, pointing to a genuine 2025 national birth rebound concentrated 
- corroborating: ['p11', 'p3', 'p4'] Seoul cumulative Jan-Nov 2025 marriage growth (+15.8%) is consistent in sign with the national monthly marriage increases in Oct-Nov 2025; both support the view that marriages were rising into the con
- corroborating: ['p5', 'p6'] Lower and upper bounds of the same 2025 TFR forecast (0.78-0.80); they are two endpoints of one forecast, not independent observations.
- corroborating: ['p12', 'p13', 'p14', 'p15', 'p16', 'p17', 'p18', 'p19', 'p20', 'p21'] All describe the same 2021-to-2025 contraction of obstetric/newborn inpatient capacity (newborn nursery beds/rooms, delivery beds/rooms, rooming-in rooms). They share one source and one measurement ba
- contextual: ['p22', 'p23', 'p24'] Operating-room and emergency-room bed counts are general hospital capacity indicators, not obstetric-specific; they show overall hospital capacity roughly flat and therefore do not corroborate or cont
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p3', 'p4'] Both are KOSTAT-derived marriage growth rates for adjacent months (Oct and Nov 2025) from the same source article; they jointly indicate a weak but positive marriage recovery in late 2025, which is th
- corroborating: ['p8', 'p9', 'p10'] Seoul, Incheon, and Gyeonggi cumulative live-birth growth rates for Jan–Nov 2025 are all positive and of similar magnitude (6.8–8.7%), from the same source. They corroborate a national-level birth inc
- corroborating: ['p11'] Seoul cumulative marriage growth (15.8%) is much stronger than the national monthly marriage growth rates in p3/p4, consistent with a marriage-led birth rebound concentrated in the capital region; it 
- corroborating: ['p5', 'p6'] Lower and upper bounds of the same 2025 TFR forecast (0.78–0.80); they are two endpoints of one forecast, not independent estimates. They provide context on the 2025 fertility level but do not directl
- corroborating: ['p12', 'p13', 'p14', 'p15', 'p16', 'p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24'] All are hospital-capacity counts from the same 2025-07-24 snapshot of one article. They consistently show declining obstetric/newborn capacity (delivery beds −16.5%, newborn nursery beds −9.1% from 20

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a8, at most 3 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | July 2026 national live-birth change factor relative to July 2025 | 1.05 | 0.95..1.16 | 0.9389..1.174 (widened) | ratio | unused | The conception window for July 2026 births is roughly October 2025. National marriage growth was weakly positive in Oct 2025 (p4, +0.2%) and Nov 2025 (p3, +2.7%), while regional cumulative live births in Jan–Nov 2025 rose 6.8–8.7% (p8, p9, p10), suggesting a modest national birth increase into 2026. | A July 2025 national monthly live-birth level is available as the base, and the marriage-led birth increase observed in late 2025 continues at a similar or slightly weaker pace into July 2026. | Evidence that national monthly live births in early 2026 turned negative year-on-year, or that the late-2025 marriage increase did not translate into a 2026 birth increase, would push the factor toward or below 1.0. |
| a2 | July 2026 national live-birth change factor relative to July 2025 (marriage-lag route) | 1.04 | 0.93..1.16 | 0.929..1.161 (widened) | ratio | unused | Same conception-window logic as a1 but anchored more directly on the marriage series: Oct 2025 marriages +0.2% (p4) and Nov 2025 +2.7% (p3), with Seoul cumulative marriages +15.8% (p11). Because national monthly marriage growth is much weaker than the regional cumulative figure, the central factor i | A July 2025 national monthly live-birth level is available and the marriage-to-birth lag of roughly 9 months holds for the Oct–Nov 2025 marriage cohort. | A breakdown in the historical marriage-to-birth relationship, or evidence that the 2025 marriage increase was concentrated in older or childless couples, would invalidate the transfer. |

Rejected by code:

- a3 July 2025 national monthly live-birth level: target-like: a level of the target quantity (unit or name matches the target, no ratio wording)
- a4 July 2025 national monthly live-birth level (marriage-lag route): target-like: a level of the target quantity (unit or name matches the target, no ratio wording)

## Ablation: no own history (--ablate-own-history)

- own_history candidate directions dropped: ['c1']
- own_history extra directions dropped: []
- entity anchors from the pinned target: ['korea']; quantity stems: ['birth', 'live', 'perso']
- points excluded before the judge: 3 of 24
- methods allowed: ['formula_mc']

  - p1 Year-on-year growth rate of South Korea live births in November 2025 = 3.1 (2025-11-30): ablation: name refers to the target entity ['korea'] and quantity
  - p2 Year-on-year growth rate of South Korea live births in October 2025 = 2.5 (2025-10-31): ablation: name refers to the target entity ['korea'] and quantity
  - p7 South Korea annual live births threshold expected to be exceeded in 2025 (250 thousand) = 25 (2025-12-31): ablation: name refers to the target entity ['korea'] and quantity

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | n/a |  | [] |  | 0.00 |  | input a: assumption a3 was rejected (target-like: a level of the target quantity (unit or name matches the target, no ratio wording)) |
| m2 | formula_mc | n/a |  | [] |  | 0.00 |  | input a: assumption a4 was rejected (target-like: a level of the target quantity (unit or name matches the target, no ratio wording)) |

Result: central **n/a**, 80% interval [n/a, n/a], basis no_method, weight rule None, weight on methods that use assumptions 0.00

## Final answer

No estimate: no estimation method could be computed from the verified evidence.

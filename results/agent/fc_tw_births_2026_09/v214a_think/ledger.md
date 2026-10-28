# Evidence ledger: fc_tw_births_2026_09

- Question: Assume today is 2026-09-08. You know nothing published after this date. Estimate the number of births registered in Taiwan in September 2026, as reported in the Ministry of the Interior's monthly household registration statistics.
- as_of: 2026-09-08
- Pinned target: Number of births registered in Taiwan during September 2026, as reported in the Ministry of the Interior's monthly household registration statistics; interpreted as the count of birth-registration events recorded by registration date during 2026-09-01 through 2026-09-30. | unit birth registration (person) | period 2026-09-01..2026-09-30 | publisher Ministry of the Interior, Taiwan (MOI), Department of Household Registration / MOI statistics

- Official value (scoring only, never shown to the agent): 7,704

## Directions and pages

### d1 [own_history] MOI monthly household-registration series

Hypothesis: September 2026 registered births can be projected from the recent level/trend in monthly birth registrations and the historical September seasonal factor; the same month in prior years and the latest months before the cutoff constrain the level.

Queries issued by the searcher: 內政部 戶政統計 出生登記數 每月 2026; 台灣 出生數 月別統計 2025 2026 內政部; 內政部 2025年9月 出生數 新生兒 較去年同期; 內政部戶政司 出生死亡及結婚離婚 月表 按登記日期 統計; 內政部 戶政統計 出生登記數 每月 2025 2026; 台灣 出生數 月別統計 2026年 內政部戶政司; 內政部戶政司 出生死亡及結離婚月表 按登記日期 統計; 2023年9月 出生數 台灣 新生兒 內政部 戶口統計 9月出生; 內政部 戶政統計 出生登記數 每月 2026; 台灣 出生數 月別 2025 2026 內政部; 2025年9月 出生數 內政部 戶口統計 新生兒 9月; 內政部戶政司 出生死亡及結離婚月表 按登記日期 ris.gov.tw 346

- `https://tools.vege.club/population/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://fwnews.com.tw/tag/%e6%96%b0%e7%94%9f%e5%85%92/page/2/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ris.gov.tw/app/portal/346` -> **snapshot** (snapshot 20260814192916); points raw/verified 0/0
- `https://news.pts.org.tw/article/821684` -> **snapshot** (snapshot 20260819203503); points raw/verified 15/15
  - p1 Taiwan monthly birth registrations, July 2026 = **7,906** birth registration (person) (2026-07-01..2026-07-31) [keep: ] quote: "7月單月出生人數為7906人,折合年粗出生率為4.01‰"
  - p2 Taiwan monthly birth registrations, May 2026 = **6,832** birth registration (person) (2026-05-01..2026-05-31) [keep: ] quote: "雖較5月的6832人、6月的7324人微幅成長"
  - p3 Taiwan monthly birth registrations, June 2026 = **7,324** birth registration (person) (2026-06-01..2026-06-30) [keep: ] quote: "雖較5月的6832人、6月的7324人微幅成長"
  - p4 Taiwan July 2026 births year-on-year change (count) = **1,033** birth registration (person) (2026-07-01..2026-07-31) [keep: ] quote: "但仍較去年同期減少1033人、減少幅度達11.56%"
  - p5 Taiwan July 2026 births year-on-year change (percent) = **11.56** % (2026-07-01..2026-07-31) [keep: ] quote: "但仍較去年同期減少1033人、減少幅度達11.56%"
  - p6 Taiwan July 2026 crude birth rate (annualised) = **4.01** birth registration (person) per 1000 person per year (2026-07-01..2026-07-31) [keep: ] quote: "7月單月出生人數為7906人,折合年粗出生率為4.01‰"
  - p7 Taiwan total population, end of July 2026 = **23,235,002** person (2026-07-31..2026-07-31) [keep: ] quote: "全台總人口降至2323萬5002人,為連續31個月出現人口負成長"
  - p8 Taiwan consecutive months of population decline through July 2026 = **31** month (2026-07-31..2026-07-31) [keep: ] quote: "是連續31個月出現人口負成長"
  - p9 Taiwan total population year-on-year change, July 2026 = **0.44** % (2026-07-01..2026-07-31) [keep: ] quote: "較比去(2025)年同期減少0.44%"
  - p10 Taiwan total population month-on-month change, July 2026 = **0.04** % (2026-07-01..2026-07-31) [keep: ] quote: "與6月相比則減少0.04%"
  - p11 Taiwan monthly deaths, July 2026 = **17,119** death (person) (2026-07-01..2026-07-31) [keep: ] quote: "至於7月死亡人數則為1萬7119人"
  - p12 Taiwan July 2026 crude death rate (annualised) = **8.67** death (person) per 1000 person per year (2026-07-01..2026-07-31) [keep: ] quote: "折合年粗死亡率為8.67‰"
  - p13 Taiwan deaths year-on-year change, July 2026 = **1.62** % (2026-07-01..2026-07-31) [keep: ] quote: "較去年同月增加1.62%,較上月增加4.77%"
  - p14 Taiwan deaths month-on-month change, July 2026 = **4.77** % (2026-07-01..2026-07-31) [keep: ] quote: "較去年同月增加1.62%,較上月增加4.77%"
  - p15 Taiwan marriages, July 2026 = **7,150** marriage (couple) (2026-07-01..2026-07-31) [keep: ] quote: "至於結婚對數,7月全台共有7150對,同婚占3.5%"
- `https://www.chinatimes.com/realtimenews/20260610002909-260407` -> **snapshot** (snapshot 20260622115614); points raw/verified 15/15
  - p16 Taiwan monthly birth registrations, May 2026 (民國115年5月) = **6,832** birth registration (person) (2026-05-01..2026-05-31) [DISCARD: Duplicate of p2 (same May 2026 births from another outlet).] quote: "115年5月出生數為6832人,約每6.5分鐘出生一個嬰兒"
  - p17 Taiwan monthly birth registrations, April 2026 (prior month) = **8,144** birth registration (person) (2026-04-01..2026-04-30) [keep: ] quote: "比4月新生兒8144人少了1312人"
  - p18 Change in Taiwan monthly births, May 2026 vs April 2026 = **1,312** birth registration (person) (2026-05-01..2026-05-31) [keep: ] quote: "較上月減少1312人"
  - p19 Taiwan lowest single-month births in 2026, February 2026 = **6,523** birth registration (person) (2026-02-01..2026-02-28) [DISCARD: Duplicate of p43 (February 2026 monthly births).] quote: "僅次於今年2月單月新生兒最低數6523人,創歷年次低"
  - p20 Change in Taiwan monthly births, May 2026 vs same month prior year = **1,601** birth registration (person) (2026-05-01..2026-05-31) [keep: ] quote: "較上年同月減少1,601人"
  - p21 Taiwan crude birth rate, annualised, May 2026 = **3.46** birth registration (person) per 1000 person per year (2026-05-01..2026-05-31) [keep: ] quote: "折合年粗出生率為千分之3.46"
  - p22 Minutes per birth implied for May 2026 = **6.5** minute per birth registration (person) (2026-05-01..2026-05-31) [keep: ] quote: "約每6.5分鐘出生一個嬰兒"
  - p23 Taiwan total population, end of May 2026 = **23,252,641** person (2026-05-31..2026-05-31) [keep: ] quote: "截至今年5月底為止,台灣總人口數為2325萬2641人"
  - p24 Taiwan total population change vs same month prior year, May 2026 = **102,829** person (2026-05-01..2026-05-31) [keep: ] quote: "與上年同月比較減少10萬2829人"
  - p25 Taiwan average daily population decrease, May 2026 = **282** person per day (2026-05-01..2026-05-31) [keep: ] quote: "平均每天減少281.72人"
  - p26 Taiwan total population change vs prior month, May 2026 = **9,903** person (2026-05-01..2026-05-31) [keep: ] quote: "與上月比較則減少9903人"
  - p27 Taiwan monthly deaths, May 2026 = **15,158** death (person) (2026-05-01..2026-05-31) [keep: ] quote: "5月死亡數為1萬5158人"
  - p28 Taiwan population aged 0-14, end of May 2026 = **2,642,980** person (2026-05-31..2026-05-31) [keep: ] quote: "0至14歲人口數為264萬2980人,占總人口比率11.37%"
  - p29 Taiwan population aged 15-64, end of May 2026 = **15,859,310** person (2026-05-31..2026-05-31) [keep: ] quote: "15至64歲人口數為1585萬9310人,占68.20%"
  - p30 Taiwan population aged 65 and over, end of May 2026 = **4,750,351** as written "4,75萬351", value check pending person (2026-05-31..2026-05-31) [keep: ] quote: "65歲以上人口數為4,75萬351人,占20.43%"
- `https://ocacnews.net/article/421847` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ocacnews.net/article/410298` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://j-media.tw/Article/Detail/37299` -> **snapshot** (snapshot 20260417185829); points raw/verified 15/15
  - p31 Taiwan annual births, 2016 = **208,440** birth registration (person) (2016-01-01..2016-12-31) [keep: ] quote: "從2016年的208,440人,到2025年的107,812人,台灣年度新生兒在十年之間幾近腰斬。"
  - p32 Taiwan annual births, 2025 = **107,812** birth registration (person) (2025-01-01..2025-12-31) [DISCARD: Duplicate of official annual 2025 births p97.] quote: "從2016年的208,440人,到2025年的107,812人,台灣年度新生兒在十年之間幾近腰斬。"
  - p33 Taiwan annual births, 2024 (Dragon year) = **134,856** birth registration (person) (2024-01-01..2024-12-31) [DISCARD: Duplicate of official annual 2024 births p98.] quote: "2024年受到「龍年效應」支撐,全年出生134,856人,年減僅0.5%"
  - p34 Taiwan births, January 2025 = **9,495** birth registration (person) (2025-01-01..2025-01-31) [DISCARD: Duplicate of p90 (January 2025 monthly births).] quote: "2025年1月出生9,495人,2月受農曆年效應拉抬至10,407人"
  - p35 Taiwan births, February 2025 = **10,407** birth registration (person) (2025-02-01..2025-02-28) [DISCARD: Duplicate of p91 (February 2025 monthly births).] quote: "2月受農曆年效應拉抬至10,407人,形成全年唯一高點"
  - p36 Taiwan births, March 2025 = **9,388** birth registration (person) (2025-03-01..2025-03-31) [DISCARD: Duplicate of p92 (March 2025 monthly births).] quote: "3月9,388人、4月8,684人、5月8,433人"
  - p37 Taiwan births, April 2025 = **8,684** birth registration (person) (2025-04-01..2025-04-30) [DISCARD: Duplicate of p93 (April 2025 monthly births).] quote: "3月9,388人、4月8,684人、5月8,433人"
  - p38 Taiwan births, May 2025 = **8,433** birth registration (person) (2025-05-01..2025-05-31) [DISCARD: Duplicate of p94 (May 2025 monthly births).] quote: "3月9,388人、4月8,684人、5月8,433人"
  - p39 Taiwan births, November 2025 = **7,946** birth registration (person) (2025-11-01..2025-11-30) [DISCARD: Duplicate of p88 (November 2025 monthly births).] quote: "進入下半年,11月更跌至7,946人,12月雖小幅回升至9,027人"
  - p40 Taiwan births, December 2025 = **9,027** birth registration (person) (2025-12-01..2025-12-31) [DISCARD: Duplicate of p89 (December 2025 monthly births).] quote: "11月更跌至7,946人,12月雖小幅回升至9,027人,全年月均出生人數約為8,984人"
  - p41 Taiwan average monthly births, 2025 = **8,984** birth registration (person) (2025-01-01..2025-12-31) [keep: ] quote: "12月雖小幅回升至9,027人,全年月均出生人數約為8,984人"
  - p42 Taiwan births, January 2026 = **8,723** birth registration (person) (2026-01-01..2026-01-31) [keep: ] quote: "進入2026年,趨勢沒有絲毫喘息。1月出生8,723人,與2025年同月相比年減8.1%"
  - p43 Taiwan births, February 2026 (record monthly low) = **6,523** birth registration (person) (2026-02-01..2026-02-28) [keep: ] quote: "2月份全國新生兒僅6,523人,首度跌破7,000人大關,創下台灣有史以來單月出生人數的最低紀錄。"
  - p44 Taiwan births, January-February 2026 cumulative = **15,246** birth registration (person) (2026-01-01..2026-02-28) [keep: ] quote: "即便如此,2026年前兩月合計僅15,246人,與2025年同期的19,902人相比"
  - p45 Taiwan births, January-February 2025 cumulative = **19,902** birth registration (person) (2025-01-01..2025-02-28) [keep: ] quote: "2026年前兩月合計僅15,246人,與2025年同期的19,902人相比,實質年減幅仍達23.4%"
- `https://www.chinatimes.com/cn/realtimenews/20251009002298-260410` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.163.com/dy/article/KV36R0PT055080L4.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.businessweekly.com.tw/focus/blog/3020868` -> **snapshot** (snapshot 20260412030843); points raw/verified 15/15
  - p46 Taiwan monthly birth registrations, February 2026 = **6,523** birth registration (person) (2026-02-01..2026-02-28) [DISCARD: Duplicate of p43 (February 2026 monthly births).] quote: "今年2月出生數為6523人,約每6.2分鐘出生一個嬰兒"
  - p47 Taiwan monthly birth registrations, January 2026 (implied by Feb level and month = **2,200** birth registration (person) (2026-01-01..2026-01-31) [DISCARD: Misparsed: 2,200 is the January-to-February decrease, not the January level.] quote: "2月新生兒共6523人,較1月少了2200人、大減25.2%"
  - p48 Taiwan month-on-month change in birth registrations, February 2026 vs January 20 = **25.2** % (2026-02-01..2026-02-28) [keep: ] quote: "較1月少了2200人、大減25.2%"
  - p49 Taiwan year-on-year change in birth registrations, February 2026 vs February 202 = **3,884** birth registration (person) (2026-02-01..2026-02-28) [keep: ] quote: "較1月減少2200人,也較去年同期減少3884人"
  - p50 Taiwan annual crude birth rate implied by February 2026 births = **3.65** births per 1,000 person per year (2026-02-01..2026-02-28) [keep: ] quote: "折合年粗出生率為千分之3.65"
  - p51 Taiwan monthly birth registrations, April 2025 (prior record low) = **8,684** birth registration (person) (2025-04-01..2025-04-30) [DISCARD: Duplicate of p93 (April 2025 monthly births).] quote: "繼去年4月新生兒8684人、5月8433人、11月7946人接連創下史上單月新低紀錄後"
  - p52 Taiwan monthly birth registrations, May 2025 (prior record low) = **8,433** birth registration (person) (2025-05-01..2025-05-31) [DISCARD: Duplicate of p94 (May 2025 monthly births).] quote: "繼去年4月新生兒8684人、5月8433人、11月7946人接連創下史上單月新低紀錄後"
  - p53 Taiwan monthly birth registrations, November 2025 (prior record low) = **7,946** birth registration (person) (2025-11-01..2025-11-30) [DISCARD: Duplicate of p88 (November 2025 monthly births).] quote: "繼去年4月新生兒8684人、5月8433人、11月7946人接連創下史上單月新低紀錄後"
  - p54 Taiwan total population, end of February 2026 = **23,280,273** person (2026-02-28..2026-02-28) [keep: ] quote: "截至民國115年2月底,台灣人口數為2328萬273人"
  - p55 Taiwan total population year-on-year decrease, February 2026 vs February 2025 = **104,341** person (2026-02-01..2026-02-28) [keep: ] quote: "與去年同期比較減少10萬4341人,平均每天減少285.87人"
  - p56 Taiwan average daily population decrease, February 2026 vs February 2025 = **286** person per day (2026-02-01..2026-02-28) [keep: ] quote: "平均每天減少285.87人"
  - p57 Taiwan deaths, February 2026 = **14,881** death (person) (2026-02-01..2026-02-28) [keep: ] quote: "2月死亡1萬4881人,平均約每2.7分鐘1人死亡"
  - p58 Taiwan natural population increase, February 2026 (births minus deaths) = **8,358** person (2026-02-01..2026-02-28) [keep: ] quote: "台灣2月人口自然增加為負8358人"
  - p59 Taiwan population aged 65 and over, end of February 2026 = **4,707,676** person (2026-02-28..2026-02-28) [keep: ] quote: "65歲以上人口數為470萬7676人,占20.22%"
  - p60 Taiwan population aged 0-14, end of February 2026 = **2,667,349** person (2026-02-28..2026-02-28) [keep: ] quote: "台灣0至14歲人口數為266萬7349人,占總人口比率11.46%"
- `https://hk.crntt.com/doc/1602/1/8/7/160218724.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-

### d2 [related_series] Annual total and year-to-date births

Hypothesis: September 2026 registrations equal an estimated 2026 annual registered-birth total multiplied by September's share of annual registrations; year-to-date 2026 data constrain the annual level.

Queries issued by the searcher: 台灣 2026年 1-8月 出生數 內政部 戶籍統計; 內政部 歷年 出生登記數 月別 統計 台灣; 內政部戶政司 115年7月 戶口統計 出生數 7906; 歷年 出生登記數 2020 2021 2022 2023 2024 2025 台灣 165249 153820 138986; 台灣 2026年1-8月 出生數 內政部 出生登記; 內政部 歷年 出生登記數 月別 統計; 2023年 台灣 出生數 13萬5千 內政部 全年 新生兒; 內政部戶政司 人口統計資料 出生登記數 按月 2022 2021; 台灣 2026年 1-8月 出生數 內政部 戶籍登記; 歷年 出生登記數 月別 統計 台灣 內政部; 內政部 115年7月 戶口統計 出生數 7906 前7月 新生兒; 內政部戶政司 戶口統計 出生 死亡 按月 統計表 114年 每月出生數

- `https://www.ey.gov.tw/File/AC31F9B96D44C356?A=C` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://rwdnews.sanlih.com.tw/news/1904770` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mombaby.com.tw/articles/9937899` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.pts.org.tw/tag/3471?page=1&type=new` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.chinatimes.com/cn/realtimenews/20260810002102-260407?chdtv` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ws.moi.gov.tw/Download.ashx?u=LzAwMS9VcGxvYWQvT2xkRmlsZS9zaXRlX25vZGVfZmlsZS82NjkzLzEwNDAxLnBkZg%3D%3D&n=MTA0MDEucGRm&icon=.pdf` -> **snapshot** (snapshot 20241203005916); points raw/verified 15/6
  - p61 Annual registered births in Taiwan, 2021 (民國110年) = **196,627** birth registration (person) (2021-01-01..2021-12-31) [DISCARD: Mislabelled ROC year: quoted row is 民國100 (2011), not 2021.] quote: "民國100年 8,057,761 23,224,912 2.88 641.70 196,627 152,915 165,327 57,008"
  - p62 Annual registered births in Taiwan, 2023 (民國112年) = **199,113** birth registration (person) (2023-01-01..2023-12-31) [DISCARD: Mislabelled ROC year: quoted row is 民國102 (2013), not 2023.] quote: "民國102年 8,286,260 23,373,517 2.82 645.81 199,113 155,908 147,636 53,604"
  - p63 Annual registered births in Taiwan, 2024 (民國113年) = **210,383** birth registration (person) (2024-01-01..2024-12-31) [DISCARD: Mislabelled ROC year: quoted row is 民國103 (2014), not 2024.] quote: "民國103年 8,382,699 23,433,753 2.80 647.47 210,383 163,929 149,287 53,190"
  - p64 Registered births in Taiwan, September 2024 (民國113年9月) = **13,837** birth registration (person) (2024-09-01..2024-09-30) [DISCARD: Unreliable September 2024 table fragment; conflicts with the implied 11,792 level from p123/p125.] quote: "5,819 13,837 12,828 10,580 16,817"
  - p65 Registered births in Taiwan, September 2023 (民國112年9月) = **13,421** birth registration (person) (2023-09-01..2023-09-30) [DISCARD: Unreliable September 2023 table fragment; value duplicates a suspicious string and cannot be cleanly aligned.] quote: "12,397 13,421 13,236 11,462 14,609 14,310 14,310"
  - p66 Registered births in Taiwan, September 2021 (民國110年9月) = **13,421** birth registration (person) (2021-09-01..2021-09-30) [DISCARD: Unreliable September 2021 table fragment; value duplicates p65's suspicious 13,421.] quote: "13,935 15,349 15,465 14,114 13,187 12,664 14,090 12,397 13,421"
- `https://worldnews.net.ph/post/217743` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ris.gov.tw/app/portal/346` -> **snapshot** (snapshot 20260814192916); points raw/verified 0/0
- `https://dev.taisounds.news/news/content/71/287932` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.mdnkids.com/content.asp?Link_String_=249B00000WBDKVW` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tw.news.yahoo.com/8%E6%9C%88%E6%96%B0%E7%94%9F%E5%85%92%E5%83%85%E5%89%A97492%E4%BA%BA-%E4%BA%BA%E5%8F%A3%E9%80%A332%E5%80%8B%E6%9C%88%E8%B2%A` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.humanfertility.org/Docs/TWN/TWNcom.pdf` -> **snapshot** (snapshot 20220323064450); points raw/verified 15/15
  - p67 Registered live births in Taiwan (Table 3, No. of Births), 1998 = **271,450** birth registration (person) (1998-01-01..1998-12-31) [keep: ] quote: "1998 145976 85.9 8.2 5.9 271450 94.9 5.1"
  - p68 Registered live births in Taiwan (Table 3, No. of Births), 1999 = **283,661** birth registration (person) (1999-01-01..1999-12-31) [keep: ] quote: "1999 173209 83.0 9.7 7.3 283661 93.9 6.1"
  - p69 Registered live births in Taiwan (Table 3, No. of Births), 2000 = **305,312** birth registration (person) (2000-01-01..2000-12-31) [keep: ] quote: "2000 181642 77.0 12.5 10.5 305312 92.4 7.6"
  - p70 Registered live births in Taiwan (Table 3, No. of Births), 2001 = **260,354** birth registration (person) (2001-01-01..2001-12-31) [keep: ] quote: "2001 170515 74.9 15.1 9.8 0.2 260354 89.3 10.7"
  - p71 Registered live births in Taiwan (Table 3, No. of Births), 2002 = **247,530** birth registration (person) (2002-01-01..2002-12-31) [keep: ] quote: "2002 172655 74.1 15.8 9.8 0.2 247530 87.5 12.5"
  - p72 Registered live births in Taiwan (Table 3, No. of Births), 2003 = **227,070** birth registration (person) (2003-01-01..2003-12-31) [keep: ] quote: "2003 171483 71.6 18.5 9.5 0.3 227070 86.3 13.4"
  - p73 Registered live births in Taiwan (Table 3, No. of Births), 2004 = **216,419** birth registration (person) (2004-01-01..2004-12-31) [keep: ] quote: "2004 131453 78.6 8.0 13.1 0.3 216419 86.7 5.2 8.0 0.1"
  - p74 Registered live births in Taiwan (Table 3, No. of Births), 2005 = **205,854** birth registration (person) (2005-01-01..2005-12-31) [keep: ] quote: "2005 141140 82.1 10.0 7.6 0.3 205854 87.1 4.9 7.9 0.1"
  - p75 Registered live births in Taiwan (Table 3, No. of Births), 2006 = **204,459** birth registration (person) (2006-01-01..2006-12-31) [keep: ] quote: "2006 142669 85.5 9.7 4.5 0.3 204459 88.3 5.1 6.5 0.1"
  - p76 Registered live births in Taiwan (Table 3, No. of Births), 2007 = **204,414** birth registration (person) (2007-01-01..2007-12-31) [keep: ] quote: "2007 135041 84.0 10.8 4.8 0.3 204414 89.8 5.0 5.2 0.1"
  - p77 Registered live births in Taiwan (Table 3, No. of Births), 2008 = **198,733** birth registration (person) (2008-01-01..2008-12-31) [keep: ] quote: "2008 154866 88.2 7.8 3.6 0.3 198733 90.4 5.0 4.5 0.1"
  - p78 Registered live births in Taiwan (Table 3, No. of Births), 2009 = **191,310** birth registration (person) (2009-01-01..2009-12-31) [keep: ] quote: "2009 117099 84.4 10.8 4.4 0.4 191310 91.3 4.6 4.0 0.1"
  - p79 Registered live births in Taiwan (Table 3, No. of Births), 2010 = **166,886** birth registration (person) (2010-01-01..2010-12-31) [keep: ] quote: "2010 138819 87.2 9.0 3.4 0.4 166886 91.3 4.9 3.7 0.1"
  - p80 Share of all live births to non-Taiwanese mothers, Taiwan, 2003 (maximum) = **13.7** % (2003-01-01..2003-12-31) [keep: ] quote: "The share of births to non-Taiwanese mothers increased rapidly from about 5% in 1998 to reach its maximum of 13.7% of all live births in 2003"
  - p81 Births in 2003 included in annual birth count whose mothers were least likely co = **31,000** birth registration (person) (2003-01-01..2003-12-31) [keep: ] quote: "in 2003 more than 31,000 births were included in the annual birth count by the vital statistics"
- dropped by code checks: 9 (period year 2020 does not appear in the page text or URL (likely mis-dated): 2; period year 2022 does not appear in the page text or URL (likely mis-dated): 2; period year 2025 does not appear in the page text or URL (likely mis-dated): 2; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1; period year 2019 does not appear in the page text or URL (likely mis-dated): 1; period year 2018 does not appear in the page text or URL (likely mis-dated): 1)

### d3 [administrative] Birth-registration administrative lag

Hypothesis: September 2026 registration counts can be built from births by occurrence month times the share of each occurrence cohort registered in September; the legal registration window creates a known lag structure.

Queries issued by the searcher: 出生登記 期限 60日 戶籍法 第48條 統計; 內政部 出生數 按出生年月 分 統計 出生登記; 內政部 戶籍人口統計速報 113年9月 出生數 統計; 台灣 出生數 按登記日期 按發生日期 差異 落後 月; 出生登記 期限 60日 統計 出生年月 登記年月; 內政部 出生數 按出生年月 分 統計; 內政部 出生數 按登記日期 統計 月 113年 出生 登記; 台灣 出生登記 落後 月數 統計 發生 登記 差異; 出生登記 期限 60日 戶籍法 統計; 內政部 出生數 按出生年月 登記 統計; "嬰兒出生數按出生日期及登記日期相差日數" 百分比分配 內政部; 台灣 出生登記 延遲 登記 比率 出生當月 登記 統計 落後

- `https://210.241.78.32/Pages/Detail.aspx?nodeid=647&pid=1248` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://www.chcg.gov.tw/UserFiles/1010096221.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.ris.gov.tw/app/portal/346` -> **snapshot** (snapshot 20260814192916); points raw/verified 0/0
- `https://web.law.ntpc.gov.tw/scripts/FLAWDOC01.aspx?fcode=B0040014&flno=48` -> **snapshot** (snapshot 20251212061107); points raw/verified 2/0
- `https://web.law.ntpc.gov.tw/scripts/FLAWDOC02.aspx?rtype=H&RCODE2=B0040015&RNO=13` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ws.moi.gov.tw/Download.ashx?u=LzAwMS9VcGxvYWQvT2xkRmlsZS9zaXRlX25vZGVfZmlsZS82NjEzLzEwMjEyLnBkZg%3D%3D&n=MTAyMTIucGRm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://stat.ncl.edu.tw/subjectResult.jsp?n=02&p=%E4%BA%BA%E5%8F%A3&q=%E5%87%BA%E7%94%9F%E7%8E%87` -> **snapshot** (snapshot 20250524124330); points raw/verified 0/0
- `https://stat.ncl.edu.tw/bulletinVolume_en.jsp?p=00000020,113,1.45757243E8` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://open2.idataiwan.com/info/28167` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://win.dgbas.gov.tw/dgbas03/bs7/calendar/doc/list111.pdf` -> **snapshot** (snapshot 20220721223600); points raw/verified 4/2
  - p82 Publication lag for Ministry of the Interior monthly population count and growth = **10** day (not stated (page dated 2021-07-08)) [keep: ] quote: "1 人口靜態統計 人口數及人口增加率 月 10日 內政部"
  - p83 Publication lag for Ministry of the Interior monthly marriage and divorce statis = **10** day (not stated (page dated 2021-07-08)) [keep: ] quote: "3 2.結婚對數、結婚率、離婚對數、離婚率 月、年 10日 內政部"
- `https://open2.idataiwan.com/tag/%E5%85%A7%E6%94%BF%E9%83%A8%E6%88%B6%E6%94%BF%E5%8F%B8%E4%BA%BA%E5%8F%A3%E7%B5%B1%E8%A8%88/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://w3fs.tainan.gov.tw/Download.ashx?u=LzAwMS9VcGxvYWQvMTYvY2tmaWxlL2U5YWIzMzgxLTQxYTktNGUyOS04YTE4LTBiNDI5YzM2YTJmMC5wZGY%3d&n=5oi25pS%2f5rOV6KaP` -> **snapshot** (snapshot 20250414143708); points raw/verified 11/1
  - p84 Effective date from which birth registration may be filed at any household offic = **106** as written "106 年 7 月 3 日", value check pending date (ROC year-month-day) (2017-07-03..2017-07-03) [keep: ] quote: "有關出生登記,自 106 年 7 月 3 日起得向戶籍地直轄市、縣 ( 市 ) 政府所轄任一戶政事務所辦理。"
- dropped by code checks: 14 (period_end missing or unparseable: 2; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 11; number: no number in value_as_written: 1)

### d4 [physical_flow] Births by occurrence month / conception timing

Hypothesis: Births occurring in August-September 2026 can be estimated from seasonal occurrence-month birth patterns or from conception cohorts around November-December 2025, then converted to September registrations using the lag distribution.

Queries issued by the searcher: 台灣 出生數 按出生月 統計 2025 內政部; Taiwan births by month 2024 2025 monthly birth statistics; 2026年7月 出生數 內政部 戶口統計 新生兒; 2026 新生兒 每月 出生人數 1月 2月 3月 4月 5月 6月; 2026年1月 2月 3月 4月 出生數 內政部 新生兒 6523 歷史新低; 台灣 出生 發生月份 統計 妊娠週數 出生登記 落後 月; 台灣 出生數 按月 統計 2025 內政部 戶政司; Taiwan monthly births 2025 statistics Department of Household Registration; 2026年 台灣 出生數 每月 內政部 戶口統計 7月 新生兒; 內政部 統計 出生數 按發生日期 出生登記 落後 月 統計表; 2025年9月 台灣 出生數 8603 新生兒 內政部 9月10日 公布; 台灣 出生 發生月份 統計 落後登記 出生登記 期限 60日 統計 差異; 台灣 出生數 按出生月 統計 2025 內政部; Taiwan births by month 2024 2025 monthly birth counts Department of Household Registration; 2026年 7月 出生數 內政部 戶口統計 新生兒; 內政部 統計月報 出生數 按發生日期 發生月份

- `https://www.ris.gov.tw/documents/data/5/2/DemographicQuarterly_Winter2025.pdf` -> **snapshot** (snapshot 20260902055959); points raw/verified 15/14
  - p85 Taiwan registered births, September 2025 (monthly total) = **8,603** birth registration (person) (2025-09-01..2025-09-30) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p86 Taiwan registered births, August 2025 (monthly total) = **8,464** birth registration (person) (2025-08-01..2025-08-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p87 Taiwan registered births, October 2025 (monthly total) = **9,458** birth registration (person) (2025-10-01..2025-10-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p88 Taiwan registered births, November 2025 (monthly total) = **7,946** birth registration (person) (2025-11-01..2025-11-30) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p89 Taiwan registered births, December 2025 (monthly total) = **9,027** birth registration (person) (2025-12-01..2025-12-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p90 Taiwan registered births, January 2025 (monthly total) = **9,495** birth registration (person) (2025-01-01..2025-01-31) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p91 Taiwan registered births, February 2025 (monthly total) = **10,407** birth registration (person) (2025-02-01..2025-02-28) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p92 Taiwan registered births, March 2025 (monthly total) = **9,388** birth registration (person) (2025-03-01..2025-03-31) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p93 Taiwan registered births, April 2025 (monthly total) = **8,684** birth registration (person) (2025-04-01..2025-04-30) [keep: ] quote: "107,812 9,495 10,407 9,388 8,684"
  - p94 Taiwan registered births, May 2025 (monthly total) = **8,433** birth registration (person) (2025-05-01..2025-05-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p95 Taiwan registered births, June 2025 (monthly total) = **8,968** birth registration (person) (2025-06-01..2025-06-30) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p96 Taiwan registered births, July 2025 (monthly total) = **8,939** birth registration (person) (2025-07-01..2025-07-31) [keep: ] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p97 Taiwan total registered births, full year 2025 = **107,812** birth registration (person) (2025-01-01..2025-12-31) [keep: ] quote: "there were 107,812 births in 2025, a decrease of 20.05 percent compared with the previous year"
  - p98 Taiwan total registered births, full year 2024 = **134,856** birth registration (person) (2024-01-01..2024-12-31) [keep: ] quote: "2024 (1) 134,856 202,107 -67,251 5.76 8.63 -2.87"
- `https://www.ydn.com.tw/tw/News/ugC_News_Detail.aspx?chapterID=1788769&type=highlight` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://rwdnews.sanlih.com.tw/news/1763612` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://j-media.tw/Article/Detail/37299` -> **snapshot** (snapshot 20260417185829); points raw/verified 15/15
  - p99 Taiwan annual births, 2016 = **208,440** birth registration (person) (2016-01-01..2016-12-31) [DISCARD: Duplicate of p31 (2016 annual births).] quote: "從2016年的208,440人,到2025年的107,812人"
  - p100 Taiwan annual births, 2025 = **107,812** birth registration (person) (2025-01-01..2025-12-31) [DISCARD: Duplicate of p32/p97 (2025 annual births).] quote: "到2025年的107,812人,台灣年度新生兒在十年之間幾近腰斬"
  - p101 Taiwan annual births, 2024 (Dragon year) = **134,856** birth registration (person) (2024-01-01..2024-12-31) [DISCARD: Duplicate of p33/p98 (2024 annual births).] quote: "2024年受到「龍年效應」支撐,全年出生134,856人,年減僅0.5%"
  - p102 Taiwan births, January 2025 = **9,495** birth registration (person) (2025-01-01..2025-01-31) [DISCARD: Duplicate of p90 (January 2025 monthly births).] quote: "2025年1月出生9,495人"
  - p103 Taiwan births, February 2025 = **10,407** birth registration (person) (2025-02-01..2025-02-28) [DISCARD: Duplicate of p91 (February 2025 monthly births).] quote: "2月受農曆年效應拉抬至10,407人,形成全年唯一高點"
  - p104 Taiwan births, March 2025 = **9,388** birth registration (person) (2025-03-01..2025-03-31) [DISCARD: Duplicate of p92 (March 2025 monthly births).] quote: "3月9,388人"
  - p105 Taiwan births, April 2025 = **8,684** birth registration (person) (2025-04-01..2025-04-30) [DISCARD: Duplicate of p93 (April 2025 monthly births).] quote: "4月8,684人"
  - p106 Taiwan births, May 2025 = **8,433** birth registration (person) (2025-05-01..2025-05-31) [DISCARD: Duplicate of p94 (May 2025 monthly births).] quote: "5月8,433人"
  - p107 Taiwan births, November 2025 = **7,946** birth registration (person) (2025-11-01..2025-11-30) [DISCARD: Duplicate of p88 (November 2025 monthly births).] quote: "11月更跌至7,946人"
  - p108 Taiwan births, December 2025 = **9,027** birth registration (person) (2025-12-01..2025-12-31) [DISCARD: Duplicate of p89 (December 2025 monthly births).] quote: "12月雖小幅回升至9,027人"
  - p109 Taiwan average monthly births, 2025 = **8,984** birth registration (person) (2025-01-01..2025-12-31) [DISCARD: Duplicate of p41 (2025 average monthly births).] quote: "全年月均出生人數約為8,984人"
  - p110 Taiwan births, January 2026 = **8,723** birth registration (person) (2026-01-01..2026-01-31) [DISCARD: Duplicate of p42 (January 2026 monthly births).] quote: "1月出生8,723人,與2025年同月相比年減8.1%"
  - p111 Taiwan births, February 2026 (record monthly low) = **6,523** birth registration (person) (2026-02-01..2026-02-28) [DISCARD: Duplicate of p43 (February 2026 monthly births).] quote: "2月份全國新生兒僅6,523人,首度跌破7,000人大關"
  - p112 Taiwan births, January-February 2026 cumulative = **15,246** birth registration (person) (2026-01-01..2026-02-28) [DISCARD: Duplicate of p44 (January-February 2026 cumulative births).] quote: "2026年前兩月合計僅15,246人"
  - p113 Taiwan births, January-February 2025 cumulative = **19,902** birth registration (person) (2025-01-01..2025-02-28) [DISCARD: Duplicate of p45 (January-February 2025 cumulative births).] quote: "與2025年同期的19,902人相比,實質年減幅仍達23.4%"
- `https://www.bigmedia.com.tw/article/1773546826373` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tw.news.yahoo.com/2025%E6%96%B0%E7%94%9F%E5%85%92%E9%A9%9F%E6%B8%9B2-5%E8%90%AC%E4%BA%BA-%E5%83%8F-%E8%B7%8C%E4%BA%86%E5%85%A9%E5%80%8B%E8%B7%` -> **snapshot** (snapshot 20260109010721); points raw/verified 15/9
  - p114 Taiwan births registered January-November 2025 (cumulative total) = **98,785** as written "九萬八千七百八十五", value check pending birth registration (person) (2025-01-01..2025-11-30) [keep: ] quote: "二○二五年一至十一月新生兒僅九萬八千七百八十五人"
  - p115 Year-on-year decline in Taiwan births, 2025 vs prior year = **25,000** as written "近二萬五千", value check pending birth registration (person) (2025-01-01..2025-12-31) [keep: ] quote: "與前年相較驟減近二萬五千人"
  - p116 Number of months in 2025 with births above 10,000 = **3** as written "三", value check pending month (2025-01-01..2025-12-31) [DISCARD: Misparsed: 三月份 means March, not three months.] quote: "僅有三月份的出生數破萬"
  - p117 Monthly births threshold of 10,000 in a single month (2025) = **100,000,000** as written "一萬", value check pending birth registration (person) (2025-01-01..2025-12-31) [DISCARD: Misparsed threshold: 100,000,000 is not a credible monthly birth count.] quote: "但要在單月生出一萬名寶寶幾乎不可能"
  - p118 Original expectation for Taiwan births in 2025 (end of 2024) = **120,000** as written "十二萬", value check pending birth registration (person) (2025-01-01..2025-12-31) [keep: ] quote: "二○二四年底原本預期二○二五年會有十二萬新生兒"
  - p119 Mid-2025 expectation for Taiwan births in 2025 = **110,000** as written "十一萬", value check pending birth registration (person) (2025-01-01..2025-12-31) [keep: ] quote: "到了去年年中認為應該能勉強守住十一萬人"
  - p120 Year-on-year decline rate in Taiwan births, 2025 (stated as one year drop) = **20** as written "兩成", value check pending % (2025-01-01..2025-12-31) [keep: ] quote: "一年跌掉兩成,等於是跌了兩個跌停板"
  - p121 Prior-year minimum expected number of mothers in labor at Tai-An Hospital = **10** as written "十", value check pending person (not stated (page dated 2026-01-02)) [DISCARD: Hospital staffing anecdote, not a quantitative birth-registration input.] quote: "往年從護理師安排的人力大致可以推敲出待產人數至少能破十人"
  - p122 Nurses per shift in delivery room in recent years (lower bound) = **2** as written "二", value check pending person (not stated (page dated 2026-01-02)) [DISCARD: Hospital staffing anecdote, not a quantitative birth-registration input.] quote: "以前產房的三班人力都配置四名護理人員,近年都已降至二到三人"
- `https://dr131.com/snakeyearbabies/` -> **snapshot** (snapshot 20260512163234); points raw/verified 15/15
  - p123 Taiwan births registered in September 2025 (single month) = **8,603** birth registration (person) (2025-09-01..2025-09-30) [DISCARD: Duplicate of p85 (September 2025 monthly births).] quote: "9月份的新生兒出生數僅8603人,相當5.1分鐘出生一名嬰兒,為歷年單月第三低的出生人數"
  - p124 Taiwan births registered in September 2024 (single month) = **3,189** birth registration (person) (2024-09-01..2024-09-30) [DISCARD: Misparsed: 3,189 is the year-on-year decrease, not the September 2024 level.] quote: "比2024年9月的出生人數大幅減少27.04%,等於少了3189個新生兒"
  - p125 Year-on-year change in Taiwan September births, 2025 vs 2024 = **27.04** % (2025-09-01..2025-09-30) [keep: ] quote: "比2024年9月的出生人數大幅減少27.04%,等於少了3189個新生兒"
  - p126 Taiwan births registered in July 2025 (single month) = **8,939** birth registration (person) (2025-07-01..2025-07-31) [DISCARD: Duplicate of p96 (July 2025 monthly births).] quote: "即使到了下半年,2025年7月的出生人數為8939人"
  - p127 Taiwan births registered in January 2025 (single month) = **9,495** birth registration (person) (2025-01-01..2025-01-31) [DISCARD: Duplicate of p90 (January 2025 monthly births).] quote: "2025年1月底是蛇年開頭,出生人數是9495人,是歷年單月分的次低。"
  - p128 Taiwan births registered in February 2025 (single month) = **10,407** birth registration (person) (2025-02-01..2025-02-28) [DISCARD: Duplicate of p91 (February 2025 monthly births).] quote: "到了 2月,略為回升到萬人,為 10407人。"
  - p129 Taiwan births registered in March 2025 (single month) = **9,388** birth registration (person) (2025-03-01..2025-03-31) [DISCARD: Duplicate of p92 (March 2025 monthly births).] quote: "可是,到了 3月,出生人數只有 9388人"
  - p130 Taiwan births registered in April 2025 (single month) = **8,684** birth registration (person) (2025-04-01..2025-04-30) [DISCARD: Duplicate of p93 (April 2025 monthly births).] quote: "4月更掉到8684人,少了7.5%,創下歷年單月最低的出生記錄"
  - p131 Taiwan births registered in May 2025 (single month) = **8,433** birth registration (person) (2025-05-01..2025-05-31) [DISCARD: Duplicate of p94 (May 2025 monthly births).] quote: "內政部統計5月出生數為8433人,比去年同期少了2735人"
  - p132 Taiwan births registered in November 2025 (single month) = **7,946** birth registration (person) (2025-11-01..2025-11-30) [DISCARD: Duplicate of p88 (November 2025 monthly births).] quote: "及至11月,出生人數不到8000人,只有7946人"
  - p133 Taiwan cumulative births registered January-November 2025 = **98,785** birth registration (person) (2025-01-01..2025-11-30) [DISCARD: Duplicate of p114 (January-November 2025 cumulative births).] quote: "2025年1至11月出生人數只有9萬8785人,尚未突破10萬人"
  - p134 Taiwan full-year births 2024 = **134,000** birth registration (person) (2024-01-01..2024-12-31) [DISCARD: Approximate duplicate of p98 (2024 annual births).] quote: "2024年全年有13.4萬人出生"
  - p135 Taiwan full-year births 2024 (dragon year, alternate figure) = **134,800** birth registration (person) (2024-01-01..2024-12-31) [DISCARD: Approximate duplicate of p98 (2024 annual births).] quote: "2024年龍年新生兒只有13.48萬人,創下新低,比2023年兔寶寶還要少。"
  - p136 Projected Taiwan full-year births 2025 if snake-year births fall 13%-14% below d = **116,550** (range 115,900..117,200) as written "11.59萬~11.72萬", value check pending birth registration (person) (2025-01-01..2025-12-31) [DISCARD: 2025 forecast superseded by actual p97; not a 2026 anchor.] quote: "如果2025年蛇寶寶比龍寶寶減少13%~14%,新生兒人數可能只有11.59萬~11.72萬人,不到12萬人"
  - p137 Projected Taiwan full-year births 2025 (Ministry of the Interior estimate, publi = **110,000** birth registration (person) (2025-01-01..2025-12-31) [DISCARD: 2025 forecast superseded by actual p97; not a 2026 anchor.] quote: "內政部推算,全年預估出生數可能不到 11萬餘人,將創下史上新低!"
- `https://www.pttweb.cc/bbs/Gossiping/t/52026617?sort=new` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://hk.crntt.com/crn-webapp/touch/detail.jsp?coluid=7&docid=160153686&kindid=0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://worldnews.net.ph/post/199123` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://marketstats.ai/graphics/births-and-deaths-in-taiwan-december-2024-2025/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.kanglin.com.tw/news/%e9%80%a358%e5%80%8b%e6%9c%88%e3%80%8c%e7%94%9f%e4%b8%8d%e5%a6%82%e6%ad%bb%e3%80%8d%e4%ba%ba%e5%8f%a3%e6%8c%81%e7%ba%8` -> **snapshot** (snapshot 20260214160656); points raw/verified 15/14
  - p138 Taiwan births registered in October 2025 (monthly count) = **9,458** birth registration (person) (2025-10-01..2025-10-31) [DISCARD: Duplicate of p87 (October 2025 monthly births).] quote: "10月出生數為9,458人,約每4.7分鐘出生一個嬰兒"
  - p139 Taiwan births registered in September 2025 (implied by October month-on-month ch = **855** birth registration (person) (2025-09-01..2025-09-30) [DISCARD: Misparsed: 855 is the October-versus-September change, not the September 2025 level.] quote: "較9月增加855人(9.94%)"
  - p140 Taiwan births registered October 2025, year-on-year change vs October 2024 = **2,612** birth registration (person) (2025-10-01..2025-10-31) [DISCARD: October 2025 YoY birth change is redundant for a September 2026 forecast because the October 2025 level is already in p8] quote: "較去年同月減少2,612人(-21.64%)"
  - p141 Taiwan births registered October 2025, year-on-year percent change = **-21.64** % (2025-10-01..2025-10-31) [DISCARD: Redundant percent version of p140; not needed once p87 supplies the October 2025 level.] quote: "較去年同月減少2,612人(-21.64%)"
  - p142 Taiwan births registered October 2025, month-on-month percent change vs Septembe = **9.94** % (2025-10-01..2025-10-31) [keep: ] quote: "較9月增加855人(9.94%)"
  - p143 Taiwan annual crude birth rate implied for October 2025 (annualized) = **4.78** birth registration (person)/(1000 person*year) (2025-10-01..2025-10-31) [DISCARD: October 2025 crude birth rate is redundant with the October 2025 birth level in p87.] quote: "折合年粗出生率為千分之4.78"
  - p144 Minutes per birth in Taiwan, October 2025 = **4.7** minute/birth registration (person) (2025-10-01..2025-10-31) [DISCARD: Minutes per birth for October 2025 is redundant with p87.] quote: "約每4.7分鐘出生一個嬰兒"
  - p145 Taiwan deaths registered October 2025 = **15,908** death registration (person) (2025-10-01..2025-10-31) [DISCARD: October 2025 deaths do not help estimate September 2026 birth registrations.] quote: "人口死亡數為1萬5,908人"
  - p146 Taiwan total population at end of October 2025 = **23,310,853** person (2025-10-31..2025-10-31) [DISCARD: October 2025 population level is not a birth-registration input.] quote: "至10月底為止全國人口數為2,331萬853人"
  - p147 Taiwan population change vs same month prior year, October 2025 = **91,951** person (2025-10-01..2025-10-31) [DISCARD: October 2025 population change is not a birth-registration input.] quote: "與去年同期相較減少9萬1,951人(-0.39%)"
  - p148 Taiwan population change vs September 2025 = **6,178** person (2025-10-01..2025-10-31) [DISCARD: October 2025 month-on-month population change is not a birth-registration input.] quote: "較9月減少6,178人(-0.03%)"
  - p149 NDC 2025 Taiwan births high projection = **133,765** birth registration (person) (2025-01-01..2025-12-31) [DISCARD: 2025 NDC projection, superseded by actual p97; not a 2026 anchor.] quote: "2025年新生兒人數按高推估為13萬3,765人"
  - p150 NDC 2025 Taiwan births medium projection = **129,897** birth registration (person) (2025-01-01..2025-12-31) [DISCARD: 2025 NDC projection, superseded by actual p97; not a 2026 anchor.] quote: "中推估為12萬9,897人"
  - p151 NDC 2025 Taiwan births low projection = **125,526** birth registration (person) (2025-01-01..2025-12-31) [DISCARD: 2025 NDC projection, superseded by actual p97; not a 2026 anchor.] quote: "低推估為12萬5,526人"
- dropped by code checks: 8 (value_as_written not in quote as a whole number: 1; period year 2026 does not appear in the page text or URL (likely mis-dated): 6; scale word '万' not supported by quote or table header: 1)

### d5 [forecasts_markets] Official population projections and annual birth forecasts

Hypothesis: An official 2026 annual births projection provides an anchor; applying a historical September share yields a constrained estimate independent of short-run monthly noise.

Queries issued by the searcher: 國發會 人口推估 2026 出生數; 台灣 2026 出生數 預估; 內政部 戶政統計 2025年9月 出生數 新生兒; 中華民國人口推估 2026年至2075年 出生數 9.4萬 中推估 報告; 內政部 2026年8月 戶口統計 出生數 7,492 前8月累計; 國發會 人口推估 2026 出生數; 台灣 2026 出生數 預估; 內政部 戶政司 人口統計 每月 出生數 2025年 9月 新生兒 統計表; 2026年 8月 新生兒 7492人 內政部 人口統計 1至8月 出生數; 國發會 人口推估 2026 出生數; Taiwan population projections 2026 births National Development Council; 內政部 戶政統計 2025年9月 出生數 新生兒 月統計; Taiwan monthly births September 2025 8,000 內政部 人口統計 出生 9月

**DIRECTION VOIDED: a searcher query contains a registered value ['(?<![\\d.,])7,492(?!\\d|[.,]\\d)', '(?<![\\d.,])7492(?!\\d|[.,]\\d)']; no pages fetched**


### d6 [base_rates] Marriage registrations and birth timing

Hypothesis: Births in September 2026 are related to marriage cohorts 12-24 months earlier and to births per marriage; marriage registration trends can constrain the direction and level of the birth forecast.

Queries issued by the searcher: 台灣 結婚登記 月別 2024 2025 內政部 統計; 台灣 出生數 與 結婚 落後 關係 研究; 內政部 戶政司 戶口統計速報 115年 出生 結婚 統計 月; 台灣 2026年 1月 2月 3月 出生數 結婚對數 統計; 台灣 結婚登記 月別 2024 2025 內政部; 台灣 出生數 與 結婚 落後 關係; marriage registrations Taiwan monthly births lag; 內政部 戶政司 115年 7月 結婚登記 出生 統計 2026; site:moi.gov.tw 115年7月 人口統計 出生 結婚; 台灣 2026 1-7月 出生數 結婚對數 統計; Taiwan births July 2026 7906 marriage registrations 2026; 台灣 結婚登記 月別 2025 內政部 統計; 台灣 出生數 與 結婚 落後 關係 分析; Taiwan marriage registrations monthly births lag relationship; 內政部 戶政司 人口統計 每月 出生 結婚 2026年8月 統計; 2026年1-7月 結婚對數 出生數 內政部 統計 每月; 國發會 人口推估 2026 首次 納入 結婚對數 短期 出生數 研判

- `https://www.ris.gov.tw/documents/data/5/2/DemographicQuarterly_Winter2025.pdf` -> **snapshot** (snapshot 20260902055959); points raw/verified 15/13
  - p152 Taiwan registered marriages (couples), 2025 annual total = **104,376** couple (2025-01-01..2025-12-31) [keep: ] quote: "there were 104,376 marriages registered in 2025, including 3,305 same-sex marriages."
  - p153 Taiwan registered marriages (couples), 2024 annual total = **123,061** couple (2024-01-01..2024-12-31) [keep: ] quote: "2024(1) 123,061 53,469 5.26 2.28"
  - p154 Taiwan registered births, 2025 annual total = **107,812** birth registration (person) (2025-01-01..2025-12-31) [DISCARD: Duplicate of p97 (2025 annual births).] quote: "there were 107,812 births in 2025, a decrease of 20.05 percent compared with the previous year"
  - p155 Taiwan registered births, 2024 annual total = **134,856** birth registration (person) (2024-01-01..2024-12-31) [DISCARD: Duplicate of p98 (2024 annual births).] quote: "2024 (1) 134,856 202,107 -67,251 5.76 8.63 -2.87"
  - p156 Taiwan registered births, September 2025 monthly total = **8,603** birth registration (person) (2025-09-01..2025-09-30) [DISCARD: Duplicate of p85 (September 2025 monthly births).] quote: "8,433 8,968 8,939 8,464 8,603 9,458 7,946 9,027"
  - p157 Taiwan registered births, October 2025 monthly total = **9,458** birth registration (person) (2025-10-01..2025-10-31) [DISCARD: Duplicate of p87 (October 2025 monthly births).] quote: "23,310,853 11,470,704 11,840,149 9,458 15,908 6,450"
  - p158 Taiwan registered births, November 2025 monthly total = **7,946** birth registration (person) (2025-11-01..2025-11-30) [DISCARD: Duplicate of p88 (November 2025 monthly births).] quote: "23,306,085 11,467,137 11,838,948 7,946 14,771 6,825"
  - p159 Taiwan registered births, December 2025 monthly total = **9,027** birth registration (person) (2025-12-01..2025-12-31) [DISCARD: Duplicate of p89 (December 2025 monthly births).] quote: "23,299,132 11,462,401 11,836,731 9,027 17,450 8,423"
  - p160 Taiwan registered marriages (couples), September 2025 monthly total = **5,844** couple (2025-09-01..2025-09-30) [keep: ] quote: "7,655 263 7,418 269 5,916 241 5,844 230 10,735 307 8,586 259 10,816 360"
  - p161 Taiwan registered marriages (couples), October 2025 monthly total = **10,735** couple (2025-10-01..2025-10-31) [keep: ] quote: "10,735 10,428 307 5.42 0.58 4.78 0.48 - 4.37 0.74 -"
  - p162 Taiwan registered marriages (couples), November 2025 monthly total = **8,586** couple (2025-11-01..2025-11-30) [keep: ] quote: "8,586 8,327 259 4.48 1.52 - 4.03 1.23 - 4.38 0.81 -"
  - p163 Taiwan registered marriages (couples), December 2025 monthly total = **10,816** couple (2025-12-01..2025-12-31) [keep: ] quote: "10,816 10,456 360 5.47 0.55 - 4.18 1.08 - 4.47 0.79 -"
  - p164 Taiwan crude marriage rate, 2025 annual = **4.47** couple per 1,000 population (2025-01-01..2025-12-31) [keep: ] quote: "with a crude marriage rate of 4.47 per 1,000 population"
- `https://joelin.cc/p/4372` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://eprintstest.lse.ac.uk/127749/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ws.moi.gov.tw/Download.ashx?u=LzAwMS9VcGxvYWQvNDAwL3JlbGZpbGUvMC8yMjY3OC9mYjFhNDNlNC0yNTQ0LTQ0NjctYWRjYi1iNDhlYWQ2ZGRkNDAucGRm&n=MTE0MDgucGRm&` -> **dropped** (unreadable PDF: Failed to load document (PDFium: Data format error).); points raw/verified -/-
- `https://blog.104.com.tw/the-relationship-between-fertility-rates-and-the-married-population/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.hkcna.hk/docDetail.jsp?id=101132664&channel=2805` -> **snapshot** (snapshot 20251011104950); points raw/verified 15/8
  - p165 Taiwan births (newborns), September 2025 = **8,603** birth registration (person) (2025-09-01..2025-09-30) [DISCARD: Duplicate of p85 (September 2025 monthly births).] quote: "9月全台新生兒僅8603人"
  - p166 Consecutive months Taiwan births below 9,000 (as of 2025) = **6** month (2025-04-01..2025-09-30) [keep: ] quote: "今年以來已連續6個月低於9000人大關"
  - p167 Consecutive months of Taiwan population decline (as of 2025) = **21** month (2024-01-01..2025-09-30) [keep: ] quote: "連續21個月呈現人口負成長"
  - p168 Share of unmarried Taiwanese women aged 15-64 willing to marry = **32.4** % (not stated (page dated 2025-10-11)) [DISCARD: Attitude share, not a monthly registration input.] quote: "僅有32.4%沒有配偶的台灣婦女有意願結婚"
  - p169 Share of unmarried Taiwanese women aged 15-64 with no intention to marry = **67.6** % (not stated (page dated 2025-10-11)) [DISCARD: Attitude share, not a monthly registration input.] quote: "其餘67.6%皆表示毫無結婚意願"
  - p170 Share of all Taiwanese women not wanting children = **26.6** % (not stated (page dated 2025-10-11)) [DISCARD: Attitude share, not a monthly registration input.] quote: "全體台灣女性中有26.6%表示不想生小孩"
  - p171 Share of all Taiwanese women not wanting children, 2019 = **19.2** % (2019-01-01..2019-12-31) [DISCARD: Attitude share, not a monthly registration input.] quote: "比2019年(19.2%)增加了7.4%"
  - p172 Share of Taiwanese women aged 15-24 not wanting children = **45.9** % (not stated (page dated 2025-10-11)) [DISCARD: Attitude share, not a monthly registration input.] quote: "其中15-24歲年輕女性拒生比例高達45.9%"
- `https://appimg.modaily.cn/app/szb/pc/content/202608/19/content_498376.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://statis.moi.gov.tw/micst/webMain.aspx?k=menum` -> **snapshot** (snapshot 20260814004253); points raw/verified 0/0
- `https://www.ris.gov.tw/documents/data/5/2/DemographicQuarterly_Spring2026.pdf` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://wantrich.chinatimes.com/search/%e6%86%b2%e6%94%bf%e5%88%86%e9%9a%9b/1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.womengroups.org.tw/OnePage.aspx?tid=1&id=5213` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ocacnews.net/article/421847` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 9 (value_as_written not in quote as a whole number: 2; scale word '万' not supported by quote or table header: 7)

### d7 [shocks] Calendar, policy, and administrative-processing effects

Hypothesis: September 2026 calendar effects, registration-office closures, typhoons, or new birth-incentive policies may shift month-end registration counts; these should adjust or widen the forecast interval rather than provide a standalone level.

Queries issued by the searcher: 2026 台灣 9月 行事曆 連假 中秋節 教師節; 內政部 戶政 統計 出生 登記 2026年 月; 內政部 2026年7月 出生數 新生兒 戶口統計 8月10日公布; 2025年9月 出生數 內政部 戶口統計 新生兒 9月; 2026 台灣 9月 行事曆 連假 中秋節 教師節; 內政部 戶政 統計 出生 登記 月報 2026; 內政部 2026年7月 戶口統計 出生數 新生兒; 2026 生育補助 每胎10萬 上路 元旦 少子化 政策; 2026 台灣 9月 行事曆 連假 中秋節; 內政部 戶政 統計 發布 時間 2026 出生 登記; 內政部 2026年7月 戶口統計 出生數 新生兒; 2025年9月 台灣 出生數 新生兒 內政部 戶口統計

- `https://hk.crntt.com/doc/1602/1/8/7/160218724.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.chinatimes.com/realtimenews/20260408001968-260405` -> **snapshot** (snapshot 20260408061231); points raw/verified 8/8
  - p173 Number of consecutive days off for Mid-Autumn Festival (Sep 25, Fri) plus Teache = **4** day (2026-09-25..2026-09-28) [DISCARD: Duplicate/less precise version of p181 for the September 2026 holiday.] quote: "25日(周五)中秋節、28日(周一)教師節,2個假期連在一起共休假4天。"
  - p174 Number of leave days an employee must take (Sep 21-24) to bridge into a 10-day b = **4** day (2026-09-21..2026-09-24) [DISCARD: Leave-bridging scenario, not a registration-day count.] quote: "上班族若想休長假,可以選在9月21日至24日請假4天"
  - p175 Total consecutive days off achievable by taking Sep 21-24 leave (Sep 19 through  = **10** day (2026-09-19..2026-09-28) [DISCARD: Leave-bridging scenario, not a registration-day count.] quote: "就能從9月19(周六)起,一路放假至9月28日教師節,一口氣連放10天假"
  - p176 Number of remaining long weekends/holiday clusters in Taiwan for the rest of 202 = **6** holiday cluster (2026-01-01..2026-12-31) [DISCARD: Other holiday blocks elsewhere in 2026; not needed for September registration adjustment.] quote: "今年還剩下6個連假,包括勞動節、端午節、教師節加中秋節、國慶日、光復節、行憲紀念日"
  - p177 Number of national holidays in September 2026 in Taiwan (Mid-Autumn Festival and = **2** holiday (2026-09-01..2026-09-30) [DISCARD: Less precise duplicate of p181's September holiday information.] quote: "9月是民眾最期待的月份,有中秋節與教師節2個國定假日"
  - p178 Number of consecutive days off for the Labor Day long weekend in Taiwan, 2026 = **3** day (2026-05-01..2026-05-03) [DISCARD: Other holiday block outside the target month.] quote: "5月1日(周五)勞動節,休假3天"
  - p179 Number of consecutive days off for the Dragon Boat Festival long weekend in Taiw = **3** day (2026-06-19..2026-06-21) [DISCARD: Other holiday block outside the target month.] quote: "6月19日(周五)端午節,同樣有3天假期"
  - p180 Number of consecutive days off achievable by taking 4 weekday leave days around  = **9** day (2026-01-01..2026-12-31) [DISCARD: Other holiday leave scenario, not a registration-day count.] quote: "其他5個連假,同樣可以在上班日請假4天,都能連休9天。"
- `https://fwnews.com.tw/tag/%E6%96%B0%E7%94%9F%E5%85%92/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://hk.crntt.com/doc/1602/2/5/9/160225974.html` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.asiaa.sinica.edu.tw/guide/holiday_c.php?i=2018&pr=1` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.chinatimes.com/realtimenews/20260903004037-260405` -> **snapshot** (snapshot 20260908020057); points raw/verified 11/11
  - p181 Taiwan 2026 Mid-Autumn Festival and Teachers' Day joint holiday length (days) = **4** day (2026-09-25..2026-09-28) [keep: ] quote: "●中秋節、教師節連假4天: 9月25日(五)~9月28日(一)"
  - p182 Number of long weekends/holiday blocks in Taiwan from September 2026 to end of 2 = **4** holiday block (2026-09-01..2026-12-31) [DISCARD: Holiday blocks after September; not needed for the target month.] quote: "2026年9月起至年底有4個連假"
  - p183 Number of long weekends in Taiwan from late September to end of October 2026 (pe = **3** holiday block (2026-09-01..2026-10-31) [DISCARD: Holiday blocks after September; not needed for the target month.] quote: "9月底到10月底就有3個連假"
  - p184 Number of long weekends in Taiwan at end of December 2026 (per netizen comment) = **2** holiday block (2026-12-01..2026-12-31) [DISCARD: Holiday blocks after September; not needed for the target month.] quote: "12月底又2個連假"
  - p185 Annual leave days needed to bridge Constitution Day holiday to 2027 New Year (da = **4** day (2026-12-28..2026-12-31) [DISCARD: December leave scenario, not a September input.] quote: "只要請12月28日至12月31日共4天特休"
  - p186 Total consecutive days off from 2026-12-25 to 2027-01-03 using 4 annual leave da = **10** day (2026-12-25..2027-01-03) [DISCARD: December-2026/January-2027 leave scenario, not a September input.] quote: "從12月25日一路放到隔年1月3日,爽休10天"
  - p187 Taiwan 2027 New Year holiday length (days) = **3** day (2027-01-01..2027-01-03) [DISCARD: 2027 New Year holiday, not a September input.] quote: "2027年元旦連假(1月1日(五)~1月3日(日),共3天)"
  - p188 Taiwan 2026 National Day holiday length (days) = **3** day (2026-10-09..2026-10-11) [DISCARD: October holiday block, not a September input.] quote: "●國慶日連假3天: 10月9日(五)~10月11日(日)"
  - p189 Taiwan 2026 Retrocession Day holiday length (days) = **3** day (2026-10-24..2026-10-26) [DISCARD: October holiday block, not a September input.] quote: "●光復節連假3天: 10月24日(六)~10月26日(一)"
  - p190 Taiwan 2026 Constitution Day holiday length (days) = **3** day (2026-12-25..2026-12-27) [DISCARD: December holiday block, not a September input.] quote: "●行憲紀念日連假3天: 12月25日(五)~12月27日(日)"
  - p191 Months remaining in 2026 as of September (months) = **4** month (2026-09-01..2026-12-31) [DISCARD: Calendar countdown context, not a birth-registration input.] quote: "時序進入9月,轉眼間2026年只剩下4個月"
- `https://news.pts.org.tw/article/821731` -> **snapshot** (snapshot 20260811182642); points raw/verified 15/6
  - p192 Average age of Taiwanese women at first birth = **32** year (not stated (page dated 2026-08-10)) [DISCARD: Long-run fertility context, not a monthly registration input.] quote: "台灣女性生育第一胎的平均年齡大約落在32歲"
  - p193 Share of obstetric medical institutions closed in Taiwan over the past 5 years = **3** % (closed obstetric institutions / obstetric institutions) (not stated (page dated 2026-08-10)) [DISCARD: Obstetric-capacity context, not a monthly registration input.] quote: "這5年來差不多關了3成的產科醫療機構"
  - p194 Decline in births at large hospitals in Taiwan over the past 5 years (lower boun = **2** % (decline in births / births) (not stated (page dated 2026-08-10)) [DISCARD: Obstetric-capacity context, not a monthly registration input.] quote: "大醫院大概這5年差不多掉2、3成的出生數"
  - p195 Decline in births at large hospitals in Taiwan over the past 5 years (upper boun = **3** % (decline in births / births) (not stated (page dated 2026-08-10)) [DISCARD: Obstetric-capacity context, not a monthly registration input.] quote: "大醫院大概這5年差不多掉2、3成的出生數"
  - p196 Decline in births at primary/grassroots level in Taiwan over the past 5 years (l = **6** % (decline in births / births) (not stated (page dated 2026-08-10)) [DISCARD: Obstetric-capacity context, not a monthly registration input.] quote: "可是在基層來講大概掉6、7成"
  - p197 Decline in births at primary/grassroots level in Taiwan over the past 5 years (u = **7** % (decline in births / births) (not stated (page dated 2026-08-10)) [DISCARD: Obstetric-capacity context, not a monthly registration input.] quote: "可是在基層來講大概掉6、7成"
- `http://hk.crntt.tw/touch/detail.jsp?coluid=46&kindid=0&docid=160255313` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://fwnews.com.tw/tag/%e6%96%b0%e7%94%9f%e5%85%92/page/2/` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://rwdnews.sanlih.com.tw/news/1887028` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ieknet.iek.org.tw/ieknews/news_open.aspx?nsl_id=a993b8150b6c4f59b5ce02b47e347ed0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://hk.crntt.tw/touch/detail.jsp?coluid=46&kindid=0&docid=160245185` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 9 (period year 2026 does not appear in the page text or URL (likely mis-dated): 9)

### b1 [related_series] latest-month nowcast

Hypothesis: August 2026 monthly birth registrations are the missing latest observation. They would update the own-history series and supply an August year-on-year ratio, narrowing the May-July YoY bridge in m2 and reducing reliance on July alone.

Queries issued by the searcher: site:ris.gov.tw 115年8月 出生數; 內政部 戶政 統計 8月 出生 2026 出生數; 2026年7月 出生數 內政部 戶口統計 7月新生兒; ris.gov.tw 戶口統計 出生數 統計速報 115年; site:ris.gov.tw 115年8月 出生數; 內政部 戶政 統計 2026年7月 出生數; 114年9月 出生數 內政部 戶口統計 新生兒; 114年8月 出生數 內政部 戶口統計 新生兒 2025; site:ris.gov.tw 115年8月 出生數; 內政部 戶政 統計 8月 出生 2026; 內政部 2026年7月 戶口統計 出生數 新生兒 7月; ris.gov.tw 戶口統計資料 115年7月 出生 統計表

- `https://news.pts.org.tw/article/821731` -> **snapshot** (snapshot 20260811182642); points raw/verified 14/9
  - p198 Average age of Taiwanese women at first birth = **32** year (not stated (page dated 2026-08-10)) [keep: ] quote: "台灣女性生育第一胎的平均年齡大約落在32歲"
  - p199 Share of obstetric medical institutions closed in Taiwan over the past 5 years = **3** % (not stated (page dated 2026-08-10)) [DISCARD: Quote says '3成' (about 30%), but value is 3%; mis-scaled.] quote: "這5年來差不多關了3成的產科醫療機構"
  - p200 Decline in births at large hospitals in Taiwan over the past 5 years (lower boun = **2** % (not stated (page dated 2026-08-10)) [DISCARD: Quote says '2、3成' (20-30%), but value is 2%; mis-scaled.] quote: "大醫院大概這5年差不多掉2、3成的出生數"
  - p201 Decline in births at large hospitals in Taiwan over the past 5 years (upper boun = **3** % (not stated (page dated 2026-08-10)) [DISCARD: Quote says '2、3成' (20-30%), but value is 3%; mis-scaled.] quote: "大醫院大概這5年差不多掉2、3成的出生數"
  - p202 Decline in births at primary-care level in Taiwan over the past 5 years (lower b = **6** % (not stated (page dated 2026-08-10)) [DISCARD: Quote says '6、7成' (60-70%), but value is 6%; mis-scaled.] quote: "可是在基層來講大概掉6、7成"
  - p203 Decline in births at primary-care level in Taiwan over the past 5 years (upper b = **7** % (not stated (page dated 2026-08-10)) [DISCARD: Quote says '6、7成' (60-70%), but value is 7%; mis-scaled.] quote: "可是在基層來講大概掉6、7成"
  - p204 Highest county/city crude birth rate in Taiwan (Taitung County), per 1,000 popul = **6.06** birth registration (person)/(1000 person) (not stated (page dated 2026-08-10)) [keep: ] quote: "粗出生率最高為台東縣千分之6.06"
  - p205 Second-highest county/city crude birth rate in Taiwan (Yunlin County), per 1,000 = **5.29** birth registration (person)/(1000 person) (not stated (page dated 2026-08-10)) [keep: ] quote: "其次為雲林縣千分之5.29"
  - p206 Lowest county/city crude birth rate in Taiwan (Keelung City), per 1,000 populati = **2.1** birth registration (person)/(1000 person) (not stated (page dated 2026-08-10)) [keep: ] quote: "最低為基隆市千分之2.10"
- `https://rwdnews.sanlih.com.tw/news/1887028` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://hk.crntt.tw/touch/detail.jsp?coluid=46&kindid=0&docid=160255313` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.pts.org.tw/article/821684` -> **snapshot** (snapshot 20260819203503); points raw/verified 15/15
  - p207 Taiwan July 2026 monthly registered births = **7,906** birth registration (person) (2026-07-01..2026-07-31) [DISCARD: Duplicate of July 2026 births p1.] quote: "7月單月出生人數為7906人,折合年粗出生率為4.01‰"
  - p208 Taiwan July 2026 births year-on-year change (count) = **1,033** birth registration (person) (2026-07-01..2026-07-31) [DISCARD: Duplicate of July 2026 YoY birth change p4.] quote: "但仍較去年同期減少1033人、減少幅度達11.56%。"
  - p209 Taiwan July 2026 births year-on-year change (percent) = **11.56** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of July 2026 YoY birth change rate p5.] quote: "但仍較去年同期減少1033人、減少幅度達11.56%。"
  - p210 Taiwan June 2026 monthly registered births = **7,324** birth registration (person) (2026-06-01..2026-06-30) [DISCARD: Duplicate of June 2026 births p3.] quote: "雖較5月的6832人、6月的7324人微幅成長"
  - p211 Taiwan May 2026 monthly registered births = **6,832** birth registration (person) (2026-05-01..2026-05-31) [DISCARD: Duplicate of May 2026 births p2.] quote: "雖較5月的6832人、6月的7324人微幅成長"
  - p212 Taiwan July 2026 crude birth rate (annualised) = **4.01** births per 1,000 person (2026-07-01..2026-07-31) [DISCARD: Duplicate of July 2026 crude birth rate p6.] quote: "7月單月出生人數為7906人,折合年粗出生率為4.01‰"
  - p213 Taiwan total population at end of July 2026 = **23,235,002** person (2026-07-31..2026-07-31) [DISCARD: Duplicate of July 2026 total population p7.] quote: "全台總人口降至2323萬5002人,為連續31個月出現人口負成長。"
  - p214 Taiwan total population year-on-year change, July 2026 = **0.44** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of July 2026 population YoY change p9.] quote: "較比去(2025)年同期減少0.44%,與6月相比則減少0.04%"
  - p215 Taiwan total population month-on-month change, July 2026 = **0.04** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of July 2026 population MoM change p10.] quote: "與6月相比則減少0.04%,是連續31個月出現人口負成長。"
  - p216 Taiwan July 2026 deaths = **17,119** death registration (person) (2026-07-01..2026-07-31) [DISCARD: Duplicate of July 2026 deaths p11.] quote: "至於7月死亡人數則為1萬7119人,平均約每2.6分鐘有一人死亡"
  - p217 Taiwan July 2026 crude death rate (annualised) = **8.67** deaths per 1,000 person (2026-07-01..2026-07-31) [DISCARD: Duplicate of July 2026 crude death rate p12.] quote: "折合年粗死亡率為8.67‰,較去年同月增加1.62%,較上月增加4.77%。"
  - p218 Taiwan July 2026 deaths year-on-year change = **1.62** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of July 2026 deaths YoY change p13.] quote: "折合年粗死亡率為8.67‰,較去年同月增加1.62%,較上月增加4.77%。"
  - p219 Taiwan July 2026 deaths month-on-month change = **4.77** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of July 2026 deaths MoM change p14.] quote: "較去年同月增加1.62%,較上月增加4.77%。"
  - p220 Taiwan July 2026 marriages = **7,150** marriage (couple) (2026-07-01..2026-07-31) [DISCARD: Duplicate of July 2026 marriages p15/p297.] quote: "至於結婚對數,7月全台共有7150對,同婚占3.5%;離婚對數為4450對,同婚占1.7%。"
  - p221 Taiwan July 2026 divorces = **4,450** divorce (couple) (2026-07-01..2026-07-31) [DISCARD: July 2026 divorces are not relevant to the birth-registration target.] quote: "離婚對數為4450對,同婚占1.7%。"
- `http://dev.taisounds.news/news/content/71/287932` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `http://hk.crntt.tw/touch/detail.jsp?coluid=92&kindid=0&docid=160266835` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://gb.crntt.com/crn-webapp/doc/docDetailCreate.jsp?coluid=7&kindid=0&docid=160266835` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://rwdnews.sanlih.com.tw/news/1904770` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ieknet.iek.org.tw/ieknews/news_open.aspx?nsl_id=a993b8150b6c4f59b5ce02b47e347ed0` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.womengroups.org.tw/OnePage.aspx?tid=1&id=5245` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://turnnewsapp.com/livenews/politicsv3/20260910001998-260407` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.pts.org.tw/article/826497` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- dropped by code checks: 5 (period year 2026 does not appear in the page text or URL (likely mis-dated): 5)

### b2 [administrative] partial-period validation

Hypothesis: Early September 2026 registration counts or hospital newborn counts would allow a partial_period check for the first week of September. Even a few local office counts could show whether September is tracking the July level or the weaker May-June level.

Queries issued by the searcher: 2026年9月 出生登記 戶政事務所 新生兒; 內政部 戶政統計 2026年8月 出生登記 人數; 2025年9月 出生數 內政部戶政司 新生兒 較上月; 2026年9月 新生兒 醫院 出生 統計 台灣; 2026年9月 出生登記 戶政事務所 新生兒; Taiwan births September 2026 monthly household registration statistics; 內政部戶政司 2026年8月 戶口統計 出生數 公布; 2026年9月 出生登記 人數 戶政事務所 統計 台北市; 2026年8月 出生登記 戶政 台灣 新生兒 統計; 內政部 戶政司 出生登記 2026年7月 統計; 2026年9月 出生登記 戶政事務所 新生兒 人數; 台北市 民政局 出生登記 2026年8月 統計 新生兒

- `https://rwdnews.sanlih.com.tw/news/1904770` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://tw.news.yahoo.com/8%E6%9C%88%E6%96%B0%E7%94%9F%E5%85%92%E5%83%85%E5%89%A97492%E4%BA%BA-%E4%BA%BA%E5%8F%A3%E9%80%A332%E5%80%8B%E6%9C%88%E8%B2%A` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://taihai.fjsen.com/wap/2026-09/11/content_32251583.htm` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.chinatimes.com/campus/20251010000241-261509?chdtv` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://ocacnews.net/article/410298` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://hk.crntt.com/doc/1602/6/6/8/160266835.html?coluid=46&kindid=21991&docid=160266835&mdate=0910183009` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://bccnews.com.tw/archives/730546` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://worldnews.net.ph/post/203596` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.pttweb.cc/bbs/Gossiping/M.1759985967.A.201` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.pts.org.tw/article/774467` -> **snapshot** (snapshot 20251119042015); points raw/verified 15/15
  - p222 Taiwan September 2025 newborn births (monthly total, Ministry of the Interior) = **8,603** birth registration (person) (2025-09-01..2025-09-30) [keep: ] quote: "根據內政部統計,今(2025)年9月新生兒出生數為8603人"
  - p223 Year-on-year change in Taiwan September births, 2025 vs 2024 (decrease) = **3,189** birth registration (person) (2025-09-01..2025-09-30) [keep: ] quote: "相較去(2024)年同期減少3189人"
  - p224 Taiwan September 2025 crude birth rate (annualised) = **4.49** births per 1,000 person (2025-09-01..2025-09-30) [keep: ] quote: "今年9月出生數為8603人,折合年粗出生率為千分之4.49"
  - p225 Year-on-year decrease in Taiwan births, first three quarters 2025 vs 2024 = **16,352** birth registration (person) (2025-01-01..2025-09-30) [keep: ] quote: "今年前3季出生人數更是較去年同期減少1萬6352人"
  - p226 Taiwan total population at end of September 2025 = **23,317,031** person (2025-09-30..2025-09-30) [keep: ] quote: "截至今年9月底台灣人口數是2331萬7031人"
  - p227 Consecutive months of Taiwan population decline through September 2025 = **21** month (2025-09-30..2025-09-30) [keep: ] quote: "已連續21個月負成長"
  - p228 Share of Taiwan population aged 65+ at end of September 2025 = **19.8** % (2025-09-30..2025-09-30) [keep: ] quote: "65歲以上人口更達到19.8%"
  - p229 Super-aged society threshold share of population aged 65+ = **20** % (not stated (page dated 2025-10-10)) [keep: ] quote: "距離超高齡社會20%只差一步"
  - p230 Shin Kong Hospital monthly births when doctor first joined (range) = **150** (range 100..200) as written "100個到200個", value check pending birth registration (person) (not stated (page dated 2025-10-10)) [DISCARD: Single-hospital historical monthly birth range is not representative of Taiwan national registrations.] quote: "我剛來新光醫院的時候,我們每個月大概可以生100個到200個左右"
  - p231 Shin Kong Hospital current-year average monthly births (range) = **85** (range 70..100) as written "70到100個", value check pending birth registration (person) (2025-01-01..2025-12-31) [DISCARD: Single-hospital current monthly birth range is not a national monthly count.] quote: "目前今年的話平均大概都是70到100個左右"
  - p232 National Day (Oct 10) babies at Taipei Chang Gung Hospital, as of afternoon = **2** birth registration (person) (2025-10-10..2025-10-10) [DISCARD: Tiny one-day hospital anecdote, not a national monthly birth input.] quote: "包含台北長庚2位"
  - p233 National Day (Oct 10) babies at Linkou Chang Gung Hospital, as of afternoon = **8** birth registration (person) (2025-10-10..2025-10-10) [DISCARD: Tiny one-day hospital anecdote, not a national monthly birth input.] quote: "林口長庚8位"
  - p234 National Day (Oct 10) babies at Taipei City Hospital, as of afternoon = **2** birth registration (person) (2025-10-10..2025-10-10) [DISCARD: Tiny one-day hospital anecdote, not a national monthly birth input.] quote: "北市聯醫2位"
  - p235 National Day (Oct 10) babies at Shin Kong Hospital, as of afternoon = **4** birth registration (person) (2025-10-10..2025-10-10) [DISCARD: Tiny one-day hospital anecdote, not a national monthly birth input.] quote: "新光4位"
  - p236 National Day (Oct 10) babies at Cathay Hospital Xizhi and Hsinchu branches, as o = **1** birth registration (person) (2025-10-10..2025-10-10) [DISCARD: Tiny one-day hospital anecdote, not a national monthly birth input.] quote: "國泰汐止分院1位、新竹分院5位"
- `http://dev.taisounds.news/news/content/71/287932` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.kanglin.com.tw/news/%e5%ae%b6%e5%ba%ad%e8%a6%8f%e6%a8%a1%e6%8c%81%e7%ba%8c%e7%b8%ae%e5%b0%8f-9%e6%9c%88%e6%af%8f%e6%88%b6%e5%b9%b3%e5%9d%8` -> **snapshot** (snapshot 20260214163654); points raw/verified 15/14
  - p237 Taiwan births registered in August 2025 (monthly count) = **8,603** birth registration (person) (2025-08-01..2025-08-31) [DISCARD: Labeled August 2025 but value 8,603 matches September 2025 p85 and conflicts with official RIS August 2025 p86.] quote: "新生兒部份,8月出生數為8,603人,約每5.1分鐘出生一個嬰兒"
  - p238 Taiwan births registered in August 2025, change from same month previous year = **3,189** birth registration (person) (2025-08-01..2025-08-31) [DISCARD: Labeled August 2025 but the -3,189 YoY change matches September 2025, not August 2025.] quote: "較上年同月減少3,189人,較上月增加139人。"
  - p239 Taiwan births registered in August 2025, change from previous month = **139** birth registration (person) (2025-08-01..2025-08-31) [DISCARD: Labeled August 2025 but the +139 prior-month change matches September 2025, not August 2025.] quote: "較上年同月減少3,189人,較上月增加139人。"
  - p240 Taiwan crude birth rate, August 2025, annualised = **4.49** birth registration (person) per 1,000 person per year (2025-08-01..2025-08-31) [DISCARD: Labeled August 2025 but the 4.49‰ rate matches September 2025 p224.] quote: "折合年粗出生率為千分之4.49"
  - p241 Minutes per birth in Taiwan, August 2025 = **5.1** minute per birth registration (person) (2025-08-01..2025-08-31) [DISCARD: Labeled August 2025 but minutes-per-birth matches the September 2025 level p85.] quote: "約每5.1分鐘出生一個嬰兒"
  - p242 Taiwan deaths registered in August 2025 (monthly count) = **15,387** death registration (person) (2025-08-01..2025-08-31) [DISCARD: August 2025 deaths are not a birth-registration input.] quote: "8月人口死亡數為1萬5,387人,平均2.8分鐘死亡1個人"
  - p243 Taiwan marriages in September 2025 = **5,844** couple (2025-09-01..2025-09-30) [keep: ] quote: "9月5,844對新人結婚,4,402對夫妻離婚。"
  - p244 Taiwan total population at end of September 2025 = **23,317,031** person (2025-09-30..2025-09-30) [DISCARD: Duplicate of September 2025 total population p226.] quote: "至9月底為止全臺人口數為2,331萬7,031人"
  - p245 Taiwan population change from same month previous year, September 2025 = **87,107** person (2025-09-01..2025-09-30) [DISCARD: September 2025 population change is not a birth-registration input.] quote: "與去年同月比較減少8萬7,107人(-0.37%)"
  - p246 Taiwan population change from previous month, September 2025 = **11,312** person (2025-09-01..2025-09-30) [DISCARD: September 2025 month-on-month population change is not a birth-registration input.] quote: "較8月再減1萬1,312人(-0.05%)"
  - p247 Taiwan households at end of September 2025 = **9,837,386** household (2025-09-30..2025-09-30) [DISCARD: September 2025 household count is not a birth-registration input.] quote: "9月底戶數983萬7,386戶"
  - p248 Taiwan average persons per household at end of September 2025 = **2.37** person per household (2025-09-30..2025-09-30) [DISCARD: September 2025 persons per household is not a birth-registration input.] quote: "每戶平均人口數則降至2.37人,較去年同月減少0.13人。"
  - p249 Taiwan share of population aged 0-14 at end of September 2025 = **11.58** % (2025-09-30..2025-09-30) [DISCARD: September 2025 age-share context is not needed for the monthly birth forecast.] quote: "9月底0-14歲兒少占11.58%"
  - p250 Taiwan share of population aged 65+ at end of September 2025 = **19.8** % (2025-09-30..2025-09-30) [DISCARD: September 2025 65+ share duplicates p228 and is not a birth-registration input.] quote: "65歲以上人口比例較前月略增達到19.8%"
- dropped by code checks: 1 (value_as_written not in quote as a whole number: 1)

### b3 [forecasts_markets] annual anchor

Hypothesis: An official 2026 annual births projection or a 2026 January-August cumulative total would provide an independent annual anchor for September's seasonal share, reducing dependence on the volatile recent monthly YoY ratios.

Queries issued by the searcher: 國發會 2026 出生數 推估 人口推估; 內政部 2026年 1-7月 出生數 統計; 2025年9月 出生數 內政部 戶口統計 新生兒; 內政部 戶籍人口統計 出生數 月別 統計表 2026; 內政部戶政司 戶籍人口統計 出生登記 統計資料 全球資訊網 月報; "2026" 台灣 全年出生數 預估 11萬 新生兒 上半年 少子化 統計; 國發會 2026 出生數 推估; 內政部 2026 全年 出生 預估; 內政部 2026年8月 出生數 戶口統計 新生兒; 2025年9月 出生數 內政部 戶口統計 新生兒 11萬7812; 國發會 2026 出生數 推估; 內政部 2026年 1-8月 出生數 統計; 內政部戶政司 115年7月 戶口統計 出生數 較上月; 2025年9月 台灣 出生數 內政部 統計 新生兒

- `https://www.ndc.gov.tw/nc_27_40407` -> **snapshot** (snapshot 20260906021513); points raw/verified 15/11
  - p251 Share of population aged 0-14, NDC 2026 projection (Table 1) = **11.1** % (2026-01-01..2026-12-31) [keep: ] quote: "2026 23,191 2,577 15,756 4,858 11.1 67.9 20.9"
  - p252 Share of population aged 65+, NDC 2026 projection (Table 1) = **20.9** % (2026-01-01..2026-12-31) [keep: ] quote: "2026 23,191 2,577 15,756 4,858 11.1 67.9 20.9"
  - p253 Taiwan median age, NDC 2026 projection (Table 2) = **46.4** years (2026-01-01..2026-12-31) [keep: ] quote: "2026 46.4 3.2 47.2 16.4 30.8"
  - p254 Taiwan potential support ratio (working-age per elderly), NDC 2026 projection (T = **3.2** person aged 15-64 per person aged 65+ (2026-01-01..2026-12-31) [keep: ] quote: "2026 46.4 3.2 47.2 16.4 30.8"
  - p255 Taiwan total dependency ratio (per 100 working-age), NDC 2026 projection (Table  = **47.2** person per 100 person aged 15-64 (2026-01-01..2026-12-31) [keep: ] quote: "2026 46.4 3.2 47.2 16.4 30.8"
  - p256 Taiwan total fertility rate (TFR), 2025 actual per MOI statistics = **0.695** births per woman (2025-01-01..2025-12-31) [keep: ] quote: "依據內政部最新統計,我國總生育率於去(2025)年降至0.695人,降幅較原先預期顯著"
  - p257 NDC long-term TFR assumption, high scenario, reached by 2075 = **1.1** births per woman (2075-01-01..2075-12-31) [keep: ] quote: "高、中及低情境由前次假設2070年達1.3人、1.0人及0.8人,微調為2075年達1.1人、0.8人及0.6人。"
  - p258 NDC long-term TFR assumption, medium scenario, reached by 2075 = **0.8** births per woman (2075-01-01..2075-12-31) [keep: ] quote: "高、中及低情境由前次假設2070年達1.3人、1.0人及0.8人,微調為2075年達1.1人、0.8人及0.6人。"
  - p259 NDC long-term TFR assumption, low scenario, reached by 2075 = **0.6** births per woman (2075-01-01..2075-12-31) [keep: ] quote: "高、中及低情境由前次假設2070年達1.3人、1.0人及0.8人,微調為2075年達1.1人、0.8人及0.6人。"
  - p260 Previous NDC long-term TFR assumption, high scenario, reached by 2070 = **1.3** births per woman (2070-01-01..2070-12-31) [keep: ] quote: "高、中及低情境由前次假設2070年達1.3人、1.0人及0.8人,微調為2075年達1.1人、0.8人及0.6人。"
  - p261 Number of measures in Taiwan population strategy family-support chapter = **18** measure (2026-05-01..2026-05-31) [keep: ] quote: "並於今年5月推出「台灣人口對策新戰略-家庭支持篇」,涵蓋安心生養、強化托育、教育加碼、友善職場以及居住減壓等計18項措施。"
- `https://news.pts.org.tw/article/824643` -> **snapshot** (snapshot 20260829081337); points raw/verified 11/7
  - p262 Taiwan total population in 2045 (NDC projection, first drop below 20 million) = **20,000,000** person (2045-01-01..2045-12-31) [keep: ] quote: "2045年首度跌破2000萬人"
  - p263 Taiwan total population in 2055 (NDC projection) = **17,510,000** person (2055-01-01..2055-12-31) [keep: ] quote: "2055年只剩1751萬人"
  - p264 Taiwan total population in 2075 (NDC projection) = **12,150,000** person (2075-01-01..2075-12-31) [keep: ] quote: "50年後台灣人口剩1215萬"
  - p265 Average age of first-time mothers in Taiwan (latest) = **31.8** year (not stated (page dated 2026-08-28)) [keep: ] quote: "首胎生母平均年齡31.8歲"
  - p266 Share of women aged 15-49 in total female population in 2075 (NDC projection, up = **2** % (2075-01-01..2075-12-31) [keep: ] quote: "2075年15到49歲的育齡婦女,占全體女性比率將不到2成"
  - p267 Decline in working-age population over next 50 years (NDC projection, nearly two = **0.6667** as written "三分之二", value check pending 1 (2026-01-01..2075-12-31) [keep: ] quote: "未來50年,工作年齡人口總量將減少近三分之二"
  - p268 Year from which over half of working population will be aged 45-64 = **2,037** year (2037-01-01..2037-12-31) [keep: ] quote: "從2037年起,過半數的工作人口年齡將落在45至64歲中高齡族群"
- `https://www.chinatimes.com/realtimenews/20260828003674-261502?chdtv` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.businessweekly.com.tw/focus/blog/3022387` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://rwdnews.sanlih.com.tw/news/1897905` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.pts.org.tw/video/21583` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www3.businessweekly.com.tw/focus/blog/3022387` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.pts.org.tw/tag/3755/` -> **snapshot** (snapshot 20260617165351); points raw/verified 15/14
  - p269 Yunlin County first-quarter newborn count, 2026 = **838** birth registration (person) (2026-01-01..2026-03-31) [keep: ] quote: "但縣內第一季新生兒,經過統計僅有838名,比去(2025)年同期減少約3成。"
  - p270 Yunlin County first-quarter newborn YoY change, 2026 vs 2025 = **3** % (2026-01-01..2026-03-31) [DISCARD: Quote says '約3成' (about 30%), but value is 3%; mis-scaled.] quote: "但縣內第一季新生兒,經過統計僅有838名,比去(2025)年同期減少約3成。"
  - p271 Yunlin County 'Wanbaolong' birth program total newborns over prior 2 years = **11,000** birth registration (person) (not stated (page dated 2026-06-15)) [keep: ] quote: "雲林縣正府前2年推動「萬寶龍」生育計畫,催生出超過1.1萬多名新生兒。"
  - p272 Yunlin County cash bonus for third child onward, 2026 = **100,000** TWD (2026-01-01..2026-12-31) [keep: ] quote: "而今(2026)年計畫調整,雖然第3胎起加碼到10萬元"
  - p273 South Korea newborn count, 2025 = **254,000** birth registration (person) (2025-01-01..2025-12-31) [keep: ] quote: "2025年南韓新生兒人數突破25.4萬大關,不僅連續2年增長"
  - p274 South Korea newborn increase, 2025 = **16,000** birth registration (person) (2025-01-01..2025-12-31) [keep: ] quote: "而去(2025)年新生兒增加了1萬6000人,是從2010年增加2萬5000人以來最大規模的成長。"
  - p275 South Korea newborn increase, 2010 = **25,000** birth registration (person) (2010-01-01..2010-12-31) [keep: ] quote: "而去(2025)年新生兒增加了1萬6000人,是從2010年增加2萬5000人以來最大規模的成長。"
  - p276 South Korea total fertility rate threshold reclaimed, 2025 = **0.8** birth/(person) (2025-01-01..2025-12-31) [keep: ] quote: "總和生育率更在時隔4年後,成功收復0.8名的關鍵防線。"
  - p277 Taitung County births through November, 2025 = **1,100** birth registration (person) (2025-01-01..2025-11-30) [keep: ] quote: "今年到11月已出生超過1100名嬰兒。"
  - p278 Taitung County birth subsidy per birth, raised in 2024 = **40,000** TWD (2024-01-01..2024-12-31) [keep: ] quote: "又從去(2024)年提高生育補助到4萬元"
  - p279 Taitung County combined assisted-reproduction and egg-freezing subsidy = **120,000** TWD (not stated (page dated 2026-06-15)) [keep: ] quote: "還有不孕夫妻人工生殖和凍卵的補助共12萬元"
  - p280 Taitung County assisted-reproduction subsidy (each of IVF and egg freezing) = **60,000** TWD (not stated (page dated 2026-06-15)) [keep: ] quote: "台東縣府衝生育率 人工生殖、凍卵各補助6萬"
  - p281 Growth in number of women freezing eggs over recent 5 years (Taiwan reproductive = **30** % (not stated (page dated 2026-06-15)) [keep: ] quote: "國內生殖中心最新統計發現,近5年女性凍卵人數成長近30%"
  - p282 Number of pronatal policy items announced (Taiwan population strategy) = **18** policy item (not stated (page dated 2026-06-15)) [keep: ] quote: "共針對生育、教養與教育提出18項不同政策,並將其區分為5大面向。"
- `https://ncusec.ncu.edu.tw/news/press_content.php?P_ID=46641` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://www.chinatimes.com/cn/realtimenews/20260828003674-260410?chdtv` -> **dropped** (no snapshot <= as_of; live pages not used in backtests (as_of before fetch day)); points raw/verified -/-
- `https://news.pts.org.tw/article/821684` -> **snapshot** (snapshot 20260819203503); points raw/verified 15/15
  - p283 Taiwan total population, July 2026 (month-end level) = **23,235,002** person (2026-07-31..2026-07-31) [DISCARD: Duplicate of July 2026 total population p7.] quote: "全台總人口降至2323萬5002人,為連續31個月出現人口負成長。"
  - p284 Taiwan births registered, July 2026 (single month) = **7,906** birth registration (person) (2026-07-01..2026-07-31) [DISCARD: Duplicate of July 2026 births p1.] quote: "7月單月出生人數為7906人,折合年粗出生率為4.01‰"
  - p285 Taiwan crude birth rate, July 2026 (annualised) = **4.01** births per 1,000 person (2026-07-01..2026-07-31) [DISCARD: Duplicate of July 2026 crude birth rate p6.] quote: "7月單月出生人數為7906人,折合年粗出生率為4.01‰"
  - p286 Taiwan births registered, May 2026 (single month) = **6,832** birth registration (person) (2026-05-01..2026-05-31) [DISCARD: Duplicate of May 2026 births p2.] quote: "雖較5月的6832人、6月的7324人微幅成長"
  - p287 Taiwan births registered, June 2026 (single month) = **7,324** birth registration (person) (2026-06-01..2026-06-30) [DISCARD: Duplicate of June 2026 births p3.] quote: "雖較5月的6832人、6月的7324人微幅成長"
  - p288 Taiwan July 2026 births year-on-year change (persons) = **1,033** birth registration (person) (2026-07-01..2026-07-31) [DISCARD: Duplicate of July 2026 YoY birth change p4.] quote: "但仍較去年同期減少1033人、減少幅度達11.56%。"
  - p289 Taiwan July 2026 births year-on-year change rate = **11.56** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of July 2026 YoY birth change rate p5.] quote: "但仍較去年同期減少1033人、減少幅度達11.56%。"
  - p290 Taiwan deaths registered, July 2026 (single month) = **17,119** death registration (person) (2026-07-01..2026-07-31) [DISCARD: Duplicate of July 2026 deaths p11.] quote: "至於7月死亡人數則為1萬7119人,平均約每2.6分鐘有一人死亡"
  - p291 Taiwan crude death rate, July 2026 (annualised) = **8.67** deaths per 1,000 person (2026-07-01..2026-07-31) [DISCARD: Duplicate of July 2026 crude death rate p12.] quote: "折合年粗死亡率為8.67‰,較去年同月增加1.62%,較上月增加4.77%。"
  - p292 Taiwan total population year-on-year change rate, July 2026 = **0.44** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of July 2026 population YoY change p9.] quote: "較比去(2025)年同期減少0.44%,與6月相比則減少0.04%"
  - p293 Taiwan total population month-on-month change rate, July 2026 = **0.04** % (2026-07-01..2026-07-31) [DISCARD: Duplicate of July 2026 population MoM change p10.] quote: "與6月相比則減少0.04%,是連續31個月出現人口負成長。"
  - p294 Taiwan share of population aged 65+, end of July 2026 = **20.54** % (2026-07-31..2026-07-31) [DISCARD: July 2026 65+ share is not a monthly birth-registration input.] quote: "截自7月底,台灣年齡分布持續呈現超高齡化,65歲以上人口占20.54%"
  - p295 Taiwan share of population aged 15-64, end of July 2026 = **68.15** % (2026-07-31..2026-07-31) [DISCARD: July 2026 working-age share is not a monthly birth-registration input.] quote: "15至64歲人口占68.15%、0至14歲占11.30%。"
  - p296 Taiwan share of population aged 0-14, end of July 2026 = **11.3** % (2026-07-31..2026-07-31) [DISCARD: July 2026 0-14 share is not a monthly birth-registration input.] quote: "15至64歲人口占68.15%、0至14歲占11.30%。"
  - p297 Taiwan marriages registered, July 2026 (couples) = **7,150** couple (2026-07-01..2026-07-31) [DISCARD: Duplicate of July 2026 marriages p15.] quote: "至於結婚對數,7月全台共有7150對,同婚占3.5%"
- `https://news.pts.org.tw/tag/1774?type=new&page=2` -> **snapshot** (snapshot 20260421044251); points raw/verified 4/4
  - p298 Taiwan population decrease in 2025 vs 2024 (MOI household registration statistic = **100,000** person (2025-01-01..2025-12-31) [keep: ] quote: "據內政部戶政司統計,2025年和2024年人口相比,減少超過10萬人。"
  - p299 Taiwan monthly newborn count, February 2026, first time below 7000 = **7,000** birth registration (person) (2026-02-01..2026-02-28) [DISCARD: Duplicate context for the February 2026 record low already in p43.] quote: "單月新生兒人數今(2026)年2月更首度跌破7000人,只有6523人。"
  - p300 Taiwan monthly newborn count, February 2026 (actual) = **6,523** birth registration (person) (2026-02-01..2026-02-28) [DISCARD: Duplicate of February 2026 births p43.] quote: "單月新生兒人數今(2026)年2月更首度跌破7000人,只有6523人。"
  - p301 Taiwan male-female population gap, 2025 (males fewer than females) = **370,000** person (2025-01-01..2025-12-31) [DISCARD: Male-female population gap is not a birth-registration input.] quote: "以去年來說,男性比女性少37萬多人。"
- dropped by code checks: 9 (scale word 'thousand' not supported by quote or table header: 4; period year 2026 does not appear in the page text or URL (likely mis-dated): 3; period_end missing or unparseable: 2)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords []: no market keywords from plan markets=0


## Judge

### round 1
- corroborating: ['p1', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12', 'p13', 'p14', 'p15'] Same July 2026 MOI release: p1 gives births, p4/p5 the year-on-year change, p6 the annualised crude birth rate, and the population/death/marriage figures are context. They agree internally but are not
- corroborating: ['p2', 'p16', 'p18', 'p21', 'p22'] May 2026 release. p2 and p16 are duplicate reports of the same 6,832 May births; p18 is the April-to-May change; p21/p22 are rate and minutes-per-birth conversions. One underlying MOI series.
- corroborating: ['p3', 'p17', 'p19', 'p42', 'p43', 'p44', 'p45', 'p48', 'p49'] 2026 monthly and cumulative birth reports. p42/p43/p44 imply the record-low February and the weak January-February total; p45 is the 2025 comparator. Values are mutually consistent where periods overl
- corroborating: ['p85', 'p86', 'p87', 'p88', 'p89', 'p90', 'p91', 'p92', 'p93', 'p94', 'p95', 'p96', 'p97', 'p98', 'p114'] Official RIS/MOI 2025 monthly and annual data. The 2025 monthly values sum to p97 (107,812), and p114 plus December helps confirm the annual total. These are the cleanest target-history points.
- corroborating: ['p34', 'p35', 'p36', 'p37', 'p38', 'p39', 'p40', 'p102', 'p103', 'p104', 'p105', 'p106', 'p107', 'p108', 'p123', 'p126', 'p127', 'p128', 'p129', 'p130', 'p131', 'p132', 'p138', 'p156', 'p157', 'p158', 'p159', 'p165'] Secondary-source copies of the same 2025 monthly MOI/RIS birth registrations. They corroborate the official table but add no independent information; several are exact duplicates.
- conflicting: ['p61', 'p62', 'p63'] These are mislabelled by year. The quoted rows are 民國100/102/103 (2011/2013/2014), not 2021/2023/2024. Using them as recent annual births would be wrong.
- conflicting: ['p64', 'p65', 'p66', 'p124', 'p125'] Historical September table fragments conflict. p124's 3,189 is a decrease, not a September 2024 level; p125 says September 2025 was 27.04% below September 2024, which implies about 11,792 September 20
- conflicting: ['p136', 'p137', 'p149', 'p150', 'p151'] These are 2025 forecasts, now superseded by the actual 2025 annual total p97. They are not 2026 anchors and their miss does not directly determine September 2026.
- corroborating: ['p181', 'p173', 'p177'] September 2026 calendar evidence. p181 is the clearest: four-day Mid-Autumn/Teachers' Day break on 25-28 September 2026. Holiday closure may delay some month-end registrations, but this is a small tim
- conflicting: ['p47', 'p116', 'p117', 'p139'] Misparsed quantities. p47's 2,200 is a month-on-month decrease, not January level; p116's 三月份 means March, not three months; p117's 100,000,000 is not a monthly birth threshold; p139's 855 is an Octob
- context: ['p168', 'p169', 'p170', 'p171', 'p172', 'p192', 'p193', 'p194', 'p195', 'p196', 'p197'] Fertility-attitude and obstetric-capacity context. They describe long-run downward pressure but do not supply a monthly registration level or a September 2026 conversion factor.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p90', 'p91', 'p92', 'p93', 'p94', 'p95', 'p96', 'p86', 'p85', 'p87', 'p88', 'p89'] Official RIS monthly registered-birth series for 2025; levels are internally consistent and supply the prior-year September anchor p85 and the monthly denominators needed for YoY scaling.
- corroborating: ['p42', 'p43', 'p17', 'p2', 'p3', 'p1', 'p44', 'p45', 'p48', 'p49', 'p50'] 2026 monthly and cumulative birth observations are mutually consistent: p48 and p49 imply the February 2026 level in p43, while p44 and p45 are the January-February cumulative totals for the two years
- corroborating: ['p1', 'p4', 'p5', 'p207', 'p208', 'p209', 'p284', 'p288', 'p289'] Duplicate reports of July 2026 births and the July YoY decline; p4 and p5 are consistent with the p1 level and the prior-year July denominator in p96.
- corroborating: ['p85', 'p222', 'p223', 'p224', 'p125', 'p142'] Multiple reports agree on September 2025 registered births at 8,603 and the 3,189 YoY decrease; p142's October month-on-month increase also back-implies a September 2025 level close to p85.
- conflicting: ['p237', 'p238', 'p239', 'p240', 'p241'] These are labeled August 2025 but their values (8,603; -3,189 YoY; +139 vs prior month; 4.49‰) match September 2025 and conflict with the official RIS August 2025 level in p86. They should not be trea
- conflicting: ['p199', 'p200', 'p201', 'p202', 'p203', 'p270'] Chinese '成' percentages were parsed as percent points: '3成' means about 30%, not 3%; '2、3成' means 20-30%; '6、7成' means 60-70%. The recorded numeric values are mis-scaled and unusable.
- contextual: ['p31', 'p41', 'p97', 'p98', 'p114', 'p115', 'p118', 'p119', 'p120'] Annual birth totals and expectations document Taiwan's steep and continuing fertility decline. They support a low September 2026 level but do not directly determine the monthly registration count.
- contextual: ['p152', 'p153', 'p160', 'p161', 'p162', 'p163', 'p164', 'p15', 'p220', 'p243', 'p297'] Marriage counts provide directional context for future births, but the lag and births-per-marriage conversion are not quantified here; they are not used as a direct monthly birth predictor.
- contextual: ['p181'] The late-September 2026 four-day Mid-Autumn/Teachers' Day holiday may affect registration-office timing at month-end, so it is a reason to widen uncertainty rather than a standalone level adjustment.
- contextual: ['p251', 'p252', 'p253', 'p254', 'p255', 'p256', 'p257', 'p258', 'p259', 'p260', 'p261', 'p262', 'p263', 'p264', 'p265', 'p266', 'p267', 'p268'] NDC long-term population and TFR projections confirm a low-fertility environment, including the 2025 TFR in p256, but they are not monthly 2026 birth-registration observations.
- contextual: ['p82', 'p83', 'p84'] MOI monthly statistics have about a ten-day publication lag, and birth registration can be filed at any household office. This explains why August 2026 was not yet available at the cutoff and why regi
- contextual: ['p230', 'p231', 'p232', 'p233', 'p234', 'p235', 'p236'] Hospital-level birth anecdotes are far too small and non-representative to set the national monthly level; they are useful only as qualitative evidence of soft demand.
- contextual: ['p67', 'p68', 'p69', 'p70', 'p71', 'p72', 'p73', 'p74', 'p75', 'p76', 'p77', 'p78', 'p79', 'p80', 'p81'] Historical parity and maternal-origin data describe old birth-composition patterns; they are not suitable for direct numeric substitution into a September 2026 monthly forecast.
- contextual: ['p198', 'p204', 'p205', 'p206', 'p269', 'p271', 'p272', 'p273', 'p274', 'p275', 'p276', 'p277', 'p278', 'p279', 'p280', 'p281', 'p282'] County, hospital, and international policy anecdotes are qualitative context on pronatal efforts and regional fertility; they lack a national monthly conversion and are not used as direct inputs.

## Assumptions (proposed by the judge, validated by code)

None proposed.

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | series_auto | 7,206 | ['p94', 'p95', 'p96', 'p85', 'p2', 'p3', 'p1'] / [] | [] |  | 0.50 | B1 of 3 blocks, geometric mean of 2 methods sharing inputs; median of blocks: this block is the median |  |
| m2 | formula_mc | 7,288 | ['p85', 'p1', 'p96', 'p3', 'p95', 'p2', 'p94'] / [] | [] |  | 0.50 | B1 of 3 blocks, geometric mean of 2 methods sharing inputs; median of blocks: this block is the median |  |
| m3 | formula_mc | 7,601 | ['p1', 'p85', 'p96'] / [] | [] |  | 0.00 | B2 of 3 blocks; median of blocks: not the median (one vote, counts in the interval) |  |
| m4 | formula_mc | 6,612 | ['p85', 'p44', 'p45'] / [] | [] |  | 0.00 | B3 of 3 blocks; median of blocks: not the median (one vote, counts in the interval) |  |

- m2 coverage: the whole target
- m3 coverage: the whole target
- m4 coverage: the whole target

Method details (computed by code):

- m1 series_auto, yoy path: yoy3: last year's same month x the summed growth of the latest 3 year-on-year pairs. Members: yoy3 7,206 (base month 2025-09 = 8,603 x growth 0.8376 over 3 year-on-year pair(s): sum of these months / sum of the same months a year earlier, 2026-05: 6,832 / 8,433; 2026-06: 7,324 / 8,968; 2026-07: 7,906 / 8,939). Data window 2025-05 (p94), 2025-06 (p95), 2025-07 (p96), 2025-09 (p85), 2026-05 (p2), 2026-06 (p3), 2026-07 (p1) (7 months used, not consecutive; last month 2026-07, 2 month(s) before the target; the run of consecutive months ending there is 4 long). Calibrated 80% interval 5,921 to 8,939; own 80% width x/÷1.23 (benchmark calibration, row yoy\|pairs3\|h2 of table bench-d12f86e0-1013c974)
- m2 formula_mc: p85 * mean(p1 / p96, p3 / p95, p2 / p94); Monte Carlo P10 to P90 5,753 to 9,255; result unit (person/month) * 1 month converted to person; own 80% width x/÷1.38 (no error evidence, code's default width)
- m3 formula_mc: p1 * (p85 / p96); Monte Carlo P10 to P90 5,532 to 10,439; result unit (person/month) * 1 month converted to person; own 80% width x/÷1.38 (no error evidence, code's default width)
- m4 formula_mc: p85 * (p44 / p45); Monte Carlo P10 to P90 4,797 to 9,055; result unit (person/month) * 1 month converted to person; own 80% width x/÷1.38 (no error evidence, code's default width)
- Combination: 3 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1 + m2, geometric mean of methods sharing p1, p2, p3, p85, p94, p95, p96: 7,247 (width x/÷1.38, no error evidence, code's default width); B2 = m3: 7,601 (width x/÷1.38, no error evidence, code's default width); B3 = m4: 6,612 (width x/÷1.38, no error evidence, code's default width). Estimate = the median of the blocks.
- Interval: root mean square of the block widths x/÷1.38; Birge ratio 0.28 (not above one, so no widening); final width x/÷1.38.
- Seasonal naive baseline (not combined): 8,603 (2025-09, point p85, from m1); the estimate is -15.8% against it.

Result: central **7,247** person, 80% interval [5,260, 9,984] person, basis blocks (several routes with separate inputs: the width is the typical width of the routes' own intervals, not narrowed for their number), weight rule equal_blocks_median, weight on methods that use assumptions 0.00

Unit of the estimate: person (birth registration (person); total for 2026-09-01 to 2026-09-30)

## Published-value check (live use only)

Status: **not_checked**. not checked: backtest or scored question (as_of before today, or an official value is registered), so the target cannot have been published by as_of


## Final answer

The best computed estimate is 7,247 person (80% model-based interval 5,260 to 9,984 person) for birth-registration events recorded in Taiwan during 2026-[n]-[n] through 2026-[n]-[n], as reported in MOI monthly household-registration statistics.

Main evidence: the September 2025 level (8,603 birth registration (person)) anchors the seasonal pattern, and recent 2026 months (6,832 birth registration (person), 7,324 birth registration (person), 7,906 birth registration (person)) show a lower level; the earlier-year signal (15,246 birth registration (person) vs 19,902 birth registration (person)) is weaker. Methods m1 (7,206, weight 50%) and m2 (7,288, weight 50%) share most inputs and form one block; m3 (7,601) and m4 (6,612) are separate blocks, and the combination takes the median of blocks.

Observed: the listed monthly points. Assumed/transferred: that 2025 seasonal ratios and recent 2026 YoY declines carry into September 2026.

Biggest risk: registration-date timing and the missing August 2026 data. The most useful improvement would be August 2026 registrations.

Unit of the estimate: person (birth registration (person); total for 2026-09-01 to 2026-09-30).

Key assumptions: none (every formula input is an observed data point).

Method details (computed by code):
- m1 series_auto, yoy path: yoy3: last year's same month x the summed growth of the latest 3 year-on-year pairs. Members: yoy3 7,206 (base month 2025-09 = 8,603 x growth 0.8376 over 3 year-on-year pair(s): sum of these months / sum of the same months a year earlier, 2026-05: 6,832 / 8,433; 2026-06: 7,324 / 8,968; 2026-07: 7,906 / 8,939). Data window 2025-05 (p94), 2025-06 (p95), 2025-07 (p96), 2025-09 (p85), 2026-05 (p2), 2026-06 (p3), 2026-07 (p1) (7 months used, not consecutive; last month 2026-07, 2 month(s) before the target; the run of consecutive months ending there is 4 long). Calibrated 80% interval 5,921 to 8,939; own 80% width x/÷1.23 (benchmark calibration, row yoy|pairs3|h2 of table bench-d12f86e0-1013c974)
- m2 formula_mc: p85 * mean(p1 / p96, p3 / p95, p2 / p94); Monte Carlo P10 to P90 5,753 to 9,255; result unit (person/month) * 1 month converted to person; own 80% width x/÷1.38 (no error evidence, code's default width)
- m3 formula_mc: p1 * (p85 / p96); Monte Carlo P10 to P90 5,532 to 10,439; result unit (person/month) * 1 month converted to person; own 80% width x/÷1.38 (no error evidence, code's default width)
- m4 formula_mc: p85 * (p44 / p45); Monte Carlo P10 to P90 4,797 to 9,055; result unit (person/month) * 1 month converted to person; own 80% width x/÷1.38 (no error evidence, code's default width)
- Combination: 3 block(s), equal weight per block (methods whose inputs overlap by at least half form one block; backtest errors set widths, not weights): B1 = m1 + m2, geometric mean of methods sharing p1, p2, p3, p85, p94, p95, p96: 7,247 (width x/÷1.38, no error evidence, code's default width); B2 = m3: 7,601 (width x/÷1.38, no error evidence, code's default width); B3 = m4: 6,612 (width x/÷1.38, no error evidence, code's default width). Estimate = the median of the blocks.
- Interval: root mean square of the block widths x/÷1.38; Birge ratio 0.28 (not above one, so no widening); final width x/÷1.38.
- Seasonal naive baseline (not combined): 8,603 (2025-09, point p85, from m1); the estimate is -15.8% against it.

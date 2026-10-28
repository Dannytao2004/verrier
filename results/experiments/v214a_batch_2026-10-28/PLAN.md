# v2.14a 试跑：10 次运行的口径和记录（2026-10-28）

用户 10-27 晚：「修完以后，谷价的时候把刚刚那个 sponsor，还有 2 个过往测试过的有特点的题目，和接下来会公布的题目里选 1–2 个再跑一下。口径由你核对，并且记下你写的什么口径。思考和不思考各来一次。总共大概 8–10 次，记下。」

代码：v2.14a（修正轮只准改被点名的路线和假设，没写理由的删除由代码放回；冲突时列出两条路线的输入；去掉「fix or drop」）。
时间：DeepSeek 谷价时段，UTC 2026-10-28 10:00 起（美国中部时间 05:00）。
思考设置：关 = 全部角色不开；开 = plan / judge / repair = high，audit / unit_arbiter = low（和留出测试 3、4 相同）。

## 口径（跑之前写下，跑完不改）

### 1. sponsor（口径由我定，严格口径）

用户原问题：「美国2026年面向国际学生且支持sponsor的所有应届生岗位，包括summer intern和全职工作，今年总共有大概多少个？」

我写的题干（英文，给 agent）：

> Estimate the number of distinct job postings published in the United States during calendar year 2026 (2026-01-01 to 2026-12-31) for new-graduate roles — summer internships plus full-time entry-level positions for new bachelor's or master's graduates with 0–1 years of experience, in professional (white-collar) occupations — whose posting text explicitly states that the employer will sponsor a work visa (for example "H-1B sponsorship available" or "visa sponsorship provided"). Count each posting once even if it appears on several job boards. Do not count postings that do not state sponsorship in their text, even if the employer has sponsored visas before or ticks a "will sponsor" box on a job platform, and do not count postings that rule sponsorship out.

口径说明（中文）：
- **数什么**：2026 全年在美国发布的不同职位帖子数（流量，不是某一天在架的存量，也不是录用人数）；同一帖子在多个网站出现只算一次。
- **哪些岗位**：summer intern + 全职应届（本科 / 硕士应届，0–1 年经验，白领类职业）；不含钟点工、服务业的 entry-level。
- **什么算支持 sponsor**：帖子正文里明说会办工作签证（严格口径）。雇主在平台上勾选「可以担保」、或历史上办过 H-1B 但帖子没写的，不算；明说不担保的不算。
- **为什么选严格口径**：10-27 复盘里三次运行的分歧主要来自这里（正文明说 0.1–0.3% 对平台勾选 2.6%，差约 10 倍）；严格口径有可核对的实测比率。宽口径这次不跑。

### 2. 台湾 9 月出生数（回测，题干不改）

> Assume today is 2026-09-08. … Estimate the number of births registered in Taiwan in September 2026, as reported in the Ministry of the Interior's monthly household registration statistics.

核对：口径清楚（内政部户籍登记的当月出生数，官方月报）。真值 7,704（2026-10-08 公布）。为什么选：明天演示的题；以前 agent +1.1% / +3.3%，直接问 +42.8%。

### 3. 德国 9 月新车注册（回测，题干不改）

> Assume today is 2026-09-05. … Estimate the number of new passenger cars (Pkw) registered in Germany in September 2026, as it will be first reported in the Kraftfahrt-Bundesamt's (KBA) monthly press release on vehicle registrations.

核对：口径清楚（KBA 月度新闻稿首发的 Pkw 新注册数）。真值 256,774（2026-10-05）。为什么选：单位和修正轮的「问题户」（v2.11g 回归 −69%、留出测试 2 −99.9%）；v2.13a 带期间单位只在探针里验证过（236,815），没跑过整题。

### 4. 英国 9 月轿车产量（留出测试 4，首发前跑，题干不改）

> Assume today is 2026-10-28. … Estimate the number of cars manufactured in the United Kingdom in September 2026 (total car production for home and export markets, excluding commercial vehicles), as it will be first reported in the Society of Motor Manufacturers and Traders' (SMMT) monthly UK car manufacturing release.

核对：口径清楚（只算轿车，不含商用车；SMMT 首发值）。首发 2026-10-29 00:01 UK。为什么选：上一轮（v2.13b）关思考 51,144，锚在被 JLR 网络攻击压低的 2025 年 9 月上，假设单位 % 被 ÷100（S78）；开思考 65,782。

### 5. 英国 9 月住宅交易（留出测试 4，首发前跑，题干不改）

> Assume today is 2026-10-28. … Estimate the number of UK residential property transactions (with a value of £40,000 or above) in September 2026, seasonally adjusted, as it will be first reported (provisional estimate) in HM Revenue & Customs' monthly release …

核对：口径清楚（≥£40,000，季调，首发的临时数）。首发 2026-10-30 09:30 UK。为什么选：上一轮关思考裁判输出在 24,000 处截断、没出数（S76）；v2.13d 放宽到 96,000 以后第一次重跑。

## 运行记录

（跑完填：每次的估计、区间、误差 / 待打分、花费、用时、修正轮做了什么、代码退回了什么）

| # | 题 | 思考 | 结果目录 | 估计 | 80% 区间 | 误差 | 花费（token / 含假设搜索费） | 用时 | 修正轮 |
|---|---|---|---|---|---|---|---|---|---|

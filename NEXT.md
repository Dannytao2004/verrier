# 断点（2026-10-16 晚，第一轮修复）

当前代码：tag `v2.6d`（fc11b6c）。第一轮修复按 `FIX_PLAN.md` 做（决定 D1–D9、第 3 节模块约定、第 4 节门槛 G1–G8、第 6 节本轮不做），
原则是只修不加功能、模块的输入输出约定不变（公开签名和返回结构不改，state.json 只追加键）。
每条问题现在的状态见 `BUGS.md` 的「本轮状态」列（另补了 N1–N46 和本轮新发现的 R1–R14）；阶段状态见 `docs/structure.html` 第 5 节。
阶段报告在 `probes/out/stages/S0.md`–`S8.md`（被 gitignore，只在本机）：每份写了改了什么、改到的函数和上下一层的输入输出、改前 / 改后示例、
门槛的命令和关键输出、和计划的出入、发现但没改的事。
全程离线：没联网、没调模型、没读 `.env`；`results/`、`data/` 一个字节没改（每个阶段 G8 有文件快照）。

## 做完的阶段（每个都过了 G1–G8 才打 tag）

| 阶段 | tag | commit | 改了什么 | 测试数 |
|---|---|---|---|---|
| S0 | `tools-regress-v1` | 590bb8f | `probes/recheck_continuous.py` 加 `--code` / `--json` / `--diff`、全量回归表（40 行）和终稿 lint；`tests/test_agent.py` 的 `__main__` 守卫挪到末尾（N45） | 240 |
| S1 | `v2.5.3` | 7fef548 | `config.MAX_TOKENS` 一张表（值不变），final 显式传参；Z90 / MC_N / MC_SEED 改为引用；state.json 追加 `settings`（N1、N6）。这一步的 commit 是父会话做的（第一次运行的 commit 步骤拒绝了） | 247 |
| S2 | `v2.5.4` | 188004c | 假设的 unit 带 % 就按百分数换算（`assumptions.is_pct`），unit 原文保留用于显示（N17） | 260 |
| S3 | `v2.5.5` | 19a71fa | 先拿并发名额再预扣（N2） | 264 |
| S4 | `v2.6a` | 8a19c18 | searcher 上限 2048 → 8192；n_search_errors 认 list 里的错误块（N24、N25） | 267 |
| S5 | `v2.6b` | 7559140 | 裁判第 2 轮表格（D1 / N11）；量纲规则的报错点名每个输入（B5 的一部分）；回复示例补 role（N15） | 273 |
| S6 | `v2.6c` | 2767296 | 回测时查询词命中登记值的方向整个作废（D3 / C2）；k / M 写法后面加字母边界（N31） | 280 |
| S7 | `v2.6d` | fc11b6c | 终稿数字出口（D4：F1、F2、N32–N34）；`run.score_all` 去掉「去年同月」臂（N44） | 290 |

每个阶段的门槛结果：G1 全过，没有本来就失败的测试；G3 回归表 40 行对上一个 tag 0 差异、7/7；G5 内存里的 `showcase.build()` 和已提交的
`results/showcase/summary.json` 逐字节相同（37026 字节）；G7 冻结路径 diff 为空、`check_naive` 源码 sha256 不变；
G4 有差异的只有 S2（4 个 key，都是韩国 showcase1 的 a2 换算）和 S5（22 个 key，都是量纲报错多出的输入说明），报告里逐个解释了。

## G2 的 sha256（`probes/compare_continuous_prompts.py`，假模型跑一遍连续题的全部 prompt）

| 适用的代码 | sha256 | 为什么变 |
|---|---|---|
| web-v0.3、S0–S4 | `4a56d5864fe6d024d5f91e79a3b878b2ccd3687de2797ff9d9222a7eea56e9b6` | 原值 |
| S5、S6（`v2.6b`、`v2.6c`） | `c96dc2faeffecd6f9bb876b0f4d0e2634c0d85dd95f5eb3359db55e484db2d92` | S5 改了 JUDGE_USER 的两处：任务 2 那句（「没列出 = 保留」只对表格里的点）、回复示例 m2 的 inputs 补 role。8 个 prompt 里只有 judge:r1、judge:r2、judge:r2:repair 的 user 变了；假裁判第 1 轮不丢点，所以没有紧凑段 |
| S7 起（`v2.6d`；S8 工作区的代码也是这个值） | `bbcfa3b1da2ff3d90cf24d9f9c4473ab81e1406d79efab9aef58072ffc52649a` | S7 改了 FINAL_SYSTEM 的例外句（离 as_of 10 年内的年份、Q / H 标签、方法 id、「- assumption」「- observed point」行列出的 id）和 FINAL_USER 两处，final 的输入多了 observed point 行和 `p{n}_value` 占位符。只有 final 这一个 prompt 和 `final` 记录变了 |

S7 返工前登记过的 `85e10616…`、`c04dd0ec…` 都已作废。之后不改 judge / final prompt 的阶段应该仍是 `bbcfa3b1…`。

## 没做完的

- **S8（`v2.6e`，中日韩数字和日期：N26、N27、C1 的解析部分，也是 B1 的主因）停在核查**。代码改完了，在工作区、没提交：
  ` M triangulate/agent/evidence.py`、` M triangulate/agent/pipeline.py`、`?? tests/test_cjk_numbers.py`（24 个测试；全量 314 个全过；G2 仍是 `bbcfa3b1…`）。
  第三轮之后的核查退回 2 条，都是 `probes/out/stages/S8.md` 第 2 节输入输出表的文字错误，代码不用动：
  1. 第 146 行「`leak_forms` 多 6 个（1 亿以上 8 个）中日韩精确写法」不对：每种字形登记「不分隔」和「千分位」两种写法，各段都不到 1000 时两种相同，去重后只多 3 个
     （例：7,180,000 只多 718万 / 718萬 / 718만）。应写成「对 |n| ≥ 1 万的整数最多多 6 个，1 亿以上最多 8 个，两种写法相同时去重」。
  2. 第 142 行的 `compute._point_years`（`compute.py:75`）不存在，应为 `compute._span`（`compute.py:74-77`，`build_series` 和 `published.candidates` 都经过它），再加上 `compute.run` 的目标期间（`compute.py:136-137`）。
  下一步：改这两行 → 再核查 → 显式 add 这 3 个文件提交、打 `v2.6e`。S8.md 第 8 节有要用户定的事：千 / 천 要不要支持；
  中日韩的四舍五入写法（344万、13.4萬）登不登记哨兵（和 C3 一起定）。另外，S8 的新哨兵下 S6 的「47 个里正好 5 个作废」会变成 6 个（S8.md 第 4.3 节）。
- **S9（`v2.6f`，页面解码顺序 + zstd）没开始**：依赖 S8（先能解析再能解码，否则中日韩数字会悄悄小 10^4 倍）。
- **S10（`v2.6g`，key 不跟随跳转）没开始**：只依赖 S1，可以单独做。注意 N30 的证据位置是 `agent/search.py` 自己调的 `urlopen`，不在 S10 的文件列（`llm.py`、`jev.py`）里。
- **收尾 `fixround1-docs`**：这次更新了 BUGS.md、NEXT.md、docs/structure.html 并提交；S8–S10 没做完，所以没打这个 tag。

## 等用户定的事（FIX_PLAN 第 6 节、D5–D8）

- **S11 重跑 7 道开发 / 留出题**（约 $3.45）：要联网花钱，等批准（D7）。离线检查只证明已存结果不变；S4 的 8192、S6 的方向作废、S7 的终稿规则对真实运行的效果都还没验证。
  重跑以后 tw、lhr、jp_births 三道留出题只能算开发数据（部分修复的依据来自它们自己）。挑错意见建议命令固定为 `--arms full`
  （`probes/run_v2_backtests.py` 默认 `--arms both`，会把消融版也跑一遍，费用翻倍）。
- **B0 展示集打分**：10-21（JNTO）、10-28（韩国出生）公布后，各登记一次官方值、`python -m triangulate showcase` 打分并提交。
  登记 JNTO 真值时 `tests/test_showcase.py:58-59`（断言未公布题的 answer_value 为 None）会失败，要同时改测试。冻结路径（G7）到 10-28 打分提交为止不能动。
- **结构化基线修复（G1、G2、N38–N41）等 10-28 打分提交之后**（D5）：先处理「每千人」双重换算（N38），再改量纲报错的反馈；规则不放松；补充运行另存。
  之后 G5 的口径要改成只比较数值字段（errors 文字会变）。
- **区间规则放到 v2.7**（D6；A1–A7、B2、B3、N18–N23）：先定新的预注册（Winkler interval score、≥ 10 道新留出题、其中 ≥ 3 道非英文），再只用开发集调。本轮只改了标签。
- **Kalshi**（D8）：没补查，记为和预注册不一致（预注册要求的补查只能在 2026-10-16 UTC 当天做；这是新的外部 API，没批准）。
- 要联网核实、本轮没做：searcher 的 thinking / temperature（N4）、搜索单价（G7）、deepseek-flash 的输出上限。

## 发现了、这次没改的文档问题

- `docs/structure.html` 是按 6226d9e 生成的快照，这次只改了阶段状态和表下那行说明。页面里还有几处过时：第 5 节的「编号对照」框和「读这页时要注意」的前两条说
  FIX_PLAN 第 3 节的阶段编号、parse_value 的返回值写错了，这两处在 dea7efa、cb6db0e 已经改了；门槛 G2 的引文还是旧编号「S6、S8」（FIX_PLAN 现在写的是 S5、S7）；
  第 2、3、4 节还写着 `JUDGE_MAX_TOKENS`（S1 已删；`grep -n JUDGE_MAX_TOKENS docs/structure.html` 命中 140、453、468、469 行）。
- `docs/prompts_bilingual.md` 和 `probes/gen_prompts_bilingual.py` 的中文对照没跟上 S5、S7 改过的 prompt（BUGS.md R13）。
- `AGENT_MVP.md:25` 写每个方向最多 5 个 URL，代码是 4（BUGS.md N46）；下面 v2.5 未解决问题第 7 条的「默认的 60 s 超时」不准（BUGS.md C8）。

---

# 断点（2026-10-16，第一轮修复之前；下面是当时的原文）

当前代码：tag `v2.5.2`（agent，1bd2077，没改）+ arm (3) 联网直接答（`showcase-arm3`，3d57649；补充运行用的 max_tokens 参数 447c66a）
+ 展示集汇总 `triangulate/showcase.py`。测试见展示集结果的提交。

## 展示集 showcase1（2026-10-16，中期）：结果在 `SHOWCASE.md`

- 已公布 2 题：NHS A&E 9 月 agent 2,447,480（+0.3%，区间盖住；结构化 −0.7%，直接问 −13.9%）；日本 8 月移动者 agent **没有估计**
  （直接问 +12.1% 赢，结构化也没有估计）。未公布 2 题的预测已记下，10-21（JNTO）、10-28（韩国出生）公布后登记官方值、
  `python -m triangulate showcase` 打分。成功标准按 4 题定义，现在只能报中期数字。
- arm (3) 预注册运行两题都没给出数（max_tokens 4096 是实现失误），记为失败；只改 max_tokens 的补充运行不进标准，单列。
- NHS 题的 searcher 搜索词里出现了真值「2.44 million」（搜索不能限定日期），结果带保留。
- 这次发现的 7 个问题（非英文统计取证、变化率当水平值、searcher 看到答案、假设和理由矛盾、公式常数、arm (3) 的 max_tokens 和
  重试、series_naive = 去年同月进入答案）见 `SHOWCASE.md` 末尾，下一轮先定再改。

`v2.5`（f5b3c79）是 published2 实测用的代码；v2.5.1 多一处提前停的检查，v2.5.2 修了审查的两条中等意见（见下）。上一版 `v2.4.1`（4165105）的记录在下面。

## v2.5：真实使用直接抓 live 页 + 确认已公布就提前停（2026-10-16 批准的范围）

- 抓取（`fetch.fetch_live`、`net.get_live`）：真实使用（as_of 是今天、没有登记真值，条件同 `run.checks_published`）时只抓 live 页，
  不调 `cdx_lookup`、不请求 web.archive.org。页面超时 15 s、robots.txt 10 s，连接失败和 429/503 都不重试、不退避（回测仍是 90 / 45 s
  加 10 / 30 s 退避）。一个方向的 URL 同时开抓（`pipeline._live_pages`），按 URL 顺序抽取（点的编号可复现）；每个 host 请求开始
  至少隔 1 秒（或 Crawl-delay）、每个 host 最多 4 个连接、robots 规则都没改（`net.LIMITER`）。live 页的收下条件不变：读得出日期且
  <= as_of、正文没有晚于 as_of 的显式日期；quote、数字、倍数词、期间年份的核对不变。
- 提前停（`published.EarlyWatch`，真实使用、连续值目标、非消融）：每页核对完，把这一页的新点（临时 id e1 ...）按 v2.4 的候选规则
  （`candidates(judged_only=False)`，不要求裁判看过）选候选，有候选就调一次 v2.4 的确认（role `published:early`）。第一次 resolve 出
  published 就停：其余子 agent 不再搜索 / 抽取，裁判节点只编号（临时 id 换成 p 编号），不调裁判、不算 compute，直接 final；终稿由代码写，
  末尾写明「No estimate was made ...」。确认的值互相矛盾（conflict）就关掉提前检查，照常走裁判、估计和 v2.4 的检查。
  记录：`state.json` -> `published`（`early_stop: true`）和 `published_early`（每次检查）。离散目标不提前停（结果列表由裁判定义）。
- 回测：`fetch_page` 的快照路径没改。`probes/compare_continuous_prompts.py` sha256 仍是 4a56d586…，`probes/recheck_continuous.py` 7/7。
- 离线测试 15 个（`tests/test_live.py`）：live 路径不请求 Wayback、不调 cdx_lookup、超时短、不重试；日期 / robots / http 状态的丢弃
  原因；回测的 fetch_page 只请求 web.archive.org（有快照、没快照两种）；一个方向里不同 host 同时抓、同一 host 的请求开始间隔不小于
  限速间隔、robots 禁止的 URL 不请求；回测方向走 fetch_page；提前停（裁判 / 核对 / 终稿模型 / 别的方向的抽取都没调）；没确认时
  裁判之后的 prompt、points、judge_rounds、compute、published、final 与关掉提前检查逐字相同；conflict 关掉提前检查；回测、离散不提前停；
  只送新点；prepare_run 的开关。
- v2.5.1（ed077f0）：published2 里 d5 在提前停时正在等第一页，取回后照样抽取了（多 1 次抽取、约 7 s，跑在最后）。现在取页返回后再查
  一次。新测试在 v2.5 上失败、在 v2.5.1 上通过。**v2.5.1 没有真实运行复测**；按 published2 的调用记录估计会省掉这 1 次抽取
  （$0.004）和约 6 s（未实测）。
- v2.5.2（1bd2077）：审查 v2.5 / v2.5.1 的 10 条意见，2 条中等已修（下面两条），8 条低的记进下面未解决问题 9–16。**没有真实运行复测。**
  - 走不走 live 只在 prepare_run 时定一次（中等，已修）：`fetch_live` 自己不查 as_of >= 今天，运行跨过午夜、网页上隔天才批准
    （awaiting_approval 没有超时）、命令行停在 input() 过夜时，as_of 已早于取页当天仍抓 live 页（fetch.py 文件头说的那种泄漏）。
    现在 `fetch_live` 每次取页再判断，as_of 早于今天就按回测走 `fetch_page` 的快照路径（同 v2.4.1 每次取页的 allow_live），
    页面记录带 `live_skipped`。审查的复现（今天 10-17、as_of 10-16、页面日期 10-05）不再收成 live_dated。批准时没有重算
    check_published / live_fetch：取页这一层已经挡住；这时的提前检查和 v2.4 检查看的是日期 <= as_of 的快照页，前提仍成立。
  - 提前检查出错后另一页一确认就停（中等，已修）：出错（transport、两次输出无效、预算）那次的候选不算送过，和下一页的候选一起
    再送一次，resolve 因此看得到矛盾的值（审查复现：340,000 那次出错、350,536 确认，现在判 conflict、关掉提前检查；值一致时照样停，
    note 写「re-sent k candidate(s) from failed early check(s)」）。`published_early` 加 `by_status`、`n_error`，每次检查加
    `resent_ids`；有检查出错时账本那一行写出每种状态的次数。终稿没改：停下的那次检查已经看过出错页的候选。最后一次检查出错时
    没有下一次，照旧由裁判之后的 v2.4 检查兜底。
  - 新测试 2 个（在 v2.5.1 上失败、现在通过）；`tests/test_live.py` 里已有的 fetch_live 调用改为显式给「今天」，并发测试的 as_of
    用真的今天（否则日期一过就走快照路径）。223 个测试全过；`probes/compare_continuous_prompts.py` sha256 仍是 4a56d586…，
    `probes/recheck_continuous.py` 7/7（回测路径不变）。

### 实测 published2（2026-10-16，代码 f5b3c79 = v2.5，--auto-approve）

| | published1（v2.4） | published2（v2.5） |
|---|---|---|
| 结果 | published 350,536（p52 fleetnews live 页） | published 350,536（p62，同一篇 fleetnews live 页，页面日期 2026-10-05）；没有做估计 |
| 总用时 | 1631.9 s | **37.7 s** |
| 成本 | $0.4601（token $0.1401 + 假设搜索费 $0.32） | $0.3845（token $0.0845 + 假设搜索费 $0.30） |
| 调用 | 41 | 18（plan 1、search 8、extract 8、published:early 1） |
| 抽取的页 | 29（13 快照 + 16 live） | 8（全是 live；每个方向 1 页） |

用时拆分（`probes/time_split.py`；各方向并行，「跨度」= 这一阶段第一次开始到最后一次结束，括号里是从运行开始算的秒数；
原点和 wall_s 的原点不同、时刻只到秒，括号里的数和跨度误差约 ±1 s，见未解决问题 16）：

| 阶段 | published1 | published2 |
|---|---|---|
| plan | 14.2 s | 13.5 s |
| search（8 次） | 跨度 14.7 s（合计 76.0 s） | 跨度 12.9 s（合计 70.1 s；14.0–26.9） |
| fetch | 没有逐页记录；最后一次搜索结束到最后一次抽取开始 1558 s（CDX 多次 503 / 504、Wayback 单连接） | 8 页记录：跨度 11.8 s（19.0–30.8），合计 10.9 s，最慢 3.78 s（kba.de） |
| extract | 29 次，合计 151.7 s，跨度 1342.6 s | 8 次，合计 51.9 s，跨度 17.4 s（21.0–38.4） |
| 已公布检查 | 1 次 2.7 s（裁判之后） | 1 次 2.0 s（27.0–29.0，d8 的第一页） |
| judge / audit / final | 34.2 s / 1.7 s / 不调 | 都不调 |

- 第一次检查（d8 的 fleetnews 页）有 5 个候选：总数 350,536 判 target，fleet / business / BEV 分项 4 个判 different；确认后约 9 s
  全部方向停下（最后是 d5 的那次多余抽取，见 v2.5.1）。
- 取页数：每个方向搜完就把它的 4 个 URL 同时开抓，共 32 个（20 个不同 URL）；state.json 只记了抽取过的 8 页；停下后别的取页在后台跑完，
  data/raw 里这次运行写入了 18 个不同的已收下页面（按文件修改时间数）。HTTP 请求总数（含 robots 和重定向）没有记录。
- 报的版本取决于谁先抽取完：d6 的 parliamenttoday 页（页面日期 2026-10-02，350,518，「preliminary figures published today by SMMT」）
  的抽取比 d8 晚结束（calls.jsonl 的开始时刻只到秒，差多少算不准），交给检查时 d8 的检查正在进行，确认后就停了，没被检查。两个值相差 0.005%，同一次检查里也会判一致；**哪个是 SMMT 的正式数，仍未核实**。

### v2.5 的未解决问题（open problems）

1. 先到先得：提前停报的是第一页确认的值，之后到的版本（published2 的 350,518）不再看；v2.4 那种「所有保留的点一起看、相差 > 0.5% 记
   conflict」在提前停时只覆盖第一页之内。可能的做法：确认后再等几秒收齐已在抽取的页，或停下前把已核对的候选一起送一次。要先定。
2. 停下后的取页不进 state.json：published2 的 32 个 URL 只记了 8 页，其余后台跑完（15 s 是 socket 超时，不是每页总时限，见 12），页面写进 data/raw。
   可能的做法：停下时把没抽取的 URL 记成「stopped early before extraction」并带上取页结果。
3. 同一个 URL 被几个方向各抓一次：published2 里 parliamenttoday 6 次、fleetnews 5 次（限速排队，但多占请求和时间）。没有每次运行的
   live 页缓存（v2.5 范围外，没做）。
4. live 页必须读得出日期（沿用的规则）：以前没日期的 live 页可能由 Wayback 快照救回，现在直接丢。published2 记录的 8 页都有日期；
   对别的题漏了多少，没有测。
5. 网页进度页：提前停时 compute 卡片不更新（compute 由裁判节点写，进度页只看 compute 节点），裁判一栏显示「没有完成：published value
   confirmed early; judge not called」；停下的方向显示 stopped。网页没改。
6. 离散目标不提前停（结果列表要裁判定义）；离散题的已公布值仍要等到裁判之后的 v2.4 检查。
7. markets 节点（Polymarket）在真实使用时仍用默认的 60 s 超时和重试，裁判要等它；published2 里没拖慢（没有逐项计时）。
8. 现在最慢的是两次模型调用：plan 13.5 s、search 跨度 12.9 s（最慢一次 12.95 s），合起来约占 published2 的 70%。

v2.5 / v2.5.1 审查的低优先级意见（2026-10-16；机制都对着代码核实过，没改；探针的计时、published2 的页数和文件时刻引自审查，没有重跑）：

9. 提前检查的汇总状态只有 published / off / not_confirmed：全部检查出错也记 not_confirmed（v2.4 检查照常跑，结果不受影响）。
   v2.5.2 起账本那一行会附上「by status: error k」，状态词本身没改。可能的做法：有 error 且没确认时记 error。
10. Crawl-delay 的第一跳：取 robots.txt 时 `LIMITER.wait` 已按 1 秒排好这个 host 的下一次，`set_interval` 只改间隔、不往后推，
    所以 robots.txt 和第一次页面请求只隔 1 秒（审查探针，Crawl-delay 3：0.0 / 1.0 / 4.0 / 7.0 s）。v2.4.1 以前就有，v2.5 每次 live
    取页都经过这里；README 的「or the robots.txt Crawl-delay」这一跳做不到。可能的做法：HostLimiter 记每个 host 上次开始的时刻，
    set_interval 时把下一次推到 上次开始 + Crawl-delay。
11. 停下后的取页并没有取消：线程池大小 = 预留的 URL 数，submit 时每个任务都已有线程，`shutdown(cancel_futures=True)` 一个也取消
    不了（停下后所有 URL 照样发 robots 和页面请求，照样限速）；方向线程在 `fut.result()` 上等当前这页，期间不看 stop，图的屏障要等
    最慢的那次取页（published2 的 d5 在停下后又等 kba.de 约 1.8 s）。`pipeline._live_pages` 的 docstring「没开始的抓取取消」不准。
    可能的做法：`_timed_live` 开头查 stop；主循环用 `concurrent.futures.wait(timeout=0.5)` 轮询 stop；net 每一跳前接受取消回调。
12. `LIVE_TIMEOUT_S = 15` 是 urllib 的 socket 超时（连接、每次 recv 各算），不是整页总时限：慢慢吐字节的服务器（最多 6 MB）一页可以
    远超 15 s（审查探针：每 0.5 s 写 10 字节共 8 次，timeout 1 s，用时 4.01 s），再加最多 4 跳重定向和每个新 host 先取 robots.txt
    （10 s）。README 的「short timeouts (15 s per page ...)」不准。可能的做法：分块读、每块后查总截止时间；get_live 对整次调用
    （含重定向）加总时限，再改 README。
13. 一个方向的页名额在开头全部预留，只有提前停那条路会退还；`_process_page` 抛异常（BudgetExceeded，或取页 / 转文字里没捕获的
    异常）时剩下的不退，`budget.pages_used` 偏高（审查复现：4 个 URL、抽取抛 BudgetExceeded，pages_used = 4，旧的顺序循环为 1）。
    运行已中止，只影响 state.json 的 pages_used 和用它的统计。可能的做法：finally 里退还还没进 `_process_page` 的名额。
14. live 模式的 robots.txt 只试一次（10 s），取不到（599 / 5xx）就全部禁止，并且永久写进进程级缓存 `_ROBOTS`（没有 TTL）：网页
    服务这种长进程里，一次网络抖动会让这个 host 在之后所有运行里都记「live fetch blocked by robots.txt」，直到重启。保守，不违反
    robots。可能的做法：599 / 5xx 只缓存约 10 分钟，200 / 404 照旧长期缓存。
15. live 页的存盘文件名只由 url + 'live' 决定：几个方向（或同一方向的并发线程）抓同一 URL 时后写的覆盖先写的，同时写还可能互相截断；
    各方向 state.json 的 raw_path 不一定是它当时抽取的那份字节（live 页在一次运行里可能改过数）。published2：fleetnews 的
    02da71950dfcce99.raw 由 d8、d2、d7 先后写入，文件时刻是 d7 那次；三份 text_chars 都是 3810，没看到损坏。可能的做法：文件名加
    sha1(body)，临时文件 + os.replace 原子写，raw_path 记实际写入的文件。
16. `probes/time_split.py` 的原点：from_start_s 以 started_at 为原点（prepare_run 开头取、截到整秒），wall_s 却从 prepare_run 结束时的
    t0 算起；calls.jsonl 的 at 和 fetch_at 也只到秒。所以上面用时拆分表的「extract 21.0–38.4」超过了总用时 37.7 s，跨度写到 0.1 s，
    误差其实约 1 s（审查反推：原点比 wall_s 的原点早约 0.74–1.0 s；其余数字审查逐项对过文件）。可能的做法：state 记毫秒精度的 t0，
    at / fetch_at 用 timespec='milliseconds'，time_split 用同一原点。

## v2.4.1：「答案已公布」候选规则的审查修复（离线，未调模型）

审查 v2.4 的 9 条意见：2 条中等已修（下面两条），7 条低的记进下面「答案已公布」的未解决问题 10–16。

- 候选不看日期和 quote（中等，已修）：页面日期（快照 = 快照日期）或页面写明的发布日期早于目标期末的点直接排除
  （`_dated_before`；日期不完整时取最晚可能的日期，期末当天不排除）；quote 里数值所在的那一段（逗号 + 空格、分号、冒号、括号、
  句末标点、破折号之间）有预测 / 预期词（forecast、projected、predict、expect、consensus、anticipat、outlook、will be、on track，
  按词首匹配，所以 unexpectedly 不算）也排除（`_forecast_quote`）。涨跌词不看（实际值的 quote 常写「rose 12% to 350,536」）。
  说明里记「k point(s) ... excluded as dated before the period end or quoted as a forecast」。
  审查的复现（页面日期 2026-08-20、「SMMT expects around 340,000 ...」）现在不进候选；只改日期或只改 quote 的两种也不进。
- 实体词把量词和发布方当实体（中等，已修）：句首的大写词组后面紧跟 of / in / for / at / on、后面还有别的专名词组时，它算量的名字，
  它的词、整个词组、缩写和 what 里同样的全大写缩写都不算实体词（'Real GDP of France ...' -> ['france']）；发布方的写法
  （publisher_terms）只从第一个子句以外来的全大写缩写里去掉（'..., as reported by SMMT' 的 smmt；第一个子句里的
  'the next FOMC meeting' 的 fomc 保留）。一个实体词都没有时说明写「none (no entity constraint)」。README 改成如实描述：这一条只是粗筛。
  审查的两个复现（Germany real GDP 进了 France 的候选；SMMT UK 总数进了 Scotland 的候选）现在都不进。
- 已保存目标的实体词变化（33 个不同的 what / publisher）：UK 题去掉 smmt，日本两题去掉 jnto / mhlw，韩国题去掉 kostat，
  Yellowstone 题去掉 nps；FOMC 题不变（['fomc', 'us']）。published1 的 35 个候选和送去确认的前 20 个（id、顺序）与 v2.4 相同，
  确认 prompt 只由 target、as_of 和候选决定，所以也相同（calls.jsonl 不存 prompt，没有逐字节比）。
- 全部保存运行的 1827 个保留点里，quote 规则命中 19 个不同的 quote：经济学家预期（90,000 / 3.6% / 0.2%）、「markets ... expect
  the FOMC to hold ... 3.75% and 4%」、施工延误「expect delays of ...」、问卷「81% expect ...」，以及两个误伤：
  「18 participants submitted projections」（不是目标值）和韩国总和生育率的定义句「The number of babies a woman is expected to have
  ... increased to 0.8」（见未解决问题 4）。
- 离线：`probes/recheck_continuous.py` 7/7 相同；`probes/compare_continuous_prompts.py` 的 sha256 仍是 4a56d586…（回测路径不变；
  回测不调这一检查）。新测试 2 个（`tests/test_published.py`），在 v2.4 代码上失败、在 v2.4.1 上通过；`test_terms` 的期望改成
  ['uk', 'united kingdom']。

## v2.4：答案已公布（只在真实使用时）

起因：ask_fa4b4c74（英国 2026 年 9 月新车注册，as_of 2026-10-15）找到并保留了 SMMT 的 350,518，却和「去年同月」方法 50/50 平均成 331,271。

- 触发（`run.checks_published`）：as_of 是今天（或更晚）且题目没有登记真值。回测和留出题一律 `not_checked`、不调模型
  （测试逐题核对了 forecast.py 的全部 7 道题）。对象构造的 Context 默认关。
- 候选（代码，`published.py`）：裁判看过并保留的点里，期间 = 目标期间（同年、期末和期长各差 <= 3 天）、name 里有目标实体词
  （what 第一个子句的大写专名词组：整个词组、首字母缩写、非通用类别词；what / publisher 里的全大写缩写）、name 或 unit 和目标量
  有共同词干、% 与非 % 一致、不是概率 / 预测 / 预期 / 变化（名字里的词）或百分点 / 基点。按共同词干数排序，最多 20 个。
- 确认（模型一次，role `published`，形式同输入核对）：每个候选回 `target` / `different` 和理由；数字取自数据点，模型回复里的数字不用。
  prompt 用 plan 的 target（不带裁判写的结果列表说明）。
- 结果（代码）：确认的值互相一致（相对差 <= 0.5%）= `published`：报其中一个（先取提到发布方的，再取位数多的，再取编号小的），
  `compute.result` 换成这个值（basis `published`，无区间），原来的组合估计存 `compute.estimate_result`，终稿由代码写
  （不调终稿模型）、估计只作参考列出；离散目标报这个值落在哪个结果上（先相等，再尾部），记 `resolved`。确认的值不一致 =
  `conflict`：照常报估计，终稿后面附一句。账本有「Published-value check」一节（候选表 + 判定），graph.html 页头和目标节点标 published。
- 离线：`probes/recheck_continuous.py` 7/7 相同；`probes/compare_continuous_prompts.py` 的 sha256 与 v2.3.1 相同（4a56d586…），
  即回测的全部 prompt、judge_rounds、compute、final 逐字节不变。新测试 16 个（`tests/test_published.py`）：候选规则、近似但不是的点
  （别的期间 / 年份 / 实体 / 量、预测、增长率、累计、裁判丢掉的）、模型确认了非候选 id 被忽略、冲突、离散 resolved 和尾部、回测不触发。

### 实测（2026-10-16，代码 c80036b）

| tag | 题 | 结果 | 成本 / 用时 |
|---|---|---|---|
| published1 | ask_a63174a0「How many new cars were registered in the UK in September 2026, as reported by SMMT?」（as_of 2026-10-16） | **published 350,536**（p52，fleetnews.co.uk live 页，页面日期 2026-10-05，「Preliminary figures from the SMMT」；p91 tradingeconomics、p152 同值也确认）；估计方法仅作参考：352,638（80% 255,968–485,816） | $0.4601（token $0.1401 + 按假设单价记的搜索费 $0.32），1631.9 s，41 次调用；确认调用 $0.0016、2.7 s |
| recheck1 | fc_yell_2026_09 回测（--auto-approve） | 834,910（80% 561,207–1,242,100，historical_errors），官方 868,450，-3.9%；检查 `not_checked` | $0.5654，782.3 s，25 次调用 |

- published1：35 个候选里送了前 20 个，模型把 17 个分项（私人 / 车队 / 小企业 / BEV）判为 different，3 个总数判为 target。
  同一篇 fleetnews 文章的 2026-10-02 快照写 350,518（去年同月 312,793），live 页写 350,536（去年同月 312,891）：文章改过数。
  裁判把 7 个 350,518 的点当作「被后一版取代」丢掉了，所以检查只看到 350,536。**哪个是 SMMT 的正式数，未核实。**
  两个参考方法（m1 = 三个 350,536 点的平均；m2 = 私人 + 车队 + 小企业）本身就是已公布的数，不是独立估计。
- recheck1 和 v21b（847,216，80% 571,724–1,255,458，monte_carlo，-2.4%；$0.502，2281.9 s）的差别来自检索：两次只有 12 个 URL
  相同，可用快照页 9 对 15；v21b 拿到了 nbcmontana 的 2024 年 9 月（852,435），这次最近的 9 月是 2023 年（838,458，nps.gov 23038）。
  两次的方法结构一样（最近的 9 月 × 变化倍数假设 1.0，加 series_naive），锚点年份不同；这次 series_naive 的回测含 2022 年（洪水，567,587），
  误差 0.295，区间依据变成 historical_errors。这次比「去年同月」基线（839,579，-3.3%）差。v2.4 没改回测的 prompt；
  v21b 以来连续题 prompt 的改动（v2.2 的 outcome_type 句、单位换算常数、target JSON 多一个字段）和检索的随机性用一次运行分不开。

### 「答案已公布」的未解决问题（open problems）

1. 候选上限 20、同分按编号：published1 有 35 个候选，3 个总数排在第 8、9、14 位，是碰巧没被截掉（分项和总数的共同词干一样多）。
   可能的做法：同分时按数值从大到小（总数不小于它的分项），或提高上限。没改，要先定。
2. 只看裁判保留的点：裁判丢掉的官方值不会被发现（published1 的 350,518 被当作旧版丢掉；结果碰巧仍是 SMMT 的数，但哪一版对未核实）。
3. 修订 / 多版本：确认的值相差 > 0.5% 记 conflict、照常报估计；没有「取最新一版」的规则。相差 <= 0.5% 时报的那个不一定是最新的。
4. 实体词只认大写专名和缩写：point name 里没写实体（「New car registrations, September 2026」）、或写成形容词（British）、
   或别的语言，都会漏；漏的后果 = 照旧估计。what 第一个子句全是通用类别词时（United Kingdom）只剩整个词组和缩写（uk）。
   v2.4.1 后仍是粗筛：量的缩写不在句首词组里（'France real GDP' 的 GDP）、量的名字后面不是介词（'Bank Rate set by the Bank of
   England' 仍有 rate / bank rate）时，别的实体仍会通过；反过来，'Real GDP of France' 这类目标的点 name 只写「real GDP」不写
   France 时会漏。日期规则：文章写明的发布日期早于期末、内容后来更新过的页面会被排除（漏）；quote 规则会误伤定义里带
   expected 的量（总和生育率「expected to have over her lifetime」）。
5. 分项（私人 / 车队 / 某个燃料类型）代码放过，只靠模型拒；published1 里拒对了 17 个，没有更多实测。
6. 离散目标只有数值结果能 resolved：数据点只有数字，人名、是 / 否这类结果判不了；只有离线测试，没有真实运行。
7. 网页没改：运行进度页的 compute 卡片显示的是估计（published 节点的更新没接）；结果页的估计卡片显示已公布值、区间「—」、
   basis published，没有专门的「已公布」标记（终稿文字里有）。
8. 已公布时终稿全由代码写，没有模型写的说明段（例如「这是初值，可能修订」只有一句通用的话）。
9. 目标期间还没结束（period_end > as_of）时不检查；as_of 当天才公布、页面还没被抓到的情况照旧估计。

v2.4 审查的低优先级意见（2026-10-16，都已对着代码或保存的数据核实，没改；第 11 条的计数和第 13 条的 graph.html 复现数字引自审查，没有重算）：

10. 单日 / 时点目标的期间容差：期间比较沿用 `compute._same_calendar`（期末、期长各差 <= 3 天）。目标 Bank Rate 2026-09-17..2026-09-17，
    点「Bank of England Bank Rate before the September 2026 decision」（期间 2026-09-15，4.0）会进候选；模型判成 target 时，离散目标会落到
    议息前的旧利率上、记 resolved。可能的做法：目标期长为 0 天时要求期末完全相等；或 NOT_VALUE 加 before / prior / ahead of。
11. 终稿里点的 name / unit 没经过 `graph.scrub_digits`（`published.py` 的 `_evidence_lines`、`final_text`）：抽取模型写的数字原样进终稿，
    破坏「模型写的数字换成 [n]」的约定。审查统计保存的运行里有 86 个点的 name 带数值（口径没有复核；例如 discrete2「... target range 3.50% to 3.75% at
    June 17, 2026」）。可能的做法：name / unit 先 scrub（保留年份），或终稿只用已核对的 quote 和 value_as_written。
12. 终稿和冲突说明的已公布值用 `_fmt`（>= 100 取整，其余 4 位有效数字）：101.3 index 写成「Published value: 101 index.」，2850.46 写成
    2,850，却说这是「the pinned target itself as already published」。可能的做法：写 value_as_written（加已核对的 scale_word），或按它的小数位数格式化。
13. 离散 resolved 后 graph.html 页头的列名仍是「agent (pooled)」、显示 100% / 0%，pooled 估计本身（estimate_result）在 graph.html 里不出现
    （离线复现：m1 50/50、m2 24/76，pooled 37% / 63%，用 3.75% resolve 后页头只有 100.0% / 0.0%）；网页结果页对已公布的运行，各方法 weight
    一律 0.0、assumption_share None，参考估计和区间只在终稿文字里（published1：estimate 卡片 350536 / None / None）。上面第 7 条只提到连续值的
    估计卡片。可能的做法：resolved 时列名改「result (published)」并另写 estimate_result 的 pooled 概率；web 的 result_view 在 basis 为 published
    时读 estimate_result 的 weights 和区间，作为参考字段返回。
14. 「先取提到发布方的点」用子串匹配（`resolve` 里 `t in text`）：publisher「Office for National Statistics (ONS)」的 ons 会命中 registrations、
    operations、nations。只影响 0.5% 以内互相一致的点选哪一个。可能的做法：和 candidates 一样按词边界匹配。
15. 确认 prompt 带着规划写的 caveats（`PB.prompt` 把 plan.target 整个 JSON 发出去）：published1 的 caveats 写着「No official SMMT data for
    September 2026 can exist on or before the cutoff ... Any estimate must be a forecast」，和这次检查的前提相反，会推着模型判 different（漏检）；
    这次没被带偏。可能的做法：只发 what / unit / period / publisher / outcome_type。
16. README 对 published1 的描述不完整（只记在这里，README 那句没改）：350,518 有 7 个点、来自 5 个域名——fleetnews 2026-10-02 快照 3 个
    （p17、p116、p186）、cardealermagazine 快照（p39）、parliamenttoday 页面日期 2026-10-02 的 live 页（p197，「preliminary figures published
    today by the Society of Motor Manufacturers and Traders」）、bmmagazine 和 am-online 2026-10-07 的快照（p81、p209）——都被裁判以「被后一版
    取代 / 重复」丢掉；350,536 只来自 fleetnews 改过的 live 页（p52、p152）和 tradingeconomics（p91，quote 里没有 SMMT 也没有 preliminary）。
    README 的「SMMT preliminary figure via fleetnews.co.uk and tradingeconomics.com」因此不准。哪个数是 SMMT 的正式数，仍未核实。

## v2.3.1：审查修复（离线，未调模型）

- 修正轮列出已丢弃的点（discrete6 两轮都卡在这里）：修正轮的表格不标保留 / 丢弃，previous 里也没有 decisions，而代码按第一次回复的
  decisions 校验依据 id。现在离散题的修正 prompt 末尾由代码写「These points are discarded ...: p2, p3, ...」（这一轮和更早轮次丢掉的点），
  并说明修正回复里的 decisions 不改变它；修正回复的 decisions 记进 `jr["repair"]["decisions_in_reply"]`，**仍不采用**。
  依据 id 必须全部是保留的点这条规则没变（修正回复还引用丢掉的点照旧被拒）。
- 第二轮修订的列表已通过、但方法没过进入修正轮时，方法说明改按新列表重写（「defined in judge round 2」+「already revised once」），
  不再同时出现旧列表的「Keep this list」和「accepted by code」；REPAIR_OUTCOMES_KEPT 由代码列出被接受的那份列表。
- 合并尾部的含义写进 label：带 `le` 的 label 必须匹配 TAIL_LE（or lower / or below / or less / or fewer），带 `ge` 的必须匹配 TAIL_GE，
  否则列表被拒（discrete6 第 2 轮修正列表的「4.00」带 le，现在会被拒）；裁判 prompt 的规则句（DISCRETE_OUTCOME_RULES）同步。Jev 的简报和 criteria 改用
  `D.value_text`（尾部带 or lower / or higher）。账本表的 value 列没改（label 已带尾部）。
- 连续模式：`probes/recheck_continuous.py` 7/7 相同；`probes/compare_continuous_paths.py` 对 v2.3 比 129 个裁判轮次全部相同；
  `probes/compare_continuous_prompts.py` 用假模型跑一遍连续题（两轮 + 修正轮，全部 prompt、judge_rounds、compute、final），
  v2.3 与 v2.3.1 的 sha256 相同（4a56d586…）。
- 更正：v2.3 的 README / 本文件 / 提交 162efe5 说 discrete6 的修正列表「引用了同一回复里自己丢掉的点」。保存的数据只能说明
  p27 / p28、p18 / p96 是**各轮第一次回复**丢的；修正回复的 decisions 当时没有记录，calls.jsonl 里也没有原始回复。下文已改。

## v2.3：结果列表在证据之后由裁判定义（2026-10-15 批准的范围）

- 规划：target 只留 `outcome_type`，另有可选的 `outcome_kind` 提示（例如 "policy rate in fixed steps"）；规划不再列结果，
  回复里还带 outcomes 就忽略并记 plan note。连续值 target 的字段不变（仍只有 `"outcome_type": "continuous"`）。
- 裁判第一轮（离散）：在回复里加 `outcomes`（2–6 个 `{label, value}`；数值型时最低的带 `le`、最高的带 `ge`，等于它的 value）
  和 `outcomes_basis`（`{"ids": [...], "note"}`）。代码校验：label 唯一、2–6 个、数值要么全有要么全无、数值不重复、
  两个尾部（只许最低带 le、最高带 ge）、依据至少一个 id 且每个都是这一轮保留的点。不合格就进现有的修正轮
  （第一轮后面还要搜时也修，只修列表；方法留到第二轮再核对）；修正后的列表再校验一次。记录在 `state["outcomes"]`。
- 之后的轮次：裁判看到第一轮的列表和依据 id，不给 outcomes 就沿用；新证据矛盾时可修订一次（要 `outcomes_revision_reason`），
  代码记 `revised_round`、`previous_list`。一轮里已通过的列表在修正轮里不再改。
- outcome_probs、compute、Jev 臂、终稿都用裁判的列表；没有合格列表时每个方法报 `no outcome list`，终稿写
  「the judge did not define a valid outcome list」，Jev 臂 skipped。
- 输入核对：每行的 role 由代码写成裁判列表里的那个结果（尾部带 or lower / or higher），核对 prompt 前面另列结果列表和依据点的证据。
- 打分认 `le` / `ge`（旧列表仍按 label 里的 or lower / or higher）。账本在结果概率表前写「列表由第几轮裁判、根据哪些点定义」。
- 连续模式：`probes/recheck_continuous.py` 7/7 相同；`probes/compare_continuous_paths.py` 对 v2.2.1 比 129 个裁判轮次，
  compute / 假设校验 / `_problems` / 输入核对的行和表头全部相同。连续题的规划 prompt 只改了 outcome_type 那一句和模板字段。
- 只跑 plan 节点（`probes/plan_only.py`，结果 `results/agent/plan_only_v2.3/`）：开发 4 题 + 留出 3 题，规划给的
  outcome_type 全部是 continuous（已关掉「有真值只认 continuous」的代码改写），7 次调用共 $0.0179。
- 离线重放（`probes/replay_judge_outcomes.py` → `results/agent/ask_0e2d5021/replay_judge_outcomes_v2.3.json`）：
  - discrete4 / discrete5 的 plan 列表原样当裁判列表：都被拒（没有 le / ge、没有依据；discrete4 还有 7 个结果）。
  - 补上尾部和依据后，**discrete5 的错列表（4.50% or lower … 5.75% or higher）通过代码校验**：代码查不出「现实的 4.00% / 4.25%
    被并进 4.50% or lower 尾部」，只能靠 prompt 的「按证据定义」和依据 id。
  - 两次运行第一轮都已有当前利率点（discrete4 p3；discrete5 p1/p4/p76，另有 FedWatch p14/p15），所以按证据构造的列表
    （3.75% or lower / 4.00% / 4.25% / 4.50% or higher）第一轮就能通过；但 discrete4 的 p3 在第二轮被丢了（沿用时不复查）。
  - 保存的方法是按旧 label 写的，原样重算全部 unknown label；按数值换 label 后 discrete4 第 2 轮修正前的 m1 =
    4.00% 56.3%、4.25% 43.7%，discrete5 的方法因为本来就放错桶，换完仍算不出。

## 已完成：「离散结果」模式（v2.2，按 2026-10-15 批准的设计）

- 规划：target 带 `outcome_type` 和 `outcomes`（2–10 个 `{label, value}`）；不合格退回 continuous 并记 plan note。
- 判断：离散目标只有 `outcome_probs`；% 转小数、[0, 1]、余下结果（其余之和 <= 1.02）、无余下时和在 [0.9, 1.1] 再归一化；
  多方法等权平均；复述保留点规则、输入核对（每个概率一行）、裁判修正轮都适用；连续方法被拒。
- 结果、终稿（代码生成各结果概率行）、ledger、graph.html、网页结果页都有结果概率表；有真值时打分：真结果概率、Brier、最可能结果对不对。
- 单位换算常数 `k_bp_per_pct_point = 100`、`k_percent_per_unit = 100`。
- Jev 对照臂（`jev.py`，官方端点，只在设了 `TYPESAFE_KEY_FILE` 时跑，不并入 agent 的答案）。价格 $0.042 / 百万输入 token、输出免费
  （docs.typesafe.ai/models，2026-10-15 核对）。**还没有真实调用过**（没有 key）。
- 和设计的出入：没有输入、也不是余下结果的结果概率记为 0（写进方法 notes），不再报错。原因见下表 discrete1/2/4。
- 连续模式：**只有 compute 离线重算相同**。7 次保存的开发 / 测试运行，中心估计和 P10/P90 全部相同（`probes/recheck_continuous.py`，7/7）；
  v2.2.1 另比了 35 个连续目标 state.json 的 129 个裁判轮次，compute.run、假设校验、`_problems`、输入核对的行和表头与 v2.2 逐字节相同。
  但规划和裁判的 prompt 变了（PLAN_USER 加了 outcome_type 说明和模板字段，METHODS_SPEC 加了两个单位换算常数，target JSON 多了
  `"outcome_type": "continuous"`），**真实运行没有复测**。

## v2.2.1：审查修复（离线，未调模型）

- 每个 outcome_probs 方法至少一个保留的观测点（同 formula_mc）；只有假设加余下结果的方法拒绝（discrete1/4 第 1 轮）。
- 一个 id 只能给一个结果（discrete2 的 p87、discrete4 的 a2）。
- 当概率用的观测点 name 或 unit 必须带 probability / odds / chance / likelihood；单位是百分点或基点（变化量）的点和假设拒绝
  （discrete4 的 p95「概率变化 22.1 percentage points」、p117 失业率）。没收 implied / priced：「market-implied rate」是水平。
  没做「数值等于某个结果的值、单位是目标单位就拒绝」：利率题里「降息概率 4.0%」会和结果 4.00% 撞上，误伤。
- 离散方法之间的冲突检查：两个分布的 total variation distance > 0.5 就交回裁判（对应连续值的 3 倍规则）。没用「最可能的结果不同」：
  56/44 对 45/55 这种接近五五开的两个来源也会触发修正轮。
- 输入核对：离散方法每行的 role 由代码写成「target 取结果 X（数值、单位）的概率」再附上裁判的 role；余下结果也核对一行
  （代码算的 1 − 其余之和、其余输入覆盖了哪些结果）；表头要求核对证据是不是这个结果的概率。连续值的核对 prompt 没动。
- 有真值的题（回测 / 留出）只有题目标了 `outcome_type: "discrete"` 才接受离散目标，否则代码改回 continuous 并记 plan note。
- 打分：合并的尾部结果（label 带 or lower / or higher 等）认超出它的真值；`score_all` 对离散运行不再算点估计误差（真值 0 不再除零）。
- Jev 臂：`http.client.HTTPException`（IncompleteRead 等）记为错误；jev 节点出任何异常都记 status = error，不让整题崩掉。
- 重放（`probes/replay_discrete_rules.py`）：discrete1/4 第 1 轮只有假设的方法、discrete2 第 1 轮 m2、discrete4 第 2 轮修正前的 m2
  现在都被代码拒绝；discrete4 第 2 轮修正前只剩 FedWatch 方法：4.00% or lower 56.3%。构造的「{4.25%: p22}，余下给 3.25%」
  代码仍然接受，只能靠新的余下结果核对行（模型判断，**没有用真实模型验证**）。

## FOMC 真实运行（`results/agent/ask_0e2d5021/`），全部没出数

| tag | 代码 | 结果 | 没出数的原因 |
|---|---|---|---|
| discrete1 | 1b60230 | 无 | 10 个结果；给 3.75% 的假设 a1（0.1%，low = 0）被假设校验拒绝（要求 low > 0） |
| discrete2 | 3541b7a | 无 | 第一次回复 3 个假设 low = 0 被拒且漏了 3.25%；修正轮只修了假设，两个方法仍漏 3.25% |
| discrete4 | 8e196cd | 无 | FedWatch 维持 56.3% + 加息 43.7%（和 1.00）的干净方法，因其余 5 个结果没输入被拒；修正轮更糟 |
| discrete5 | d914126 | 无 | 规划在搜索前定的结果列表是 4.50%–5.75%，不含 4.00% / 4.25%；裁判把证据塞进错的桶，输入核对正确地拒了 |
| discrete6 | f173c84（v2.3） | 无 | 两轮的第一次回复都没给 outcomes；修正回复给的列表本身合格（v2.3 规则下），但依据里引用了这一轮第一次回复丢掉的点（修正轮看不到丢弃标记），整个列表被拒（见下；v2.3.1 修了提示） |

（discrete3 中断，没有 state.json，已删。）离线重放 discrete4 第 2 轮裁判原始回复（v2.2.1 规则）：4.00% or lower 53.1%、4.25% 46.9%；
其中 m2 用同一个假设 a2（50%）同时给两个结果，质量可疑。

discrete6（$0.4716，其中 token $0.1316、按假设单价记的搜索费 $0.34；556.7 s；39 次调用；6 个方向 + 3 个补充方向；106 个点，最后保留 9 个）：
- 第 1 轮：第一次回复没有 outcomes → 修正轮。修正回复的列表 = 3.75% or lower / 4.00% / 4.25% / 4.50% or higher（le / ge 都对），
  依据 p1、p4（9 月 16 日决议后上限 4.0%）、p16–p19、p27、p28；p27 / p28（9 月、7 月会议日期）是这一轮第一次回复丢掉的点 → 拒。
- 第 2 轮：没有列表，所以再次要求定义；第一次回复又没给 → 修正回复的列表 = 4.00（le）/ 4.25 / 4.50 or higher（ge），
  依据里的 p18、p96（当前上限 4.0%）是这一轮第一次回复作为「重复」丢掉的点 → 拒。没有列表，方法全部 `no outcome list`。
- 证据：p1 / p4 当前上限 4.00%。FedWatch 读数的页面日期（page_date）都是 2026-10-14，但互相矛盾：p19（CNBC，URL /2026/10/14/）
  10 月 28 日会议加息 25bp 53.7%；p85 / p89（9fzt、jrj）加息 43.7%，p86 / p90 维持 56.3%。p19 的 period_end 2026-10-15 是抽取模型填的，
  同页 p20「a day ago 22.1%」也跟着往后挪了一天。哪个读数对，没有核实。
- 离线反事实（不进结果）：只看列表、不查依据是否保留，两个列表在 v2.3 规则下都合格（v2.3.1 起第 2 轮列表的「4.00」带 le、label
  没写 or lower，会被拒）。第 1 轮修正后的 m1（4.25% ← p19，余下给 4.00%）=
  4.00% 46.3%、4.25% 53.7%；但 compute 用的是第 2 轮的方法：m1 把 p19（CNBC 加息 53.7%）和 p86（9fzt 维持 56.3%）两个来源的同日读数相加 = 1.10，
  又指定了余下结果，即使列表通过也会因「其余之和 > 1.02」被拒，而那一轮已经用掉了修正机会。

## 离散模式的未解决问题

1. （discrete6）裁判两轮的第一次回复都没给 outcomes。定义要求写在方法说明里，JUDGE_USER 的回复 JSON 模板里没有 outcomes /
   outcomes_basis。可能的做法：离散题的回复模板加这两个字段。是 prompt 改动，要先定。
2. （discrete6）依据 id 必须全部是保留的点：修正回复引用了这一轮第一次回复当「重复」丢掉的点（p18 / p96 是 p1 / p4 的副本，
   p27 / p28 是会议日历），整个列表因此被拒，修正机会也用掉了。v2.3.1 只在修正 prompt 里列出丢掉的 id（没有真实运行验证）；
   规则本身没放宽。可能的进一步做法：至少一个保留的 id 时只去掉丢掉的 id 并记 note；或修正轮也采用修正回复里的 decisions。
   这会放宽批准的规则，要先定。
3. （重放）代码查不出列表有没有「按证据」：discrete5 的错列表补上尾部和依据后通过校验（现实的 4.00% / 4.25% 被并进
   「4.50% or lower」）。可能的代码规则：依据里不是概率、单位和目标一致的「水平」点，其数值必须是一个单独（非尾部）的结果；
   风险是误伤（例如依据里引用下限 3.75%）。要先定。
4. （重放）沿用第一轮列表时不复查依据：discrete4 第一轮的依据点 p3 在第二轮被丢掉。是否复查、复查不过怎么办，要先定。
5. 数值结果中间不查步长：「4.00% or lower / 4.50% / 4.75% or higher」漏了 4.25% 也能通过。代码不知道步长（只有 outcome_kind 提示）。
6. （discrete6）同日不同来源的 FedWatch 读数冲突混在一个方法里（p19 CNBC 加息 53.7% + p86 9fzt 维持 56.3%，和 1.10；保留的 p85 / p89
   是加息 43.7%）。现在只有和的检查兜底。
7. 网页计划表（`app.js` 的 targetTable）从 plan 的 target 读 outcomes，v2.3 起离散题这一格是空的；结果页读 compute 的结果，不受影响。
   要显示 `state["outcomes"]` 得改前端（这次没改）。
8. 规划不确定「下一次会议」是哪天（discrete6 的 caveats 仍写「未知」）；这次裁判从 p19（「Oct. 28 FOMC meeting」）和会议日历点找到了 10 月 28 日。
9. Jev 臂只有离线测试（discrete6 没有列表，Jev 臂 skipped；也没配 key）。
10. 余下结果放错桶（构造的「{4.25%: p22}，余下给 3.25%」）代码仍接受，只靠输入核对。更强的代码规则（余下概率不超过观测点的最大值、
    或余下结果必须和某个有输入的结果相邻）会误伤合法用法（FedWatch 只报加息 43.6%、余下给维持 56.4%），要先定方案。
11. 网页「已保存的运行」列表的假设占比只算有 estimate 的方法，离散运行总是「—」。直接用 `assumption_weight_share` 会让
    「FedWatch + 1% 尾部假设」显示「假设为主」；离散运行的假设占比怎么定义（假设给的概率质量？算不算余下结果？）要先定。
12. 离散题的字符串真值（answer_value = "4.25%" 或人名）会让 `prepare_run`（泄漏哨兵）和 `save_run` / ledger（`{:,}` 格式化）崩掉。
13. `render_graph` 用链式 `str.replace` 填模板：meta 里模型写的 outcome label 或 Jev 返回的文字含 `__GRAPH__` 时，图 JSON 会被插进
    页头 HTML；从磁盘 file:// 打开没有 CSP 保护（v2.3 起 label 由裁判写，风险不变）。
14. `jev._urllib_post` 跟随 301/302/303 时会把 `Authorization` 头带到跳转后的地址（需要官方端点自己返回跳转）。可以换成不跟随跳转的 opener。
15. 两个单位换算常数只能在 formula_mc 里用，而离散题禁用 formula_mc，所以它们实际只影响连续题的 prompt。
16. （v2.3.1 审查，低）输入核对的 prompt 带上了裁判自己写的论证：`check(t)` 的 target 来自 `with_outcomes`，含 `outcomes_basis.note`
    （裁判自由文本，≤ 400 字符），`AUDIT_USER.format(target=dumps(target))` 整段交给核对模型；v2.2.1 的核对 target 里没有。note 里
    正是核对要独立检查的说法（discrete6：「The market prices a hold at 4.00% (p86) and a 25bp hike to 4.25% (p19)」），有锚定风险，
    对核对结论的影响没有实测。可能的做法：传给 audit 的 target 去掉 note（AUDIT_OUTCOMES 已由代码列出依据点的证据）。
17. （v2.3.1）修正回复里的 decisions 只记录不采用；修正轮的表格本身仍不标保留 / 丢弃（`_table` 连续题共用，没改）。第一轮在第一次
    回复里定义的列表通过、方法没过时，修正轮的方法说明仍是「define it in this reply」，只靠末尾代码列出的列表说明「已接受、不要改」。

已解决：v2.2 的「结果列表在规划时定死」（v2.3 改由裁判定义，但见上面 1–4）；「同一个 id 给两个结果」（v2.2.1）；
「留出测试前先只跑 plan 看 outcome_type」（v2.3：7/7 continuous）。

## 之后的清单（demo 收尾）

1. ~~修「答案已公布」~~：v2.4 已做（见上；未解决问题另列）。
2. 把留出测试扩到 10 题左右（先预注册，含 1–2 道非英语题）。
3. 挑 3–5 个展示用的运行，首页放入口；README 首屏放回测表、架构图、截图和局限说明。
4. 「假设占比」计入公式弹性（审查意见）；识别「样本 × 放大系数」这种伪装假设（日本题）。
5. 「梯度下降」调研：4 份领域报告已完成，汇总和核查被额度闸门挡住；续跑时要改动汇总和核查的 prompt，避免回放缓存里的 stopped 结果；先删掉停止标记文件。

## 2026-10-15 补记：discrete7（v2.3.1）首次出数

FOMC 题：3.75 or lower 1.9%、4.00 53.6%、4.25 41.6%、4.50 or higher 2.9%，最可能 4.00（维持）。4.00 和 4.25 来自两个来源报道的同一组 CME FedWatch 读数（10/14：维持 56.3%、加息 43.7%）；两头的尾部是判断节点的假设（加息 50bp 3%、降息 2%）。两个方法用的是同一组读数，不算独立证据。用时 384 s，0.38 美元。

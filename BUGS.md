# BUGS：当前全部已知问题（2026-10-16 整理，代码 v2.5.2 + showcase 臂；同日晚按第一轮修复的结果更新状态，代码 v2.6d）

只做整理，没改代码、没重跑。来源：NEXT.md、SHOWCASE.md 的记录，加上 2026-10-16 对 showcase1 结果和代码的检查。
「新」= 这次检查新发现（证据是这次跑的离线查询）；「记」= 以前已经记录（NEXT.md / SHOWCASE.md 有详细说明，当时对着代码核实过）。
严重度：**高** = 影响结果对不对，或者影响和基线的对比公不公平；**中** = 影响部分题、可信度或可读性；**低** = 边角情况、记录精度。

**第一轮修复后的状态（2026-10-16 晚更新）**：每张表最后一列是「本轮状态」，依据 `FIX_PLAN.md`（决定 D1–D9、第 6 节「本轮不做」）和阶段报告
`probes/out/stages/S0.md`–`S8.md`（被 gitignore，只在本机）。

- 「已修 `tag`」：改动过了 FIX_PLAN 第 4 节的门槛 G1–G8，并打了 tag。全部是离线验证（没联网、没调模型），已存的 `results/` 一个字节没改；
  对以后运行的真实效果要等重跑（D7，没批准）。
- 「部分修 `tag`」：只修了写明的那一部分。
- 「未修（阶段没完成）」：FIX_PLAN 排了阶段，但本轮没做完。S8（`v2.6e`）的改动在工作区、停在核查，没提交；S9、S10 没开始。
- 「本轮不修」：FIX_PLAN 第 6 节或 D5–D8 写明不做，括号里是原因。
- 「订正」：按 `probes/out/fixplan_analysis.json` 或阶段报告里核对过的事实改了描述，括号里留了原来的写法。
- 证据里的行号是整理时的行号（A–H 对 v2.5.2，N 对 web-v0.3）；S1–S8 改过的文件，行号已经移动。

## A. 区间与不确定度

| # | 严重度 | 问题 | 证据 / 出处 | 来源 | 本轮状态 |
|---|---|---|---|---|---|
| A1 | 高 | 「80% 区间」名不副实：三层保守规则叠加，区间约 ±30–50%；当前版本 8 次成功运行的误差都 ≤ 6.1%（ln 误差 RMS 约 0.03，区间 σ 约 0.31），宽了约 10 倍 | `methods.py:184-227`（combine）、`assumptions.py`（MIN_WIDTH）、`methods.py:27`（DEFAULT_REL_U）；全部保存运行的误差 / 区间表 | 新 | 本轮不修（D6：规则放到 v2.7，先定新的留出集和 interval score）；`v2.6d` 只改了标签：终稿写「80% model-based」，并附区间依据的说明（F2） |
| A2 | 高 | 区间只反映「输入的随机误差」，兜不住结构性错误：v21 韩国 −87%、v21b JNTO +183%、几次 noown −100%，区间同样宽，都没盖住 | 同上的运行表 | 新 | 本轮不修（D6） |
| A3 | 中 | `is_change_factor` 靠关键词正则：「September-to-June seasonal ratio」「as a factor of September 2025 total」没有 growth / change 等词，被当普通假设按 2 倍放宽，而不是 1.25 倍 | `assumptions.py` CHANGE_WORDS；NHS a1 / a3、JNTO a1 / a2 | 新 | 本轮不修（D6，和假设 kind 字段一起定） |
| A4 | 中 | 观测点一律 ±20%，不区分精确官方数（2,395,886）和二手转述 | `compute.py`（formula_mc 的 point 分支）、`methods.py:27` | 新 | 本轮不修（D6） |
| A5 | 中 | 合并时区间取最宽单方法的 MC 宽度：多个方法互相印证，区间也不会收窄（NHS 三个方法之间只差约 2.5%，没用上） | `methods.py:214-226` | 新 | 本轮不修（D6） |
| A6 | 中 | 没有回测时 FALLBACK_SIGMA = 0.25 是硬下限，区间不可能窄于 −27% / +38%（韩国题就卡在这里，basis = no_basis） | `methods.py:24, 225` | 新 | 本轮不修（D6） |
| A7 | 中 | 「假设占比」不计公式弹性，会低估 | NEXT.md 收尾清单 4 | 记 | 本轮不修（D6） |
| A8 | 中 | 预注册成功标准看「区间是否覆盖真值」，区间这么宽，覆盖没有信息量；没有比较区间宽度（如 interval score） | EVAL_SHOWCASE_PLAN.md、`showcase.py` | 新 | 本轮不修（第 6 节：下一轮预注册加 Winkler interval score；showcase1 的成功标准是预注册，不改） |

## B. 判断节点与方法

| # | 严重度 | 问题 | 证据 / 出处 | 来源 | 本轮状态 |
|---|---|---|---|---|---|
| B1 | 高 | 把变化率当成水平值：日本迁移题 p12 = 「2025 比 2024 +0.3%」被当成「全年 519 万人」；代码拦住了，但修正轮没修好，整题没有估计。**订正主因**（原来只写了上面这些）：表示水平值的点「519万548」在核对阶段就因为 `more than one number in value_as_written` 被丢了（N26），裁判手里只剩 0.3% 这个变化率；p12 的 quote 原文是「…は519万548人で、前年に比べ1万7,198人(0.3%)の減少」，value_as_written 却是 0.3%。修正轮的报错看不出是哪个输入（B5）是次因 | SHOWCASE.md 日本迁移节；`results/agent/fc_jp_movers_2026_08/showcase1/state.json` 的 p12 和 dropped_points（挑错意见离线核对） | 记 | 未修（阶段没完成）：主因 N26 在 S8，没提交；次因已在 `v2.6b` 改了：量纲规则的报错点名每个输入 |
| B2 | 高 | 伪装的「样本 × 放大系数」假设识别不了：留出集日本出生题靠「单家诊所接生数 × 放大系数」得出 +0.8% | NEXT.md 收尾清单 4、docs/project.html 的提醒框 | 记 | 本轮不修（D6） |
| B3 | 中 | series_naive（就是去年同月）仍会进 agent 的答案：韩国 8 月题占 50% 权重。去年同月不再作为对照之后，这个方法保不保留、权重怎么定，还没定 | SHOWCASE.md 发现 7 | 记 | 本轮不修（D6：series_naive 的地位放到下一轮预注册） |
| B4 | 中 | 假设的取值和它自己的理由矛盾，没有检查：JNTO a2 取 1.05，理由里写的是 0.95 / 0.98 | SHOWCASE.md 发现 4 | 记 | 本轮不修（第 6 节：rationale 一致性检查要先定设计） |
| B5 | 中 | 修正轮只有一次，修不好就整题没有估计（日本迁移） | `graph.py` 修正轮 | 新 | 部分修 `v2.6b`：量纲规则（「至少一个输入是量」）的报错点名每个输入的 id / unit / name；修正轮仍只有一次（第 6 节：修正次数本轮不改） |
| B6 | 低 | 公式里写了数字常数被拒（NHS m4 的 3、JNTO m3 的 0.5）：规则对，但裁判 prompt 没说清，白白浪费一个方法名额 | SHOWCASE.md 发现 5 | 记 | 本轮不修（第 6 节：改 prompt 收益小） |
| B7 | 低 | 方法引用已丢弃的点（韩国 m2 → p56）；yoy_scaling 缺信号年份（韩国 m3） | 韩国 8 月 state.json | 新 | 本轮不修（第 6 节）。注：p56 是同一份回复自己丢掉又引用的，S5 的第 2 轮表格解决不了它 |

## C. 取证 / 检索

| # | 严重度 | 问题 | 证据 / 出处 | 来源 | 本轮状态 |
|---|---|---|---|---|---|
| C1 | 高 | 非英文官方统计取证弱：日本迁移题 44 页里只有 3 页能用。13 页是 PDF（不支持）；7 页 stat.go.jp HTML 解码失败；21 页在截止日前没有快照。截止日前已公布的 7 月官方数也没拿到。**订正**（原写「解码失败原因没查，可能是编码问题，未核实」）：`fetch._decode` 只看 HTTP 头里的 charset，不看 meta，也不认带引号的写法（N28）；这些快照的头只有 `text/html`，Shift_JIS 页面按 utf-8 解码，U+FFFD 超过 1% 就判 undecodable。同类的还有日本出生留出题 2 页 mhlw.go.jp（meta 是 shift_jis），以及 LHR 留出题 3 页 zstd 压缩的快照（`net.decompress` 只认 gzip / deflate；用标准库 `compression.zstd` 解开后 U+FFFD 为 0）。能解码的页面上，中日韩倍数字又会被丢（N26） | SHOWCASE.md 日本迁移节；`fetch.py:121-127`、`net.py:76-89`；zstd 的缓存快照 `data/raw/agent/_cache/snap/2a926955898fcc3d.bin`、`38932b7bcaf4fcb7.bin`（挑错意见离线核对） | 记 | 未修（阶段没完成）：解析部分在 S8（没提交），解码和 zstd 在 S9（没开始）；PDF 本轮不做（不加依赖） |
| C2 | 高 | 泄漏风险：searcher 的搜索不能限定日期，能看到公布后的结果，并把真值写进了查询（NHS「2.44 million」）。只有 URL 往下传，但选哪些 URL 可能受答案影响；只能事后审计，挡不住 | NHS state.json 的 leakage 字段 | 记 | 部分修 `v2.6c`（D3）：回测时，查询词命中登记值的方向整个作废（不取页、不重搜），原因写进 `search.voided` 和审计的 `directions_voided`；已存的 50 个审计里会有 7 个运行各作废 1 个方向。searcher 仍然看得到公布后的结果，没作废的方向选 URL 仍可能受影响（残余风险） |
| C3 | 低 | 哨兵误杀：7.27 million 撞上登记的 6–8 月合计，整页被排除。**订正**（原写「很可能是候诊人数，未核实」）：S6 核对了这一页的上下文，原文是「The waiting list fell to 7.27 million」，确实是候诊名单 | 同上；`data/raw/agent/fc_nhs_ae_2026_09/f706a9125ce75ee7.txt`（S6.md 第 4.2 节） | 记 | 本轮不修（D3：四舍五入写法命中照旧整页排除，护栏不放松）；`v2.6c` 之后这一页只由「7.27 million」命中，原来那条「7.27 M」是误报，已去掉（N31）。中日韩四舍五入写法要不要登记，还没定 |
| C4 | 中 | live 页读不出日期就直接丢，漏了多少没测 | NEXT.md v2.5 第 4 条 | 记 | 本轮不修（第 6 节：live 取页收尾） |
| C5 | 低 | 同一个 URL 被几个方向重复抓；live 存盘文件名冲突会互相覆盖 | NEXT.md v2.5 第 3、15 条 | 记 | 本轮不修（第 6 节） |
| C6 | 低 | robots.txt 取失败被永久缓存；Crawl-delay 的第一跳只隔 1 秒 | NEXT.md v2.5 第 14、10 条 | 记 | 本轮不修（第 6 节：HTTP 客户端统一） |
| C7 | 低 | 提前停之后取页没有被取消；15 s 是 socket 超时，不是整页总时限；pages_used 偏高；停下后的取页不进 state.json | NEXT.md v2.5 第 11、12、13、2 条 | 记 | 本轮不修（第 6 节） |
| C8 | 低 | markets 节点在真实使用时走的是 `net.get` 的重试请求，judge 要等它。**订正**（原写「仍是 60 s 超时加重试」）：`markets.py:68、98` 传的是 `timeout=30`，再加上 `net.get` 默认的 2 次重试、10 / 30 s 退避和 robots 30 s 超时，一次请求最坏远超 60 s。49 次保存运行里 markets 一个点都没产出（分析时统计）。NEXT.md v2.5 第 7 条也写成了 60 s | `markets.py:68、98`；`net.py:165-166`（N46） | 记 | 本轮不修（第 6 节：HTTP 客户端统一）；描述已订正 |

## D. 「答案已公布」检测

| # | 严重度 | 问题 | 证据 / 出处 | 来源 | 本轮状态 |
|---|---|---|---|---|---|
| D1 | 中 | 先到先得：报的是第一页确认的值，后到的版本不再看；英国新车 350,518 和 350,536 哪个是 SMMT 正式数，未核实 | NEXT.md v2.5 第 1 条 | 记 | 本轮不修（第 6 节） |
| D2 | 中 | 候选规则粗筛：只看裁判保留的点、上限 20 个、没有「取最新一版」、实体词只认大写专名、分项只靠模型拒、单日目标的期间容差、publisher 用子串匹配、确认 prompt 带着规划的 caveats、期间没结束就不查 | NEXT.md「答案已公布」第 1–5、9、10、14、15 条 | 记 | 本轮不修（第 6 节） |
| D3 | 低 | 终稿里点的 name 没经过 scrub_digits；已公布值格式化会丢精度（101.3 → 101） | 同上第 11、12 条 | 记 | 本轮不修（第 6 节） |

## E. 离散模式

| # | 严重度 | 问题 | 证据 / 出处 | 来源 | 本轮状态 |
|---|---|---|---|---|---|
| E1 | 中 | 字符串真值（"4.25%"、人名）会让泄漏哨兵和 save_run / ledger 崩掉 | NEXT.md 离散第 12 条 | 记 | 本轮不修（第 6 节：运行骨架的机械问题） |
| E2 | 中 | 回复模板里没有 outcomes 字段；依据 id 规则过严（引用了丢弃的点就整份列表被拒） | 离散第 1、2 条 | 记 | 本轮不修（第 6 节：离散规则） |
| E3 | 中 | 代码查不出列表是不是「按证据定的」；沿用列表时不复查；不查步长；同日冲突的 FedWatch 读数混进一个方法；余下概率放错桶 | 离散第 3–6、10 条 | 记 | 本轮不修（第 6 节：离散规则） |
| E4 | 低（安全） | render_graph 用链式 str.replace，label 里含 `__GRAPH__` 可注入；jev 跟随跳转时会带上 Authorization 头 | 离散第 13、14 条 | 记 | 未修：jev 跳转的部分排在 S10（没开始）；render_graph 的部分 FIX_PLAN 没排阶段 |
| E5 | 低 | 输入核对的 prompt 带着裁判写的 note，有锚定风险；修正回复里的 decisions 不采用；Jev 臂没真实调用过 | 离散第 16、17、9 条 | 记 | 本轮不修（第 6 节：离散规则；Jev 真实调用要外部 key，没批准） |

## F. 终稿文字与网页

| # | 严重度 | 问题 | 证据 / 出处 | 来源 | 本轮状态 |
|---|---|---|---|---|---|
| F1 | 中 | 终稿里出现「[n]」占位符（模型写的、无法溯源的数字被遮掉），读者看着像 bug（NHS、韩国） | 两题 final.text | 新 | 已修 `v2.6d`（D4）：离 as_of 10 年以内的四位年份、Q1–Q4 / H1–H2、方法和点 id 不再被清洗；方法用到的观测点各有 `p{n}_value` 占位符；state 另存模型原文 `final.model_text`。已存终稿的 template 已经清洗过，修不回来；剩下的来源见 R3 |
| F2 | 中 | 区间依据显示成「(80%; no basis)」（韩国），没有说清是什么区间 | 韩国 final.text | 新 | 已修 `v2.6d`：区间标签写成「80% model-based」，依据由 `outputs.BASIS_TEXT` 写成一句说明，终稿、ledger、graph.html 页头和网页结果页都用它 |
| F3 | 低 | 网页：提前停时 compute 卡片不更新；已公布运行的估计卡片和权重显示；离散题计划表的 outcomes 是空的；离散运行的假设占比显示「—」 | NEXT.md v2.5 第 5 条、v2.4 第 7、13 条、离散第 7、11 条 | 记 | 本轮不修（第 6 节：网页展示） |
| F4 | 低 | 用时拆分的时间原点不一致，误差约 1 s | NEXT.md v2.5 第 16 条 | 记 | 本轮不修（第 6 节） |

## G. 对照臂与评测

| # | 严重度 | 问题 | 证据 / 出处 | 来源 | 本轮状态 |
|---|---|---|---|---|---|
| G1 | 高 | **不联网结构化基线的路线大量被量纲检查拒掉**：「人口 × 每人每年就诊次数 × 9 月占全年份额」算出来是 /year，被判 dimension mismatch。11 道题里 7 道至少有一条路线因此被拒；日本迁移 3/3 全拒，NHS 2/3 被拒；台湾留出题基线的「没有估计」，两次尝试的报错都是这条和 G2，具体是哪条拦下了最后一条路线没有逐条核实。**订正**（原写「语义上是对的」「和基线的对比因此偏向 agent」）：基线 prompt（`triangulate/prompts.py:42`）本来就要求「目标是一段时间的总量时加 period_length 输入」，这些路线没加，检查没有判错；问题在报错是 SI 写法（NHS 两次尝试都是 `dimension mismatch: formula gives s**-1, target is dimensionless`），模型看不懂、改不对（N39）。偏向哪边也不一致：分析时在内存里做的反事实（没重跑）NHS 会变成 −10.0%（现存 −0.7%），也就是在 NHS 上量纲检查反而帮了基线；日本迁移从没有估计变成 +33.4%，台湾 +36.2% | `engine.py:141`；`results/forecast/raw/structured/*.json` | 新 | 本轮不修（D5：`showcase.py` 每次打分都用当前 engine 重算结构化臂，10-28 打分提交前改就是改预注册的对照臂；之后先处理 N38，再改报错反馈）；描述已订正 |
| G2 | 中 | 结构化基线不允许公式里出现数字常数：日本迁移、台湾两题都有路线因为 1000 被拒。**订正**（原写「和『每千人』这类比率冲突」）：单位串里的 per 1000 代码已经换算过（`parse_unit('births per 1000 people per year').factor` = 3.17e-11/s），模型又在公式里除以 1000，这些路线放行就会双重换算、小 1000 倍（N38）。台湾第 2 次尝试把常数改名（`people_per_birth_rate_unit`）绕过了常数规则，拦住它的只剩量纲错误 | `expr.py:85`；`results/forecast/raw/structured/fc_tw_births_2026_09.json` 第 2 次尝试的 p1 | 新 | 本轮不修（D5）；描述已订正 |
| G3 | 高（我的失误） | 联网直接答臂 max_tokens 写成 4096，预注册那次两题都没出数；不带工具重试时，模型把工具调用写成了文本 | SHOWCASE.md arm (3) 节 | 记 | 没改值：`v2.5.3` 把 4096 收进 `config.MAX_TOKENS["search_direct"]`（值不变）；预注册那次不能重跑；以后的默认值没定 |
| G4 | 中 | 预测市场臂没查 Kalshi，和预注册不一致 | SHOWCASE.md「不一致」第 3 条 | 记 | 本轮不补查（D8：Kalshi 是新的外部 API，没批准；按预注册只能在 2026-10-16（UTC）当天补查），记为和预注册不一致 |
| G5 | 中 | 样本太少：真正的样本外只有 4 题（留出 3 题 + NHS）；dev 4 题是边调边跑的，不能当测试成绩 | — | 新 | 本轮不修（第 6 节：要先定新的留出集）。另：S11 重跑以后，tw、lhr、jp_births 三道留出题只能算开发数据 |
| G6 | 低 | NHS 官方值只有 3 位有效数字（±0.2%），agent 和结构化之间的差距与舍入误差同一量级 | SHOWCASE.md NHS 节 | 记 | 本轮不修（打分口径，只能进下一轮预注册；FIX_PLAN 没排） |
| G7 | 中 | agent 成本的大头是「每次搜索 $0.01」这个假设单价（NHS $0.62 里 token 只有 $0.12），单价没有核实 | SHOWCASE.md 成本表 | 新 | 本轮不修（要联网核实单价） |

## N. 第一轮修复计划补的编号（N1–N46，来自 `probes/out/fixplan_analysis.json` 的 `interact.new_issues_merged`）

证据是分析时的离线核对；标了「读者」的是分析里另一个子 agent 核实、合并时没有复核的。行号对 web-v0.3。

| # | 严重度 | 问题 | 证据位置 | 本轮状态 |
|---|---|---|---|---|
| N1 | 中 | max_tokens 散落成 9 个字面量，final 角色靠隐式默认值；judge 在 12000 处仍截断过 1 次 | `graph.py:176/372/396/509/573/649`、`pipeline.py:88/122/231`、`published.py:370`、`search.py:49`、`arms.py:57/65`、`search_direct.py:23`；截断是 ask_fa4b4c74/web_20261015T192127Z 的 judge:r2 | 已修 `v2.5.3`：`config.MAX_TOKENS` 一张表，值不变，final 显式传参；judge 保持 12000（D2） |
| N2 | 中 | 先预扣、后排队：第一轮 10 个方向同时预扣 $0.915（上限 $1.00）；超限后的中止是粘滞的 | `pipeline.py:67-73、82-88、315`；离线算 `Budget()`：10 × 0.09146 | 部分修 `v2.5.5`：先拿并发名额再预扣，在途预扣最多 8 份；粘滞中止按计划不变 |
| N3 | 低 | HTTP 客户端和重试循环有三套以上，行为不一致 | `llm.py`、`search.py:53-74`、`search_direct.py:33-67`、`jev.py:35` | 本轮不修（第 6 节：HTTP 客户端统一） |
| N4 | 中 | 各臂和 Searcher 的 thinking / temperature 不一致；接口能否关 thinking 未核实 | `llm.py:38-40`；`search.py:49-51`、`search_direct.py:141` 不设 | 本轮不修（要联网核实） |
| N5 | 低 | prompt 里写死的数字和代码常数重复，两处已经不一致（plan 写 up to 8、代码 directions = 10；quote 写 200 字、代码到 400 才拒） | `prompts.py:58、130`；`pipeline.py:43-44、179` | 本轮不修（第 6 节） |
| N6 | 低 | 代码常数重复定义（Z90 三份、MC_N / MC_SEED 两份），state 只记了一部分区间常数 | `methods.py:23、25-26`、`mc.py:13`、`web/results.py:15、24-26`、`config.py:21-22`、`app.js:375-376` | 部分修 `v2.5.3`：Z90 / MC_N / MC_SEED 改为引用，值不变；state.json 追加 `settings`（含 MIN_WIDTH_CHANGE、FALLBACK_SIGMA）。`app.js` 的 4096 / 32000 文案、`web/results.py` 的 `SHARE_DEFINITION`（1.2816、v/1.2）没动（改了网页输出会变） |
| N7 | 低 | 并发没有统一上限：MAX_CONCURRENCY 只有 runner 在用 | `forecast.py:143、170`；`config.py:30` | 本轮不修（第 6 节；`forecast.py` 冻结） |
| N8 | 低 | 「今天」有时按本机日期、有时按 UTC | `run.py:115、125`；`fetch.py:145` | 本轮不修（第 6 节） |
| N9 | 低 | 价格表只有 deepseek-flash，换模型时静默回退；预扣用模块级的 MODEL | `pipeline.py:83、87`；`config.py:56` | 本轮不修（第 6 节） |
| N10 | 低 | 图节点没有兜底的异常处理，出异常时 state.json、ledger 都不写 | `graph.py:397、510`；`run.py:150-158` | 本轮不修（第 6 节） |
| N11 | 中 | 第二轮裁判看不到第一轮的丢弃：prompt 说「没列出的都保留」，代码却沿用丢弃 | `graph.py:128-136、519-521`；`prompts.py:206`；ask_fa4b4c74/web_20261015T192127Z | 已修 `v2.6b`（D1）：之前丢掉的点另列紧凑行（id / name / value / 第几轮丢弃），写明要恢复就写 keep:true；判定代码没动 |
| N12 | 低-中 | 第一轮有追加方向时方法不经试跑和核对；第二轮失败时 compute 回退到第一轮未核对的方法 | `graph.py:540、619`；fc_yell_2026_09 旧运行（读者） | 本轮不修（第 6 节） |
| N13 | 低 | compute 重新编号 m1..mN，和裁判、核对阶段的编号对不上 | `compute.py:141-143`；`graph.py:624-628` | 本轮不修（第 6 节） |
| N14 | 低 | 人工改方向后 candidate_id 丢失，候选的 selected 标记也不更新 | `graph.py:434-436`；ask_fa4b4c74 | 本轮不修（第 6 节） |
| N15 | 低 | JUDGE_USER 回复示例里 formula_mc 的 inputs 没有 role，和规则矛盾 | `prompts.py:249` 对 `prompts.py:149`；`graph.py:356-359` | 已修 `v2.6b` |
| N16 | 低 | 旧判据和旧入口只剩测试在用 | `graph.py:216-223、265-268`；`methods.py:129-141` | 本轮不修（第 6 节） |
| N17 | 高（潜在） | 假设 unit 是「% of ...」时不除以 100，结果会大 100 倍 | `assumptions.py:29、76`；fc_kr_births_2026_08/showcase1 的 a2 | 已修 `v2.5.4`：`assumptions.is_pct(unit)`，unit 原文保留用于显示；观测点一侧的同类问题没改，见 R1 |
| N18 | 中 | combine 有历史误差时忽略 MC 宽度，2 个回测年就能把区间压到 ±4.5% | `methods.py:217-223`；fc_yell_2026_08/v21b（读者重算） | 本轮不修（D6） |
| N19 | 低 | 连续值 formula_mc 不用假设的 value，采样中位数是 sqrt(p10_used × p90_used) | `compute.py:183`；`assumptions.py:112-113` | 本轮不修（D6） |
| N20 | 中 | 百分比 / 比率 / 变化的分类器有 5 套，彼此不一致 | `compute.py:16-17`、`assumptions.py:29-33`、`evidence.py:66`、`discrete.py:29-34`、`published.py:131-132`（读者） | 本轮不修（D6）；`v2.5.4` 只把假设一侧收成 `is_pct` |
| N21 | 低 | MIN_WIDTH 放宽时不考虑占比的上界 1 | `assumptions.py:104-113` | 本轮不修（D6） |
| N22 | 低 | formula_mc_samples 不检查非有限、非正样本；p10 <= 0 的方法在 combine 里静默丢掉 MC 宽度 | `methods.py:149-152、214-215` | 本轮不修（D6） |
| N23 | 低 | 反比回测误差权重不考虑回测年数 | `methods.py:198` | 本轮不修（D6） |
| N24 | 中 | searcher 的 max_tokens 写死 2048、不关 thinking、不检查 stop_reason：493 次搜索 39 次截断，其中 32 次模型一个 URL 都没给 | `search.py:49、94-103`；`results/agent/**/calls*.jsonl` | 部分修 `v2.6a`：上限 2048 → 8192（只改表里这一项）；thinking 没改（N4），stop 仍只记在 calls.jsonl |
| N25 | 低 | 搜索错误计数永远是 0；超出 max_uses 的调用也被计数 | `search.py:86-91`；web_search_requests 分布 4:425、5:22、6:22（max_uses = 3） | 部分修 `v2.6a`：agent 的 searcher 认 list 里的 `web_search_tool_result_error`；arm (3) 的 `search_direct.audit` 有同样的问题，没改（预注册对照臂，S4.md 第 7 节）；超出 max_uses 的调用收不收费等 G7 |
| N26 | 中 | 中日韩倍数字（万 / 億 / 만）被静默丢掉，或整个点被拒：`parse_value('519万','')` = (519.0, False)，`'35万6713'` 报错；含万 / 萬 / 만 / 億的复合写法因为 more than one number 被丢 464 个点，unknown scale word 189 个点 | `evidence.py:63-65`（SCALES）、`82-139`；全量统计见挑错意见 | 未修（阶段没完成）：S8（`v2.6e`）的改动在工作区、停在核查，没提交。S8 的规则、已知局限和要用户定的事（千 / 천）见 `probes/out/stages/S8.md` 第 7、8 节 |
| N27 | 低-中 | 日期识别只认英文和 ISO：`text_dates('令和8年3月27日公表 2026年3月27日')` 返回 [] | `evidence.text_dates`、`parse_date` | 未修（阶段没完成）：同 N26，在 S8 |
| N28 | 低 | `_decode` 的 charset 正则不认带引号的写法 | `fetch.py:123` | 未修（阶段没完成）：S9 没开始 |
| N29 | 低 | CDX 查询失败被记成「no snapshot <= as_of」 | `fetch.py:155-158、196` | 本轮不修（第 6 节） |
| N30 | 低（安全，假设性） | DeepSeek 的 key 在重定向时也会被带过去（E4 只写了 jev） | `search.py:56-59`（urllib 跟随重定向时保留其他请求头，读者读了 venv 源码） | 未修（阶段没完成）：S10 没开始。注意 S10 的文件列只有 `llm.py`、`jev.py`，这条的证据位置 `search.py` 自己调 `urlopen`，S10 做的时候要一起看 |
| N31 | 低 | 泄漏哨兵的写法过宽：非整数登记 .1f 截断写法（`leak_forms(4.25)` = ['4.2','4.25']）；缩写不区分大小写、后面没有字母边界（「7.27 M」命中「7.27 miles」） | `evidence.py:240-249` | 部分修 `v2.6c`：k / M 结尾的写法后面不能再接字母；.1f 截断写法和不区分大小写没改 |
| N32 | 中 | 连续值终稿没有观测输入值的占位符；未知占位符渲染成 [unknown placeholder] | `graph.py:696-717、747`；fc_jnto_2026_08/v21b（读者） | 已修 `v2.6d`：方法用到的点各给 `p{n}_value`；没加 `p{n}_period`（D4 只写了 value） |
| N33 | 中 | 清洗规则和 FINAL_SYSTEM 矛盾；连续值的 keep_ids 不含点 id | `prompts.py:268`；`graph.py:107-108、736` | 已修 `v2.6d` |
| N34 | 低 | 终稿只保存清洗后的 template，不保存模型原文 | `graph.py:750-751、810-811` | 已修 `v2.6d`：`state.final.model_text` |
| N35 | 低 | 数字格式化有 7 份，规则不一致；graph.html 页头一律取整 | `graph.py:122-125`、`run.py:198-199`、`outputs.py:17`、`published.py:59`、`viewer.py:71`、`report.py:156`、`app.js:11`（读者） | 本轮不修（第 6 节） |
| N36 | 低 | docs/project.html 是手写的，没有生成脚本；「已知局限」两条已过时 | `docs/project.html:107-108` | 本轮不修（第 6 节） |
| N37 | 低 | 网页把展示集的真实运行标成「--ask」；用时按分钟取整 | `web/results.py:109-113`；`app.js:195`（读者） | 本轮不修（第 6 节） |
| N38 | 高（G1 / G2 一修就会暴露） | 结构化基线的「每千人」双重换算：单位已乘 1e-3，模型又在公式里除以 1000 | `parse_unit('births per 1000 people per year')`；`results/forecast/raw/structured/fc_tw_births_2026_09.json` 第 2 次尝试的 p1 | 本轮不修（D5：B0 之后先处理它，再改 G1 的报错反馈） |
| N39 | 中 | 基线重试反馈改不动错：报错用 SI 写法，常数错误会遮住量纲错误 | `engine.py:122-126、141`；台湾第 1、2 次尝试 | 本轮不修（D5） |
| N40 | 中（G1 修好以后才会出现） | 基线区间把 outlier 路线的样本也混进去 | `mc.py:77-78` | 本轮不修（D5） |
| N41 | 低 | MC 之后才判无效的路线不进 errors，不触发重试 | `engine.py:152、178-180` | 本轮不修（D5） |
| N42 | 低 | 「没有估计时算不算覆盖」三处口径不一致 | `forecast.py:196`、`showcase.py:150-151`、`report.py:99`（读者） | 本轮不修：三个文件都在冻结清单里（G7，到 10-28 打分提交为止），FIX_PLAN 没排阶段 |
| N43 | 低 | arm (3) 取文字的方式和预注册写法有细微差别 | `EVAL_SHOWCASE_PLAN.md:63`；`search_direct.py:85-91`（读者） | 本轮不修：预注册的对照臂，FIX_PLAN 没排阶段，只记录 |
| N44 | 低 | run.score_all 仍然写出 last_year_same_period 臂 | `run.py:239-243`；`EVAL_SHOWCASE_PLAN.md:12` | 已修 `v2.6d` |
| N45 | 低 | 测试缺口；tests/test_agent.py 的 `__main__` 守卫写在最后一个测试类之前 | `tests/test_agent.py:695-699`；`tests/test_graph.py:115-120`（读者） | 部分修 `tools-regress-v1`：守卫挪到文件末尾；`test_graph` 的 G1 场景测试没加（G1 本轮不修）。各阶段新加的测试见 R 节前的说明 |
| N46 | 低 | BUGS.md 和文档里有几处描述与代码不符 | BUGS.md C8、G2；`AGENT_MVP.md:25` 对 `pipeline.py:38` | 订正（本次文档提交）：BUGS.md 的 B1、C1、C3、C8、G1、G2 已改。`AGENT_MVP.md:25` 写每个方向最多 5 个 URL，代码是 4（现在是 `pipeline.py:39` 的 `urls_per_direction: int = 4`），AGENT_MVP.md 本次没改；NEXT.md v2.5 第 7 条的「60 s」同 C8，原文没改 |

本轮新加的测试：S0 基线 240 个 → `v2.6d` 290 个（S1 `test_settings`、S2 `test_pct_units`、S3 `test_budget_order`、S4 `test_search_errors`、S5 `test_judge_protocol`、
S6 `test_leak_guard`、S7 `test_final_text`），每个阶段 `unittest` 全过、没有本来就失败的测试。S8 在工作区的 `tests/test_cjk_numbers.py` 另有 24 个（没提交）。

## R. 本轮修复中新发现、没改的问题（来自阶段报告「发现但没改」一节）

| # | 严重度 | 问题 | 证据 / 出处 | 状态 |
|---|---|---|---|---|
| R1 | 中 | 观测点一侧的百分数 unit 只有精确的 `"%"` 才除以 100：已存 4691 个点里 771 个的 unit 是别的百分数写法（`percent` 593 个……），`fc_jnto_2026_08/v21` 第 2 轮 m3 就是因为 p36（9.6 percent）没除以 100 而失败（开发运行）。但 FOMC 的目标本身是 percent per annum，点一侧不能一律按 is_pct 除 | `compute.py` formula_mc 的点分支；`probes/out/stages/S2.md` 第 6 节第 1 条 | 没改：要先定点的 unit 规则 |
| R2 | 中（潜在） | 点 id 和区间占位符同名：点 p10 / p90 的值占位符是 `[[p10_value]]` / `[[p90_value]]`，而 `[[p10]]` / `[[p90]]` 是区间上下限。模型写 `[[p10]]` 想指点 p10 时会渲染成区间 P10，数字错而且没有提示。已存运行里只有 `fc_kr_births_2026_08/showcase1` 会碰上 | S7.md 第 8 节第 6 条 | 没改：改名等于改终稿的输入输出约定（G2 还要再变），下一轮再定 |
| R3 | 低 | F1 剩下的来源：ISO 日期仍被清洗成 `2026-[n]-[n]`（已存终稿 116 个 `[n]` 里 18 个来自日期）；贴着字母数字的年份（`FY2025`）照旧被清洗，prompt 没写这一点 | S7.md 第 8 节第 7、8 条 | 没改（D4 没覆盖日期） |
| R4 | 低 | URL 在右括号处被截断（`agent/search.py` 的 `URL_RE` 排除了 `)`），IRMA 的两个 URL 只剩半截；对取页的影响未核实 | S4.md 第 7 节第 2 条 | 没改 |
| R5 | 低 | 搜索预扣不是严格的单次上界：按 30,000 个输入 token 估，已存搜索最多 97,500 个；靠搜索费那一份兜住，493 次里没有一次实际花费超过预扣 | S4.md 第 4 节、第 7 节第 3 条 | 没改 |
| R6 | 低 | 23 次 `stop=tool_use` 的搜索全都没有模型给的 URL；和上限、thinking 有没有关系未核实 | S4.md 第 7 节第 4 条 | 没改（要联网） |
| R7 | 低 | 预算中止以后，调用要先等到并发名额才抛 BudgetExceeded（不是立刻失败） | S3.md 第 6 节第 1 条 | 没改（「粘滞中止不变」；已存结果里从没中止过） |
| R8 | 低 | 连续值修正轮复用第 2 轮的 prompt（含「要恢复就写 keep:true」），但修正回复里的 decisions 代码不看（E5 的一部分）；紧凑行没有 unit / 期间 / 来源（例：p128 的「4」其实是 4%） | S5.md 第 8 节第 1、2 条 | 没改（修正轮规则不在 S5 范围；紧凑行格式是 D1 定的） |
| R9 | 低 | ledger 方法表只显示报错的前 200 个字符，多个输入时只看得到第一个（网页和 state.json 是全文） | `outputs.py:211`；S5.md 第 8 节第 3 条 | 没改 |
| R10 | 低 | `probes/replay_discrete_rules.py` 原样跑会在 discrete6 处 `KeyError: 'outcomes'`（探针写于 v2.2.1，之后结果列表改存在 `state["outcomes"]`） | S5.md 第 5 节、第 8 节第 4 条 | 没改（S5 用 scratch 副本跑完了对比） |
| R11 | 低 | 哨兵的字母边界会漏掉「2.44mn / 2.44 mln / 2.44 Mio」这类写法（「million」整词照旧命中）；作废规则对四舍五入写法也生效（韩国「24,000명」） | S6.md 第 8 节第 1、4 条 | 没改（D3 定的写法和代价） |
| R12 | 低 | 网页：泄漏审计表不显示 `directions_voided`，作废的方向只显示「0 页」；实时进度页的 compute 卡片仍显示原始 basis 键；ledger 和 graph.html 的「80% interval」字样没改成 model-based | S6.md 第 8 节第 3 条；S7.md 第 7 节第 7 条、第 8 节第 5 条 | 没改（`web/runs.py`、`_leakage_view` 不在阶段文件里） |
| R13 | 低 | `docs/prompts_bilingual.md`（和生成它的 `probes/gen_prompts_bilingual.py` 里的中文对照）没跟上 S5、S7 改过的 JUDGE_USER、FINAL_SYSTEM、FINAL_USER | S5.md 第 8 节第 5 条；S7.md 第 8 节第 10 条 | 没改（本次文档提交只改 BUGS.md、NEXT.md、docs/structure.html） |
| R14 | 低 | 「% points」写法会被 `is_pct` 当成百分数（已存假设没有这种写法）；restated_point 的词干比较仍会误伤；依赖图标签和网页假设表对「% of ...」的假设多一个 `%` 后缀 | S2.md 第 6 节第 2–4 条 | 没改 |

## H. 我的做事方式（这些低级错误的来源）

1. 每条规则只对着引发它的那次失败验证，不量几条规则叠在一起的效果（A1–A6）。
2. 该让模型显式声明的类别，用关键词正则去猜（A3；D2 里的实体词也是同一类问题）。
3. 不逐字读最终输出（F1、F2），没检查对照臂的参数（G3），没检查基线是不是被自己的检查器误伤（G1）。

以后打 tag 前的门槛：全量「误差 / 区间 / 覆盖」回归表 + 逐字读终稿和网页（已写进长期记忆）。

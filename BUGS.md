# BUGS：当前全部已知问题（2026-10-16 整理，代码 v2.5.2 + showcase 臂；10-16 晚、10-17 凌晨按第一轮修复的结果更新状态，代码 v2.6g；10-17 补 Q 节：v2.7 的 U0，没提交；10-17 下午：U0 提交为 v2.7a，Q 节补上 U1（没提交）的已知限制；10-17 晚：结构化基线修复 `v2.8c`（G1、N39、N41），冻结前冒烟测试的发现和 `v2.8d` 的修复见 S 节）

只做整理，没改代码、没重跑。来源：NEXT.md、SHOWCASE.md 的记录，加上 2026-10-16 对 showcase1 结果和代码的检查。
「新」= 这次检查新发现（证据是这次跑的离线查询）；「记」= 以前已经记录（NEXT.md / SHOWCASE.md 有详细说明，当时对着代码核实过）。
严重度：**高** = 影响结果对不对，或者影响和基线的对比公不公平；**中** = 影响部分题、可信度或可读性；**低** = 边角情况、记录精度。

**第一轮修复后的状态（2026-10-16 晚更新，10-17 凌晨按 S8–S10 再更新）**：每张表最后一列是「本轮状态」，依据 `FIX_PLAN.md`（决定 D1–D10、第 6 节「本轮不做」）和阶段报告
`probes/out/stages/S0.md`–`S10.md`（被 gitignore，只在本机；S9b 没有单独的报告，依据是提交 16673a4 的说明）。

- 「已修 `tag`」：改动过了 FIX_PLAN 第 4 节的门槛 G1–G8，并打了 tag。全部是离线验证（没联网、没调模型），已存的 `results/` 一个字节没改；
  对以后运行的真实效果要等重跑（D7，没批准）。
- 「部分修 `tag`」：只修了写明的那一部分。
- FIX_PLAN 第 5 节排的 S0–S10 都已提交并打了 tag，上次更新时的「未修（阶段没完成）」已经没有了。S9 之后多了一个 S9b（`v2.6f1`）：按用户的要求（「直接找个项目或者别的库放进去，编码这种问题别自己死命干」），手写的解码顺序换成 w3lib 库，见 FIX_PLAN 的 D10。
- 「本轮不修」：FIX_PLAN 第 6 节或 D5–D8 写明不做，括号里是原因。
- 「订正」：按 `probes/out/fixplan_analysis.json` 或阶段报告里核对过的事实改了描述，括号里留了原来的写法。
- 证据里的行号是整理时的行号（A–H 对 v2.5.2，N 对 web-v0.3）；S1–S10 改过的文件，行号已经移动。

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
| B1 | 高 | 把变化率当成水平值：日本迁移题 p12 = 「2025 比 2024 +0.3%」被当成「全年 519 万人」；代码拦住了，但修正轮没修好，整题没有估计。**订正主因**（原来只写了上面这些）：表示水平值的点「519万548」在核对阶段就因为 `more than one number in value_as_written` 被丢了（N26），裁判手里只剩 0.3% 这个变化率；p12 的 quote 原文是「…は519万548人で、前年に比べ1万7,198人(0.3%)の減少」，value_as_written 却是 0.3%。修正轮的报错看不出是哪个输入（B5）是次因 | SHOWCASE.md 日本迁移节；`results/agent/fc_jp_movers_2026_08/showcase1/state.json` 的 p12 和 dropped_points（挑错意见离线核对） | 记 | 部分修：主因 N26 已在 `v2.6e` 修了（`parse_value('519万548','')` 现在是 5,190,548；S8 的重放里，日本迁移题这一页的 8 个复合写法点都能解析、都过邻接检查）；次因已在 `v2.6b` 改了：量纲规则的报错点名每个输入。已存的点不重新核对，这道题能不能出数要等重跑（D7）；修正轮仍只有一次 |
| B2 | 高 | 伪装的「样本 × 放大系数」假设识别不了：留出集日本出生题靠「单家诊所接生数 × 放大系数」得出 +0.8% | NEXT.md 收尾清单 4、docs/project.html 的提醒框 | 记 | 本轮不修（D6） |
| B3 | 中 | series_naive（就是去年同月）仍会进 agent 的答案：韩国 8 月题占 50% 权重。去年同月不再作为对照之后，这个方法保不保留、权重怎么定，还没定 | SHOWCASE.md 发现 7 | 记 | 本轮不修（D6：series_naive 的地位放到下一轮预注册） |
| B4 | 中 | 假设的取值和它自己的理由矛盾，没有检查：JNTO a2 取 1.05，理由里写的是 0.95 / 0.98 | SHOWCASE.md 发现 4 | 记 | 本轮不修（第 6 节：rationale 一致性检查要先定设计） |
| B5 | 中 | 修正轮只有一次，修不好就整题没有估计（日本迁移） | `graph.py` 修正轮 | 新 | 部分修 `v2.6b`：量纲规则（「至少一个输入是量」）的报错点名每个输入的 id / unit / name；修正轮仍只有一次（第 6 节：修正次数本轮不改）；冒烟测试 smoke1 里披萨、茶两题的方法都是在唯一的修正轮里出错（S1–S3），`v2.8d` 修了这几处报错和规则，修正次数仍是一次 |
| B6 | 低 | 公式里写了数字常数被拒（NHS m4 的 3、JNTO m3 的 0.5）：规则对，但裁判 prompt 没说清，白白浪费一个方法名额 | SHOWCASE.md 发现 5 | 记 | 本轮不修（第 6 节：改 prompt 收益小）；`v2.8d`：钉了单位时，这条报错还说明「只是换单位的数就删掉、在 unit 里写清单位」（冒烟测试 S2） |
| B7 | 低 | 方法引用已丢弃的点（韩国 m2 → p56）；yoy_scaling 缺信号年份（韩国 m3） | 韩国 8 月 state.json | 新 | 本轮不修（第 6 节）。注：p56 是同一份回复自己丢掉又引用的，S5 的第 2 轮表格解决不了它 |

## C. 取证 / 检索

| # | 严重度 | 问题 | 证据 / 出处 | 来源 | 本轮状态 |
|---|---|---|---|---|---|
| C1 | 高 | 非英文官方统计取证弱：日本迁移题 44 页里只有 3 页能用。13 页是 PDF（不支持）；7 页 stat.go.jp HTML 解码失败；21 页在截止日前没有快照。截止日前已公布的 7 月官方数也没拿到。**订正**（原写「解码失败原因没查，可能是编码问题，未核实」）：`fetch._decode` 只看 HTTP 头里的 charset，不看 meta，也不认带引号的写法（N28）；这些快照的头只有 `text/html`，Shift_JIS 页面按 utf-8 解码，U+FFFD 超过 1% 就判 undecodable。同类的还有日本出生留出题 2 页 mhlw.go.jp（meta 是 shift_jis），以及 LHR 留出题 3 页 zstd 压缩的快照（`net.decompress` 只认 gzip / deflate；用标准库 `compression.zstd` 解开后 U+FFFD 为 0）。能解码的页面上，中日韩倍数字又会被丢（N26） | SHOWCASE.md 日本迁移节；`fetch.py:121-127`、`net.py:76-89`；zstd 的缓存快照 `data/raw/agent/_cache/snap/2a926955898fcc3d.bin`、`38932b7bcaf4fcb7.bin`（挑错意见离线核对） | 记 | 部分修：解析部分 `v2.6e`（N26、N27）；解码和 zstd `v2.6f`，`v2.6f1` 起解码改用 w3lib（D10）。缓存 286 个快照里原来 undecodable 的 7 个（stat.go.jp 3、mhlw.go.jp 2、LHR 的 zstd 2）现在都能解码、U+FFFD 为 0，其余快照的正文不变（S9.md 第 4 节、提交 16673a4）。PDF 本轮不做（不加依赖）。已存结果没重跑；能解码不等于能拿到数：stat.go.jp 移动报告在 as_of 前最新的快照只有 2 月结果，mhlw 两页是目录页（S9.md 第 8 节）。残余情况见 R18 |
| C2 | 高 | 泄漏风险：searcher 的搜索不能限定日期，能看到公布后的结果，并把真值写进了查询（NHS「2.44 million」）。只有 URL 往下传，但选哪些 URL 可能受答案影响；只能事后审计，挡不住 | NHS state.json 的 leakage 字段 | 记 | 部分修 `v2.6c`（D3）：回测时，查询词命中登记值的方向整个作废（不取页、不重搜），原因写进 `search.voided` 和审计的 `directions_voided`；已存的 50 个审计里会有 7 个运行各作废 1 个方向；`v2.6e` 登记中日韩精确写法以后多作废 1 个（`fc_jnto_2026_08/v21b_noown` 第 2 轮 b2，查询词里有 as_of 之后才公布的 7 月值「344万2100」），共 8 个方向（S8.md 第 4.3 节）。searcher 仍然看得到公布后的结果，没作废的方向选 URL 仍可能受影响（残余风险） |
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
| E4 | 低（安全） | render_graph 用链式 str.replace，label 里含 `__GRAPH__` 可注入；jev 跟随跳转时会带上 Authorization 头 | 离散第 13、14 条 | 记 | 部分修 `v2.6g`（D9）：jev 遇到 3xx 不跟随，抛 `JevError`（消息不带 key），`run_arm` 记 `status="error"`；render_graph 的注入 FIX_PLAN 没排阶段，没改 |
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
| G1 | 高 | **不联网结构化基线的路线大量被量纲检查拒掉**：「人口 × 每人每年就诊次数 × 9 月占全年份额」算出来是 /year，被判 dimension mismatch。11 道题里 7 道至少有一条路线因此被拒；日本迁移 3/3 全拒，NHS 2/3 被拒；台湾留出题基线的「没有估计」，两次尝试的报错都是这条和 G2，具体是哪条拦下了最后一条路线没有逐条核实。**订正**（原写「语义上是对的」「和基线的对比因此偏向 agent」）：基线 prompt（`triangulate/prompts.py:42`）本来就要求「目标是一段时间的总量时加 period_length 输入」，这些路线没加，检查没有判错；问题在报错是 SI 写法（NHS 两次尝试都是 `dimension mismatch: formula gives s**-1, target is dimensionless`），模型看不懂、改不对（N39）。偏向哪边也不一致：分析时在内存里做的反事实（没重跑）NHS 会变成 −10.0%（现存 −0.7%），也就是在 NHS 上量纲检查反而帮了基线；日本迁移从没有估计变成 +33.4%，台湾 +36.2% | `engine.py:141`；`results/forecast/raw/structured/*.json` | 新 | 已修 `v2.8c`（用户 10-17：「没有基线我做个毛线的测试啊」）：engine 的量纲报错改成白话（SI 写法留在括号里），点名哪些输入带时间单位、怎么让它抵消；规则不变。showcase1 打分改用冻结的 `showcase_engine.py`（`d79db02` 的 engine 原样复制），预注册的对照臂不变。已存的 55 次尝试重算数字全部相同。冒烟测试 smoke1（v2.8c，目标单位给对之后）结构化基线 4 题都出了数 |
| G2 | 中 | 结构化基线不允许公式里出现数字常数：日本迁移、台湾两题都有路线因为 1000 被拒。**订正**（原写「和『每千人』这类比率冲突」）：单位串里的 per 1000 代码已经换算过（`parse_unit('births per 1000 people per year').factor` = 3.17e-11/s），模型又在公式里除以 1000，这些路线放行就会双重换算、小 1000 倍（N38）。台湾第 2 次尝试把常数改名（`people_per_birth_rate_unit`）绕过了常数规则，拦住它的只剩量纲错误 | `expr.py:85`；`results/forecast/raw/structured/fc_tw_births_2026_09.json` 第 2 次尝试的 p1 | 新 | 部分修 `v2.8c`：规则不变（公式里仍不许出现数字常数）；结构化 prompt 加一句「单位里的倍数（per 1000）由 Python 换算，公式不能再乘除一次」，带倍数单位的输入在报错里另有提示（N38） |
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
| N26 | 中 | 中日韩倍数字（万 / 億 / 만）被静默丢掉，或整个点被拒：`parse_value('519万','')` = (519.0, False)，`'35万6713'` 报错；含万 / 萬 / 만 / 億的复合写法因为 more than one number 被丢 464 个点，unknown scale word 189 个点 | `evidence.py:63-65`（SCALES）、`82-139`；全量统计见挑错意见 | 已修 `v2.6e`：认 万/萬/億/亿/兆/만/억/조、复合写法（519万548、2만4,275）、倍数字后接单位（万人、兆円）和 `'000s`；只抄了中日韩数字一截的点改为丢掉。已存点的 parse_value 重放：复合写法 464 个里 426 个解析出值，unknown scale word 189 个里 187 个（S8.md 第 4.1 节；已存的点不回写）。千 / 천 不支持，见 R15；其他已知局限见 R16、R17 |
| N27 | 低-中 | 日期识别只认英文和 ISO：`text_dates('令和8年3月27日公表 2026年3月27日')` 返回 [] | `evidence.text_dates`、`parse_date` | 已修 `v2.6e`：认 YYYY年M月D日、YYYY년 M월 D일、令和 / 平成 N年、民国 / 民國 N年，期间年份检查也认纪年；上面的例子现在返回两个 2026-03-27（收尾时离线核对）。昭和和 R8 / H31 这类缩写没做；不带前缀的 1NN年 见 R16 |
| N28 | 低 | `_decode` 的 charset 正则不认带引号的写法 | `fetch.py:123` | 已修 `v2.6f`；`v2.6f1` 换成 w3lib 以后，双引号和不带引号的写法都认，单引号（`charset='Shift_JIS'`）不认，见 R18 |
| N29 | 低 | CDX 查询失败被记成「no snapshot <= as_of」 | `fetch.py:155-158、196` | 本轮不修（第 6 节） |
| N30 | 低（安全，假设性） | DeepSeek 的 key 在重定向时也会被带过去（E4 只写了 jev） | `search.py:56-59`（urllib 跟随重定向时保留其他请求头，读者读了 venv 源码） | 已修 `v2.6g`（D9）：新函数 `llm.urlopen_no_redirect`（标准库 `HTTPRedirectHandler` 的子类，不生成跳转请求）；`LLM._post`、`Searcher.search`、`DirectClient.call`、`jev._urllib_post` 和手动探针 `probes/deepseek_search_probe.py` 都走它（比 S10 的文件列多了 `search.py`、`search_direct.py` 和探针，S10.md 第 5 节）。3xx 时各客户端沿用原来的传输错误处理（Searcher 返回 `error="http_3xx"`），key 不会发到跳转后的地址；200 的结果逐字不变。真实端点会不会回 3xx 没核实 |
| N31 | 低 | 泄漏哨兵的写法过宽：非整数登记 .1f 截断写法（`leak_forms(4.25)` = ['4.2','4.25']）；缩写不区分大小写、后面没有字母边界（「7.27 M」命中「7.27 miles」） | `evidence.py:240-249` | 部分修 `v2.6c`：k / M 结尾的写法后面不能再接字母；.1f 截断写法和不区分大小写没改 |
| N32 | 中 | 连续值终稿没有观测输入值的占位符；未知占位符渲染成 [unknown placeholder] | `graph.py:696-717、747`；fc_jnto_2026_08/v21b（读者） | 已修 `v2.6d`：方法用到的点各给 `p{n}_value`；没加 `p{n}_period`（D4 只写了 value） |
| N33 | 中 | 清洗规则和 FINAL_SYSTEM 矛盾；连续值的 keep_ids 不含点 id | `prompts.py:268`；`graph.py:107-108、736` | 已修 `v2.6d` |
| N34 | 低 | 终稿只保存清洗后的 template，不保存模型原文 | `graph.py:750-751、810-811` | 已修 `v2.6d`：`state.final.model_text` |
| N35 | 低 | 数字格式化有 7 份，规则不一致；graph.html 页头一律取整 | `graph.py:122-125`、`run.py:198-199`、`outputs.py:17`、`published.py:59`、`viewer.py:71`、`report.py:156`、`app.js:11`（读者） | 本轮不修（第 6 节） |
| N36 | 低 | docs/project.html 是手写的，没有生成脚本；「已知局限」两条已过时 | `docs/project.html:107-108` | 本轮不修（第 6 节） |
| N37 | 低 | 网页把展示集的真实运行标成「--ask」；用时按分钟取整 | `web/results.py:109-113`；`app.js:195`（读者） | 本轮不修（第 6 节） |
| N38 | 高（G1 / G2 一修就会暴露） | 结构化基线的「每千人」双重换算：单位已乘 1e-3，模型又在公式里除以 1000 | `parse_unit('births per 1000 people per year')`；`results/forecast/raw/structured/fc_tw_births_2026_09.json` 第 2 次尝试的 p1 | 部分修 `v2.8c`：prompt 和报错提示都说明单位里的倍数已换算；代码不拦，模型把常数改名绕过规则时仍可能双重换算 |
| N39 | 中 | 基线重试反馈改不动错：报错用 SI 写法，常数错误会遮住量纲错误 | `engine.py:122-126、141`；台湾第 1、2 次尝试 | 已修 `v2.8c`：报错用白话（SI 留在括号里）；常数错误不再遮住同一路线的其他问题 |
| N40 | 中（G1 修好以后才会出现） | 基线区间把 outlier 路线的样本也混进去 | `mc.py:77-78` | 本轮不修（D5） |
| N41 | 低 | MC 之后才判无效的路线不进 errors，不触发重试 | `engine.py:152、178-180` | 已修 `v2.8c`：MC 之后判无效的路线进 errors，触发重试 |
| N42 | 低 | 「没有估计时算不算覆盖」三处口径不一致 | `forecast.py:196`、`showcase.py:150-151`、`report.py:99`（读者） | 本轮不修：三个文件都在冻结清单里（G7，到 10-28 打分提交为止），FIX_PLAN 没排阶段 |
| N43 | 低 | arm (3) 取文字的方式和预注册写法有细微差别 | `EVAL_SHOWCASE_PLAN.md:63`；`search_direct.py:85-91`（读者） | 本轮不修：预注册的对照臂，FIX_PLAN 没排阶段，只记录 |
| N44 | 低 | run.score_all 仍然写出 last_year_same_period 臂 | `run.py:239-243`；`EVAL_SHOWCASE_PLAN.md:12` | 已修 `v2.6d` |
| N45 | 低 | 测试缺口；tests/test_agent.py 的 `__main__` 守卫写在最后一个测试类之前 | `tests/test_agent.py:695-699`；`tests/test_graph.py:115-120`（读者） | 部分修 `tools-regress-v1`：守卫挪到文件末尾；`test_graph` 的 G1 场景测试没加（G1 本轮不修）。各阶段新加的测试见 R 节前的说明 |
| N46 | 低 | BUGS.md 和文档里有几处描述与代码不符 | BUGS.md C8、G2；`AGENT_MVP.md:25` 对 `pipeline.py:38` | 订正（e757e61）：BUGS.md 的 B1、C1、C3、C8、G1、G2 已改。`AGENT_MVP.md:25` 写每个方向最多 5 个 URL，代码是 4（现在是 `pipeline.py:39` 的 `urls_per_direction: int = 4`），AGENT_MVP.md 两次文档提交都没改；NEXT.md v2.5 第 7 条的「60 s」同 C8，原文没改 |

本轮新加的测试：S0 基线 240 个 → `v2.6g` 338 个（S1 `test_settings`、S2 `test_pct_units`、S3 `test_budget_order`、S4 `test_search_errors`、S5 `test_judge_protocol`、
S6 `test_leak_guard`、S7 `test_final_text`、S8 `test_cjk_numbers` 24 个、S9 `test_decode` 21 个（S9b 改写后 18 个）、S10 `test_redirect` 6 个），每个阶段 `unittest` 全过、没有本来就失败的测试。

## R. 本轮修复中新发现、没改的问题（来自阶段报告「发现但没改」一节）

| # | 严重度 | 问题 | 证据 / 出处 | 状态 |
|---|---|---|---|---|
| R1 | 中 | 观测点一侧的百分数 unit 只有精确的 `"%"` 才除以 100：已存 4691 个点里 771 个的 unit 是别的百分数写法（`percent` 593 个……），`fc_jnto_2026_08/v21` 第 2 轮 m3 就是因为 p36（9.6 percent）没除以 100 而失败（开发运行）。但 FOMC 的目标本身是 percent per annum，点一侧不能一律按 is_pct 除 | `compute.py` formula_mc 的点分支；`probes/out/stages/S2.md` 第 6 节第 1 条 | 没改：要先定点的 unit 规则。v2.7 的 U2（`UNITS_PLAN.md` 的百分数守卫）计划处理，U2 还没开始；接入时注意 Q5 |
| R2 | 中（潜在） | 点 id 和区间占位符同名：点 p10 / p90 的值占位符是 `[[p10_value]]` / `[[p90_value]]`，而 `[[p10]]` / `[[p90]]` 是区间上下限。模型写 `[[p10]]` 想指点 p10 时会渲染成区间 P10，数字错而且没有提示。已存运行里只有 `fc_kr_births_2026_08/showcase1` 会碰上 | S7.md 第 8 节第 6 条 | 没改：改名等于改终稿的输入输出约定（G2 还要再变），下一轮再定 |
| R3 | 低 | F1 剩下的来源：ISO 日期仍被清洗成 `2026-[n]-[n]`（已存终稿 116 个 `[n]` 里 18 个来自日期）；贴着字母数字的年份（`FY2025`）照旧被清洗，prompt 没写这一点 | S7.md 第 8 节第 7、8 条 | 没改（D4 没覆盖日期） |
| R4 | 低 | URL 在右括号处被截断（`agent/search.py` 的 `URL_RE` 排除了 `)`），IRMA 的两个 URL 只剩半截；对取页的影响未核实 | S4.md 第 7 节第 2 条 | 没改。v2.11c 的 candidates 按计划用同一个 parse_urls 规范化，所以同样截断：重放 `probes/out/deepseek_search_probe.json`，第 1、2 组各 1 个 IRMA URL 停在 `(1979+-+Last+Calendar+Year`，后面的 `)&_15=True…&Park=YELL` 丢了（和选中的 URL 一致） |
| R5 | 低 | 搜索预扣不是严格的单次上界：按 30,000 个输入 token 估，已存搜索最多 97,500 个；靠搜索费那一份兜住，493 次里没有一次实际花费超过预扣 | S4.md 第 4 节、第 7 节第 3 条 | 没改 |
| R6 | 低 | 23 次 `stop=tool_use` 的搜索全都没有模型给的 URL；和上限、thinking 有没有关系未核实 | S4.md 第 7 节第 4 条 | 没改（要联网） |
| R7 | 低 | 预算中止以后，调用要先等到并发名额才抛 BudgetExceeded（不是立刻失败） | S3.md 第 6 节第 1 条 | 没改（「粘滞中止不变」；已存结果里从没中止过） |
| R8 | 低 | 连续值修正轮复用第 2 轮的 prompt（含「要恢复就写 keep:true」），但修正回复里的 decisions 代码不看（E5 的一部分）；紧凑行没有 unit / 期间 / 来源（例：p128 的「4」其实是 4%） | S5.md 第 8 节第 1、2 条 | 没改（修正轮规则不在 S5 范围；紧凑行格式是 D1 定的） |
| R9 | 低 | ledger 方法表只显示报错的前 200 个字符，多个输入时只看得到第一个（网页和 state.json 是全文） | `outputs.py:211`；S5.md 第 8 节第 3 条 | 没改 |
| R10 | 低 | `probes/replay_discrete_rules.py` 原样跑会在 discrete6 处 `KeyError: 'outcomes'`（探针写于 v2.2.1，之后结果列表改存在 `state["outcomes"]`） | S5.md 第 5 节、第 8 节第 4 条 | 没改（S5 用 scratch 副本跑完了对比） |
| R11 | 低 | 哨兵的字母边界会漏掉「2.44mn / 2.44 mln / 2.44 Mio」这类写法（「million」整词照旧命中）；作废规则对四舍五入写法也生效（韩国「24,000명」） | S6.md 第 8 节第 1、4 条 | 没改（D3 定的写法和代价） |
| R12 | 低 | 网页：泄漏审计表不显示 `directions_voided`，作废的方向只显示「0 页」；实时进度页的 compute 卡片仍显示原始 basis 键；ledger 和 graph.html 的「80% interval」字样没改成 model-based | S6.md 第 8 节第 3 条；S7.md 第 7 节第 7 条、第 8 节第 5 条 | 没改（`web/runs.py`、`_leakage_view` 不在阶段文件里） |
| R13 | 低 | `docs/prompts_bilingual.md`（和生成它的 `probes/gen_prompts_bilingual.py` 里的中文对照）没跟上 S5、S7 改过的 JUDGE_USER、FINAL_SYSTEM、FINAL_USER | S5.md 第 8 节第 5 条；S7.md 第 8 节第 10 条 | 没改（两次文档提交都只改了 BUGS.md、NEXT.md、docs/structure.html，第二次另加 FIX_PLAN.md 的 D10 一行） |
| R14 | 低 | 「% points」写法会被 `is_pct` 当成百分数（已存假设没有这种写法）；restated_point 的词干比较仍会误伤；依赖图标签和网页假设表对「% of ...」的假设多一个 `%` 后缀 | S2.md 第 6 节第 2–4 条 | 部分已修 `v2.11b`（只修 restated_point 一条）：词干分支要求两边的 `is_pct` 相同，比词干之前按整词去掉通用比率词（`compute.RESTATE_GENERIC`：ratio(s)、share(s)、fraction(s)、factor(s)、multiplier、multiple(s)、proportion(s)、percent、percentage、pct、dimensionless、times、fold；index 不去）。「% of annual live births」8.4 对「live births (persons)」8.4 不再算复述。10-22 离线重放（`results/` 下每个 state.json、每个裁判轮的 assumptions，加上 repairs[*] 或旧格式 repair 里的 previous_assumptions，共 311 个快照；`AS.validate` 保留的 1168 个假设次 × 每个点调 restated_point）：按「运行 / 假设 / 点」去重的复述对从 33 个变成 29 个，翻掉的只有 token 题 v1（`ask_02c360ec/web_20261021T224831Z`）第 2 轮的 a1、a11 对 p151、p158（都是 7、`ratio`），没有新增的；离散题 19 个快照（`discrete.with_outcomes` 补上结果列表后跑 discrete.run）0 差异。重算时 v1 这一轮的 m4（裁判写的 m5）改报 S27 的 `formula has more than 60 nodes`：报错晚了一步，m4 的记录因此多了 inputs_detail（16 条）、used_ids（7 个点）、used_assumptions（7 个假设），n_point_inputs、n_assumption_inputs 由 0 变成 7，rests_mainly_on_assumptions 由 false 变成 true；重新渲染时 ledger 方法表的 inputs 列、终稿 summary 的「inputs of m4」和点的「input of m4」、graph.html 的 A→M:m4 边会跟着多出来（已存文件没有重新渲染）；central / p10 / p90、权重、组合结果不变。两边都是 % 的分支没动（S35）；新的取舍见 S36–S38。「% points」和 `%` 后缀两条没改；v2.11b 起「% points」被当成百分数还会让 restated_point 漏掉百分点对百分点的复述：`percentage points` 0.5 对 `% points` 0.5、`percent points` 对 `percentage points` 同值，v2.11a 算复述，现在两边 is_pct 不同（已存的点和假设里 unit 含「% points」「percent points」的 0 个） |
| R15 | 中（要用户定） | 千 / 천 不当倍数：已存的点里 37 个仍被丢（29 个韩文「N만N천N」如 `2만4천275`，8 个以「千」结尾如 `61万1千`），韩国出生题的新闻常用这种写法（缓存页 51 处）；不带倍数字的数后面接千（「12,345千人」里只写 `12,345`）照旧按原文数字取值、小 1000 倍，和 v2.6d 相同 | S8.md 第 7 节第 1 条、第 8 节第 1 条和第 7 条 (f) | 部分已修 `v2.11a`：韩文一组之内的「N천M」（`2만4천275`、`7천478`、`1천72만`、`42억8천400만`、`22조 4천802억`）和 만 后面的「N천」（`2만4천`）由代码读；千万 / 千億 / 천억 这类复合词也能当连写数字的一段（`1億3千万`、`27억6천만`）。已存丢点里因此能解析的 39 个（`probes/replay_scale_v211a.py` 丢点侧）。仍报错丢点、不读错：억 / 조 后面的尾段「N천」（`1억2천`、`1억2천500`：口语里常省掉 만，照字面读会错，未核实语料；方案决定 13 写的是「支持」，这里按「不猜」做，要用户定）、中文单独的「千」段（`61万1千`、`247万6千`）。不带倍数字的数后面接千（`12,345千人`）照旧 |
| R16 | 低 | 不带前缀的「1NN年」（100–199）对所有页面都按民国纪年认：日文 / 中文页上的「創業100年」「過去115年」会被当成 2011 / 2026 年，期间年份检查因此放宽。已存缓存页里这种写法只出现在台湾题的 3 页，都是真的民国年 | S8.md 第 7 节第 3 条 | 没改 |
| R17 | 低 | 中日韩数字仍会读错或误丢的已知写法：「兆」后面的 SI 单位只认 瓦 / 赫 / 帕 / 焦 / 字节 / 比特；中日文段间有空格（「1億 3000万人」）不连读；韩文「조」也是「条」（「제3조 2항」）；数字后隔一个空格接 만 / 억 / 조 开头的韩文词（「2024 조사」）会被当成一截丢掉（相对 v2.6d 是回归，缓存页 0 处）；页面级「（単位：万人）」表头、「成」、「千分之」没处理 | S8.md 第 8 节第 2、3、7 条 | 部分已修 `v2.11a`：「제N조」按法条编号处理（`parse_value('제3조')` 由 3e12 变成 3，`'제3조 2항'` 由 3e12+2 变成 more than one number 报错；quote 里是 `제10조`、vw 只写 `10조` 时丢点）；제 前面是韩文音节的（`결제 1조 원`、`실제 3조원`）照旧当倍数。其余没改（多数写法在缓存页里 0 处；区分「29 만 명」和「2024 조사」要靠词表） |
| R18 | 低 | 页面解码的残余情况（`v2.6f1`）：(1) 头里单引号的 charset（`charset='Shift_JIS'`）w3lib 不认，几乎全 ASCII 的 Shift_JIS 页在 v2.6f1 会被自动探测猜成 cp1250，`v2.6h` 起按 utf-8 解（和 v2.6e、浏览器相同，日文处是 U+FFFD）；日文为主的页由探测解对；双引号和不带引号的写法都认。另：没有声明、夹了几个坏字节的 utf-8 页在 v2.6f1 会被猜成 mac_* 编码，`v2.6h` 已修（S9c）。(2) 自动探测的猜测质量一般：小段 cp1252 法文也被猜成 cp1250，重音字母错、ASCII 数字不错。(3) 页面其实是 UTF-8、头里没 charset、meta 写错（如 iso-8859-1）时按 meta 解成乱码（v2.6e 解对），这和浏览器的做法相同。缓存 286 个快照的头里没有带引号的 charset，也没有 (3) 这种页面；S9 时没有缓存页走到 charset 探测（v2.6f1 没重新统计） | 收尾时离线核对 `probes/out/_docs_r2_check.py`；`probes/out/_rev_s9b/edges.out`、`edges2.out`；S9.md 第 8 节 | 没改（(3) 要用户定） |
| R19 | 低 | S10 遗留：`llm.json_call`、`Searcher.search`、`DirectClient.call` 的 `except HTTPError` 没有关闭响应，走到 3xx / 4xx / 5xx 时有 `ResourceWarning`（G1 输出里 5 条，不是失败，原来就有的写法，以前没有测试走到）；`llm.py` 新加的 `_NoRedirect` 和 `agent/net.py` 取页用的同名类重复，没有合并 | S10.md 第 6 节 | 没改（属于 N3「HTTP 客户端统一」；合并要挪 `net.py`，是重构） |

## Q. v2.7 单位轮新发现、没改的问题（`triangulate/agent/qty.py` 和 U1 的规划钉单位；来自 U0、U1 阶段报告和审查；U0 已提交为 `v2.7a`，U1 没提交，代码只在工作区）

在 `v2.7a` 上 qty 还没接入任何流程，Q1–Q10 都不影响运行结果，U1 / U2 接入以后才会出现。Q11–Q20 来自 U1（工作区，规划节点已经调用 qty）的阶段报告第 8–10 节和第三轮审查；U1 不碰计算，流程里的数和 `v2.7a` 相同。

| # | 严重度 | 问题 | 证据 / 出处 | 状态 |
|---|---|---|---|---|
| Q1 | 低 | `/` 后面的比率基数检查漏了连字符写法：`USD/1000-person` → `0.001 USD * person`、`birth/1000-person` → `0.001 birth * person`、`USD/1-person` → `USD * person`（悄悄读成乘法），同一个串用 per 写是 `0.001 USD / person`；`USD/1000 people` 已经报错。原因是 `_number` 不看下一项是不是 `('op', '-')`，`_expr` 把数字后的 `-` 变成 `*`。量纲变了，下游一般报不符、不会悄悄算错 | 第三轮审查 `probes/out/_rev_u0r3/probe1.py`、`slash_vs_per.py`（5450 对里 112 对不同）；`qty.py:265`、`:329`（行号是第三轮的代码） | 已修（`v2.7a`）：三种写法都报 `number … right after '/' divides only itself, so the unit after it would multiply; put the base and its unit in parentheses or use 'per'`，`tests/test_qty.py` 的 `test_numbers_only_as_rate_base` 管着；`USD per 1000-person` 仍是 `0.001 USD / person`。10-17 下午在 HEAD 上复查 |
| Q2 | 低 | 单数化有错，不完整，举例如下：cookies → cooky、movies → movy、series → sery、species → specy、buses → buse、caches → cach、headaches → headach；us / is 结尾不去 s（taxis、menus、kiwis、skis 不变）；knives → knive、lives → live、potatoes → potatoe、heroes → heroe、gas → ga、news → new、lens → len。只在同一个名词单复数混用时报名词不符，不会算错数 | U0.md 第 9 节第 1 条；第三轮审查 `probe1.py` | 没改；U1 / U2 的 prompt 可以要求计数名词一律写单数 |
| Q3 | 低 | 量纲对、系数和某些用法不同、qty 照 pint 读的写法（会悄悄算错，费米题里少见），不完整，举例如下：gallon / pint / quart / cup 是美制（英制 gallon 大 20%）；`oz` 是常衡 28.35 g，不是金衡 31.10 g；`nm` 是纳米，不是海里；`hp` 是机械马力；`month` 是 30.4375 天的平均月；`B` 是 byte（系数 8），当「十亿」写会差 8 倍 | U0.md 第 9 节第 2 条 | 没改（不要画蛇添足）；U2 的 AUDIT「单位是否和证据一致」可以顺带看 |
| Q4 | 低 | pint 把计数名词或缩写读成物理单位：前后写法一致时数字对、只是名字怪；混用时报错文字里出现 parsec、pint 这类名字，修正轮可能看不懂。不完整，举例如下：EV / TV / PV = exavolt / teravolt / petavolt，`kt` = knot，`pcs` = parsec，`pt` / `pts` = pint，hands、leagues、links（长度），sections（面积），stones、grains（质量），barns | U0.md 第 9 节第 3 条 | 没改；U1 / U2 的 prompt 可以要求计数名词用小写英文单词（vehicle、television、piece） |
| Q5 | 中（潜在，U2 接入后才会出现） | 百分数可能被除两次：`compute.run` 已对 unit 正好是 `"%"` 的点除以 100，`assumptions.effective_range` 已对 `is_pct` 的假设除以 100；U2 再按方法里写的 `percent` 乘 `base_factor` = 0.01，这两类输入差 100 倍。披萨的 p84（`% of population`）compute 没除，乘 0.01 正好对 | U0.md 第 9 节第 4 条；和 R1 同源 | 没改：U2 开工前要先定代码已经换算过的输入按什么单位算 |
| Q6 | 低 | 单位显示不好看：short_ton 显示成 `ton`，quarter、decade 显示成 `quarter_year`、`decade_year`，倍数不是 1 的倒数单位显示成 `1000 1 / kilogram` | U0.md 第 9 节第 5 条 | 没改（`text()` 只影响显示；U4 显示单位时要注意） |
| Q7 | 低 | 自动定义的计数名词存在模块级注册表里，进程内越积越多（每个词一个基本维度）；解释和解析顺序无关（有测试钉住） | U0.md 第 9 节第 6 条 | 没改 |
| Q8 | 低 | `per mille` 被当成计数名词 mille（`1 / mille`），不是 permille；和别的单位混用报量纲不符，不会悄悄算错。`per mil` 报错（mil 在 pint 里是角度单位） | U0.md 第 9 节第 7 条 | 没改（审查没要求映射） |
| Q9 | 低 | 有些写法的报错原样带出 pint 的异常类名，可读性一般，不完整，举例如下：`kg^`、`s^-`（`DefinitionSyntaxError: missing operand`）、`1/0`、`per 0 people`（`ZeroDivisionError`）、`kg^kg`（`DimensionalityError`）、`per 00 **`（`AssertionError`，没有说明文字）、`year^11000`（`OverflowError`）。另外 `g e` 的报错写的是并成一个词后的 `g_e`；`2015 USD` 的理由「the value is already scaled」对不变价美元不完全贴切（给的改法是对的）；U1 起目标单位里写倍数词也报这一句，理由同样不完全贴切（U1.md 第 9 节第 2 条）。这些写法都不会被当成合法单位 | U0.md 第 7 节 G6；`probes/out/u0/r3/fuzz2_new.txt` | 没改（不要画蛇添足） |
| Q10 | 低 | requirements.txt 只加了 `pint==0.26.1`，pint 的依赖 `flexcache==0.3`、`flexparser==0.4`、`platformdirs==4.13.3` 已装在 .venv、没写进去，新环境装出来的版本不一定相同 | U0.md 第 8 节第 5 条；第三轮审查（排序后对比 `pip freeze`） | 已补（`v2.7a`）：requirements.txt 有这 3 行 |
| Q11 | 低 | U1 的测试 `tests/test_plan_unit.py` 第 98、99 行（`test_valid_unit_kept`）的两个换算断言没有检验力：`assertAlmostEqual` 默认 `places=7`，比的是绝对差，而期望值只有 1/365250 ≈ 2.7e-6 和 1e-8；percent 多乘一次 0.01、或一年按 365 天算，都照样通过。U1.md 第 3、4 节把它说成验证了换算 | U1 第三轮审查（实测 `assertAlmostEqual(x, 1e-8)` 在 x = 0.0、1e-10、1e-9、4e-8 时都通过，`assertAlmostEqual(1/365000, 1/365250)` 也通过）；同样的系数 `tests/test_qty.py:283` 已经精确检查 | 没改：U1 受阻就是因为这一条；收尾改成相对比较（`places=12`）或删掉，U1.md 措辞跟着改 |
| Q12 | 低 | qty 遇到幂塔写法会挂死，挂死时一直持有模块锁（`qty.py` 的 `_LOCK` 是 RLock，`parse_unit` 里 `with _LOCK:`）：`kg**2**3**4**5` 的指数是 2**(3**1024)。U1 把 `qty.parse_unit` 接进 plan 节点，模型写出这种单位时 plan 节点一直挂着，同一进程里其他调用 qty 的线程（网页上同时进行的其他运行）也一起卡住。另外 `kg**999999999`、`kg**inf`、`kg**nan`、`kg^1e308` 会被当成合法单位钉住（到 U2，`base_factor` 会对非有限系数报错）。不会悄悄算错数，真实模型写出这种单位的可能性很低 | U1 第三轮审查 `probes/out/_rev_u1r3/hang_find.py`（前 21 个输入各自不到 0.01 s，第 22 个跑满 60 s 被 timeout 杀掉）；10-17 下午复查：后 4 种 `_pin_unit` 都原样钉住、错误为空 | 没改：按 QTY SCOPE 不改 qty，留给 U2 或以后（例如限制指数的大小或嵌套层数） |
| Q13 | 低 | 钉住的 `unit_canonical` 原样存进 target：不截断（target 的其他字段都截到 300 字符），内部的换行也保留。它会写进 state.json，并通过 `dumps(target)` 进入裁判、输入核对、终稿、已公布检查的每一条 prompt | U1 第三轮审查 `probes/out/_rev_u1r3/paths_probe.py`；10-17 下午复查：`'kg/' + 'day/'*200 + 'day'`（806 字符）、`'kg\n/day'` 都原样钉住 | 没改（可选：超过 300 字符按错误处理，或存空白归一后的写法） |
| Q14 | 低 | qty 能解析、但语义不对的目标单位拦不住：`kg / lb` 解析成 `kilogram / pound`；一段期间的总量写成 `visitor/month` 也能解析（prompt 里举了这个反例）。要到 U2 和证据的单位对照时才会报不符 | U1.md 第 8 节第 8 条、第 9 节第 1 条 | 没改 |
| Q15 | 低（潜在，U2 / U4 接入后） | qty 收下、但多半不是模型本意的目标单位：`birth/1000` → `0.001 birth`（本意多半是 `birth/(1000 person)`）；`kt/day` → knot / day；`T/day` → tesla / day；`kvisitor` → 新的计数名词。后 3 种在 U2 换算时会报 `cannot be converted`；只有 `birth/1000` 在公式给 `birth` 时换算系数是 1000、不报错，结果按「千分之一个出生」表示，显示成 `… birth/1000` 读起来是错的 | U1.md 第 9 节第 8 条；`probes/out/u1/_qty_edges.py`（`U1_qty_edges.txt`）；审查 `probes/out/_rev_u1r2/units_probe.py` | 没改：要不要在钉单位时拒收「纯计数、倍数不是 1」的写法，留给 U2 定 |
| Q16 | 低 | 单位重问的回复和它被拒的原因都没有保存：calls.jsonl 只记计量字段（重问只多一行 `arm "plan"`、`attempt 1`，`ok` 只表示回复是 JSON 对象），state.json 只有被采用的那一份规划。真实运行之后能看出重问有没有改对，看不出改对时第一次错在哪、没改对时为什么被拒 | U1.md 第 8 节第 9 条、第 9 节第 7 条；`probes/out/u1/_calls_log.py`（`U1_calls_log.txt`） | 没改：要不要把重问的结果写进 plan note（会改 U1 规定的 note 格式）等用户定，阶段报告推荐改 |
| Q17 | 低 | 重问的回复钉住了单位、有方向，但方向比第一份少或差，仍会整份替换：代码只判断能不能用，不判断规划的好坏 | U1.md 第 9 节第 6 条 | 没改 |
| Q18 | 低 | graph.py 现在 import qty（pint 注册表），`import triangulate.agent.graph` 从 1.15 s 变成 1.58 s（各跑一次） | U1.md 第 9 节第 3 条 | 没改 |
| Q19 | 低 | `probes/web_demo_fake.py` 用 `tests/test_web.py` 的 FakeLLM，假规划没有 unit_canonical：演示服务里规划会多问一次（多等约 5 s），审批页多一条 `unit not pinned` 的 note | U1.md 第 9 节第 4 条 | 没改（FakeLLM 很多测试共用）；要看「钉住」的样子，可以在 web_demo_fake 的 SlowLLM 里给 plan 回复加 unit_canonical |
| Q20 | 中（潜在，只在 U1 提交之后、U2 之前做真实运行时） | 过渡期：裁判、输入核对、终稿、已公布检查的 prompt 都能看到钉住的 `unit_canonical`，但 compute 还不做量纲检查和换算，终稿可能把用别的单位算出来的数标成钉住的单位 | U1.md 第 0 节第 4 条、第 10 节；钉住版 G2 `probes/out/u1/g6_pinned_r3.txt` | 没改：照 UNITS_PLAN，U3 做完之前不做真实运行 |

## S. 冻结前冒烟测试（2026-10-17 晚，代码 `v2.8c`，tag `smoke1`；修复 `v2.8d`；10-18 单位核对 `v2.8e`，冻结）

4 道题：芝加哥披萨（t/day）、东京迪士尼 2026 年 9 月日均入园（visitor/day）、纽约 2026 年 10 月出租车 + 网约车日均行程（trip/day）、英国每天喝几杯茶（cup/day）。
agent 用命令行 `--ask --auto-approve`，两个基线用 `probes/smoke_run.py`；结果在 `results/agent/smoke_*/smoke1/`，基线回复在 `probes/out/smoke/`（gitignore）。
速览脚本 `probes/smoke_inspect.py`。

| 编号 | 严重度 | 问题 | 证据 | 状态 |
|---|---|---|---|---|
| S1 | 高 | 假设 id 只有 a1..a8：披萨题修正轮写到 a10，用到 a9 的「餐馆 + 在家」加总方法被拒，整题没有估计 | `results/agent/smoke_pizza/smoke1/state.json` 的 compute.methods（m4、m5：`assumption a9 was rejected (id must be a1..a8)`） | 已修 `v2.8d`：id 放到 a1..a12（MAX_PER_RUN = 12），sum 方法仍最多 8 个（MAX_PER_SUM）。用 v2.8d 重算这次保存的方法：82.5 t/day |
| S2 | 高 | 「numeric constant 1000 not allowed…; make it a named input」把修正轮带偏：第一轮的 `/ 1000` 只是克换千克，修正轮照提示自造了 `k_grams_per_kg`（不存在的常数） | 同上，judge_rounds[1].repair.errors 和 m1、m2 的报错 | 已修 `v2.8d`：钉了单位时，报错接着说「只是换单位的数就删掉、在 unit 里写公式给出的单位，代码换算到目标单位」 |
| S3 | 中 | 公式里直接写了代码给的常数（k_days_per_year），inputs 里漏列，方法被拒（茶题的供给路线 m1、m3） | `results/agent/smoke_tea/smoke1/state.json`：`formula names ['a2', 'k_days_per_year', 'p135'] != inputs ['a2', 'p135']` | 已修 `v2.8d`：代码给的常数出现在公式里、inputs 没列时由代码补上（不改模型给的 params）。重算：茶 1.00 亿 → 8,361 万 cup/day（供给路线进了合并） |
| S4 | 低 | 终稿单位重复：「100,000,000 cups of tea per day cups per day」「19,800,000 trips trips」。`[[pN_value]]` 本来就带点的单位，U4 让模型在估计值后写 `[[unit]]` 之后，模型在观测值后也补了单位 | 三道出数题的 final.template | 已修 `v2.8d`（prompt 一句）：观测点占位符已经带单位，后面不要再写。只能在新运行里看效果 |
| S5 | 低（我的失误） | 冒烟脚本第一次给两个基线的目标单位是 `""`（无量纲），每天的量、质量题基线必然被量纲检查拒掉，看起来像 G1 没修好 | `probes/out/smoke/first_try_dimless/` | 已改：按题给 `tonne/day` 等单位重跑。预注册的题目：按日均问的必须带单位，只有一段时间的总数才能用 `""` |
| S6 | 记 | 模型的建模错误，不是代码问题：纽约题用 2 月的月总量除以 10 月的天数（k_days_target）；迪士尼题 m1、m3 是同一个式子的两种写法（重复方法，用户 10-17 定为搁置）；结构化基线把 0.008 这样的占比标成 `%`（披萨基线因此小 100 倍） | 各题 state.json；`probes/out/smoke/structured_smoke_pizza.json` | 不修。方法声明的 unit 写错（比如年总量写成 per day）代码查不出来，是已知限制 |
| S7 | 记 | 东方乐园（OLC）的 IR PDF 被 robots.txt 禁止，照规矩跳过；PDF 取文本（L2）在披萨题里正常（USDA 两份 PDF 各抽出 18、15 个点） | smoke_tdr、smoke_pizza 的 pages | 正常行为 |
| S8 | 高 | 裁判声明的结果单位写错，代码照用：smoke2 披萨 1,027,630 t/day（公式给的是「每天多少个 100 g」，声明成 t/day），大一万倍 | `results/agent/smoke_pizza/smoke2/state.json` | 已修 `v2.8e`（用户 10-18 的设计）：三个模型核对 + 一个模型裁定结果单位，`agent/unit_review.py`。重放 smoke2：102.8 t/day；smoke3 实跑披萨 128 t/day、茶 1.09 亿 cup/day，茶题里一个声明成 kg/day 的方法被改成 1000 cup/day |
| S9 | 记 | `v2.8e` 冻结时已知、没修的问题（用户 10-18：版本测试里没出现的错误不拦）：(1) 单位核对判失败的方法只放进 failed、没进 audit_failed，compute 仍按裁判的单位算并参与合并（审查用假模型复现）；(2) 代码不核对裁定的 result_unit 是否等于它自己推导的结果，重试时可能只改结果串（旧版 prompt 重放里茶题出现过一次 1000 倍）；(3) 三个核对模型的 prompt 相同、temperature 0，答案几乎总是一样；(4) 给旧回测运行补上 unit_canonical 重放时，「全年 × 月份额」的写法（韩国 m2、台湾 m3）被推成 birth/year、判失败 | 审查结论 `probes/out/unit_review/workflow_verified.txt`；重放 `probes/out/unit_review/replay*.json`（gitignore） | 冻结版不修。smoke3 两次实跑都没有触发。冻结后改过的 graph.py 一行、prompt 一句没测全，撤回了，diff 留在 `probes/out/unit_review/untested_after_v28e.diff` |
| S10 | 记 | 一道网页实跑题没出数（冻结版 v2.8e，10-18 用户实跑）。三处流程问题叠在一起：(1) 裁判第 2 轮丢掉第 1 轮已经用上的总数点，把这个总数写成假设，公式全是假设；(2) `assumptions.target_reason` 按单位词干判「目标的水平值」，目标单位和假设单位都是 person、名字没有比率词，这个总数被当成目标本身拒掉（误伤：目标只是其中一部分）；(3) 修正轮只有一次，compute 只报第一个输入错误，修正轮没看到「公式至少要一个观测点」这条，裁判把假设改个编号原样交回，再被拒。证据本身够做带数据的估计：总数点 × 观测到的比例，再借同类对象的比例 | 该运行的 state.json（judge_rounds[1].repair） | 冻结版不修（用户 10-18 同意记为已知局限），预注册和留出测试之后再看 |
| S11 | 记 | 同一道题第二次实跑也没出数，原因不同：修正轮裁判已经修对，m1 = 上一期的实测总数（role 写明「作为基数」）× 两个比例，m2 再乘一个期间比和更早一期的比例（role 写明期间），代码都能算；输入核对（模型调用）却判两者「role 要求目标那一期、证据是更早的期」，把目标的期间当成了 role 的要求，两个方法都被排除。初稿里「总数写成假设、被像目标的规则拒」又出现一次（同 S10） | 该运行 state.json 的 judge_rounds[1].audit_failed 和 methods 的 role | 冻结版不修；属于「模型核对不可靠」一类，和单位核对实验（S9）同类 |
| S12 | 记（用户 10-18 指出） | 参照对象层次不可比：两次实跑里当参考的对象层次远高于目标，它们的比例搬到目标上很可能偏高；会公布这类数字的多是头部对象，取证本身有选择偏差。裁判第一次运行的理由里写过「目标层次较低可能拉低比例」，仍照搬头部对象的比例。裁判 prompt 和输入核对都不检查参照对象的可比性（输入核对只拦「不同实体」） | 两次运行的假设 a1 / a2 及其 rationale | 冻结版不修；以后的方向：参照对象要求写明可比性（层次、规模），或让核对按可比性给出降权 / 放宽区间，等留出测试后再定 |
| S13 | 记 | v2.8e 冻结后实跑暴露、已修的问题（详见 NEXT.md 断点表）：期间留空被丢（v2.8f）、中文表头单位和千分位（v2.8g/h）、套用可比对象不调整（v2.8i）、单位核对失败的方法仍进合并 + 期间总量换算（v2.8j，即 S9(1)）、% 除两次（v2.8k）、修正只有一次（v2.8l，即 B5）、每方法假设上限 3（v2.8m）、份额乘错基数（v2.8n） | 各运行 results/agent/ask_9b1539aa 等的 v28*_test | 已修，冻结 `frozen-v2.8n` |
| S14 | 已修（v2.8o） | 原文用单词、分数、区间写的数一律被丢（披萨题 NHANES「males had four and females had three slices」、「1/6 of 14-inch pizza」；历史运行约 255 + 78 个） | `results/agent/smoke_pizza/smoke4` 的 dropped_points | v2.8o：抽取员给 number / low / high，算前模型核对（NEXT.md 断点） |
| S15 | 已修（v2.8p，按数值比） | 泄漏哨兵只登记数字和中日韩写法，没有英文数词；v2.8o 之后单词写的数能进证据，真值如果在页面上写成单词（"two million"）哨兵查不到。实跑里没出现 | `evidence.leak_forms` | 回测 / 留出测试前再看 |
| S16 | 已修（v2.8p：提示词 + 第 2 轮看到第 1 轮方法；v28p_test 里块数进了最终答案） | 披萨 v2.8o 实跑：裁判第 1 轮方法用了 NHANES 块数（mean(p35, p36) × p37），第 2 轮改写时换成假设「每次吃多少克」，这条又被单位核对否掉，块数最终没用上；修正轮还有「assumption a3 rejected: value, low and high must be numbers」 | `results/agent/smoke_pizza/v28o_test/state.json` 的 judge_rounds | 没改（裁判的选择） |
| S17 | 记 | v2.8o 行为变化：欧式小数逗号（"16,8%"、"R$ 54,46"）、OCR 错字（"8l,030"）、".75" 以前被代码丢，现在走抽取员读数 + 模型核对进来（这次 24 个真实点全部核对通过） | 同上运行的 points | 观察 |
| S18 | 记 | 披萨 v2.8p 实跑：NHANES 路线只用了男性每次 4 块（p6），乘假设 a3 = 0.9「Chicago 每次块数相对 NHANES」，没用女性 3 块（p7）；数值接近男女平均 3.5，但 a3 的含义混了「男→全体」和「芝加哥→全国」两件事。修正轮 3 轮都在修「每天的比例 × 每次块数」消不掉 occasion 的单位 | `results/agent/smoke_pizza/v28p_test/state.json` | 没改（裁判的选择） |
| S19 | 已修（v2.8r；v2.8q 只修单位核对一层，回退） | 数和单位不成对：代码已按 scale_word 乘了 万，unit 仍写「万元 (10,000 CNY)」，单位核对判成 10000 CNY/year 又乘 10^4（恒顺 v2.8p 6089 万瓶）；已存 7597 个点里有 76 个是这种状态 | `results/agent/ask_9b1539aa/v28p_test` | v2.8r 三层：提示词、代码配对单位、单位核对兜底 |
| S20 | 已修（v2.8r） | 终稿和点表里乘过倍数的值配着原单位串（「47,741,300 万元 RMB」），裁判也据此写 role「in 10,000 CNY」 | `v28q_test` 终稿 | v2.8r 第 1、2 层 |
| S21 | 记 | 单位裁定隐含密度：恒顺 v2.8i m2「吨 / (毫升/瓶)」被裁定成 1000000 bottle/year（默认 1 kg/L），量纲上缺一个密度输入 | `probes/out/unit_multiplier/replay.json` | 没改 |
| S22 | 记（用户 10-18 指出） | 修正轮把裁判修不了的问题也交回裁判：恒顺 v2.8p 三轮修正都收到「m1 和 m3 差 3 倍以上」，真正原因在单位核对层，裁判看不到；m1 三轮结果逐位相同也不停，修正阶段占这次运行 43% 的 token | `v28p_test` 的 judge_rounds[1].repairs、calls.jsonl | 没改 |
| S23 | 记（test2 未公布题，冻结版不修） | 墨西哥出口 `fc_mx_exports_2026_09` 没出数：173 个点裁判只保留 8 个，4 个方法引用的正是它自己丢掉的点（p43、p1、p110、p29，"id unknown or discarded"）；3 轮修正每轮换一个被丢的点去引用，都没修好。所有模型调用都成功，不是基础设施故障，按预注册记为失败。**根因归 S24**（10-19 复盘）：代码丢的 183 个点里 156 个是西文写法（INEGI 表格空格千分位 `56 487.9`、西文表头 `millones de dólares`、`mdd`、`mil millones`），INEGI 的美元水平值全部丢光，过代码检查的水平值只剩 2 个英文页的四舍五入值；裁判引用已丢的点是下游症状，这个问题本身仍在 | `results/agent/fc_mx_exports_2026_09/test2/state.json` 的 judge_rounds[1].repairs | 没改 |
| S24 | 记（test2 未公布题，冻结版不修） | 德文 / 欧式数字写法：千分位用「.」时，两个点的写法（`2.994.415`）因为有歧义被丢，一个点的写法（`-66.981`、`-44.000`）被当成小数读成 -66.981、-44.0。德国失业 `fc_de_unemployed_2026_10` 因此只剩读错的变化量，「水平值 + 负变化量」又没法按对数正态抽样，没出数。也会影响回测题里的 KBA（`256.774`）和 INE（`371,6 millones`）。10-19 复盘补充：德国还丢了 `Millionen`/`Tsd.`/`Mio.` 倍数词和「(in Tausend)」表头；墨西哥（S23）的根因也是这一类（西文倍数词、空格千分位、西文表头）；离线检查 `parse_value('2,994 Millionen','')` 静默返回 2994.0（未核实有没有点因此过检） | `results/agent/fc_de_unemployed_2026_10/test2/state.json` 的 p11、p20 | 部分已修 `v2.11a`：德语 / 西语 / 葡语等倍数词（`Millionen`、`Mio`、`Milliarden`、`Tsd`、`mil millones`、`milhões`、`mdd`、`mld`）报错丢点，`parse_value('2,994 Millionen','')` 不再静默返回 2994.0；读数路径上只在这个词后面不再有数时报错（墨西哥 15 个复合写法点不变）。欧式千分位（一个点的 `-66.981` 读成小数）、空格千分位、西文表头没改 |
| S25 | 记（用户 10-20：「DeepSeek 开思考模式容易出格式问题」，先不修） | DeepSeek 思考模式（v2.9a/b 的 `TRIANGULATE_THINKING`）下，裁判的 JSON 经常不合法：思考臂 17 题共 66 次裁判调用（含修正轮）里 16 次 invalid_json，全部 finish_reason=stop、没有截断；v2.9b 抓到的 10 例全是同一种：方法对象在下一个 `{"id": ...}` 之前少了一个右花括号（解析器报 "Expecting property name enclosed in double quotes"）。规划、输入核对、单位裁定、修正轮几乎不出错，问题集中在输出最长、嵌套最深的裁判。加拿大（第 1 次）和台湾出生因此没出数。候选修法（没做）：A 在报错位置定点补括号、B JSON 无效时关思考重问、C 让模型只修语法 | `results/agent/*/test2_think*/calls.jsonl`、`results/agent/*/think/calls.jsonl` 里 error=invalid_json 的记录（v2.9b 起带 text_head / text_at_error） | 没改 |
| S26 | 中 | 区间读数被预乘：抽取员把 low / high 先乘了倍数（违反 prompts.py:138「number 不乘倍数词」），代码再乘写法末尾的倍数，大 1000 倍以上。例：ask_02c360ec v1 的 p78 `32K-128K` = 8e7、p83 `200K-400K` = 3e8；ask_81334846 的 `24 million to 24 billion` = 1.2012e19、`~27-29k` = 2.8e7，全部 value_check 还是 pending，没有方法用过。另外 split_multiplier 只切最后一个倍数（`32K-128K` → `('32K-128', 1e3)`），两端倍数不同（`500K-1.2M`）也不报错。v2.11a 让「缩写配全词」的区间点不再被倍数依据挡掉（`90 - 95k` + thousand、`4.5-5M` + million），以后这类点会更多地以 pending 进来，要靠 value_check 拦（核对模型看到的写法是去掉倍数的 `90 - 95`） | 这 4 个点的 state.json；v2.11 方案第 5 节（不在本仓库） | 没改（v2.11a 明确不做，单独提） |
| S27 | 低 | formula_mc 的节点上限 60（`methods.py:28` 的 MAX_NODES_AGENT）：token 题 v1（`ask_02c360ec/web_20261021T224831Z`）第 2 轮的 m5 是多项相加的长公式，`check_agent_formula` 报 `formula has more than 60 nodes`；已存的报错是 R14 的 `restates kept data point p151`，R14 修好后会换成这一条 | 10-22 离线用 `methods.check_agent_formula` 复核 | 没改 |
| S28 | 低（冻结） | `triangulate/units.py`（G7 冻结到 10-28 打分提交）不认 quadrillion：`parse_unit('quadrillion tokens')` 得 factor 1.0、计数名词 ('quadrillion', 'tokens')（`million tokens` 是 1e6）。`units.parse_unit` 只有 arms / data / engine / showcase_engine 调用；agent 路径经 `expr.py`（`agent/methods.py` 导入）只用 units 的量纲工具（DIMLESS、dims_*），不解析单位串，agent 的单位解析走 `agent/qty.py` | 10-22 离线复现 | 没改：10-28 之后再补 |
| S29 | 低 | `_pair_unit` 每个倍数只试一个写法（`SCALE_FOR_FACTOR`）：倍数只写在 unit 里、quote 用的是另一种文字的写法时不挪到数上。例：韩文 `만 명`（1e4 的写法是「万」）、繁体表头。1e10 / 1e11（百亿、千亿、천억）v2.8r 起单位里认得出、但没有挪到数上的写法，unit `千亿元` / `천억 원` + vw `3.5` 照旧是 3.5 配原单位（数和单位仍成对，没读错；v2.11a 为了不改已有行为没补）。多写法循环会改变今天韩文 / 繁体表头的结果 | `tests/test_large_units.py` 的 `test_unit_multiplier_pairing` 钉住现状 | 没改（v2.11a 明确不做） |
| S30 | 低 | 单位里的倍数正则 `_UNIT_MULT` 不分大小写，缩写会撞州名：现有的 `mn` 让 unit `housing starts in MN` 报 `names a different multiplier (MN)`，点被丢。所以 v2.11a 没往这个正则里加 `tn` / `bln` / `trn`（TN 是田纳西）；value_as_written 里的 `$5 tn`、`5bln` 照常认（那是另一套读法） | 10-22 离线复现 `strip_unit_multiplier('housing starts in MN', 1e3)` | 没改 |
| S31 | 低 | 泄漏哨兵的写法没扩：`leak_forms` / `_cjk_exact_forms` 只登记 thousand / k、million / M 和 万 / 億 / 亿 / 억 段，1e9 以上的 billion / trillion / 兆 / 조 写法都没登记。fc_kr_online_2026_08（登记值 24211800000000、18902100000000）最可能的写法「24조 2천118억」「24조 2,118억」没登记（10-22 扫缓存页：这两个值的这几种写法 0 处）。v2.11a 没让哨兵从倍数表派生，登记写法逐字不变。v2.11a 审查发现的回归：fc_kr_births_2026_07 的登记值 24275 在韩文报道里写成 `2만4천275명`（`data/raw/agent/fc_kr_births_2026_08/159e23d84a6ae699.txt`），页面哨兵没登记这个写法；v2.10i 代码解析不了、点走读数路径，被 `leak_number_hit` 按数值比过，v2.11a 代码能读了就不比了。已修：`pipeline._process_page` 改用 `ev.leak_point_hit`，代码解析的中日韩写法按精确值比（四舍五入写法照旧不比，C3），抽取员读的数照旧；已存回测运行的保留点里 0 个会因此命中（重放第 4 项）。顺带看到的：英文写法 `3.2 million` 对登记值 3,200,000 也不在写法表里（只登记 `3.20 million`），fc_ca_rail_2026_07 有 3 个已存保留点（p23、p57、p70）的值正好等于登记值，这次没改（是不是泄漏未核实） | v2.11 方案第 5 节（同上）；`tests/test_leak_guard.py` 仍钉着 1e9 以下的写法表；`tests/test_large_units.py` 的 TestLeakGuardForCjkParsedNumbers | 写法表没改（版本测试没触发过，按规则不修）；中日韩代码解析的数按精确值比：已修 `v2.11a` |
| S32 | 记 | v2.11a 之后仍按面值读、或仍可能读错的已知写法（不完整）：空格隔开、前面没有货币符号的 K / M / B（`5.8 B` → 5.8）；小写 t 在 scale_word 为空时按吨（`100t` → 100）；scale_word 填了 trillion 时 quote 里紧跟数字的 t 也算依据（`3.5t gvw` 会读成 3.5e12，代码解析的数不交模型核对）；`100兆宽带` → 1e14（R17）；韩文「해」不处理；德语 Billion（= 1e12）按英文 billion 读成 1e9；法文页面的 `5 mn`（分钟，未核实语料）会按 million 读；`$5BB`、`$3MMM`（有的金融写法 = 1e9；BB 也是债券评级，没收）、不在 Rs / ₹ / INR 后面的 `cr`（`$500 Cr` 可能是贷方）、不在货币后面的 `bil` / `mm`（`5 bil` 挪威语是汽车、`5mm` 是毫米）按面值；数字后面直接接「千 + SI 单位字」（`3千米`、`12,345千瓦`）照旧把千当倍数（3000、1.2345e7，v2.8g 起；unit 再写 千米 / 千瓦 就差 1000 倍）；억 / 亿 后面直接接没有倍数字的阿拉伯数字（`1억 5000`、`3亿5000`）照字面读成 100,005,000 / 300,005,000（v2.6e 起；口语里常是 1억5000만，未核实语料）；没收的外语倍数词（阿尔巴尼亚 `milionë` 等）按面值。以下报错丢点（不是读错）：억 / 조 后面的尾段「N천」（`1억2천`、`1억2천500`，见 R15）、천 后面接 백 / 십（`2천5백만`）、白名单外的 hundred 叠加（`3 hundred trillion`）。连写数字的 split_multiplier 报最后一段的倍数（`1조 2천억` → 1e11，v2.6e 起的约定），unit_review 的「代码乘过」说明据此写 | `probes/replay_scale_v211a.py --readings`；`tests/test_large_units.py` | 记 |
| S33 | 中 | 货币符号前面的负号被丢掉：`_NUM` 只认紧贴数字的负号，`negative US$5.9 billion`、`-$1.2B`、`minus €3bn` 读成正数。fc_googl_tokens test2 的保留点 p97（Alphabet 季度自由现金流 `negative US$5.9 billion`）存的是 +5.9e9，只出现在点的分组里、没进方法；v2.11a 按倍数比对之后，fc_meta_capex test2_think 的 `negative $9.14bn`（以前因为倍数依据被丢）会以正数保留，所以同版修。`(-1,234)` 以前读成 +1234，也一起改成负数 | `results/agent/fc_googl_tokens_2026_q3/test2/state.json` 的 p97；`results/agent/fc_meta_capex_2026_q3/test2_think` 的丢点（缓存页 7702547e375fccb7） | 已修 `v2.11a`（`_SIGN_BEFORE`；重放里 p97 变成 -5.9e9） |
| S34 | 低 | 「只抄了中日韩数字的一截」检查（`_cjk_reads` 第 ① 条）只认单个倍数字，连写数字的后一段单独抄出来会被当成完整的数：`3천억 5천만 원` 里只写 `5천만`（保留 5e7，真值 3.0005e11）、`3千亿5千万` 里的 `5千万`、`22조 4천802억` 里的 `802억`。v2.10i 就有；v2.11a 的 parse_value 能把整串读成一个数之后，两边不一致更明显 | 10-22 审查复现；已存保留点 0 个受影响（重放） | 已修 `v2.11a`（`_CJK_BEFORE` 认复合倍数词和「数字 + 千 / 百」，往前看 8 个字符） |
| S35 | 低 | restated_point 两边都是 % 的分支只比数值，不同量的两个百分数同值也算复述。已存运行里 2 处：`fc_lhr_pax_2026_09/think` 第 2 轮 a1「September 2026 Heathrow passenger loss from early-September NATS disruption」0.5 % 撞上 p24「Heathrow total air transport movements, September 2025, year-on-year % change」0.5 %（保存的 m1 因此被拒）；`smoke_pizza/smoke2` 第 1 轮 a6「Share of Chicago pizza mass sold through restaurants」56 % 撞上 p174「Share of Americans selecting Illinois as a top-five pizza state」56 % | 10-22 离线逐对重放（口径见 R14 状态格）：这个分支在已存运行里一共 11 对，另外 9 对按名称人工看是假设照抄了点的值（FedWatch 5 对、恒顺美国占比、另一道网页题 2 对、黄石 9 月占比） | 没改（v2.11 方案决定 16：这个分支挡住的多数是真复述，包括 FedWatch；再要求名称词干有交集，这 2 个误判还在，另一道网页题那一对真复述反而会漏。10-22 用 `assumptions.stems` 比名称复核过：两个误判的名称词干交集是 heath / septe、pizza / share；另一对的点名称是中文，交集为空） |
| S36 | 低 | v2.11b 的通用词表里有 `shares`，它既是份额（share 的复数），也是股数。按整词去掉之后，股数单位只剩 `shares` 时不再比词干：`'shares'` 对 `'shares'`、`'shares'` 对 `'common shares'` 同值都不再算复述（v2.11a 算）；`shares outstanding` 这种还有别的实词的照旧抓到 | 10-22 离线复现；已存运行的点和假设里 unit 含整词 shares 的 0 个 | 没改（方案按审查把它列进通用词表） |
| S37 | 低 | v2.11b 起只要有一边的单位去掉通用词后什么都不剩，词干交集就是空的，这一对就不再算复述（% 分支只管两边都是 % 的，兜不住）：`ratio` 对 `ratio`、`times` 对 `times`、`share (0-1)` 对 `share`，以及只有一边是纯通用词的 `fraction` 对 `fraction of US adults`、`ratio` 对 `ratio of exports to GDP`、`share of households` 对 `share`，同值都不再算（v2.11a 算），真的复述会漏检；只靠单位分不出两个比率是不是同一个量。规模：已存的 1168 个保留假设次（口径同 R14）里不是 % 的 985 个，其中 661 个去掉通用词后没有词干（659 个是 v2.11b 才变空的：ratio 356、fraction 120、dimensionless 85、share 51、factor 19 等），它们的 restated_point 一律返回空串。`tests/test_pct_units.py` 的 `test_non_percent_rules_unchanged` 钉住 `ratio` 对 `ratio` 返回空串 | 10-22 离线复现；已存运行里因此不再算复述的只有 R14 那 4 对（点一侧都是 `ratio`，按名称看都是误判） | 没改（v2.11 方案 D1 的取舍） |
| S38 | 低 | v2.11b 通用词表的写法缺口：(1) `per cent` 被 `ablation._tokens` 切成 per（停用词）和 cent，cent 不在 RESTATE_GENERIC 里，所以 `per cent of respondents` 对 `per cent growth` 同值照旧算复述（共享的只是「百分数」），换成 percent 写法就不算，同一条规则按拼写给出不同结果；cent 不能直接加进词表，它也是货币单位（已存点里有 `US cents per question`、`USD cents`）。(2) 词表里 multiplier、percentage 只有单数，`multipliers` 对 `multipliers`、`percentages` 对 `percentages` 同值仍算复述，单数写法不算 | 10-22 审查复现（假设先过 `AS.validate`）；已存保留假设里 unit 含整词 per cent、multipliers、percentages 的 0 个（点里 per cent 20 个），已存运行不受影响 | 没改（cent 怎么处理、复数要不要补，要用户定） |
| S39 | 低 | v2.11c 的 candidates 两处形状上的限制：(1) OpenAI / Kimi 每个 web_search_call 一组，组里只有 queries 和 urls，不记 action 类型：open_page 的组是 `{"queries": [], "urls": [打开的 url]}`、find_in_page 的组是 `{"queries": [], "urls": []}`，和一次没带查询词的 search 调用形状相同，事后分不出来；(2) Anthropic 格式（DeepSeek / Claude）的先进先出兜底不看先后：没有 id 的结果块出现在所有 server_tool_use 之前，也会配给后面那个查询词 | 10-22 读码 + `tests/test_search_candidates.py` 的 OpenAI 一例；DeepSeek 探针回复和金样本里结果块都在对应的 use 之后，(2) 没触发过 | 没改（计划只要求 queries 列表和先进先出，加 action 字段或按先后配要用户定） |
| S40 | 低 | v2.11c 给 adapter 的 search_unpack 加了新约定（返回 `groups`；Anthropic 格式另返回和 queries 一一对应的 `query_ids`），但 `PROVIDERS.md` 第 3 节 adapter 接口表（:59）的 search_unpack 一行还是「查询词、结果 URL、文字块、搜索次数、搜索错误数」，没写这两个字段。`by_query` 对缺 `groups` 的回复按空处理（`p.get("groups") or []`），不报错：以后新加的 adapter 如果照这张表写、不返回 groups，这家的 candidates 会静默变成 `by_query: []`（选中的 URL、计量不受影响）。:170 那句「只有 json_402、search_402 两组的返回值有意不同」在第 7 节「Verification（v2.10a）」里，是 v2.10a 当时的记录，不算过时 | 10-22 审查；读码 + `PROVIDERS.md:59` | 没改（v2.11c 的范围只写了 search.py 的模块说明；接口表补不补一句、要不要对缺 groups 报错，要用户定） |
| S41 | 低 | v2.11d 的 `fetch.page_published` 按计划用 htmldate `original_date=True, extensive_search=False`，但这个快速模式并不只认结构化位置的日期：(1) meta、JSON-LD、time 标签都没有日期时，最后一步在正文里找裸写的日期（htmldate 1.11 `find_date` 的 `if not extensive_search` 分支，`pattern_search(text, TIMESTAMP_LOOSE_PATTERN)`）。catalystcoop 那页（fc_us_gen_2026_07 test2 的快照，2026-04-15，标题「PUDL 2026.4.0 documentation」）因此取到正文里数据的起始日「beginning 2018-07-01」，这页 8 个期间缺失的丢点在新代码下会被标成 2018-07-01；同样来自正文的还有 token 题 v1 的 ai.google.dev（11 个点，2026-10-13）和 arxiv 2601.20115v3（2 个点，2026-05-04），这两个日期看上去是对的。(2) 结构化日期晚于上限时，htmldate 退成同月 1 日再试，没越界就用它：2026-09-03、上限 2026-09-01 得 2026-09-01（不会晚于上限，所以不是泄漏，只是日期偏几天） | 10-22 离线重算（`probes/out/v211d/loose_fallback.py`，不进 git：把正文裸日期那一步换成返回 None 再算一遍，test2 的 168 个可兜底点里 8 个、v1 的 109 个里 13 个变成没有日期，v2 的 137 个 0 个）；`tests/test_page_date.py` 的 htmldate 月初一例 | 没改（取法是计划和决定 3 定的；要不要去掉正文裸日期这一步、要不要拒收退到月初的结果，要用户定） |
| S42 | 低 | 依赖图的点详情（`graph.html` 和 Verrier 控制台图侧栏，都用 `outputs.dep_graph` 的固定键，outputs.py:116）没有 `period_source`：v2.11d 用页面日期兜底的点在这里显示 period_start 为空、period_end 是页面日期，看不出期间是页面日期补的。计划 B 第 5 条列的显示处里没有这一处，所以没改 | 10-22 读码 | 没改（加这个键，每个点的详情都会多一行 null；只给兜底的点加，要用户定） |
| S43 | 中 | v2.11d 的页面日期点能成为「已公布」候选：`published.candidates`（published.py:175-176）用 `C._span` 比期间，页面日期点期初为空、`_span` 取 ps = pe = 页面日期，目标是时点或 3 天以内（期初 = 期末，例如「as of 2026-10-21」）、页面日期离目标期末不超过 3 天、页面的 page_date 又不早于目标期末时，它就过期间筛选，进 EarlyWatch（真实使用、裁判之前）和 published 节点。模型确认后提前停、终稿由代码写：证据行先写 `(period not stated (page dated …))`，下一句是 `A separate model check confirmed that this data point has the pinned target's entity, measure and period`（published.py:281），前后矛盾；PUBLISHED_USER 也对模型说候选的期间和目标一致。改前同样期间为空的点进不了候选（非 base_rates 直接丢；base_rates 豁免的点 pe 为 None 被跳过）。计划的决定 9 只排除了 build_series，published 这条路没人定过 | 10-22 审查复现（`probes/out/v211d/review/published_cand.py`，不进 git：ask_81334846/web_20261021T213815Z 的目标 + 一个期间为空、page_published 2026-10-19、page_date 2026-10-21 的点：`verify_point` 通过，`candidates` 返回 1 个，同一点按改前写法 0 个）；已存运行里时点目标 2 个（ask_81334846/web_20261021T213815Z、smoke_tea/smoke3）；固定回归不做已公布检查，不受影响 | 已修 `v2.11d`：选 (a)，`published.candidates` 跳过 `period_source == page_date` 的点（和决定 9 一致）；`tests/test_page_date.py` 的 TestPublishedSkipsPageDated |
| S44 | 低 | v2.11d 的标记 `not stated (page dated D)` 的 D 是 page_published，同一行的 via 列（graph.py:144，裁判 prompt 定义为 `via = archived snapshot date or live page date`，prompts.py:203）和 published 候选行的 `({via} page dated …)`（published.py:206 `_via`）用的是 page_date（live 页取所有日期里最晚的一个）。live 页上两个日期不同时，同一行出现两个不同的「页面日期」，published 候选行和终稿证据行字面上写两次 `page dated`；决定 6 不改 prompt，模型分不出两者各指什么 | 10-22 审查复现：ask_02c360ec/web_20261021T233106Z b2 的 szhzxw.cn（page_date 2026-10-03，live_dates 2026-07-07 / 2026-10-03，page_published 重算 2026-07-07），裁判表行 `… \| not stated (page dated 2026-07-07) \|  \| www.szhzxw.cn \| live_dated 2026-10-03 \| …`，候选行 `period not stated (page dated 2026-07-07), source www.szhzxw.cn (live_dated page dated 2026-10-03)`；能兜底的 live 点里两个日期不同的：test2 13/101、token 题三次运行 73/246（`probes/out/v211d/review/date_mismatch.py`，不进 git，离线重算） | 没改（标记文字是计划定的；要不要换成不和 via 列撞词的写法，例如 `not stated (page published D)`，要用户定。只改 period_text 一处，prompt 模板不变，钉住的测试串跟着改） |
| S45 | 低 | htmldate 1.11 的 `load_html` 收到以 `http` 开头、不含空格的 str 会当成 URL，用它自己的 urllib3 pool 下载（`htmldate.utils.fetch_url`，timeout 30s）：不经 net.get、不查 robots、不限速、不用项目 UA，下载回来那页的日期还会被当成结果。fetch 把 `_decode(body)` 的 str 交给 `find_date`：live 页的 `page_dates`（fetch.py:129，以前就有）和 v2.11d 的 `page_published`（fetch.py:207）。v2.11d 在快照页也调 page_published（fetch.py:311），这个口子扩到了回测路径（回测规定一律不用 live 页）。触发条件：`_to_text` 收下的 text/plain、text/csv 页正文以 URL 开头且没有空格（换行不算空格） | 10-22 审查复现（`probes/out/v211d/review/htmldate_net.py`，不进 git：socket 层全拦、mock `fetch_url`）：正文 `https://example.com/moved-here` 和两行 URL 列表都让 fetch_url 被调一次，page_published 返回 mock 页的 meta 日期；已存 data/raw/agent 的 1539 个原件、快照缓存 538 个正文里以 http 开头的都是 0 个，已存运行没触发过 | 没改（版本测试没触发；最小修法二选一：只对 HTML 调 htmldate，或者先 `lxml.html.fromstring` 再把树传给 find_date；两种都只动 page_dates / page_published，可能让少数页的日期变，要用户定） |
| S46 | 低 | `parse_date` 把半年写法静默读成 1 月或 2 月：`2025-H1` -> 2025-01-01..2025-01-31，`2025-H2` -> 2025-02-01..2025-02-28，`2025 H1`、`1H 2025` 同样（走 dateparser，把 H 后面的数字当成月份）。抽取员写半年期间时，点会被标到 1 或 2 月，过 date_check，也过字面年份检查；`2025-Q3`、`FY2025`、`first half of 2025` 返回 None（照旧丢） | 10-22 审查复现（`ev.parse_date('2025-H2', end=True)` = 2025-02-28）；已存保留点里期间写成 H1 / H2 / 半年的 0 个。计划第 5 节要求记进 BUGS | 没改（计划第 5 节：要做另开一步） |
| S47 | 低 | 两位数的中日韩年份：页面写「24年全球收入超9000万美元」，抽取员把期间写成 2024 年（对的），字面年份检查（pipeline.py:434）在正文里找「2024」找不到，以 `period year 2024 does not appear in the page text or URL (likely mis-dated)` 丢掉；`era_years` 只认令和 / 平成 / 民國和 1NN年，不认两位年份 | 10-22 复现：ask_02c360ec/web_20261021T233106Z 的 finance.sina.com.cn（2025-07-28）3 个点（9000万美元、500家、1500项）；全部已存运行里年份检查丢的 748 个点中，页面正文含对应两位「YY年 / YY년」的 20 个（上限：没核对是不是同一处） | 没改（计划第 5 节：字面年份检查的变体不进默认设计，要做另开一步） |
| S48 | 中 | v2.11d 冒烟（`results/agent/ask_8db1fabf/v211d_smoke`，全球 2025 token 题，deepseek-flash）：v2.11a 和 v2.11d 放进来的点多了（保留 347 个，此前同题 185 / 227 个），第 2 轮裁判两次都在 max_tokens 12000 处截断（`finish_reason=length`），整轮作废，终稿只用第 1 轮的 2 条方法 | calls.jsonl 的 `judge:r2` 两行 `completion_tokens 12000`；已存 365 次裁判调用里另有 8 次 length | 已修 `v2.11d`：`config.MAX_TOKENS` 的 judge、repair 12000 -> 24000（只按实际用量计费）。网页 BYOK 的最坏预扣随之上升：$2 上限下 17 个模型 × 区域的可跑 / 拒跑状态和方向数都不变，已拒跑的最小上限 Opus 4.0 -> 4.5、Kimi K3 3.0 -> 3.5、Fable 9.5 -> 10.0、GPT-6 Astra 10.0 -> 10.5 |
| S49 | 低 | v2.11e 回裁判后方法仍失败、其余路线吻合时，`repair.errors_after` 是 `[]`（错误已发过，不再列），网页修正卡显示「修正后仍有的问题：无」，但该方法仍没出数（错误只在 compute 的方法记录里） | tests/test_resend_failed_methods.py `test_still_failing_is_sent_once_and_the_error_stays` | 记 |
| S50 | 低 | v2.11e 多出的 `judge:rN:repair` 预扣（repair 24000 tokens）放不下 usd 上限时置 `budget.aborted`：central 不变，但终稿不再调模型、退成代码模板（graph.py:911），网页标 done 带 stopped；HEAD 同上限能出模型终稿。任何修正轮撞上限本来如此 | 10-22 探针（假 json_call、真 `Budget.hold`、上限 $0.105）：HEAD 调用含 `final`；工作区无 `final`，aborted `usd cap 0.105 would be exceeded (spent 0.0840 + in flight 0.0000 + 0.0311)`；已存 128 个带 budget 的运行终了时离上限都 ≥ $0.1427 [网页行为只读码] | 没改（加预算判断是新守卫，决定 10） |
| S51 | 低 | v2.11e 的图测试没钉住「交回完整清单」和「对照本轮全部 repairs 去重」：把 graph.py 改成只发 resent 那几行、或只对照最后一次修正，5 个测试照样全过（代码本身对） | 10-22 变异复现两次 `OK`；探针：加一个被输入核对否掉的 m4，errors 带它、resent 不带；1.1 -> 1.2 -> 1.1 修 2 次（只对照最后一次的变异修 3 次） | 没改（测试覆盖缺口） |

## H. 我的做事方式（这些低级错误的来源）

1. 每条规则只对着引发它的那次失败验证，不量几条规则叠在一起的效果（A1–A6）。
2. 该让模型显式声明的类别，用关键词正则去猜（A3；D2 里的实体词也是同一类问题）。
3. 不逐字读最终输出（F1、F2），没检查对照臂的参数（G3），没检查基线是不是被自己的检查器误伤（G1）。

以后打 tag 前的门槛：全量「误差 / 区间 / 覆盖」回归表 + 逐字读终稿和网页（已写进长期记忆）。

# FIX_PLAN：第一轮修复计划（2026-10-16 定稿）

用户的要求（2026-10-16 晚，原话）：「控制bug之间的牵连，稳定每个模块的输入和输出……你已经不需要再升级功能了，就把目前的东西给修复完整即可」。
用户睡前把执行交给了我，下面的设计决定是我按推荐方案定的，每条都写了理由，用户可以推翻。

依据：`BUGS.md`（A1–G7）；只读分析的完整结果在 `probes/out/fixplan_analysis.json`（已被 gitignore；里面有 6 份模块结构图、
全仓参数清单、88 条 bug 和代码的对应关系、75 条牵连关系、两版方案、合并方案和挑错意见）。新编号 N1–N46 来自这次分析。

## 1. 原则（每个阶段都要遵守）

1. **只修不加功能。** 不新增能力、不加依赖、不接新的外部 API（PDF、Kalshi、Jev 真实调用都不做）。
2. **模块的输入输出约定不变**（见第 3 节）。公开函数的签名和返回结构不改；需要新信息时只**追加**可选字段，不改名、不删除。
   `state.json` 也只追加键。确实要改约定时，上下游在同一个阶段一起改、一起验证，并在阶段报告里写明改前 / 改后的输入输出示例。
3. **一个阶段只做一件事**，单独 commit + tag。代码和结果分开提交。不顺手重构。
4. **不碰预注册。** 已存的 `results/**`（尤其 showcase1）一个字节都不改；10-28 韩国题打分之前，冻结路径不动（第 4 节 G7）。
5. **不联网、不调模型**（本轮全部离线验证）；不读 `.env` 和 key 文件；`data/`、`results/` 只读。
6. **打 tag 前过门槛**（第 4 节），任何一项不过就不打 tag，停下来。

## 2. 我替用户定的设计决定（可推翻）

| # | 问题 | 定的做法 | 理由 |
|---|---|---|---|
| D1 | 裁判第 2 轮看不到第 1 轮的丢弃（N11：prompt 说「没列出 = 保留」，代码却沿用丢弃） | **折中**：第 2 轮（和修正轮）的完整表格只列仍保留的点和新点；之前丢掉的点另起一小段，每个一行（id / name / value / 第几轮丢弃，不带 quote），并写明「这些点保持丢弃，要恢复就在 decisions 里写 keep:true」。没有已丢弃的点时这一段不出现 | 挑错意见：恢复通道真用过（ask_fa4b4c74 恢复的点撑起了权重 0.5 的 m1），整段删掉违反原则 4；紧凑行能让表格大幅缩短，prompt 和代码也说同一件事 |
| D2 | max_tokens 统一与取值 | 先把所有上限收进 `config.MAX_TOKENS` 一张表，**值全部不变**；再把并发名额和预扣的顺序调对；最后只把 searcher 从 2048 调到 8192，judge 保持 12000 | 493 次搜索里 39 次截断、32 次因截断一个 URL 都没给；不先调预扣顺序，10 个方向同时预扣会贴着 $1.00 上限 |
| D3 | 回测泄漏：searcher 把真值写进搜索词（C2） | 回测时，查询词命中登记值的方向**整个作废**（不取页、不重搜），原因写进 state；k / M 缩写后面加字母边界（7.27 miles 不再误中） | 改审计为拦截，只加护栏不放松；重搜时 searcher 还会看到同样的结果 |
| D4 | 终稿数字出口（F1、F2） | 年份、Q1–Q4 / H1–H2、方法用到的点 id 不再被清洗；方法用到的观测点各给一个 `p{n}_value` 占位符；区间依据用一张 BASIS_TEXT 映射；区间标签写成「80% model-based」；state 另存模型原文 | 数字仍然只从代码出来（原则 2）；「[n]」出现在 27/50 个终稿里 |
| D5 | 结构化基线被量纲反馈误伤（G1） | **本轮不改**，等 10-28 打分提交之后：先处理「每千人」双重换算（N38），再改报错反馈；规则不放松；补充运行另存 | `showcase.py` 每次打分都用当前 engine 重算结构化臂，10-28 前改就是改预注册的对照臂；N38 不先处理，修好反馈反而会放进小 1000 倍的路线 |
| D6 | 区间规则（A1–A6） | **本轮只改标签**（D4），规则本身放到 v2.7：先定新的留出集和 interval score，再只用开发集调 | 现在成功的运行全是调参时看过的，现在调宽度等于对着答案调 |
| D7 | 修完要不要重跑 7 道开发 / 留出题（约 $3.45） | **不跑**，等用户批准 | 用户睡前说过先别重跑；离线检查只能证明「已存结果不变」，真实效果要等重跑 |
| D8 | Kalshi 补查（预注册要求，今天 UTC 截止） | **不补查**，记为与预注册不一致 | 新的外部 API，用户没批准 |
| D9 | key 跟着 HTTP 跳转带出去（N30、E4） | **修**：LLM 客户端和 jev 都不跟随跳转（遇到跳转直接报错） | 安全问题，改动小，可以离线测试 |

## 3. 模块的输入输出约定（本轮不改，除非阶段里写明）

完整结构见 `docs/structure.html` 和 `probes/out/fixplan_analysis.json` 的 `maps`。本轮会碰到的约定：

| 模块 / 函数 | 输入 | 输出 | 本轮谁会碰 |
|---|---|---|---|
| `search.Searcher.search` | 查询意图、as_of | `{queries, urls, usage…}` | S5：只修 n_search_errors 的计数，结构不变 |
| `pipeline.run_direction` | 方向、ctx | 方向结果（search、pages、points） | S4 只换锁的顺序；S7 追加 `search.voided` |
| `evidence.parse_value(value_as_written, scale_word)` | 原文数字、倍数词 | (数值, 是否有倍数) 或报错 | S9：多认中日韩倍数和复合写法，返回结构不变 |
| `evidence.text_dates / parse_date` | 文本 / 日期串 | 日期列表 / date | S9：多认中日韩和纪年写法 |
| `evidence.leak_forms / leak_patterns` | 登记值 | 写法列表 / 正则 | S7 加边界；S9 加中日韩写法 |
| `fetch._decode`、`net.decompress` | body、HTTP 头 | 文本，或 undecodable | S10：解码顺序和 zstd |
| `assumptions.validate / effective_range` | 裁判的假设列表、target | `{kept, rejected}`、(P10, P90, widened) | S3：只改百分数判断 |
| `compute.run` | methods、points、target、assumptions | `{methods, result, …}` | S6：只改量纲报错的文字 |
| `methods.combine` | 方法结果 | central / p10 / p90 / basis… | 本轮不碰 |
| `graph` 裁判表格 `_table` | points | 表格文字 | S6（D1） |
| `graph` 终稿（final 节点） | compute、points、模型文字 | `state.final{template, text, placeholders…}` | S8：追加 model_text、basis 文字 |
| `run.save_run` | 图的 state | state.json / ledger.md / graph.html | S1 追加 settings；S8 用 basis 文字 |
| `run.score_all` | 已存 state | summary_<tag>.json | S8：去掉「去年同月」臂（用户已决定去掉这个对照） |
| `web/results.py` | state.json、summary | 网页 JSON | S8：追加 basis_text |
| `llm.py`、`jev.py` 的 HTTP | 请求 | 回复 | S11：不跟随跳转 |

## 4. 门槛（每个 tag 前都要过；各阶段的检查以它为底）

- **G1** `./.venv/Scripts/python.exe -m unittest` 全过（S0 先跑一次记下基线；本来就失败的测试要列出来，不能变多）。
- **G2** `probes/compare_continuous_prompts.py`（假模型跑一遍连续题的全部 prompt）的 sha256：预期不变的阶段必须仍是 `4a56d586…`；
  会变的阶段（S6、S8）登记新值和原因。
- **G3** 全量回归表（S0 做的工具）：当前代码对上一个 tag 的导出（`git archive <上一个tag> triangulate` 解到 `probes/out/_old_<tag>/`）逐行相同，
  或者逐行解释差异。
- **G4** `probes/compare_continuous_paths.py` 两份代码逐 key 相同，或列出差异并解释。
- **G5** 在内存里跑 `showcase.build()`（不调 write），和已提交的 `results/showcase/summary.json` 逐字节相同。
- **G6** 输出有变化时（终稿、ledger、网页），逐字读，阶段报告里贴改前 / 改后原文。
- **G7** 冻结路径（到 10-28 打分提交为止）：`triangulate/engine.py`、`expr.py`、`units.py`、`mc.py`、`triangulate/graph.py`、`report.py`、
  `showcase.py` 的 `git diff` 为空；`arms.check_naive` 的源码（`inspect.getsource`）不变；`config` 里 MC 常数的值不变；`forecast.py` 不改。
- **G8** `git status`：除了这次阶段的文件和已知的 4 个未跟踪路径（`results/agent/fc_yell_2026_08/post_review/`、
  `results/agent/post_review_08.log`、`results/agent/summary_post_review.json`、`docs/verrier.html`）以外没有别的变化；`results/`、`data/` 没有新文件。
- 每个阶段写一份报告 `probes/out/stages/<阶段>.md`：改了什么、改前 / 改后的输入输出示例、各门槛的命令和关键输出、和计划的出入。

## 5. 阶段（按依赖排好；前一个 tag 打好才开始下一个）

| 阶段 | tag | 修什么 | 文件 | 依赖 | 对已存结果 |
|---|---|---|---|---|---|
| S0 | `tools-regress-v1` | 门槛工具：`probes/recheck_continuous.py` 加 `--code` 参数和全量回归表（每个连续值运行：中心、P10、P90、P90/P10、basis、误差、覆盖）+ 终稿 lint（`[n]`、`[unknown placeholder]`、`no basis` 的终稿数和出现次数）；原有 7/7 统计保留；`tests/test_agent.py` 的 `__main__` 守卫挪到文件末尾（N45） | probes/recheck_continuous.py、tests/test_agent.py | — | 无 |
| S1 | `v2.5.3` | 基础设置单一来源（N1、N6）：`config.MAX_TOKENS` 表（plan 6000、extract 4000、judge 12000、repair 同 judge、audit 4000、published 3000、early 同、final 4000、search 2048、naive 500、structured 6000、search_direct 4096），所有调用处和预扣都查表，final 显式传参；Z90 / MC_N / MC_SEED 的重复定义改为引用（值不变）；`save_run` 在 state.json 追加 `settings`（这张表 + Budget 默认参数 + 区间常数）；测试：假模型跑一遍记录每个角色实际传的 max_tokens，和表逐项比对 | config.py、agent/pipeline.py、agent/graph.py、agent/published.py、agent/search.py、arms.py（只改两个实参，check_naive 不动）、search_direct.py、agent/methods.py、web/results.py、agent/run.py、tests | S0 | 无（以后的 state 多一个 settings 键） |
| S2 | `v2.5.4` | 假设单位里带 % 的按百分数换算（N17，潜在 100 倍错）：收成一个 `is_pct(unit)`；只决定是否除以 100，原始 unit 文字保留用于显示；`restated_point` 用同一个函数；percentage points / pp / bp 不换算 | agent/assumptions.py、agent/compute.py、tests | S1 | 无（只有韩国 showcase1 的 a2 的校验输出会变，列出来；a2 被 m2 引用过，只是 m2 因为 p56 失败才没出数） |
| S3 | `v2.5.5` | 先拿并发名额再预扣（N2）：`pipeline.py` 两处 `with hold(...), sem` 改成 `with sem, hold(...)`；粘滞中止不变；测试：10 个方向并发时任何时刻在途预扣 ≤ 8 份 | agent/pipeline.py、tests | S1 | 无 |
| S4 | `v2.6a` | searcher 上限 2048 → 8192（N24，只改表里这一项）；n_search_errors 认 list 里的 `web_search_tool_result_error`（N25）；不往 state 加新字段；离线检查：用已存 calls.jsonl 的时间线重放预算，在新预扣值下没有任何一次会超限 | config.py、agent/search.py、tests | S3 | 无（以后的运行取到的 URL 会变） |
| S5 | `v2.6b` | 裁判轮次协议：D1 的折中表格（N11）；量纲规则报错点名每个输入的 id / unit / name（B5 的一部分）；JUDGE_USER 回复示例里 formula_mc 的 inputs 补上 role（N15，示例和规则矛盾）。检查加 `probes/replay_discrete_rules.py` 改前改后对比（离散共用表格） | agent/graph.py、agent/prompts.py、agent/compute.py、tests | S0 | G2 的 sha256 预期会变（示例改了），登记新值 |
| S6 | `v2.6c` | 回测泄漏护栏（C2、N31）：D3；扫已存查询词，47 个有审计的运行里应正好 5 个各作废 1 个方向，列出来；缓存页重扫哨兵，列出因字母边界不再命中的页并逐页确认是误报 | agent/pipeline.py、agent/evidence.py、agent/outputs.py、agent/run.py、tests | S5 | 无（只影响以后的回测） |
| S7 | `v2.6d` | 终稿数字出口（F1、F2、N32、N33、N34）：D4；`run.score_all` 去掉「去年同月」臂（N44）；网页结果页显示 basis 文字；在内存里用保存的 template 重渲染全部终稿，逐条读 `basis == no_basis` 的那句并贴改前改后 | agent/graph.py、agent/prompts.py、agent/outputs.py、agent/run.py、web/results.py、web/static/app.js、tests | S5 | 显示层立刻变（只是显示，不改已存文件）；G2 sha256 会变，登记 |
| S8 | `v2.6e` | 中日韩数字和日期（N26、N27、C1 的解析部分，也是 B1 日本迁移题没出数的主因：「519万548」被丢）：倍数字 万/萬/億/亿/兆/만/억/조；复合写法（519万548、2만4,275、1億2345万）；倍数字后接单位（万人、万人泊、兆円）和复合倍数（万亿）；英文 `'000s`；日期 YYYY年M月D日、YYYY년 M월 D일、令和/平成 N年、民国/民國 N年（1911+N）；期间年份检查认这些纪年；哨兵登记中日韩的精确写法（a万b）。离线检查：用已存的 value_as_written + scale_word 重放 parse_value（464 个复合写法点 + 189 个 unknown scale word 点 + 14 个丢了倍数字的点），列出新值并对照缓存原文抽查；verify_point 的完整重放做不到（丢弃点没存 quote），写明。不做汉字数词（三百）和 PDF | agent/evidence.py、agent/pipeline.py（期间年份检查）、tests | S6（和 S6 改同一个 leak_forms） | 无（已存的点不重新核对） |
| S9 | `v2.6f` | 页面解码（C1 解码部分、N28）：顺序改成 HTTP 头 charset（允许引号）→ BOM → meta → utf-8（U+FFFD 低于阈值就用）→ 自动探测（`trafilatura.utils.detect_encoding` 或 charset-normalizer，都已在 requirements.txt）；net.decompress 认 zstd 魔数并用标准库 `compression.zstd` 解压（LHR 留出题有 3 页因此被丢）。检查：全部缓存快照新旧解码对比，旧解码正常的页逐字节相同，只有原来 undecodable 的页变，逐页列出 | agent/fetch.py、agent/net.py、tests | S8（先能解析再能解码，否则数字会悄悄小 10^4 倍） | 无 |
| S10 | 记 | 一道网页实跑题没出数（冻结版 v2.8e，10-18 用户实跑）。三处流程问题叠在一起：(1) 裁判第 2 轮丢掉第 1 轮已经用上的总数点，把这个总数写成假设，公式全是假设；(2) `assumptions.target_reason` 按单位词干判「目标的水平值」，目标单位和假设单位都是 person、名字没有比率词，这个总数被当成目标本身拒掉（误伤：目标只是其中一部分）；(3) 修正轮只有一次，compute 只报第一个输入错误，修正轮没看到「公式至少要一个观测点」这条，裁判把假设改个编号原样交回，再被拒。证据本身够做带数据的估计：总数点 × 观测到的比例，再借同类对象的比例 | 该运行的 state.json（judge_rounds[1].repair） | 冻结版不修（用户 10-18 同意记为已知局限），预注册和留出测试之后再看 |
| 收尾 | `fixround1-docs` | 更新 BUGS.md（每条的状态：已修 / 本轮不修 + 原因；订正挑错意见指出的不准描述；补 N 编号）、NEXT.md 断点、`docs/structure.html` 的完成状态 | 文档 | 全部 | 无 |

## 6. 本轮不做（和原因）

- **S11 重跑 7 道开发 / 留出题**（约 $3.45）：要联网花钱，等用户批准。另外 tw、lhr、jp_births 三道留出题的部分修复依据来自它们自己，重跑后只能算开发数据。
- **B0 展示集最终打分**：10-21（JNTO）、10-28（韩国）公布后各提交一次。登记 JNTO 真值时 `tests/test_showcase.py:58-59` 会失败，要同时改测试。
- **结构化基线修复（G1、G2、N38、N39、N40、N41）**：等 B0 之后，见 D5。之后 G5 的口径要改成只比较数值字段。
- **区间规则 v3、假设 kind 字段、series_naive 的地位（A1–A7、B2、B3、N18–N23）**：见 D6，要先定新的预注册（Winkler interval score、≥10 道新留出题、其中 ≥3 道非英文）。
- 运行骨架的机械问题（N10、F4、N14、N16、N8、E1）、HTTP 客户端统一（N3、N29、C6、C8）、compute 回退到第一轮方法和编号（N12、N13）、
  修正次数和 rationale 一致性检查（B4）、公式常数的 prompt 说明（B6）、B7、离散规则（E2、E3、E5）、数字格式化统一（N35）、
  live 取页收尾和已公布检测（C4、C5、C7、D1–D3）、网页和文档展示（F3、N36、N37）、PRICES 回退（N9）、prompt 里写死的数字（N5）、
  并发上限（N7）：都没有观察到影响结果的失败，或者要先定设计，或者改了会动 prompt / 回放基准而收益很小。
- 需要联网核实的：searcher 的 thinking / temperature（N4）、搜索单价（G7）、deepseek-flash 的输出上限。
- 不放松 RATIO_UNIT、不全局放开公式常数、不统一 MC 种子格式（会改变所有 MC 数字，包括展示集重算）。

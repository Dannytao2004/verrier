# 断点（2026-10-15）

当前代码：tag `v2.3`（agent，f173c84：离散结果列表改由裁判在证据之后定义）+ `web-v0.2`（前端，75521a8，没改）。测试 185 个全过。

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
| discrete6 | f173c84（v2.3） | 无 | 两轮的第一次回复都没给 outcomes；修正回复给的列表本身合格，但依据里引用了同一回复里自己丢掉的点，整个列表被拒（见下） |

（discrete3 中断，没有 state.json，已删。）离线重放 discrete4 第 2 轮裁判原始回复（v2.2.1 规则）：4.00% or lower 53.1%、4.25% 46.9%；
其中 m2 用同一个假设 a2（50%）同时给两个结果，质量可疑。

discrete6（$0.4716，其中 token $0.1316、按假设单价记的搜索费 $0.34；556.7 s；39 次调用；6 个方向 + 3 个补充方向；106 个点，最后保留 9 个）：
- 第 1 轮：第一次回复没有 outcomes → 修正轮。修正回复的列表 = 3.75% or lower / 4.00% / 4.25% / 4.50% or higher（le / ge 都对），
  依据 p1、p4（9 月 16 日决议后上限 4.0%）、p16–p19、p27、p28；p27 / p28（9 月、7 月会议日期）是它在同一回复里丢掉的点 → 拒。
- 第 2 轮：没有列表，所以再次要求定义；第一次回复又没给 → 修正回复的列表 = 4.00（le）/ 4.25 / 4.50 or higher（ge），
  依据里的 p18、p96（当前上限 4.0%）是它在这一轮作为「重复」丢掉的点 → 拒。没有列表，方法全部 `no outcome list`。
- 证据本身是对的：p1 / p4 当前上限 4.00%；p19 CME FedWatch 10 月 28 日会议加息 25bp 53.7%（2026-10-15）；p86 维持 56.3%（2026-10-14）。
- 离线反事实（不进结果）：只看列表、不查依据是否保留，两个列表都合格。第 1 轮修正后的 m1（4.25% ← p19，余下给 4.00%）=
  4.00% 46.3%、4.25% 53.7%；但 compute 用的是第 2 轮的方法：m1 把 p19（10-15）和 p86（10-14）两个不同日期的概率相加 = 1.10，
  又指定了余下结果，即使列表通过也会因「其余之和 > 1.02」被拒，而那一轮已经用掉了修正机会。

## 离散模式的未解决问题

1. （discrete6）裁判两轮的第一次回复都没给 outcomes。定义要求写在方法说明里，JUDGE_USER 的回复 JSON 模板里没有 outcomes /
   outcomes_basis。可能的做法：离散题的回复模板加这两个字段。是 prompt 改动，要先定。
2. （discrete6）依据 id 必须全部是保留的点：裁判会引用自己在同一回复里当「重复」丢掉的点（p18 / p96 是 p1 / p4 的副本，
   p27 / p28 是会议日历），整个列表因此被拒，修正机会也用掉了。可能的做法：至少一个保留的 id 时只去掉丢掉的 id 并记 note；
   或修正轮也采用修正回复里的 decisions。这会放宽批准的规则，要先定。
3. （重放）代码查不出列表有没有「按证据」：discrete5 的错列表补上尾部和依据后通过校验（现实的 4.00% / 4.25% 被并进
   「4.50% or lower」）。可能的代码规则：依据里不是概率、单位和目标一致的「水平」点，其数值必须是一个单独（非尾部）的结果；
   风险是误伤（例如依据里引用下限 3.75%）。要先定。
4. （重放）沿用第一轮列表时不复查依据：discrete4 第一轮的依据点 p3 在第二轮被丢掉。是否复查、复查不过怎么办，要先定。
5. 数值结果中间不查步长：「4.00% or lower / 4.50% / 4.75% or higher」漏了 4.25% 也能通过。代码不知道步长（只有 outcome_kind 提示）。
6. （discrete6）不同日期的概率混在一个方法里（p19 10-15 加息 53.7% + p86 10-14 维持 56.3%，和 1.10）。现在只有和的检查兜底。
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

已解决：v2.2 的「结果列表在规划时定死」（v2.3 改由裁判定义，但见上面 1–4）；「同一个 id 给两个结果」（v2.2.1）；
「留出测试前先只跑 plan 看 outcome_type」（v2.3：7/7 continuous）。

## 之后的清单（demo 收尾）

1. 修「答案已公布」：真实使用时，如果搜到的数据点就是目标本身（同一对象、同一期间、发布日期已过），直接报出来，不再拿去平均。
2. 把留出测试扩到 10 题左右（先预注册，含 1–2 道非英语题）。
3. 挑 3–5 个展示用的运行，首页放入口；README 首屏放回测表、架构图、截图和局限说明。
4. 「假设占比」计入公式弹性（审查意见）；识别「样本 × 放大系数」这种伪装假设（日本题）。
5. 「梯度下降」调研：4 份领域报告已完成，汇总和核查被额度闸门挡住；续跑时要改动汇总和核查的 prompt，避免回放缓存里的 stopped 结果；先删掉停止标记文件。

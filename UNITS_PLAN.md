# UNITS_PLAN：单位、量纲和覆盖范围（v2.7，2026-10-17 用户批准）

起因：2026-10-17 用户的真实运行「芝加哥人每天吃多少披萨」（`results/agent/ask_3e7f14f7/web_20261017T072118Z`）只报了一个数
104,880,723，没有单位，而且数本身是错的：
- 目标单位写成「pizza mass per day (kg or lbs)」，不唯一；
- m1 的结果是 克/天，并且观测点「11 % of population」没有除以 100；
- m2、m3 用的是全年营收，得到的是 公斤/年；
- m3 只覆盖冷冻披萨这一个渠道，却和全量路线等权平均。

按同一个单位离线重算（`probes/out/_pizza_tonnes.py`）：m1 64.8 吨/天，m2 59.9，m3 22.3。按用户的口径把餐馆和冷冻加起来作为供给侧，
得到 86.2 吨/天，和消费侧（m1）的 64.8 只差 1.33 倍。

用户批准的范围（原话：「我觉得还行，起码比把应该搭配使用的channel分开来用要好很多。改吧」）：
钉死单位（2）、量纲检查（3，用 pint）、百分数 bug（4）、方法层的覆盖声明（6 的第一步）、显示单位（1）。
数据点层的完整集合坐标（6 的第二步）这轮不做。

## 2026-10-17 修订：改成简单版（用户：「我意思已经给你了，自己改」），以本节为准

U0、U1 之后，逐项量纲推导（下面「量纲检查」一节）被放弃：它让日历常数 k_months_per_year 换算后等于 1，「年总量 / 12」会悄悄大 12 倍；
qty 的自然语言解析（约 500 行）不断冒出边角问题。现在的做法：

- **qty.py 是 pint 的薄封装**（约 100 行）：只认 pint 写法（`kg/day`、`USD/year`、`birth/(1000 person)`、`percent`），补货币（各自独立、不换算）、
  计数名词（自动定义，复数归单数）、「给了几个候选」报错。没有指数、长度这类保护。
- **U1（`v2.7b`）**：规划钉死 `target.unit_canonical`，解析不了重问一次，仍不行就记 plan note、这次不做单位换算。
- **U2（`v2.7c`）**：钉了单位时，每个 formula_mc 方法声明一个 `"unit"`（公式结果的单位，例如 `kg/year`），代码用 pint 把结果换到
  `unit_canonical`（g→t、year→day）；缺 unit 或换不了就是方法错误，交修正轮。**不推导每个输入的单位**，日历常数照旧是普通数字。
  观测点单位里带 %（`% of population`）就除以 100，目标本身是百分数时除外。没钉单位的运行（已存的都是）完全不变。
  已知局限：裁判把公式结果的单位写错（公式其实是每年、写成每天），代码查不出，靠输入核对。
- **U3、U4 照原计划**，同样从简：只做方法层的 coverage 声明和合并排除、显示单位，不加别的机制。

## 原则（沿用 FIX_PLAN.md 第 1、3、4 节）

- **模型提议，代码判定。** 模型负责写单位、声明覆盖范围；代码负责解析单位、推导公式的量纲、做单位换算、检查覆盖范围。
- **只追加，不改约定。** target 加 `unit_canonical`，方法的 input 加 `unit`，方法加 `coverage`，`compute.run` 加可选参数 `require_units`，
  state.json 只加键。原有字段的含义不变（target.unit 仍是给人看的描述，已公布检测仍用它）。
- **旧运行不受影响。** 已存的运行没有这些字段：重算时 `require_units=False`，结果必须和现在逐字节相同（G3 回归表 40/40）。
  新运行由 graph 传 `require_units=True`。
- **冻结路径不碰**（到 10-28 展示集打分为止）：`triangulate/engine.py`、`expr.py`、`units.py`、`mc.py`、`triangulate/graph.py`、`report.py`、
  `showcase.py`、`forecast.py`。agent 的单位功能放在新模块 `triangulate/agent/qty.py`，用 pint，不用也不改基线的 `units.py`。
- 依赖：`pint==0.26.1`（已装进 .venv，写进 requirements.txt）。按用户的要求，通用的单位换算交给库，不手写。

## 设计

### 单位注册表（`agent/qty.py`）

- 一个模块级的 pint `UnitRegistry`。
- 货币：USD、EUR、GBP、JPY、CNY、KRW、TWD、CAD、AUD、CHF、HKD、INR 各定义成独立的基本维度，互相之间**不换算**（汇率是证据，不是常数）。
  混用不同货币报量纲错误。
- 计数名词：pint 不认识的单个英文单词（person、slice、pizza、visit、birth、passenger、vehicle……）在第一次出现时自动定义成各自的
  基本维度。复数和常见不规则形式（people→person、persons→person、children→child）归一。这样「克/片 × 片/人/天 × 人 = 克/天」能消掉，
  名词写得前后不一致（eater 对 person）会报错，交回裁判修正。
- 百分数：`percent`、`%`、`pct` → 0.01（pint 内置）；percentage point / pp、bp（basis point）按需定义。
- 解析失败返回清楚的错误文字（给修正轮看），不抛异常到图里。
- 公开函数（实现时定名字，写在模块 docstring）：解析单位字符串；推导公式的单位；把样本从输入单位换到基本单位、把结果换到目标单位。

### 钉死单位（规划节点）

- PLAN prompt：target 加 `unit_canonical`，只能写一个单位，必须能被注册表解析，带时间口径（例如 `t/day`、`visitor`、`USD/year`、`percent`）。
  一段期间的总量写计数或总量单位（例如 9 月的访客总数写 `visitor`，不写 `visitor/month`）。
- 代码检查：解析不了、含 or 或多个候选 → 带着错误重问一次规划（复用现有的输出无效重试）；仍然不行 → 运行继续，
  记 plan note「unit not pinned; unit checks off」，这次运行不做量纲检查，终稿写明没有钉死单位。
- 离散题（outcome_type discrete）不需要 `unit_canonical`。

### 量纲检查（已作废，见文首「2026-10-17 修订」）

- 方法的每个 input 必须带 `unit`（规范写法，同上）。常数由代码给单位：k_days_target 是 `day`，k_days_per_week 是 `day/week`，
  k_days_per_year 是 `day/year`，k_weeks_per_year 是 `week/year`，k_months_per_year 是 `month/year`，k_bp_per_pct_point、k_percent_per_unit 按定义。
- 代码先用单位推导公式结果的单位：加减、min / max / mean 的各项单位必须相容；sqrt 和整数次幂按 pint 的规则。
- 结果单位必须和 `unit_canonical` 相容，换算系数由代码算出并乘到样本上：克/天 → 吨/天、公斤/年 → 吨/天都由代码完成。
  不相容就记方法错误，例如 `formula gives kilogram * pizza / year; target is metric_ton / day`，交给现有的修正轮。
- 百分数守卫（第 4 条）：数据点的原文单位含 %（同 S2 的 `is_pct`），而方法里给它写的单位是无量纲的 1、而不是 percent，就报错，
  让裁判改成 percent。这是确定性的检查；不靠模型自觉。
- 输入核对（AUDIT）多看一项：方法里给每个输入写的单位，是否和证据（数值、单位原文、期间）一致。例如全年营收必须写成 `USD/year`。
- 系列方法（series_naive、yoy_scaling 等）用的是目标自己的历史，单位就是目标单位，本轮不加检查（在报告里写明）。
- 离散题的 outcome_probs 不做单位检查。

### 覆盖范围（方法层，6 的第一步）

- 每个方法可以带 `coverage`：
  - 省略或 `{"kind": "full"}`：产出就是完整的目标（旧运行都按这个处理）。
  - `{"kind": "part", "dimension": "channel", "part": "frozen_retail", "siblings": ["restaurant", "other"]}`：只覆盖目标的一部分。
  - `{"kind": "sum", "dimension": "channel", "parts": ["restaurant", "frozen_retail", "other"], "missing": []}`：把各部分加起来覆盖整个目标。
- 代码规则：
  - part 方法**不进合并**（权重 0），记错误「covers only frozen_retail of channel; sum it with its siblings (restaurant, other) in one method,
    with an allowance assumption for parts without evidence」，交给现有的修正轮。
  - sum 方法的 missing 不为空：同样不进合并，提示补齐（给缺的部分一个假设）或删掉。
  - sum 方法每个部分最多 3 个假设，整个方法最多 8 个（每次运行最多 8 个的规则不变）；其他方法仍是每个最多 3 个。
- 合并时只用 full 和完整的 sum 方法；方法之间分歧太大的规则不变。
- 输入核对多看一项：方法声明的覆盖范围是否和输入的证据一致（例如全美餐馆营收不能声明成覆盖所有渠道）。

### 显示单位（第 1 条）

- 终稿加占位符 `[[unit]]`（值来自 `unit_canonical`，没有就用 target.unit），FINAL prompt 要求估计值和区间后面跟单位。
- 控制台（`verrier_console.js`）、经典界面结果页、ledger、graph.html 页头在估计值和区间旁边显示单位。
- 结果的 JSON（`web/results.py`）追加 `estimate.unit`。

## 阶段（每个阶段一个 tag；门槛同 FIX_PLAN.md 第 4 节 G1–G8）

| 阶段 | tag | 内容 | G2（prompt sha256） | 状态（2026-10-17 下午） |
|---|---|---|---|---|
| U0 | `v2.7a` | `agent/qty.py` 和单元测试；requirements.txt 加 pint。不接入任何流程 | 不变 | 完成 `v2.7a`（`bfa8825`）；G2 仍是 `bbcfa3b1…` |
| U1 | `v2.7b` | 规划钉死单位（prompt、代码检查、重问一次、plan note） | 变，登记 | 完成 `v2.7b`（`e60e921`） |
| U2 | `v2.7c` | formula_mc 量纲检查和单位换算、百分数守卫、常数单位、AUDIT 加单位一项、JUDGE / METHODS_SPEC 的说明和回复示例 | 变 | 完成 `v2.7c`（`5df9238`），按文首「2026-10-17 修订」的简单版：方法声明结果单位，代码换算 |
| U3 | `v2.7d` | 方法层覆盖范围（coverage、合并排除、修正提示、sum 的假设上限、AUDIT 加覆盖一项） | 变 | 完成 `v2.7d`（`5fad7fb`）；sum 的假设上限 8 不变，每次运行的假设 id 在 `v2.8d` 放到 a1..a12（BUGS.md S1） |
| U4 | `v2.7e` | 显示单位（终稿 `[[unit]]`、控制台、经典界面、ledger、graph.html、results JSON） | 变 | 完成 `v2.7e`（`b81384f`）；终稿重复单位在 `v2.8d` 改了 prompt（BUGS.md S4） |

状态的写法：「完成 `tag`」= 过了 G1–G8 并打了 tag；「受阻」= 停在审查，没提交；「未开始」。

每个阶段除了 G1–G8，还要：
- 用假模型跑一遍完整的图（同 `tests/test_web.py` 的 FakeLLM），新字段齐全时能出数；
- 把披萨这次的三条路线，按新规则补上单位和覆盖范围，写成单元测试：
  - U2 之后 m1 得到约 64.8 吨/天、m2 约 59.9 吨/天；
  - U3 之后 m3 被排除在合并之外；把 m2、m3 合成一个 sum 方法（按本文件的规则补上 other 的假设）可以出数。
- 回归表（G3）：已存运行重算的结果和上一个 tag 逐行相同（旧运行走 `require_units=False`）。

## 结果（2026-10-17 晚）

U0–U4 都已提交（见上表）。第一次真实运行是冻结前的冒烟测试（tag `smoke1`，代码 `v2.8c`）：4 道题的单位都钉住了（t/day、visitor/day、trip/day、cup/day），出数的方法都带 unit_check；纽约题模型写出了 coverage sum（黄出租 + 绿出租 + 网约车）；披萨题模型写出了「餐馆 + 在家」的 sum，但因为假设 id 上限和一条误导的报错没出数，`v2.8d` 修了（BUGS.md S 节）。

## 旧的结果（2026-10-17 下午，停在 U1）

**完成 1 个阶段（U0 = `v2.7a`），U1 受阻，U2–U4 未开始。** `v2.7b`–`v2.7e` 都不存在。

**U0 / `v2.7a`（`bfa8825`，完成）**：新模块 `triangulate/agent/qty.py`、`tests/test_qty.py`（28 条），requirements.txt 加 `pint==0.26.1` 和它的依赖
`flexcache==0.3`、`flexparser==0.4`、`platformdirs==4.13.3`。没有接入任何流程：在 `v2.7a` 上没有一处 import `qty`，**agent 的行为和 web-v0.5 相同**
（披萨题现在重跑，终稿仍然没有单位、m1 的 11 % 仍然不除以 100、m3 仍然和全量路线等权平均）。
第三轮审查退回的第 1、3 条在提交前改了（第 2 条是 U0.md 的措辞，只在 BUGS.md Q2 写全）：`/` 后面的连字符基数（`USD/1000-person`、`USD/1-person`、`birth/1000-person`）现在报
`number … right after '/' divides only itself …`，不再悄悄读成乘法（测试 `test_numbers_only_as_rate_base`，10-17 下午在 HEAD 上另跑探针复查）；依赖补进了 requirements.txt。
门槛：提交说明记 374 个测试 OK、G2 `bbcfa3b1…` 不变、回归 41/41 相同、showcase 相同、冻结路径没动；U1 的「改前」在 `v2.7a` 导出上量到同样的 374 OK 和 `bbcfa3b1…`。
U0.md 停在第三轮（没写提交前这两处改动）。

**U1 / 计划 `v2.7b`（受阻）**：plan 节点钉死 `target.unit_canonical`。PLAN_USER 要求一个 qty 能解析、带时间口径的单位；连续题解析不了就带着错误重问一次
（`PLAN_UNIT_RETRY`，`tries=1`）；重问的回复钉住了单位**并且**有至少一个 dict 方向才替换第一份规划，否则沿用第一份、记 plan note
`unit not pinned: <错误>; unit checks off`，运行不中止；离散题不检查、不存。只追加：target 多 `unit_canonical`（钉住时），plan_notes 可能多一条。
工作区文件：`triangulate/agent/graph.py`（`c549585e35e0…`）、`triangulate/agent/prompts.py`（`72327db97002…`）、`tests/test_plan_unit.py`（新，10 条，`c344d988abf1…`）。
第三轮门槛（U1.md 第 5 节）：G1 384 个测试 OK（`v2.7a` 374）；G2 `826f8362…`（PLAN_USER 改了；探针的假规划没有 unit_canonical，多一条重问的 plan prompt）；
G3 41 行 0 差异；G4、G5、G7、G8 过；假模型全图 20 条 OK；变异 19 个全部被抓到。第三轮审查停在 verify：
1. （低，退回的原因）`tests/test_plan_unit.py` 第 98、99 行（`test_valid_unit_kept`）的两个换算断言没有检验力：`assertAlmostEqual` 默认 `places=7`（绝对差小于 5e-8），
   期望值本身只有 2.7e-6 和 1e-8，percent 多乘一次 0.01、或一年按 365 天算，照样通过。U1.md 第 3、4 节说它「验证了」换算，说重了。
   这两个系数 `tests/test_qty.py:283` 已经精确检查过。改法：改成相对比较（`f * 365250`、`f * 1e8` 对 1.0，`places=12`），或删掉、注释指向 test_qty；U1.md 措辞跟着改；
   重跑 G1、变异检查和 G8。只改测试，G2 应保持 `826f8362…`。
2. （信息）qty 遇到幂塔写法（`kg**2**3**4**5`）会挂死，挂死时一直持有模块锁；`kg**999999999`、`kg**inf`、`kg**nan` 会被钉住。按 QTY SCOPE 只记为已知限制（BUGS.md Q12）。
3. （信息）钉住的 `unit_canonical` 不截断、内部换行保留（target 其他字段截到 300 字符）（BUGS.md Q13）。

**披萨题的数字**（`tests/test_qty.py` 的 `TestPizzaFixtures`，用字面值重建，不读 results/；测试断言 64.8 / 59.9 / 22.3 / 86.2 / 74.7，容差 0.05。
10-17 下午在工作区重跑 `tests.test_qty tests.test_plan_unit` 38 条 OK、全部 384 条 OK；qty.py 和 `v2.7a` 相同；数字用 `probes/out/docs_v27/_pizza_numbers.py` 按同样的夹具打印）：

| 路线 | qty 推导的公式单位 | 吨/天（P10..P90） | `_pizza_tonnes.py` |
|---|---|---|---|
| m1 消费侧 `a*b*c*d*e` | gram * percent / day | 64.79（30.9..135.5） | 64.8 |
| m2 餐馆 `a*b/c*d` | kilogram / year | 59.89（29.5..120.8） | 59.9 |
| m3 冷冻 `a*b/c*d` | kilogram / year | 22.29（10.2..48.6） | 22.3 |
| 餐馆 + 冷冻，一个公式 | kilogram / year | 86.18（47.1..156.1） | 86.2 |
| `methods.combine(m1, 餐馆 + 冷冻)` | | 74.72，80% [35.67, 156.53]，monte_carlo | 74.7 |

这些数是**测试自己**做了 U2、U3 该做的事得到的：输入先按 `PIZZA_UNITS` 乘 `base_factor` 换到基本单位，再交给现有的 `compute.run`（不认单位），
结果除以 `base_factor('t/day')`；「餐馆 + 冷冻」用了 5 个假设，测试里临时把 `MAX_PER_METHOD` 放宽到 5（U3 的 sum 方法才会放宽）。
所以它证明的是 qty 的单位推导和换算对，不证明流程里会这样算。U1 不碰计算，流程里的数和 `v2.7a` 相同（G3 0 差异）。
「阶段」一节「每个阶段除了 G1–G8，还要」里的两条（U2 之后 m1、m2 出数；U3 之后 m3 被排除、sum 方法出数）要等 U2、U3 做完才能写成流程上的测试。

**和计划的出入**：
- U0（U0.md 第 8 节）：按字面值直接相乘，m1 是 65.748375 吨/天；64.8 是 MC 中位数（假设按 low / high 的 lognormal 采样，中位数是 sqrt(low × high)；
  a1、a2 的区间被代码放宽），两种都写成了测试。`convert_factor` 的报错是 `X cannot be converted to Y`，计划举的「formula gives …; target is …」由 U2 在 compute 里拼。
  qty 的规则比「设计」一节多：拦住 pint 和常见用法不一致的读法（ton、mt、calorie、barrel、point、全大写缩写、无量纲但系数不是 1 的 degree / grade / turn 等、
  非乘性单位）、单位前面的数字报错、`1.000` 报错、虚词和两个单词并排报错、quarter / decade 映射到 3 个月 / 10 年。
- U1（U1.md 第 8 节）：没有复用 `AgentLLM.ask` 自带的「输出无效重试」（要给 `ask` 加参数，`tests/` 里 12 个假模型的 `ask` 会 TypeError；重试用完还会丢掉第一份合法的规划），
  改成在 plan 节点里再调一次 `ask`，一次运行规划最多调用 3 次（改前 2 次）。重问的回复要同时「钉住单位」和「有方向」才替换，所以重问也不能把连续题换成离散题。
  `allow_discrete=False` 而规划选了离散时也重问，错误后面加一句 `this question needs a continuous number …`。`unit_canonical` 加在 target 末尾。
  「终稿写明没有钉死单位」留给 U4。
- 等用户定（U1.md 第 8 节第 9 条）：要不要把重问的结果写进 plan note。现在重问的回复和它被拒的原因都没有保存，真实运行之后能看出重问有没有改对，
  看不出改对时第一次错在哪、没改对时为什么被拒。阶段报告推荐改；这会改 U1 规定的 note 格式。

**U2 开工前要定**：
1. 百分数的口径（U0.md 第 9 节第 4 条，BUGS.md Q5、R1）：`compute.run` 已经对 unit **正好是** `"%"` 的观测点除以 100，`assumptions.effective_range` 也已经对 `is_pct`
   的假设除以 100。U2 如果再按方法里写的 `percent` 乘 `base_factor = 0.01`，这两类输入会差 100 倍（披萨的 p84 原文是 `% of population`，compute 没除，乘 0.01 正好对）。
   要先定：代码已经换算过的输入按什么单位算。
2. 目标单位自带的倍数（U1.md 第 9 节第 8 条，BUGS.md Q15）：`birth/1000` 会被钉住（`0.001 birth`），公式给 `birth` 时换算不报错，结果按「千分之一个出生」表示。
   要不要在钉单位时拒收「纯计数、倍数不是 1」的写法，由 U2 定。
3. 过渡期（U1.md 第 10 节）：U1 提交之后、U2 之前，裁判、输入核对、终稿、已公布检查的 prompt 都能看到钉住的单位，但 compute 不换算，终稿可能把别的单位算出的数标成钉住的单位。
   这期间不做真实运行。

**还要真实运行才能知道的**：模型会不会写出能解析的 `unit_canonical`（U1）、input 的 `unit` 和 `coverage`（U2、U3）；修正轮能不能看懂 qty 的报错文字并改对；
披萨题重跑后的数字和终稿。真实运行每次约 $0.5，要用户批准；至少要 U1–U3 做完才有意义，要在控制台看到单位还要 U4。

## 不做

- 数据点层的完整集合坐标（每个点标 geo / channel 等维度、代码做包含、重叠、重复计算检查）：等这一版跑过几道真题再定。
- 结构化基线的量纲反馈（G1、N38）：10-28 之后，见 FIX_PLAN.md D5。
- 真实运行验证要花钱（每次约 $0.5），不在 workflow 里跑；做完后由用户决定是否用控制台重跑披萨题。

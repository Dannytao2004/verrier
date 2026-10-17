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

### 量纲检查（compute 的 formula_mc，`require_units=True` 时）

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

| 阶段 | tag | 内容 | G2（prompt sha256） |
|---|---|---|---|
| U0 | `v2.7a` | `agent/qty.py` 和单元测试；requirements.txt 加 pint。不接入任何流程 | 不变 |
| U1 | `v2.7b` | 规划钉死单位（prompt、代码检查、重问一次、plan note） | 变，登记 |
| U2 | `v2.7c` | formula_mc 量纲检查和单位换算、百分数守卫、常数单位、AUDIT 加单位一项、JUDGE / METHODS_SPEC 的说明和回复示例 | 变 |
| U3 | `v2.7d` | 方法层覆盖范围（coverage、合并排除、修正提示、sum 的假设上限、AUDIT 加覆盖一项） | 变 |
| U4 | `v2.7e` | 显示单位（终稿 `[[unit]]`、控制台、经典界面、ledger、graph.html、results JSON） | 变 |

每个阶段除了 G1–G8，还要：
- 用假模型跑一遍完整的图（同 `tests/test_web.py` 的 FakeLLM），新字段齐全时能出数；
- 把披萨这次的三条路线，按新规则补上单位和覆盖范围，写成单元测试：
  - U2 之后 m1 得到约 64.8 吨/天、m2 约 59.9 吨/天；
  - U3 之后 m3 被排除在合并之外；把 m2、m3 合成一个 sum 方法（按本文件的规则补上 other 的假设）可以出数。
- 回归表（G3）：已存运行重算的结果和上一个 tag 逐行相同（旧运行走 `require_units=False`）。

## 不做

- 数据点层的完整集合坐标（每个点标 geo / channel 等维度、代码做包含、重叠、重复计算检查）：等这一版跑过几道真题再定。
- 结构化基线的量纲反馈（G1、N38）：10-28 之后，见 FIX_PLAN.md D5。
- 真实运行验证要花钱（每次约 $0.5），不在 workflow 里跑；做完后由用户决定是否用控制台重跑披萨题。

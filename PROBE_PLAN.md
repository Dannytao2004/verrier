# PROBE_PLAN（预注册）

写于 2026-10-15，在对模型发出任何调用之前提交。之后对本文件的任何改动都会在 git 历史里看得到；结果报告 `PROBE.md` 若与本计划有出入，会逐条写明。

## 1. 要回答的问题

「LLM 只提结构（3 条估算路径 + 带区间和出处的输入），算术全由 Python 做（白名单表达式求值 + Monte Carlo + 跨路径聚合）」这种结构化做法，在 Fermi 估算题上是否比「让模型直接报一个数」误差更小。

这是一个**探针**（probe）：n = 20、单模型、无检索。它只能给出「支持 / 不支持继续做」的信号，不是严格评测。

## 2. 数据

- realFP（Kalyan et al., 2021），官方仓库 allenai/fermi，commit `dfd4cee`，`test` split。详见 `DATA.md`。
- 合格题：答案是正数，且单位能被 `triangulate/units.py` 的显式单位表严格解析（547/557）。
- 选题：`random.Random(2021).sample(合格题按下标排序, 20)`。20 个 id 见 `data/backtest_realfp20_ids.json`：
  `test:422, 288, 258, 35, 463, 494, 67, 325, 281, 308, 496, 80, 169, 172, 56, 109, 306, 54, 487, 120`。
- 只把 `question` 和目标单位给模型；官方标注的 `program` / `context`（解题步骤和事实）不给。

## 3. 两个 arm

共同设置：模型 `deepseek-flash`，接口 `https://api.deepseek.com/chat/completions`，payload 含 `{"thinking":{"type":"disabled"},"response_format":{"type":"json_object"},"temperature":0}`。每次调用记一行到 `results/calls.jsonl`（arm、题 id、第几次尝试、token、延迟、finish_reason、估算 USD；不记内容）。

1. **naive**：一次调用。模型返回 `{"estimate": <number>, "unit": "<unit>"}`，要求用目标单位作答。
2. **structured**：一次调用。模型返回目标定义、一组具名输入（每个有 value / unit / low / high / provenance）和 3 条路径（top-down、bottom-up、proxy/analogy 各一条，每条是只引用输入名的公式）。模型**不算任何数**；Python 负责：
   - 公式用白名单表达式求值器解析（`+ - * / **`、括号、`min/max/sqrt`；公式里除 1 和指数外不允许数字常量）；
   - 输入单位由代码换算到 SI，路径输出量纲由代码推导，再换算到目标单位；量纲对不上的路径记为无效；
   - 每个输入按 lognormal 采样，low / high 视为该输入的 P10 / P90（中位数 = low 与 high 的几何平均）；N = 20000，固定种子 `MC_SEED = 20261015`（每题用 `"<seed>:<题 id>"` 作种子）；共享输入在各路径间用同一组样本；
   - 每条路径取样本中位数；**中心估计 = 有效路径中位数在 log 空间的中位数**（有效路径数为偶数时即中间两条的几何平均）；
   - **80% 区间 = 有效路径等权混合样本的 P10–P90**；
   - 交叉检查：路径中位数与中心估计相差超过 1 个数量级的标记为 outlier（只标记，不剔除）。

**重试规则（两个 arm 相同）**：输出不是合法 JSON、缺字段、数值不合法、公式解析失败、引用了未定义的输入、或单位无法解析/量纲不符时，带上错误清单重试一次。任务原文只要求 structured 重试；为公平起见 naive 也给同样的一次重试，两边用了几次重试都会报告。

**prompt 冻结**：prompt 开发和管线调试只用 finance demo 题（见第 7 节），不用 20 道回测题。20 道题每个 arm 只正式跑一次；若因代码 bug 必须重跑，会在 `PROBE.md` 写明原因和重跑范围。

## 4. 单位对齐

答案单位与模型单位之间的换算全部由代码按 `triangulate/units.py` 的显式表完成。无法对齐（模型单位解析失败或量纲不同）的题不静默丢弃，报告为 `unit_unreconciled`，并按第 6 节记为该 arm 失败。

## 5. 指标

对每题、每个 arm，误差 e = |log10(估计 / 答案)|（估计已换算到答案单位）。

- **主指标**：20 题上 e 的中位数。
- 1 个数量级以内的比例：e ≤ 1 的题数 / 20。
- **fp_score**：照官方 `eval_utils.accuracy_metric`，每题 `max(0, 3 − e) / 3`，20 题取平均（论文报告的就是这个分数）。
- **80% 区间原始覆盖率**：答案落在 [P10, P90] 内的比例。只适用于 structured（naive 不给区间）。
- 描述性信息：两 arm 逐题比较，structured 误差更小 / 相等 / 更大的题数。n = 20，不做显著性检验。

## 6. 失败处理

某 arm 在某题上没有可用估计（重试后输出仍无效、单位无法对齐、或所有路径都无效）时：e 记为 +∞（计入中位数，对该 arm 最不利）、1 个数量级以内记为否、fp_score 记 0、覆盖记为否。另外报告「两个 arm 都有估计的题」子集上的中位数作为辅助，但判定只看主指标。

## 7. Finance demo（不计分）

对 "Estimate the number of heavy-duty trucks sold in China in calendar year 2024" 跑一次 structured arm，生成 world model 和依赖图。不使用任何真值、不打分；输入如实标为 assumption。它同时是 prompt / 管线调试唯一使用的题。

## 8. 判定规则（STOP RULE）

**如果 structured arm 的 median |log10 err| 不低于 naive arm（即 ≥，含相等），则本探针不支持结构化方法。** 只有严格更低才算「支持继续」。这个判定不因次要指标改变。

## 9. 已知风险与局限

- **泄漏**：realFP 自 2021 年公开，题目和答案可能在模型训练数据里。两个 arm 共享这个风险；它会让两边都显得更准，并可能缩小两者差距（模型直接背出答案时 naive 占便宜）。本探针无法排除。
- **真值本身是估算**：realFP 的答案是标注者自己的 Fermi 估算，不是测量值，有些题的答案本身可疑。
- **无检索**：本阶段没有联网检索，绝大多数输入只能是 assumption；`sourced` 的输入一律只能是 `sourced_unverified`。依赖图里的 `sourced_verified` / `contradicted` 状态是为后续检索阶段保留的，本探针里不会出现。
- **样本小**：n = 20、单模型、temperature 0、单次运行。
- **预算**：预计总花费 < 0.10 USD（按 2026-10-15 查看的 deepseek-flash 价格）。

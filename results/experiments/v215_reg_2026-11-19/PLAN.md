# v2.15 固定回归：口径（2026-11-19，跑之前写定，跑完不改）

## 为什么跑

v2.15a–e（三方审计 + GPT 评估之后的五处小修：报错数字格式、裁判 JSON 补括号 / 关思考重问、百分数假设确认、量级闸门、
抽取上限 15 → 30）改了抽取 prompt 和修正报错，按规矩要跑一次固定回归，确认没有把原来能做对的题弄坏，并实测新规则在真实
运行里的效果。用户 11-19 给的额度：20 次完整运行。

## 跑什么（20 次，一次一跑、不重跑；只有基础设施故障可以重跑一次）

| # | 题 | 思考 | 用途 |
|---|---|---|---|
| 1–14 | 固定回归 14 题（同 `results/agent/summary_v211g_reg.json`）：kr_births_07、tw_births_09、lhr_pax_09、jp_births_07、nhs_ae_09、jp_movers_08、pola_teu_09、es_transit_08、ca_rail_07、de_cars_09、hk_visitors_09、us_starts_08、us_gen_07、kr_online_08 | 关 | 回归：和 v2.11g（10-22）逐题比 |
| 15–18 | ca_rail_07、tw_births_09、de_cars_09、kr_online_08 | 开（plan / judge / repair = high，audit / unit_arbiter = low，同留出测试 3、4） | 实测 S25 修法（开思考时裁判 JSON 坏过、没出数的题在内） |
| 19 | BCG 美国员工（11-12 网页那题原文 "how many ng employees in BCG USA in 2026?"，as_of 2026-11-19，真实使用） | 关 | 实测百分数确认和量级闸门在真实翻车题上的效果（11-12 那次是 101 人） |
| 20 | sponsor 严格口径（`probes/run_v214a_batch.py` 里的原文，as_of 2026-10-28） | 关 | 没有真值的费米题：看闸门会不会乱报警、修正后变成什么 |

代码：tag `v2.15g`。v2.15e 之后两个子 agent（只读）做了独立审查和存档离线重放，开跑前修了：补括号在存档那种坏法下会把
unit / coverage / rationale 静默塞进 params、闸门在修正轮用完后仍记「修过」、消融里闸门照开（v2.15f）；闸门那句话写的是
点原来记的单位而不是代码算的单位、只点名偏了的方法会泄露粗估的范围、百分数改写建议的 unit "1" 会被 target_reason 再拒
（v2.15g）。
只在 DeepSeek 谷价时段开跑（`config.is_peak`）。两条线并行，每条线一个接一个。

## 看什么（打分口径）

- 回归 14 题：每题误差、80% 区间是否盖住真值、区间宽度、有没有出数；对照 v2.11g 的同题结果。中位误差、出数题数、
  ±10% 内题数一起报。没出数照旧记为失败。
- 闸门：14 题都有真值，闸门触发次数和触发后结果变好 / 变坏都列出；触发在误差本来就小于 2 倍的题上 = 误报。
- 百分数确认：被交回的假设逐条列出（原写法、改写后），看裁判是否照做。
- 补括号 / 关思考重问：从 calls.jsonl 数 json_repaired、thinking_off_retry、invalid_json。
- 逐字读每题的终稿，有 [n]、占位符没换、单位错就记下来。
- 花费：每次运行的 usd_total_assumed 和 token 费。

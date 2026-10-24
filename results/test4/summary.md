# 留出测试 4（前瞻）：三臂 x 思考开关（probes/run_test4.py --score）

误差 = 估计 / 首发值 - 1；abs(log10) = |log10(估计 / 首发值)|。只在 forecast.TEST4_OFFICIAL 登记了首发值的题上算；这些题里没出数的配置误差记为 inf、计入中位数。80% 覆盖只算有区间的臂（直接问、联网直接问没有区间）。费用：基线 = 调用记录的 usd 合计（search_direct 含按假设单价记的搜索费）；agent = 预算的 usd_total_assumed。

## 汇总

| 臂 | 思考 | 出数 | 已打分 | 中位绝对误差 | 中位 abs(log10) | ±10% 内 | ±5% 内 | 80% 覆盖 | 费用 USD | 没出数 |
|---|---|---|---|---|---|---|---|---|---|---|
| naive | off | 2/2 | 0 | — | — | 0 | 0 | n/a (no official value yet) | 0.0001 | — |
| naive | think | 2/2 | 0 | — | — | 0 | 0 | n/a (no official value yet) | 0.0013 | — |
| search_direct | off | 2/2 | 0 | — | — | 0 | 0 | n/a (no official value yet) | 0.0426 | — |
| search_direct | think | 2/2 | 0 | — | — | 0 | 0 | n/a (no official value yet) | 0.1608 | — |
| agent | off | 2/2 | 0 | — | — | 0 | 0 | n/a (no official value yet) | 1.0816 | — |
| agent | think | 1/2 | 0 | — | — | 0 | 0 | n/a (no official value yet) | 1.0007 | fc_cn_profits_2026_09: done / no estimate |

## 逐个配置

| 题 | 臂 | 思考 | as_of | 结果 | 估计 | 误差 | abs(log10) | P10 | P90 | 覆盖 | 费用 USD | 说明 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| fc_cn_profits_2026_09 | naive | off | 2026-10-24 | done / ok | 5,400,000,000,000 | — | — | — | — | — | 0.0000 |  |
| fc_cn_profits_2026_09 | naive | think | 2026-10-24 | done / ok | 5,600,000,000,000 | — | — | — | — | — | 0.0011 |  |
| fc_cn_profits_2026_09 | search_direct | off | 2026-10-24 | done / ok | 5,620,000,000,000 | — | — | — | — | — | 0.0211 | 搜索 2 次、结果 URL 20 个、思考块 [0] |
| fc_cn_profits_2026_09 | search_direct | think | 2026-10-24 | done / ok | 5,960,000,000,000 | — | — | — | — | — | 0.0765 | 搜索 7 次、结果 URL 50 个、思考块 [5] |
| fc_cn_profits_2026_09 | agent | off | 2026-10-24 | done / ok | 58,009 | — | — | 42,107 | 79,917 | — | 0.5920 | 已公布检查 no_candidates、live 页 40、快照 0 |
| fc_cn_profits_2026_09 | agent | think | 2026-10-24 | done / no estimate | — | — | — | — | — | — | 0.3705 | 已公布检查 no_candidates、live 页 26、快照 0 |
| fc_tw_visitors_2026_09 | naive | off | 2026-10-24 | done / ok | 650,000 | — | — | — | — | — | 0.0000 |  |
| fc_tw_visitors_2026_09 | naive | think | 2026-10-24 | done / ok | 740,000 | — | — | — | — | — | 0.0002 |  |
| fc_tw_visitors_2026_09 | search_direct | off | 2026-10-24 | done / ok | 640,000 | — | — | — | — | — | 0.0215 | 搜索 2 次、结果 URL 15 个、思考块 [0] |
| fc_tw_visitors_2026_09 | search_direct | think | 2026-10-24 | done / ok | 640,000 | — | — | — | — | — | 0.0843 | 搜索 8 次、结果 URL 30 个、思考块 [4] |
| fc_tw_visitors_2026_09 | agent | off | 2026-10-24 | done / ok | 613,635 | — | — | 403,381 | 933,479 | — | 0.4896 | 已公布检查 no_candidates、live 页 26、快照 0 |
| fc_tw_visitors_2026_09 | agent | think | 2026-10-24 | done / ok | 610,381 | — | — | 440,063 | 846,618 | — | 0.6302 | 已公布检查 no_candidates、live 页 28、快照 0 |

## 首发值和参照（去年同期的登记值，不是对照臂）

| 题 | 首发时刻 | 首发值 | 去年同期 | 去年同期的误差 |
|---|---|---|---|---|
| fc_cn_profits_2026_09 | 2026-10-27T09:30:00+08:00 | 还没登记 | 5,373,200,000,000 | — |
| fc_tw_visitors_2026_09 | 2026-10-27T16:20:00+08:00 | 还没登记 | 601,339 | — |

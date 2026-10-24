# 留出测试 4（前瞻）：三臂 x 思考开关（probes/run_test4.py --score）

误差 = 估计 / 首发值 - 1；abs(log10) = |log10(估计 / 首发值)|。只在 forecast.TEST4_OFFICIAL 登记了首发值的题上算；这些题里没出数的配置误差记为 inf、计入中位数。80% 覆盖只算有区间的臂（直接问、联网直接问没有区间）。费用：基线 = 调用记录的 usd 合计（search_direct 含按假设单价记的搜索费）；agent = 预算的 usd_total_assumed。

## 汇总

| 臂 | 思考 | 出数 | 已打分 | 中位绝对误差 | 中位 abs(log10) | ±10% 内 | ±5% 内 | 80% 覆盖 | 费用 USD | 没出数 |
|---|---|---|---|---|---|---|---|---|---|---|
| naive | off | 0/2 | 0 | — | — | 0 | 0 | n/a (no official value yet) | 0.0000 | fc_cn_profits_2026_09: not run; fc_tw_visitors_2026_09: not run |
| naive | think | 0/2 | 0 | — | — | 0 | 0 | n/a (no official value yet) | 0.0000 | fc_cn_profits_2026_09: not run; fc_tw_visitors_2026_09: not run |
| search_direct | off | 0/2 | 0 | — | — | 0 | 0 | n/a (no official value yet) | 0.0000 | fc_cn_profits_2026_09: not run; fc_tw_visitors_2026_09: not run |
| search_direct | think | 0/2 | 0 | — | — | 0 | 0 | n/a (no official value yet) | 0.0000 | fc_cn_profits_2026_09: not run; fc_tw_visitors_2026_09: not run |
| agent | off | 2/2 | 0 | — | — | 0 | 0 | n/a (no official value yet) | 0.9282 | — |
| agent | think | 2/2 | 0 | — | — | 0 | 0 | n/a (no official value yet) | 1.1755 | — |

## 逐个配置

| 题 | 臂 | 思考 | as_of | 结果 | 估计 | 误差 | abs(log10) | P10 | P90 | 覆盖 | 费用 USD | 说明 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| fc_cn_profits_2026_09 | naive | off | — | not run | — | — | — | — | — | — | — |  |
| fc_cn_profits_2026_09 | naive | think | — | not run | — | — | — | — | — | — | — |  |
| fc_cn_profits_2026_09 | search_direct | off | — | not run | — | — | — | — | — | — | — |  |
| fc_cn_profits_2026_09 | search_direct | think | — | not run | — | — | — | — | — | — | — |  |
| fc_cn_profits_2026_09 | agent | off | 2026-10-24 | done / ok | 5,644,937,033,270 | — | — | 4,097,475,907,149 | 7,776,815,491,212 | — | 0.4538 | 已公布检查 no_candidates、live 页 26、快照 0 |
| fc_cn_profits_2026_09 | agent | think | 2026-10-24 | done / ok | 6,000,004,778,609 | — | — | 3,993,391,631,699 | 9,014,907,793,558 | — | 0.6125 | 已公布检查 not_confirmed、live 页 38、快照 0 |
| fc_tw_visitors_2026_09 | naive | off | — | not run | — | — | — | — | — | — | — |  |
| fc_tw_visitors_2026_09 | naive | think | — | not run | — | — | — | — | — | — | — |  |
| fc_tw_visitors_2026_09 | search_direct | off | — | not run | — | — | — | — | — | — | — |  |
| fc_tw_visitors_2026_09 | search_direct | think | — | not run | — | — | — | — | — | — | — |  |
| fc_tw_visitors_2026_09 | agent | off | 2026-10-24 | done / ok | 612,057 | — | — | 414,074 | 904,702 | — | 0.4744 | 已公布检查 no_candidates、live 页 27、快照 0 |
| fc_tw_visitors_2026_09 | agent | think | 2026-10-24 | done / ok | 608,655 | — | — | 441,803 | 838,520 | — | 0.5630 | 已公布检查 no_candidates、live 页 21、快照 0 |

## 首发值和参照（去年同期的登记值，不是对照臂）

| 题 | 首发时刻 | 首发值 | 去年同期 | 去年同期的误差 |
|---|---|---|---|---|
| fc_cn_profits_2026_09 | 2026-10-27T09:30:00+08:00 | 还没登记 | 5,373,200,000,000 | — |
| fc_tw_visitors_2026_09 | 2026-10-27T16:20:00+08:00 | 还没登记 | 601,339 | — |

# 留出测试 4（前瞻）：三臂 x 思考开关（probes/run_test4.py --score）

误差 = 估计 / 首发值 - 1；abs(log10) = |log10(估计 / 首发值)|。只在 forecast.TEST4_OFFICIAL 登记了首发值的题上算；这些题里没出数的配置误差记为 inf、计入中位数。80% 覆盖只算有区间的臂（直接问、联网直接问没有区间）。费用：基线 = 调用记录的 usd 合计（search_direct 含按假设单价记的搜索费）；agent = 预算的 usd_total_assumed。

## 汇总

| 臂 | 思考 | 出数 | 已打分 | 中位绝对误差 | 中位 abs(log10) | ±10% 内 | ±5% 内 | 80% 覆盖 | 费用 USD | 没出数 |
|---|---|---|---|---|---|---|---|---|---|---|
| naive | off | 7/7 | 2 | 8.4% | 0.037 | 1 | 0 | n/a (no interval) | 0.0003 | — |
| naive | think | 7/7 | 2 | 14.1% | 0.058 | 1 | 0 | n/a (no interval) | 0.0041 | — |
| search_direct | off | 7/7 | 2 | 5.7% | 0.025 | 2 | 1 | n/a (no interval) | 0.1370 | — |
| search_direct | think | 7/7 | 2 | 2.9% | 0.012 | 2 | 2 | n/a (no interval) | 0.5688 | — |
| agent | off | 5/7 | 2 | 50.2% | 4.009 | 1 | 1 | 1/2 | 7.9438 | fc_eqnr_prod_2026_q3: done / unit not convertible; fc_uk_homesales_2026_09: done / no estimate |
| agent | think | 5/7 | 2 | inf | inf | 1 | 1 | 1/1 | 8.9443 | fc_cn_profits_2026_09: done / no estimate; fc_eqnr_prod_2026_q3: done / unit not convertible |

## 逐个配置

| 题 | 臂 | 思考 | as_of | 结果 | 估计 | 误差 | abs(log10) | P10 | P90 | 覆盖 | 费用 USD | 说明 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| fc_cn_profits_2026_09 | naive | off | 2026-10-24 | done / ok | 5,400,000,000,000 | -10.5% | 0.048 | — | — | — | 0.0000 |  |
| fc_cn_profits_2026_09 | naive | think | 2026-10-24 | done / ok | 5,600,000,000,000 | -7.2% | 0.032 | — | — | — | 0.0011 |  |
| fc_cn_profits_2026_09 | search_direct | off | 2026-10-24 | done / ok | 5,620,000,000,000 | -6.9% | 0.031 | — | — | — | 0.0211 | 搜索 2 次、结果 URL 20 个、思考块 [0] |
| fc_cn_profits_2026_09 | search_direct | think | 2026-10-24 | done / ok | 5,960,000,000,000 | -1.2% | 0.005 | — | — | — | 0.0765 | 搜索 7 次、结果 URL 50 个、思考块 [5] |
| fc_cn_profits_2026_09 | agent | off | 2026-10-24 | done / ok | 58,009 | -100.0% | 8.017 | 42,107 | 79,917 | 否 | 0.5920 | 已公布检查 no_candidates、live 页 40、快照 0 |
| fc_cn_profits_2026_09 | agent | think | 2026-10-24 | done / no estimate | — | — | — | — | — | — | 0.3705 | 已公布检查 no_candidates、live 页 26、快照 0 |
| fc_tw_visitors_2026_09 | naive | off | 2026-10-24 | done / ok | 650,000 | +6.3% | 0.026 | — | — | — | 0.0000 |  |
| fc_tw_visitors_2026_09 | naive | think | 2026-10-24 | done / ok | 740,000 | +21.0% | 0.083 | — | — | — | 0.0002 |  |
| fc_tw_visitors_2026_09 | search_direct | off | 2026-10-24 | done / ok | 640,000 | +4.6% | 0.020 | — | — | — | 0.0215 | 搜索 2 次、结果 URL 15 个、思考块 [0] |
| fc_tw_visitors_2026_09 | search_direct | think | 2026-10-24 | done / ok | 640,000 | +4.6% | 0.020 | — | — | — | 0.0843 | 搜索 8 次、结果 URL 30 个、思考块 [4] |
| fc_tw_visitors_2026_09 | agent | off | 2026-10-24 | done / ok | 613,635 | +0.3% | 0.001 | 403,381 | 933,479 | 是 | 0.4896 | 已公布检查 no_candidates、live 页 26、快照 0 |
| fc_tw_visitors_2026_09 | agent | think | 2026-10-24 | done / ok | 610,381 | -0.2% | 0.001 | 440,063 | 846,618 | 是 | 0.6302 | 已公布检查 no_candidates、live 页 28、快照 0 |
| fc_eqnr_prod_2026_q3 | naive | off | 2026-10-27 | done / ok | 2,050,000 | — | — | — | — | — | 0.0000 |  |
| fc_eqnr_prod_2026_q3 | naive | think | 2026-10-27 | done / ok | 2,000,000 | — | — | — | — | — | 0.0005 |  |
| fc_eqnr_prod_2026_q3 | search_direct | off | 2026-10-27 | done / ok | 2,160,000 | — | — | — | — | — | 0.0212 | 搜索 2 次、结果 URL 20 个、思考块 [0] |
| fc_eqnr_prod_2026_q3 | search_direct | think | 2026-10-27 | done / ok | 2,160,000 | — | — | — | — | — | 0.0862 | 搜索 8 次、结果 URL 50 个、思考块 [4] |
| fc_eqnr_prod_2026_q3 | agent | off | 2026-10-27 | done / unit not convertible | — | — | — | — | — | — | 1.3954 | 已公布检查 no_candidates、live 页 58、快照 0；'mboe/d' (mboe / d) cannot be converted to 'boe/d' (boe / d) |
| fc_eqnr_prod_2026_q3 | agent | think | 2026-10-27 | done / unit not convertible | — | — | — | — | — | — | 1.6371 | 已公布检查 not_confirmed、live 页 59、快照 0；'mboe/d' (mboe / d) cannot be converted to 'boe/d' (boe / d) |
| fc_byd_rev_2026_q3 | naive | off | 2026-10-27 | done / ok | 215,000,000,000 | — | — | — | — | — | 0.0000 |  |
| fc_byd_rev_2026_q3 | naive | think | 2026-10-27 | done / ok | 215,000,000,000 | — | — | — | — | — | 0.0007 |  |
| fc_byd_rev_2026_q3 | search_direct | off | 2026-10-27 | done / ok | 205,000,000,000 | — | — | — | — | — | 0.0207 | 搜索 2 次、结果 URL 17 个、思考块 [0] |
| fc_byd_rev_2026_q3 | search_direct | think | 2026-10-27 | done / ok | 241,000,000,000 | — | — | — | — | — | 0.0749 | 搜索 7 次、结果 URL 41 个、思考块 [3] |
| fc_byd_rev_2026_q3 | agent | off | 2026-10-27 | done / ok | 208,949,271,568 | — | — | 151,669,469,654 | 287,861,480,549 | — | 1.4030 | 已公布检查 no_candidates、live 页 81、快照 0 |
| fc_byd_rev_2026_q3 | agent | think | 2026-10-27 | done / ok | 219,760,222,076 | — | — | 114,466,292,271 | 421,910,714,927 | — | 1.4779 | 已公布检查 not_confirmed、live 页 83、快照 0 |
| fc_uk_carprod_2026_09 | naive | off | 2026-10-27 | done / ok | 70,000 | — | — | — | — | — | 0.0000 |  |
| fc_uk_carprod_2026_09 | naive | think | 2026-10-27 | done / ok | 67,000 | — | — | — | — | — | 0.0009 |  |
| fc_uk_carprod_2026_09 | search_direct | off | 2026-10-27 | done / ok | 68,000 | — | — | — | — | — | 0.0107 | 搜索 1 次、结果 URL 10 个、思考块 [0] |
| fc_uk_carprod_2026_09 | search_direct | think | 2026-10-27 | done / ok | 70,000 | — | — | — | — | — | 0.0881 | 搜索 8 次、结果 URL 47 个、思考块 [4] |
| fc_uk_carprod_2026_09 | agent | off | 2026-10-27 | done / ok | 51,144 | — | — | 37,124 | 70,460 | — | 1.3714 | 已公布检查 not_confirmed、live 页 92、快照 0 |
| fc_uk_carprod_2026_09 | agent | think | 2026-10-27 | done / ok | 65,782 | — | — | 45,425 | 95,260 | — | 1.4214 | 已公布检查 not_confirmed、live 页 96、快照 0 |
| fc_uk_mortgages_2026_09 | naive | off | 2026-10-27 | done / ok | 62,000 | — | — | — | — | — | 0.0000 |  |
| fc_uk_mortgages_2026_09 | naive | think | 2026-10-27 | done / ok | 64,000 | — | — | — | — | — | 0.0003 |  |
| fc_uk_mortgages_2026_09 | search_direct | off | 2026-10-27 | done / ok | 61,000 | — | — | — | — | — | 0.0211 | 搜索 2 次、结果 URL 20 个、思考块 [0] |
| fc_uk_mortgages_2026_09 | search_direct | think | 2026-10-27 | done / ok | 57,000 | — | — | — | — | — | 0.0752 | 搜索 7 次、结果 URL 43 个、思考块 [4] |
| fc_uk_mortgages_2026_09 | agent | off | 2026-10-27 | done / ok | 54,766 | — | — | 38,759 | 77,384 | — | 1.4823 | 已公布检查 no_candidates、live 页 95、快照 0 |
| fc_uk_mortgages_2026_09 | agent | think | 2026-10-27 | done / ok | 54,348 | — | — | 37,184 | 79,436 | — | 1.7441 | 已公布检查 not_confirmed、live 页 113、快照 0 |
| fc_uk_homesales_2026_09 | naive | off | 2026-10-27 | done / ok | 92,000 | — | — | — | — | — | 0.0000 |  |
| fc_uk_homesales_2026_09 | naive | think | 2026-10-27 | done / ok | 95,000 | — | — | — | — | — | 0.0005 |  |
| fc_uk_homesales_2026_09 | search_direct | off | 2026-10-27 | done / ok | 97,000 | — | — | — | — | — | 0.0206 | 搜索 2 次、结果 URL 11 个、思考块 [0] |
| fc_uk_homesales_2026_09 | search_direct | think | 2026-10-27 | done / ok | 94,000 | — | — | — | — | — | 0.0835 | 搜索 8 次、结果 URL 41 个、思考块 [4] |
| fc_uk_homesales_2026_09 | agent | off | 2026-10-27 | done / no estimate | — | — | — | — | — | — | 1.2101 | 已公布检查 no_candidates、live 页 83、快照 0 |
| fc_uk_homesales_2026_09 | agent | think | 2026-10-27 | done / ok | 94,743 | — | — | 62,382 | 143,890 | — | 1.6631 | 已公布检查 no_candidates、live 页 107、快照 0 |

## 首发值和参照（去年同期的登记值，不是对照臂）

| 题 | 首发时刻 | 首发值 | 去年同期 | 去年同期的误差 |
|---|---|---|---|---|
| fc_cn_profits_2026_09 | 2026-10-27T09:30:00+08:00 | 6,033,740,000,000 | 5,373,200,000,000 | -10.9% |
| fc_tw_visitors_2026_09 | 2026-10-27T16:20:00+08:00 | 611,755 | 601,339 | -1.7% |
| fc_eqnr_prod_2026_q3 | 2026-10-28T07:00:00+01:00 | 还没登记 | 2,130,000 | — |
| fc_byd_rev_2026_q3 | 2026-10-29T00:00:00+08:00 | 还没登记 | 194,984,598,000 | — |
| fc_uk_carprod_2026_09 | 2026-10-29T00:01:00+00:00 | 还没登记 | 51,090 | — |
| fc_uk_mortgages_2026_09 | 2026-10-29T09:30:00+00:00 | 还没登记 | 65,900 | — |
| fc_uk_homesales_2026_09 | 2026-10-30T09:30:00+00:00 | 还没登记 | 95,980 | — |

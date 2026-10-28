# 留出测试 4（前瞻）：三臂 x 思考开关（probes/run_test4.py --score）

误差 = 估计 / 首发值 - 1；abs(log10) = |log10(估计 / 首发值)|。只在 forecast.TEST4_OFFICIAL 登记了首发值的题上算；这些题里没出数的配置误差记为 inf、计入中位数。80% 覆盖只算有区间的臂（直接问、联网直接问没有区间）。费用：基线 = 调用记录的 usd 合计（search_direct 含按假设单价记的搜索费）；agent = 预算的 usd_total_assumed。

## 汇总

| 臂 | 思考 | 出数 | 已打分 | 中位绝对误差 | 中位 abs(log10) | ±10% 内 | ±5% 内 | 80% 覆盖 | 费用 USD | 没出数 |
|---|---|---|---|---|---|---|---|---|---|---|
| naive | off | 0/7 | 2 | inf | inf | 0 | 0 | n/a (no interval) | 0.0000 | fc_cn_profits_2026_09: not run; fc_tw_visitors_2026_09: not run; fc_eqnr_prod_2026_q3: not run; fc_byd_rev_2026_q3: not run; fc_uk_carprod_2026_09: not run; fc_uk_mortgages_2026_09: not run; fc_uk_homesales_2026_09: not run |
| naive | think | 0/7 | 2 | inf | inf | 0 | 0 | n/a (no interval) | 0.0000 | fc_cn_profits_2026_09: not run; fc_tw_visitors_2026_09: not run; fc_eqnr_prod_2026_q3: not run; fc_byd_rev_2026_q3: not run; fc_uk_carprod_2026_09: not run; fc_uk_mortgages_2026_09: not run; fc_uk_homesales_2026_09: not run |
| search_direct | off | 0/7 | 2 | inf | inf | 0 | 0 | n/a (no interval) | 0.0000 | fc_cn_profits_2026_09: not run; fc_tw_visitors_2026_09: not run; fc_eqnr_prod_2026_q3: not run; fc_byd_rev_2026_q3: not run; fc_uk_carprod_2026_09: not run; fc_uk_mortgages_2026_09: not run; fc_uk_homesales_2026_09: not run |
| search_direct | think | 0/7 | 2 | inf | inf | 0 | 0 | n/a (no interval) | 0.0000 | fc_cn_profits_2026_09: not run; fc_tw_visitors_2026_09: not run; fc_eqnr_prod_2026_q3: not run; fc_byd_rev_2026_q3: not run; fc_uk_carprod_2026_09: not run; fc_uk_mortgages_2026_09: not run; fc_uk_homesales_2026_09: not run |
| agent | off | 2/7 | 2 | inf | inf | 0 | 0 | n/a (no interval) | 3.2437 | fc_cn_profits_2026_09: not run; fc_tw_visitors_2026_09: not run; fc_eqnr_prod_2026_q3: not run; fc_byd_rev_2026_q3: not run; fc_uk_mortgages_2026_09: not run |
| agent | think | 2/7 | 2 | inf | inf | 0 | 0 | n/a (no interval) | 3.3255 | fc_cn_profits_2026_09: not run; fc_tw_visitors_2026_09: not run; fc_eqnr_prod_2026_q3: not run; fc_byd_rev_2026_q3: not run; fc_uk_mortgages_2026_09: not run |

## 逐个配置

| 题 | 臂 | 思考 | as_of | 结果 | 估计 | 误差 | abs(log10) | P10 | P90 | 覆盖 | 费用 USD | 说明 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| fc_cn_profits_2026_09 | naive | off | — | not run | — | — | — | — | — | — | — |  |
| fc_cn_profits_2026_09 | naive | think | — | not run | — | — | — | — | — | — | — |  |
| fc_cn_profits_2026_09 | search_direct | off | — | not run | — | — | — | — | — | — | — |  |
| fc_cn_profits_2026_09 | search_direct | think | — | not run | — | — | — | — | — | — | — |  |
| fc_cn_profits_2026_09 | agent | off | — | not run | — | — | — | — | — | — | — |  |
| fc_cn_profits_2026_09 | agent | think | — | not run | — | — | — | — | — | — | — |  |
| fc_tw_visitors_2026_09 | naive | off | — | not run | — | — | — | — | — | — | — |  |
| fc_tw_visitors_2026_09 | naive | think | — | not run | — | — | — | — | — | — | — |  |
| fc_tw_visitors_2026_09 | search_direct | off | — | not run | — | — | — | — | — | — | — |  |
| fc_tw_visitors_2026_09 | search_direct | think | — | not run | — | — | — | — | — | — | — |  |
| fc_tw_visitors_2026_09 | agent | off | — | not run | — | — | — | — | — | — | — |  |
| fc_tw_visitors_2026_09 | agent | think | — | not run | — | — | — | — | — | — | — |  |
| fc_eqnr_prod_2026_q3 | naive | off | — | not run | — | — | — | — | — | — | — |  |
| fc_eqnr_prod_2026_q3 | naive | think | — | not run | — | — | — | — | — | — | — |  |
| fc_eqnr_prod_2026_q3 | search_direct | off | — | not run | — | — | — | — | — | — | — |  |
| fc_eqnr_prod_2026_q3 | search_direct | think | — | not run | — | — | — | — | — | — | — |  |
| fc_eqnr_prod_2026_q3 | agent | off | — | not run | — | — | — | — | — | — | — | 见下方打分说明； |
| fc_eqnr_prod_2026_q3 | agent | think | — | not run | — | — | — | — | — | — | — | 见下方打分说明； |
| fc_byd_rev_2026_q3 | naive | off | — | not run | — | — | — | — | — | — | — |  |
| fc_byd_rev_2026_q3 | naive | think | — | not run | — | — | — | — | — | — | — |  |
| fc_byd_rev_2026_q3 | search_direct | off | — | not run | — | — | — | — | — | — | — |  |
| fc_byd_rev_2026_q3 | search_direct | think | — | not run | — | — | — | — | — | — | — |  |
| fc_byd_rev_2026_q3 | agent | off | — | not run | — | — | — | — | — | — | — |  |
| fc_byd_rev_2026_q3 | agent | think | — | not run | — | — | — | — | — | — | — |  |
| fc_uk_carprod_2026_09 | naive | off | — | not run | — | — | — | — | — | — | — |  |
| fc_uk_carprod_2026_09 | naive | think | — | not run | — | — | — | — | — | — | — |  |
| fc_uk_carprod_2026_09 | search_direct | off | — | not run | — | — | — | — | — | — | — |  |
| fc_uk_carprod_2026_09 | search_direct | think | — | not run | — | — | — | — | — | — | — |  |
| fc_uk_carprod_2026_09 | agent | off | 2026-10-28 | done / ok | 53,625 | — | — | 38,925 | 73,877 | — | 1.5458 | 已公布检查 not_confirmed、live 页 107、快照 0 |
| fc_uk_carprod_2026_09 | agent | think | 2026-10-28 | done / ok | 59,637 | — | — | 42,825 | 83,048 | — | 1.6161 | 已公布检查 no_candidates、live 页 98、快照 0 |
| fc_uk_mortgages_2026_09 | naive | off | — | not run | — | — | — | — | — | — | — |  |
| fc_uk_mortgages_2026_09 | naive | think | — | not run | — | — | — | — | — | — | — |  |
| fc_uk_mortgages_2026_09 | search_direct | off | — | not run | — | — | — | — | — | — | — |  |
| fc_uk_mortgages_2026_09 | search_direct | think | — | not run | — | — | — | — | — | — | — |  |
| fc_uk_mortgages_2026_09 | agent | off | — | not run | — | — | — | — | — | — | — |  |
| fc_uk_mortgages_2026_09 | agent | think | — | not run | — | — | — | — | — | — | — |  |
| fc_uk_homesales_2026_09 | naive | off | — | not run | — | — | — | — | — | — | — |  |
| fc_uk_homesales_2026_09 | naive | think | — | not run | — | — | — | — | — | — | — |  |
| fc_uk_homesales_2026_09 | search_direct | off | — | not run | — | — | — | — | — | — | — |  |
| fc_uk_homesales_2026_09 | search_direct | think | — | not run | — | — | — | — | — | — | — |  |
| fc_uk_homesales_2026_09 | agent | off | 2026-10-28 | done / ok | 91,713 | — | — | 63,601 | 132,250 | — | 1.6979 | 已公布检查 no_candidates、live 页 114、快照 0 |
| fc_uk_homesales_2026_09 | agent | think | 2026-10-28 | done / ok | 94,166 | — | — | 65,585 | 135,204 | — | 1.7094 | 已公布检查 no_candidates、live 页 108、快照 0 |

## 打分说明

- **fc_eqnr_prod_2026_q3**：agent 两个配置的输出单位是 mboe/d（千桶油当量/日，Equinor 报告的写法），终稿 2,195 / 2,149 mboe/d。跑的时候（v2.13b）单位库不认识 mboe，打分换不到计分单位 boe/d，记过「unit not convertible」（BUGS S75）。v2.13c 起单位库按 SPE 惯例读 mboe = 1000 boe，同一份输出按 x1000 换算打分。用户 2026-10-27 定：算。这是打分环节的修正：agent 没有重跑，输出没改。

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

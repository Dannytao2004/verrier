# 第一轮多派搜索 agent：两次运行之间的重合度（2026-10-27）

题目：应届生 sponsor（ask_504d98a4）。规划固定用运行 B 的 7 个第一轮方向，只跑第一轮（搜索、抓 live 页、抽取、代码核对），每个设置两次。
数据点「同一个」：数值 3 位有效数字相同，单位用 pint 换算系数为 1（months/month、/年 与 /year 算同一个）。生成：probes/search_overlap_report.py。

| setting | agents | URLs/dir | pages read | page overlap | site overlap | points | point overlap | (value only) | tokens $/run | search fee (assumed) $/run | wall s |
|---|---|---|---|---|---|---|---|---|---|---|---|
| k1n4 | 1 | 4 | 19 | 12% | 12% | 218 | 53% | 59% | 0.051 | 0.30 | 44 |
| k3n6 | 3 | 6 | 28 | 24% | 30% | 302 | 57% | 71% | 0.113 | 0.89 | 66 |
| k3n8 | 3 | 8 | 32 | 9% | 11% | 328 | 50% | 59% | 0.108 | 0.84 | 182 |
| k3n10 | 3 | 10 | 42 | 27% | 31% | 450 | 65% | 74% | 0.126 | 0.91 | 85 |
| k3n12 | 3 | 12 | 57 | 30% | 39% | 551 | 73% | 82% | 0.133 | 0.91 | 103 |
| k3n14 | 3 | 14 | 66 | 44% | 53% | 682 | 77% | 87% | 0.150 | 0.88 | 110 |
| k3n16 | 3 | 16 | 77 | 31% | 39% | 752 | 72% | 84% | 0.156 | 0.87 | 118 |

marginal (each step vs the previous K=3 setting): point overlap gained per extra page read and per extra $ of tokens
  k3n6 -> k3n8: +4 pages, point overlap -8%, page overlap -16%, tokens -0.005 $/run, -21.5% overlap per 10 pages
  k3n8 -> k3n10: +11 pages, point overlap +15%, page overlap +18%, tokens +0.018 $/run, +13.7% overlap per 10 pages
  k3n10 -> k3n12: +14 pages, point overlap +8%, page overlap +3%, tokens +0.007 $/run, +5.7% overlap per 10 pages
  k3n12 -> k3n14: +8 pages, point overlap +4%, page overlap +14%, tokens +0.017 $/run, +4.5% overlap per 10 pages
  k3n14 -> k3n16: +12 pages, point overlap -5%, page overlap -13%, tokens +0.006 $/run, -4.0% overlap per 10 pages

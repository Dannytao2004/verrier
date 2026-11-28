"""Minimum detectable effects for the pre-registered comparisons (planning only). Uses design counts from runs.csv
(numbers of runs per question, no errors) and planning values cited from verify files; computes no outcome of the
planned analyses. alpha = 0.05 two-sided unless stated, power = 0.80."""
import csv, math
from pathlib import Path
from scipy import stats, special
ROOT = Path(__file__).resolve().parents[2]
rows = list(csv.DictReader(open(ROOT / "paper/analysis/data/runs.csv", encoding="utf-8")))
print("[1] paired / sign-flip MDE over G questions, in SD units of the per-question difference: (t_.975 + t_.80)/sqrt(G);"
      " exact sign-flip floor = 2/2^G (two-sided)")
for G in (6, 7, 9, 10, 12, 16, 20, 23):
    k = (stats.t.ppf(0.975, G - 1) + stats.t.ppf(0.80, G - 1)) / math.sqrt(G)
    print(f"   G={G:2d}: MDE = {k:.3f} SD; sign-flip p floor = {2 / 2 ** G:.2e}")
print("[2] variance ratio (as-is within-question variance / pool-A within-cell variance), per-question bias-corrected log ratio")
# design count: scored archive runs per question (all) -- the as-is df; non-catastrophic counts are not used (outcome-free)
from collections import Counter
n_q = Counter(r["qid"] for r in rows if r["scored"] == "True")
dfs = sorted(n - 1 for n in n_q.values() if n >= 2)
print("   as-is scored runs per question (n_q):", sorted(n_q.values()), "-> df median", dfs[len(dfs) // 2])
tri = lambda df: special.polygamma(1, df / 2)   # var of ln(chi2_df/df) = trigamma(df/2)
sd_per_q = [math.sqrt(tri(2) + tri(df)) for df in dfs]
sd = math.sqrt(sum(s * s for s in sd_per_q) / len(sd_per_q))
for G in (16, 20, 23):
    k = (stats.t.ppf(0.975, G - 1) + stats.t.ppf(0.80, G - 1)) / math.sqrt(G)
    m = k * sd
    print(f"   G={G}: sampling sd of per-question log ratio ~ {sd:.2f} (normal errors, no true heterogeneity) -> MDE ln ratio {m:.2f}"
          f" = variance ratio {math.exp(m):.2f} (sd ratio {math.exp(m / 2):.2f})")
print("   pooled within-cell SD from 23 cells x 2 df = 46 df: 95% CI factor on sigma",
      f"[{math.sqrt(46 / stats.chi2.ppf(0.975, 46)):.2f}, {math.sqrt(46 / stats.chi2.ppf(0.025, 46)):.2f}] (normal errors)")
print("[3] catastrophic rate in pool A (69 runs), exact binomial, ignoring clustering")
for n in (69, 60):
    print(f"   n={n}: rule-of-three upper bound if 0 events = {3 / n:.3f}; exact one-sided 95% upper if 0: {1 - 0.05 ** (1 / n):.3f}")
    p0 = 11 / 108   # as-is tail rate, a4_failures/verify/VERIFY.md F4
    # smallest p1 < p0 with power 0.8 for the one-sided exact test of H0: p = p0
    crit = max(k for k in range(n + 1) if stats.binom.cdf(k, n, p0) <= 0.05)
    p1 = next(p / 1000 for p in range(int(p0 * 1000), 0, -1) if stats.binom.cdf(crit, n, p / 1000) >= 0.8)
    print(f"   n={n}: H0 p = {p0:.3f} (as-is tail 11/108): reject if <= {crit} events (size {stats.binom.cdf(crit, n, p0):.3f});"
          f" power 0.8 reached at p1 = {p1:.3f}")
print("[4] pool B recurrence (24 new runs on 12 cells)")
for k in (0, 6, 12, 18, 24):
    lo = stats.beta.ppf(0.025, k, 24 - k + 1) if k > 0 else 0.0
    hi = stats.beta.ppf(0.975, k + 1, 24 - k) if k < 24 else 1.0
    print(f"   {k}/24 recurrences: Clopper-Pearson 95% [{lo:.3f}, {hi:.3f}]")
# distinguish rho = 0.9 (nearly deterministic bugs) from rho = 0.5, one-sided exact, n = 24
crit = max(k for k in range(25) if stats.binom.cdf(k, 24, 0.9) <= 0.05)
print(f"   H0 rho = 0.9: reject if <= {crit} recurrences; power at rho = 0.5: {stats.binom.cdf(crit, 24, 0.5):.3f}; at 0.7: {stats.binom.cdf(crit, 24, 0.7):.3f}")
print("[5] drift anchor: count of questions whose 2026-11-24/25 v2.17a run lies outside the range of its 3 new repeats;"
      " under exchangeability P(outside) = 0.5")
for n in (9, 10):
    crit = min(k for k in range(n + 1) if stats.binom.sf(k - 1, n, 0.5) <= 0.05)
    p1 = next(p / 100 for p in range(50, 101) if stats.binom.sf(crit - 1, n, p / 100) >= 0.8)
    print(f"   n={n}: reject if >= {crit} outside (size {stats.binom.sf(crit - 1, n, 0.5):.3f}); power 0.8 needs P(outside) >= {p1:.2f}")
print("[6] leak check: false STOP / EXCLUDE probabilities if the hosted model changed but knows nothing,"
      " per-question chance of a 'hit' q")
for q in (0.01, 0.02, 0.04, 0.06):
    b = stats.binom(23, q)
    print(f"   q={q:.2f}: P(H>=1) = {b.sf(0):.3f}  P(H>=2) = {b.sf(1):.3f}  P(H>=4) = {b.sf(3):.4f}")
print("[7] rare binary differences (catastrophic-rate reductions, rescue rates): exact sign-flip needs >= 6 questions with"
      " a non-zero difference, all in one direction, for two-sided p < 0.05 (2/2^6 = 0.031); 5 gives 0.0625")

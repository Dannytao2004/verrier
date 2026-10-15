| arm | n | median abs log10 err | within 1 OOM | fp_score | 80% coverage | failed | retried |
|---|---|---|---|---|---|---|---|
| naive | 20 | 1.10 | 45% | 0.439 | n/a | 1 | 1 |
| structured | 20 | 0.97 | 55% | 0.507 | 20% | 3 | 16 |

Both arms estimated: 16 questions; median abs log10 err naive 1.04, structured 0.79. Paired: structured better 12, equal 0, worse 8.

| id | unit | naive signed log10 err | structured signed log10 err | structured 80% covers | valid paths | path spread (OOM) | outlier paths | inputs (assumption/sourced_unverified/missing) | retries n/s |
|---|---|---|---|---|---|---|---|---|---|
| test:422 | (pure) | 1.07 | 0.55 | yes | 3 | 2.34 | p1 | 8/1/0 | 1/2 |
| test:288 | (pure) | 0.32 | no_valid_path | no | 0 | — | — | 11/0/0 | 1/2 |
| test:258 | J | 1.14 | 0.95 | no | 3 | 1.61 | p1 | 8/3/0 | 1/2 |
| test:35 | ft | 7.02 | no_valid_path | no | 0 | — | — | 11/0/0 | 1/2 |
| test:463 | km | invalid_output | 9.81 | no | 3 | 1.96 | p2 | 3/4/0 | 2/1 |
| test:494 | km | 2.76 | 0.63 | no | 3 | 0.36 | — | 5/1/0 | 1/1 |
| test:67 | (pure) | -9.78 | -0.94 | no | 3 | 1.30 | — | 12/1/0 | 1/2 |
| test:325 | (pure) | 0.90 | -1.90 | no | 3 | 0.35 | — | 14/1/0 | 1/2 |
| test:281 | (pure) | -0.70 | -0.64 | no | 2 | 0.00 | — | 5/5/0 | 1/2 |
| test:308 | (pure) | -1.00 | 0.58 | yes | 3 | 1.30 | p3 | 12/3/0 | 1/2 |
| test:496 | (pure) | 5.00 | 1.89 | no | 3 | 3.68 | p3 | 5/2/0 | 1/1 |
| test:80 | years | -0.07 | -0.01 | yes | 3 | 0.25 | — | 5/1/0 | 1/2 |
| test:169 | (pure) | -4.70 | -7.56 | no | 3 | 5.71 | p3 | 9/2/0 | 1/2 |
| test:172 | pounds | -0.05 | -0.49 | no | 3 | 0.06 | — | 7/1/0 | 1/2 |
| test:56 | cm | -0.53 | -0.47 | no | 2 | 0.01 | — | 12/0/0 | 1/2 |
| test:109 | kg*km**2*hour**-2 | 5.68 | 7.10 | no | 3 | 0.00 | — | 2/9/0 | 1/2 |
| test:306 | W | 17.59 | no_valid_path | no | 0 | — | — | 8/5/0 | 1/2 |
| test:54 | cm | 0.70 | 0.09 | yes | 2 | 0.64 | — | 10/2/0 | 1/2 |
| test:487 | (pure) | -2.44 | -1.48 | no | 3 | 0.00 | — | 9/0/0 | 1/1 |
| test:120 | ton | -0.98 | -0.98 | no | 3 | 0.00 | — | 7/0/0 | 1/2 |

| calls group | calls | ok | retry calls | prompt tokens | completion tokens | USD (est.) | median latency s | max latency s | finish_reason |
|---|---|---|---|---|---|---|---|---|---|
| naive | 21 | 19 | 1 | 4162 | 1269 | 0.0013 | 112.6 | 521.7 | {'stop': 19, 'length': 2} |
| structured | 36 | 36 | 16 | 55530 | 49649 | 0.0310 | 164.2 | 725.4 | {'stop': 36} |
| demo | 3 | 2 | 1 | 1788 | 2181 | 0.0015 | 77.2 | 900.8 | {'None': 1, 'stop': 2} |
| all | 60 | 57 | 18 | 61480 | 53099 | 0.0338 | 135.9 | 900.8 | {'None': 1, 'stop': 57, 'length': 2} |

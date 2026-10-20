# Evidence ledger: fc_googl_tokens_2026_q3

- Question: Assume today is 2026-10-19. You know nothing published after this date. Estimate the number of tokens per minute that Alphabet's first-party models (such as Gemini) process via direct API use by customers, as it will be first stated with Alphabet's third-quarter 2026 results (earnings press release or CEO earnings-call remarks); in Q2 2026 Alphabet stated this as 'Gemini models now process 22 billion API tokens per minute'. Answer in tokens per minute.
- as_of: 2026-10-19
- Pinned target: Number of tokens per minute that Alphabet's first-party models (primarily Gemini) process via direct API use by customers, as first publicly stated with Alphabet's third-quarter 2026 results (earnings press release or CEO earnings-call remarks). This is the run-rate/current-volume metric analogous t | unit tokens per minute | period 2026-07-01..2026-09-30 | publisher Alphabet Inc. (earnings press release and/or CEO earnings-call remarks)

## Directions and pages

### d1 [own_history] Alphabet investor-relations and earnings-call transcripts

Hypothesis: The Q3 2026 token/min figure will follow Alphabet's recent disclosed trajectory; the best direct input is the sequence of prior reported Gemini API token run-rates and their quarter-over-quarter growth, especially Q2 2026 = 22 billion tokens/min. The expected direction is continuation of strong growth, but the rate may decelerate as the base grows.

Queries issued by the searcher: Alphabet earnings call Gemini API tokens per minute billion; Google Q2 2026 earnings transcript Gemini tokens per minute 22 billion; Alphabet Q3 2025 earnings call Gemini models 7 billion tokens per minute up from; "tokens per minute" Gemini Q3 2026 Alphabet earnings call October 2026

- `https://www.gweb-uniblog-publish-prod.appspot.com/company-news/inside-google/message-ceo/alphabet-earnings-q2-2026/` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q1-2026/` -> **live_dated** (page date 2026-04-29); points raw/verified 2/1
  - p1 Alphabet first-party models (primarily Gemini) tokens processed per minute via d = **16,000,000,000** tokens per minute (2026-01-01..2026-03-31) [keep: ] quote: "Our first-party models now process more than 16 billion tokens per minute via direct API use by our customers, up from 10 billion last quarter."
- `https://techcrunch.com/2026/02/04/googles-gemini-app-has-surpassed-750m-monthly-active-users/` -> **live_dated** (page date 2026-02-04); points raw/verified 8/6
  - p2 Gemini monthly active users, Q4 2025 earnings disclosure = **750,000,000** monthly active users (2025-10-01..2025-12-31) [DISCARD: Consumer Gemini app MAU; target excludes consumer app and measures direct API tokens.] quote: "Google's AI chatbot Gemini has surpassed 750 million monthly active users (MAUs), according to the company's fourth-quarter 2025 earnings."
  - p3 Gemini monthly active users, prior quarter (Q3 2025) as reported last quarter = **650,000,000** monthly active users (2025-07-01..2025-09-30) [DISCARD: Consumer Gemini app MAU from prior quarter; not direct API tokens.] quote: "Last quarter, Google reported 650 million monthly active users for Gemini, indicating substantial growth in a short period."
  - p4 ChatGPT estimated monthly active users, late 2025 (comparable entity) = **810,000,000** monthly active users (2025-10-01..2025-12-31) [DISCARD: ChatGPT MAU is another entity's consumer metric and not a Gemini API token-volume input.] quote: "In comparison, ChatGPT is estimated to have around 810 million MAUs in late 2025."
  - p5 Alphabet annual revenue, first time surpassing (Q4 2025 quarter) = **400,000,000,000** USD annual revenue (2025-01-01..2025-12-31) [DISCARD: Alphabet annual revenue is irrelevant to token throughput.] quote: "The company has surpassed $400 billion in annual revenue for the first time this quarter."
  - p6 Alphabet first-party models (primarily Gemini) tokens processed per minute via d = **10,000,000,000** tokens per minute (2025-10-01..2025-12-31) [keep: ] quote: "Our first party models, like Gemini, now process over 10 billion tokens per minute via direct API use by our customers"
  - p7 Gemini App monthly active users, Q4 2025 (Pichai release quote) = **750,000,000** monthly active users (2025-10-01..2025-12-31) [DISCARD: Duplicate of p2 for Q4 2025 consumer Gemini app MAU.] quote: "the Gemini App has grown to over 750 million monthly active users."
- `https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q3-2025/` -> **live_dated** (page date 2025-10-29); points raw/verified 15/11
  - p8 Alphabet first-party models (primarily Gemini) tokens processed per minute via d = **7,000,000,000** tokens per minute (2025-07-01..2025-09-30) [keep: ] quote: "Our first-party models, like Gemini, now process 7 billion tokens per minute, via direct API use by our customers."
  - p9 Alphabet monthly tokens processed across all surfaces, as announced in July (sta = **980,000,000,000,000** tokens per month (2025-07-01..2025-07-31) [DISCARD: All-surface monthly tokens, not direct-API customer tokens; no reliable bridge.] quote: "In July, we announced that we processed 980 trillion monthly tokens across all our surfaces."
  - p10 Year-over-year growth multiple of Alphabet monthly tokens processed across all s = **20** multiple (year-over-year growth) (2024-10-01..2025-09-30) [DISCARD: All-surface token growth multiple, different scope from direct API.] quote: "We are now processing over 1.3 quadrillion monthly tokens, more than 20x growth in a year."
  - p11 Gemini app monthly active users, Q3 2025 = **650,000,000** monthly active users (2025-07-01..2025-09-30) [DISCARD: Consumer Gemini app MAU; not direct API tokens.] quote: "The Gemini app now has over 650 million monthly active users, and queries increased by 3x from Q2."
  - p12 Gemini app query growth multiple from Q2 to Q3 2025 = **3** multiple (quarter-over-quarter growth) (2025-07-01..2025-09-30) [DISCARD: Consumer Gemini app query growth; not API token volume.] quote: "The Gemini app now has over 650 million monthly active users, and queries increased by 3x from Q2."
  - p13 Google Cloud customers each processing approximately 1 trillion tokens with Alph = **150** customers (2024-10-01..2025-09-30) [DISCARD: Older customer token-threshold count; superseded by newer p33/p34 and non-binding.] quote: "Over the past 12 months, nearly 150 Google Cloud customers each processed approximately 1 trillion tokens with our models for a wide range of applications."
  - p14 Tokens processed per customer (approximately) over past 12 months by ~150 Google = **1,000,000,000,000** tokens per customer over 12 months (2024-10-01..2025-09-30) [DISCARD: Older per-customer token threshold; not aggregate API volume.] quote: "Over the past 12 months, nearly 150 Google Cloud customers each processed approximately 1 trillion tokens with our models for a wide range of applications."
  - p15 Google Cloud backlog, Q3 2025 = **155,000,000,000** USD (2025-07-01..2025-09-30) [DISCARD: Q3 2025 Cloud backlog; broad Cloud demand, not API tokens.] quote: "Cloud backlog grew 46% quarter over quarter $155 billion."
  - p16 Google Cloud backlog quarter-over-quarter growth, Q3 2025 = **46** % (2025-07-01..2025-09-30) [DISCARD: Cloud backlog growth; not API token volume.] quote: "Cloud backlog grew 46% quarter over quarter $155 billion."
  - p17 Alphabet quarterly revenue, Q3 2025 (first-ever $100 billion quarter) = **100,000,000,000** USD (2025-07-01..2025-09-30) [DISCARD: Historical quarterly revenue is not informative for API token/min.] quote: "We delivered our first-ever $100 billion quarter."
  - p18 Year-over-year growth of revenue from products built on Alphabet generative AI m = **200** % (2025-07-01..2025-09-30) [DISCARD: Q3 2025 gen-AI revenue growth; too old and not direct API token volume.] quote: "In Q3, revenue from products built on our generative AI models grew more than 200% year-over-year."
- dropped by code checks: 7 (period year 2025 does not appear in the page text or URL (likely mis-dated): 1; period_end missing or unparseable: 4; number: unknown scale word 'quadrillion': 1; period year 2020 does not appear in the page text or URL (likely mis-dated): 1)

### d2 [related_series] Google Cloud and AI infrastructure revenue / API pricing

Hypothesis: Token volume can be bounded by Google Cloud AI/API revenue divided by average revenue per token. If Cloud/AI revenue growth is known and API price per token is falling, token volume should grow faster than revenue; the relationship is target tokens/min ~ (API revenue run-rate)/(average price per token) with adjustments for free tier and mix.

Queries issued by the searcher: Alphabet third quarter 2026 results Gemini tokens per minute; Google Cloud Q2 2026 revenue Vertex AI Gemini API growth; "tokens per minute" Alphabet Q3 2026 earnings call Pichai Gemini; Alphabet Q3 2026 earnings date October 2026 Google Cloud revenue results

- `https://www.storagenewsletter.com/2026/08/03/alphabet-fiscal-2q26-financial-results/` -> **live_dated** (page date 2026-08-03); points raw/verified 14/13
  - p19 Gemini models API tokens processed per minute, as stated by Alphabet CEO (Q2 202 = **22,000,000,000** API tokens per minute (2026-04-01..2026-06-30) [keep: ] quote: "Gemini models now process 22 billion API tokens per minute and the Gemini App has 950 million monthly active users."
  - p20 Google Cloud revenues, Q2 2026 = **24,800,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "Google Cloud saw a meaningful acceleration in growth as revenues increased 82% to $24.8 billion"
  - p21 Google Cloud revenue growth year-over-year, Q2 2026 = **82** % (2026-04-01..2026-06-30) [keep: ] quote: "Google Cloud revenues accelerating to 82% growth, driven by demand for AI infrastructure and AI solutions"
  - p22 Consolidated Alphabet revenues, Q2 2026 = **119,800,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Consolidated Alphabet revenue; irrelevant to API token run-rate.] quote: "Consolidated Alphabet revenues increased 24%, or 23% in constant currency, to $119.8 billion"
  - p23 Consolidated Alphabet revenue growth year-over-year, Q2 2026 = **24** % (2026-04-01..2026-06-30) [DISCARD: Consolidated Alphabet revenue growth; irrelevant to API token run-rate.] quote: "Consolidated Alphabet revenues increased 24%, or 23% in constant currency, to $119.8 billion"
  - p24 Google Services revenues, Q2 2026 = **94,500,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Google Services revenue is too broad and not a token-volume measure.] quote: "Google Services revenues increased 15% to $94.5 billion"
  - p25 Google Services revenue growth year-over-year, Q2 2026 = **15** % (2026-04-01..2026-06-30) [DISCARD: Google Services growth is not a token-volume measure.] quote: "Google Services revenues increased 15% to $94.5 billion"
  - p26 Google Search & other revenue growth year-over-year, Q2 2026 = **17** % (2026-04-01..2026-06-30) [DISCARD: Search revenue growth is unrelated to direct API token volume.] quote: "led by 17% growth in Google Search & other"
  - p27 YouTube ads revenue growth year-over-year, Q2 2026 = **13** % (2026-04-01..2026-06-30) [DISCARD: YouTube ads growth is unrelated to direct API token volume.] quote: "and 13% in YouTube ads"
  - p28 Consolidated Alphabet operating margin, Q2 2026 = **34** % (2026-04-01..2026-06-30) [DISCARD: Operating margin is irrelevant to token throughput.] quote: "operating margin expanded by 2 percentage points to 34%"
  - p29 Share of Fortune 100 using Gemini Enterprise = **90** % (2026-04-01..2026-06-30) [DISCARD: Gemini Enterprise Fortune 100 adoption; different product and not token volume.] quote: "It's great to see wide adoption of Gemini Enterprise, with nearly 90% of the Fortune 100 using it."
  - p30 Gemini App monthly active users = **950,000,000** monthly active users (2026-04-01..2026-06-30) [DISCARD: Consumer Gemini app MAU; target is direct API.] quote: "the Gemini App has 950 million monthly active users"
  - p31 Alphabet EPS, Q2 2026 = **9.11** USD per share (2026-04-01..2026-06-30) [DISCARD: EPS is irrelevant to token throughput.] quote: "EPS increased 294% to $9.11"
- `https://finance.yahoo.com/video/inside-alphabets-earnings-call-with-google-ceo-sundar-pichai-223755892.html` -> **live_dated** (page date 2026-07-22); points raw/verified 15/0
- `https://aichip001.com/p/578778.html` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://seekingalpha.com/news/4547409-alphabet-earnings-key-takeaways-amid-earnings-beat-sharp-rise-in-2026-spending` -> **dropped** (live http 403); points raw/verified -/-
- dropped by code checks: 16 (period_end missing or unparseable: 16)

### d3 [base_rates] Comparable LLM API providers and enterprise AI adoption

Hypothesis: Alphabet's direct API token growth should roughly track overall enterprise LLM API token growth, adjusted for Gemini market-share gains or losses. Comparable disclosures from OpenAI, Anthropic, Microsoft/Azure, or enterprise LLM API surveys provide a base growth rate to apply to the Q2 2026 anchor.

Queries issued by the searcher: Google Gemini tokens per minute processed earnings call 2026; Alphabet Q2 2026 earnings call Gemini tokens per minute; OpenAI tokens per minute platform API 2026 growth disclosure; Anthropic API token volume growth 2026 tokens per day

- `https://openai.com/index/accelerating-the-next-phase-ai/` -> **dropped** (live http 403); points raw/verified -/-
- `https://www.gweb-uniblog-publish-prod.appspot.com/company-news/inside-google/message-ceo/alphabet-earnings-q2-2026/` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q1-2026/` -> **live_dated** (page date 2026-04-29); points raw/verified 15/14
  - p32 Alphabet first-party models (primarily Gemini) tokens processed per minute via d = **16,000,000,000** tokens per minute (2026-01-01..2026-03-31) [DISCARD: Redundant copy of the Q1 2026 16B/min disclosure already captured by p1.] quote: "Our first-party models now process more than 16 billion tokens per minute via direct API use by our customers, up from 10 billion last quarter."
  - p33 Google Cloud customers processing over 1 trillion tokens each, past twelve month = **330** Google Cloud customers (2025-04-01..2026-03-31) [keep: ] quote: "Over the past twelve months, 330 Google Cloud customers each processed over 1 trillion tokens."
  - p34 Google Cloud customers reaching the 10-trillion-token milestone, past twelve mon = **35** as written "Thirty-five", value check pending Google Cloud customers (2025-04-01..2026-03-31) [keep: ] quote: "Thirty-five reached the 10-trillion-token milestone."
  - p35 Gemini Enterprise paid monthly active users growth quarter-over-quarter, Q1 2026 = **40** % (2026-01-01..2026-03-31) [DISCARD: Gemini Enterprise paid MAU growth; different product, not API tokens.] quote: "Gemini Enterprise is seeing tremendous momentum, with 40% growth quarter-over-quarter in paid monthly active users."
  - p36 Google Cloud revenue growth year-over-year, Q1 2026 = **63** % (2026-01-01..2026-03-31) [keep: ] quote: "Revenue grew 63%, exceeding $20 billion for the first time, and our backlog nearly doubled quarter-on-quarter to over $460 billion."
  - p37 Google Cloud revenue, Q1 2026 (exceeded threshold) = **20,000,000,000** USD (2026-01-01..2026-03-31) [DISCARD: Cloud revenue threshold ('exceeded $20B') is imprecise and not an API token measure.] quote: "Revenue grew 63%, exceeding $20 billion for the first time, and our backlog nearly doubled quarter-on-quarter to over $460 billion."
  - p38 Google Cloud backlog, Q1 2026 (over) = **460,000,000,000** USD (2026-01-01..2026-03-31) [DISCARD: Older Cloud backlog; superseded by p57 and not a token measure.] quote: "Revenue grew 63%, exceeding $20 billion for the first time, and our backlog nearly doubled quarter-on-quarter to over $460 billion."
  - p39 Revenue from products built on Google gen AI models growth year-over-year, Q1 20 = **800** % (2026-01-01..2026-03-31) [DISCARD: Gen-AI revenue growth; not direct API token volume.] quote: "In Q1, revenue from products built on our gen AI models grew nearly 800% year-over-year."
  - p40 Gemini-powered workflows in BigQuery growth year-over-year = **30** multiple year-over-year growth (..) [DISCARD: BigQuery Gemini workflow growth; different product.] quote: "Our strength with BigQuery and Gemini Enterprise has led Gemini-powered workflows in BigQuery to grow over 30X year-over-year."
  - p41 Growth in seats sold with partners for Gemini Enterprise, year-over-year, Q1 202 = **9** multiple year-over-year growth (2026-01-01..2026-03-31) [DISCARD: Gemini Enterprise partner seats; different product.] quote: "We saw 9x year-over-year growth both in seats sold with partners, and in the number of partners adopting it for internal use."
  - p42 New customer acquisition growth compared to same period last year, Q1 2026 = **2** as written "doubling", value check pending multiple growth in new customer acquisition (2026-01-01..2026-03-31) [DISCARD: New customer acquisition growth; not token volume.] quote: "Winning new customers faster, with new customer acquisition doubling compared to the same period last year."
  - p43 Customers outpacing initial commitments, Q1 2026 = **45** % (2026-01-01..2026-03-31) [DISCARD: Customers outpacing commitments; not token volume.] quote: "And we are deepening relationships with existing customers, with customers outpaced their initial commitments by 45%, accelerating over last quarter."
  - p44 Reduction in cost of core AI responses since upgrading AI Overviews and AI Mode  = **30** % (..) [DISCARD: Cost reduction for core AI responses; not API token volume.] quote: "since upgrading AI Overviews and AI Mode to Gemini 3, we've reduced the cost of core AI responses by more than 30%"
  - p45 Total paid subscriptions across Alphabet, Q1 2026 = **350,000,000** paid subscriptions (2026-01-01..2026-03-31) [DISCARD: Paid subscription count is unrelated to API token volume.] quote: "Overall the number of paid subscriptions has now reached 350 million, with YouTube and Google One being the key drivers."
- `https://www.digitaltoday.co.kr/jp/view/47931/gpu-fees-jump-usage-limits-ai-computing-resource-depletion-side-effects-worsen` -> **live_dated** (page date 2026-04-15); points raw/verified 4/4
  - p46 OpenAI API token usage per minute, October 2025 = **6,000,000,000** tokens per minute (2025-10-01..2025-10-31) [keep: ] quote: "OpenAIのAPI経由のトークン使用量は、2025年10月の毎分60億から、2026年3月末には毎分150億へ増加した。"
  - p47 OpenAI API token usage per minute, end of March 2026 = **15,000,000,000** tokens per minute (2026-03-01..2026-03-31) [keep: ] quote: "OpenAIのAPI経由のトークン使用量は、2025年10月の毎分60億から、2026年3月末には毎分150億へ増加した。"
  - p48 CoreWeave price increase at end of 2025 = **20** % (2025-10-01..2025-12-31) [DISCARD: CoreWeave price increase is third-party compute-cost context, not an Alphabet API usage observation.] quote: "AI特化型クラウドのCoreWeaveは2025年末、価格を20%超引き上げた。"
  - p49 NVIDIA Blackwell GPU hourly spot price increase over two months = **48** % (..) [DISCARD: GPU spot-price increase is compute-cost context, not a direct token-volume observation.] quote: "NVIDIAの最新Blackwellチップの時間単価は、2カ月前に比べ48%上昇した。"
- dropped by code checks: 1 (period year 2025 does not appear in the page text or URL (likely mis-dated): 1)

### d4 [capacity_consumption] AI infrastructure capacity planner / TPU fleet

Hypothesis: External Gemini API tokens/min is constrained by deployed inference compute allocated to first-party model serving: tokens/min ~ deployed accelerators × tokens/s per accelerator × utilization × 60, multiplied by the share of capacity allocated to direct API customers. Capex and TPU deployment estimates can bound the possible run-rate.

Queries issued by the searcher: Alphabet Q3 2025 earnings call Gemini API tokens per minute Pichai; Alphabet 2026 capex guidance AI infrastructure TPU fleet size estimate; Gemini inference tokens per second per TPU benchmark Ironwood throughput; Google TPU shipments 2026 million units estimate 2025 2.5 million TrendForce

- `https://newsletter.semianalysis.com/p/tpu-inferencex-full-steam` -> **live_dated** (page date 2026-09-07); points raw/verified 15/1
  - p50 Anthropic committed TPU count (over one million, Nov 2025 commitment) = **1,000,000** as written "one million", value check pending TPUs (2025-11-01..2025-11-30) [DISCARD: Anthropic TPU commitment is another entity's capacity commitment, not Alphabet direct API usage.] quote: "In November 2025, we already said that Anthropic loves TPUs and committed to over one million of them (around 400k+ in direct purchases and 600k+ rented through GCP)"
- `https://m.163.com/dy/article/L2I2SH2H05568W0A.html` -> **live_dated** (page date 2026-07-23); points raw/verified 15/7
  - p51 Gemini model API tokens processed per minute (current quarter, as stated in Q2 r = **22,000,000,000** tokens per minute (2026-04-01..2026-06-30) [DISCARD: Redundant copy of the Q2 2026 22B/min disclosure already captured by p19.] quote: "Gemini 模型 API 每分钟处理约 220 亿个 Token,高于上一季度的 160 亿。"
  - p52 Gemini model API tokens processed per minute (prior quarter) = **16,000,000,000** tokens per minute (2026-01-01..2026-03-31) [DISCARD: Redundant copy of the Q1 2026 16B/min disclosure already captured by p1.] quote: "Gemini 模型 API 每分钟处理约 220 亿个 Token,高于上一季度的 160 亿。"
  - p53 Alphabet Q2 capex = **44,900,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate of Q2 capex in p58; p58 also provides the capex mix.] quote: "Alphabet 第二季度资本开支达到 449 亿美元,同比接近翻倍"
  - p54 Alphabet Q1 capex = **35,700,000,000** USD (2026-01-01..2026-03-31) [keep: ] quote: "加上一季度的 357 亿美元,上半年已经投入约 806 亿美元"
  - p55 Alphabet H1 2026 capex total = **80,600,000,000** USD (2026-01-01..2026-06-30) [keep: ] quote: "加上一季度的 357 亿美元,上半年已经投入约 806 亿美元"
  - p56 Google Cloud Q2 revenue = **24,800,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Duplicate of Google Cloud Q2 revenue in p20.] quote: "第二季度 Google Cloud 收入达到 248 亿美元,同比增长 82%,远高于市场预期;订单积压达到 5140 亿美元。"
  - p57 Google Cloud backlog = **514,000,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "第二季度 Google Cloud 收入达到 248 亿美元,同比增长 82%,远高于市场预期;订单积压达到 5140 亿美元。"
- `https://valueaddvc.com/blog/google-tpu-vs-nvidia-capex-split-2026` -> **live_dated** (page date 2026-09-29); points raw/verified 15/4
  - p58 Alphabet Q2 2026 actual capex = **44,900,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "Q2 2026 capex alone came in at $44.9 billion, split roughly 60% servers and 40% data centers and networking"
  - p59 Alphabet Q2 2026 capex mix: servers share = **60** % (2026-04-01..2026-06-30) [keep: ] quote: "split roughly 60% servers and 40% data centers and networking"
  - p60 Google TPU-only owned compute capacity, Q4 2025, Epoch AI estimate range = **3,800,000** (range 3,100,000..4,500,000) as written "3.1 million to 4.5 million", value check ok Nvidia-H100-equivalents (2025-10-01..2025-12-31) [keep: ] quote: "Epoch AI puts the TPU-only share at 3.1 million to 4.5 million H100-equivalents, a range that centers on close to 80% of Google's total owned compute."
  - p61 Google Nvidia GPU owned compute capacity, Q4 2025, implied estimate = **1,000,000** Nvidia-H100-equivalents (2025-10-01..2025-12-31) [keep: ] quote: "That implies the remaining fifth, call it roughly 1 million H100-equivalents, runs on Nvidia silicon."
- `https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q3-2025/` -> **live_dated** (page date 2025-10-29); points raw/verified 15/11
  - p62 First-party models (primarily Gemini) tokens processed per minute via direct API = **7,000,000,000** tokens per minute (2025-07-01..2025-09-30) [DISCARD: Duplicate of Q3 2025 7B/min in p8.] quote: "Our first-party models, like Gemini, now process 7 billion tokens per minute, via direct API use by our customers."
  - p63 Total monthly tokens processed across all Google surfaces, as announced in July  = **980,000,000,000,000** tokens per month (2025-07-01..2025-07-31) [DISCARD: Duplicate of all-surface token volume in p9.] quote: "In July, we announced that we processed 980 trillion monthly tokens across all our surfaces."
  - p64 Year-over-year growth multiple in total monthly tokens processed across all surf = **20** multiple (year-over-year growth) (2025-07-01..2025-09-30) [DISCARD: Duplicate of all-surface token growth in p10.] quote: "We are now processing over 1.3 quadrillion monthly tokens, more than 20x growth in a year."
  - p65 Google Cloud customers that each processed approximately 1 trillion tokens with  = **150** Google Cloud customers (2024-10-01..2025-09-30) [DISCARD: Duplicate of customer token milestone in p13.] quote: "Over the past 12 months, nearly 150 Google Cloud customers each processed approximately 1 trillion tokens with our models for a wide range of applications."
  - p66 Tokens processed per customer (each of ~150 Google Cloud customers) over past 12 = **1,000,000,000,000** tokens per customer over 12 months (2024-10-01..2025-09-30) [DISCARD: Duplicate of per-customer token estimate in p14.] quote: "Over the past 12 months, nearly 150 Google Cloud customers each processed approximately 1 trillion tokens with our models for a wide range of applications."
  - p67 Gemini app monthly active users = **650,000,000** monthly active users (2025-07-01..2025-09-30) [DISCARD: Duplicate of Gemini app MAU in p11.] quote: "The Gemini app now has over 650 million monthly active users, and queries increased by 3x from Q2."
  - p68 Gemini app query growth multiple from Q2 to Q3 = **3** multiple (quarter-over-quarter growth) (2025-07-01..2025-09-30) [DISCARD: Duplicate of Gemini app query growth in p12.] quote: "The Gemini app now has over 650 million monthly active users, and queries increased by 3x from Q2."
  - p69 Google Cloud backlog, quarter over quarter growth = **46** % (2025-07-01..2025-09-30) [DISCARD: Duplicate of Cloud backlog growth in p16.] quote: "Cloud backlog grew 46% quarter over quarter $155 billion."
  - p70 Google Cloud backlog level = **155,000,000,000** USD (2025-07-01..2025-09-30) [DISCARD: Duplicate of Cloud backlog level in p15.] quote: "Cloud backlog grew 46% quarter over quarter $155 billion."
  - p71 Quarterly revenue, first-ever $100 billion quarter = **100,000,000,000** USD (2025-07-01..2025-09-30) [DISCARD: Duplicate of quarterly revenue in p17.] quote: "We delivered our first-ever $100 billion quarter."
  - p72 Year-over-year growth in revenue from products built on Google generative AI mod = **200** % (2025-07-01..2025-09-30) [DISCARD: Duplicate of generative-AI revenue growth in p18.] quote: "In Q3, revenue from products built on our generative AI models grew more than 200% year-over-year."
- dropped by code checks: 37 (period_end missing or unparseable: 12; scale word 'thousand' not supported by quote or table header: 4; period_end 2026-12-31 after as_of: 13; period_end 2028-12-31 after as_of: 2; scale word 'billion' not supported by quote or table header: 1; value_as_written not in quote as a whole number: 2; period_end 2027-12-31 after as_of: 1; number: unknown scale word 'quadrillion': 1; period year 2020 does not appear in the page text or URL (likely mis-dated): 1)

### d5 [persona] Developer/enterprise customer base and usage distribution

Hypothesis: Target tokens/min can be decomposed as active direct API customers × average tokens/min per active customer, or developer accounts × integration intensity. Growth in Vertex AI/Gemini API customer counts and agentic workloads should raise average usage per customer.

Queries issued by the searcher: Vertex AI customers 2026 Gemini API developers; Alphabet Q2 2026 earnings call tokens per minute Gemini API; Alphabet Q1 2026 earnings call Pichai "16 billion tokens per minute" developers; Google Cloud number of Vertex AI customers 2026 "customers" generative AI

- `https://www.gweb-uniblog-publish-prod.appspot.com/company-news/inside-google/message-ceo/alphabet-earnings-q2-2026/` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q1-2026/` -> **live_dated** (page date 2026-04-29); points raw/verified 15/12
  - p73 Alphabet first-party models tokens processed per minute via direct API use by cu = **16,000,000,000** tokens per minute (2026-01-01..2026-03-31) [DISCARD: Redundant copy of Q1 2026 16B/min in p1.] quote: "Our first-party models now process more than 16 billion tokens per minute via direct API use by our customers, up from 10 billion last quarter."
  - p74 Google Cloud customers processing over 1 trillion tokens each, trailing twelve m = **330** customers (2025-04-01..2026-03-31) [DISCARD: Duplicate of 330-customer milestone in p33.] quote: "Over the past twelve months, 330 Google Cloud customers each processed over 1 trillion tokens."
  - p75 Google Cloud customers reaching 10-trillion-token milestone, trailing twelve mon = **35** as written "Thirty-five", value check pending customers (2025-04-01..2026-03-31) [DISCARD: Duplicate of 35-customer 10T-token milestone in p34.] quote: "Thirty-five reached the 10-trillion-token milestone."
  - p76 Gemini Enterprise paid monthly active users growth quarter-over-quarter, Q1 2026 = **40** % (2026-01-01..2026-03-31) [DISCARD: Duplicate of Gemini Enterprise paid MAU growth in p35.] quote: "Gemini Enterprise is seeing tremendous momentum, with 40% growth quarter-over-quarter in paid monthly active users."
  - p77 Google Cloud revenue growth year-over-year, Q1 2026 = **63** % (2026-01-01..2026-03-31) [DISCARD: Duplicate of Cloud Q1 growth in p36.] quote: "Revenue grew 63%, exceeding $20 billion for the first time, and our backlog nearly doubled quarter-on-quarter to over $460 billion."
  - p78 Google Cloud quarterly revenue threshold exceeded, Q1 2026 = **20,000,000,000** USD (2026-01-01..2026-03-31) [DISCARD: Duplicate of Cloud Q1 revenue in p37.] quote: "Revenue grew 63%, exceeding $20 billion for the first time, and our backlog nearly doubled quarter-on-quarter to over $460 billion."
  - p79 Google Cloud backlog, Q1 2026 = **460,000,000,000** USD (2026-01-01..2026-03-31) [DISCARD: Duplicate of Cloud backlog in p38.] quote: "Revenue grew 63%, exceeding $20 billion for the first time, and our backlog nearly doubled quarter-on-quarter to over $460 billion."
  - p80 Existing Google Cloud customers outpacing initial commitments, Q1 2026 = **45** % (2026-01-01..2026-03-31) [DISCARD: Duplicate of commitment-outperformance share in p43.] quote: "And we are deepening relationships with existing customers, with customers outpaced their initial commitments by 45%, accelerating over last quarter."
  - p81 Revenue growth from products built on Google gen AI models year-over-year, Q1 20 = **800** % (2026-01-01..2026-03-31) [DISCARD: Duplicate of generative-AI revenue growth in p39.] quote: "In Q1, revenue from products built on our gen AI models grew nearly 800% year-over-year."
  - p82 Gemini Enterprise seats sold with partners growth year-over-year, Q1 2026 = **9** multiple (seats sold with partners) (2026-01-01..2026-03-31) [DISCARD: Duplicate of Gemini Enterprise seat growth in p41.] quote: "We saw 9x year-over-year growth both in seats sold with partners, and in the number of partners adopting it for internal use."
  - p83 Gemini-powered workflows in BigQuery growth year-over-year, Q1 2026 = **30** multiple (workflows) (2026-01-01..2026-03-31) [DISCARD: Duplicate of BigQuery Gemini workflow growth in p40.] quote: "Our strength with BigQuery and Gemini Enterprise has led Gemini-powered workflows in BigQuery to grow over 30X year-over-year."
  - p84 Alphabet total paid subscriptions, Q1 2026 = **350,000,000** paid subscriptions (2026-01-01..2026-03-31) [DISCARD: Duplicate of paid subscriptions in p45.] quote: "Overall the number of paid subscriptions has now reached 350 million, with YouTube and Google One being the key drivers."
- `https://www.constellationr.com/insights/news/google-cloud-revenue-growth-hits-63-q1-20-billion` -> **live_dated** (page date 2026-04-29); points raw/verified 15/13
  - p85 Alphabet first-party models (Gemini) tokens processed per minute via direct API  = **16,000,000,000** tokens per minute (2026-01-01..2026-03-31) [DISCARD: Redundant copy of Q1 2026 16B/min in p1; p86 already preserves the growth statement.] quote: "Our first-party models, like Gemini, are now processing more than 16 billion tokens per minute via direct API use by our customers, up 60% from last quarter."
  - p86 Quarter-on-quarter growth in tokens per minute processed via direct API use by c = **60** % (2026-01-01..2026-03-31) [keep: ] quote: "up 60% from last quarter."
  - p87 Gemini Enterprise paid monthly active users quarter-on-quarter growth, Q1 2026 = **40** % (2026-01-01..2026-03-31) [DISCARD: Duplicate of Gemini Enterprise paid MAU growth in p35.] quote: "Gemini Enterprise has great momentum with 40% quarter on quarter growth in paid monthly active users"
  - p88 Google Cloud revenue growth, Q1 2026 = **63** % (2026-01-01..2026-03-31) [DISCARD: Duplicate of Cloud Q1 growth in p36.] quote: "Google Cloud revenue growth hits 63% in Q1 to $20 billion"
  - p89 Google Cloud revenue, Q1 2026 = **20,000,000,000** USD (2026-01-01..2026-03-31) [DISCARD: Duplicate of Cloud Q1 revenue in p37.] quote: "Google Cloud appears to be gaining share as its revenue growth surged 63% in the first quarter to $20 billion."
  - p90 Google Cloud operating income, Q1 2026 = **6,600,000,000** USD (2026-01-01..2026-03-31) [DISCARD: Cloud operating income is not a token-volume measure.] quote: "Google Cloud delivered operating income of $6.6 billion, well ahead of last year's tally."
  - p91 Google Cloud backlog, Q1 2026 = **460,000,000,000** USD (2026-01-01..2026-03-31) [DISCARD: Duplicate of Cloud backlog in p38.] quote: "Google Cloud backlog doubled to over $460 billion."
  - p92 Alphabet paid subscriptions, Q1 2026 = **350,000,000** subscriptions (2026-01-01..2026-03-31) [DISCARD: Duplicate of paid subscriptions in p45.] quote: "Paid subscriptions are now 350 million driven by YouTube and Google one."
  - p93 Alphabet net income, Q1 2026 = **62,600,000,000** USD (2026-01-01..2026-03-31) [DISCARD: Net income is irrelevant to token throughput.] quote: "The company overall reported first quarter net income of $62.6 billion, or $5.11 a share, on revenue of $109.9 billion, up 22% from a year ago."
  - p94 Alphabet revenue, Q1 2026 = **109,900,000,000** USD (2026-01-01..2026-03-31) [DISCARD: Alphabet revenue is not a token-volume measure.] quote: "on revenue of $109.9 billion, up 22% from a year ago."
  - p95 Alphabet revenue growth year over year, Q1 2026 = **22** % (2026-01-01..2026-03-31) [DISCARD: Alphabet revenue growth is not a token-volume measure.] quote: "on revenue of $109.9 billion, up 22% from a year ago."
  - p96 Google Services operating income, Q1 2026 = **40,590,000,000** USD (2026-01-01..2026-03-31) [DISCARD: Google Services operating income is irrelevant to token throughput.] quote: "Alphabet said Google Services delivered operating income of $40.59 billion, which led to overall results."
  - p97 Waymo fully autonomous rides per week, Q1 2026 = **50,000** as written "500,00", value check pending rides per week (2026-01-01..2026-03-31) [DISCARD: Waymo ride volume is unrelated to Gemini API token usage.] quote: "Waymo topped 500,00 fully autonomous rides a week."
- `https://tekninjas.com/blogs/google-cloud-next-26-agentic-enterprise-roundup/` -> **live_dated** (page date 2026-05-04); points raw/verified 15/0
- dropped by code checks: 20 (period year 2025 does not appear in the page text or URL (likely mis-dated): 1; number: no number in value_as_written: 2; period_end 2026-12-31 after as_of: 2; period year 2026 does not appear in the page text or URL (likely mis-dated): 8; period_end missing or unparseable: 7)

### d6 [shocks] Product launches, pricing, and API policy changes in Q3 2026

Hypothesis: Gemini model releases, price cuts, larger context windows, agentic API features, and free-tier/rate-limit changes between Q2 and the Q3 2026 earnings call can create step changes in token volume. The expected direction is positive for launches and price cuts, but the timing within the quarter matters.

Queries issued by the searcher: Alphabet Q2 2026 earnings call tokens per minute Gemini; Gemini API pricing change 2026; Alphabet third quarter 2026 results conference call date October 2026; Gemini 3.7 Flash launch August 2026 Google blog announcement

- `https://www.gweb-uniblog-publish-prod.appspot.com/company-news/inside-google/message-ceo/alphabet-earnings-q2-2026/` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://abc.xyz/investor/news/news-details/2026/Alphabet-Announces-Date-of-Third-Quarter-2026-Financial-Results-Conference-Call-2026-8tpGZsLS6v/defaul` -> **live_dated** (page date 2026-10-06); points raw/verified 0/0
- `https://benchlm.ai/google/api-pricing` -> **live_dated** (page date 2026-10-19); points raw/verified 15/2
  - p98 Gemini 4 Argon input price per million tokens = **2** USD per million input tokens (2026-09-30..2026-09-30) [keep: ] quote: "\| Gemini 4 Argon \| gemini-4-argonCurrent \| $2 \| $0.1 \| $10 \| $1 \| $5 \| 1M \| September 30, 2026 \| Google Gemini API pricing \|"
  - p99 Gemini 4 Argon output price per million tokens = **10** USD per million output tokens (2026-09-30..2026-09-30) [keep: ] quote: "\| Gemini 4 Argon \| gemini-4-argonCurrent \| $2 \| $0.1 \| $10 \| $1 \| $5 \| 1M \| September 30, 2026 \| Google Gemini API pricing \|"
- `https://docs.litellm.ai/blog/gemini-4-argon` -> **live_dated** (page date 2026-10-13); points raw/verified 15/0
- dropped by code checks: 28 (period_end 2026-12-31 after as_of: 2; number: more than one number in value_as_written: 3; period_end missing or unparseable: 15; period_end 2026-11-30 after as_of: 4; period_end 2026-12-01 after as_of: 3; scale word 'million' not supported by quote or table header: 1)

### d7 [attention] Developer attention and SDK adoption signals

Hypothesis: Developer activity around Gemini API—documentation traffic, SDK downloads, GitHub usage, and Stack Overflow questions—correlates with API integration and token growth. This is a leading/context indicator and needs a bridge to token volume, so it should mainly constrain direction rather than level.

Queries issued by the searcher: google-genai PyPI downloads 2026; Alphabet third quarter 2026 results tokens per minute Gemini; Alphabet Q3 2026 earnings call "tokens per minute" Gemini Sundar Pichai October 2026; google-genai PyPI downloads September 2026 monthly

- `https://finance.yahoo.com/video/inside-alphabets-earnings-call-with-google-ceo-sundar-pichai-223755892.html` -> **live_dated** (page date 2026-07-22); points raw/verified 15/0
- `https://presenc.ai/research/ai-sdk-download-rankings-2026` -> **live_dated** (page date 2026-05-14); points raw/verified 15/10
  - p100 PyPI monthly downloads for google-genai (Google Gen AI Python SDK), 30-day rolli = **216,729,048** downloads per month (2026-04-14..2026-05-14) [keep: ] quote: "\| google-genai \| \| 216,729,048 \| (rate-limited) \|"
  - p101 npm monthly downloads for @google/genai (Google Gen AI JS SDK), last-month windo = **45,811,559** downloads per month (2026-04-14..2026-05-14) [keep: ] quote: "\| @google/genai \| \| 45,811,559 \|"
  - p102 npm monthly downloads for @google/generative-ai (Google legacy SDK), last-month  = **12,223,790** downloads per month (2026-04-14..2026-05-14) [keep: ] quote: "\| @google/generative-ai \| Google (legacy SDK) \| 12,223,790 \|"
  - p103 npm monthly downloads for @ai-sdk/google (Vercel AI SDK Google provider), last-m = **16,840,727** downloads per month (2026-04-14..2026-05-14) [keep: ] quote: "\| @ai-sdk/google \| Vercel AI SDK (Google provider) \| 16,840,727 \|"
  - p104 PyPI monthly downloads for openai Python SDK, 30-day rolling window as of May 14 = **295,890,968** downloads per month (2026-04-14..2026-05-14) [keep: ] quote: "\| openai \| OpenAI \| 295,890,968 \| 71,743,491 \|"
  - p105 PyPI monthly downloads for anthropic Python SDK, 30-day rolling window as of May = **119,776,565** downloads per month (2026-04-14..2026-05-14) [keep: ] quote: "\| anthropic \| Anthropic \| 119,776,565 \| 28,829,540 \|"
  - p106 PyPI monthly downloads for litellm multi-vendor proxy, 30-day rolling window as  = **417,813,970** downloads per month (2026-04-14..2026-05-14) [DISCARD: Litellm multi-vendor proxy downloads; not a Gemini-specific aggregate indicator.] quote: "\| litellm \| BerriAI (multi-vendor proxy) \| 417,813,970 \| 114,389,012 \|"
  - p107 Stated PyPI OpenAI vs Anthropic monthly download gap multiple = **2.5** multiple (OpenAI PyPI downloads per Anthropic PyPI download) (2026-04-14..2026-05-14) [DISCARD: OpenAI versus Anthropic PyPI download gap; not Gemini token volume.] quote: "PyPI: 296M vs 120M (a ~2.5x gap)."
  - p108 Stated npm OpenAI vs Anthropic monthly download gap multiple = **1.2** multiple (OpenAI npm downloads per Anthropic npm download) (2026-04-14..2026-05-14) [DISCARD: OpenAI versus Anthropic npm download gap; not Gemini token volume.] quote: "npm: 84M vs 72M (a ~1.2x gap)."
  - p109 Stated ratio of Ollama Python PyPI monthly downloads to Ollama npm monthly downl = **5.5** multiple (Ollama PyPI downloads per Ollama npm download) (2026-04-14..2026-05-14) [DISCARD: Ollama Python/npm download ratio; unrelated to Gemini API volume.] quote: "Ollama JS lags Ollama Python by 5.5x. 12M PyPI vs 2.2M npm."
- `https://pypistats.org/packages/google-genai` -> **live_dated** (page date 2026-05-02); points raw/verified 4/0
- `https://coinstats.app/news/4cd15e388df005bc846a9761727e159d48de83f0b20fcd5010ad1bbf73d050bd_Alphabet-stock-rose-more-than-4%25-after-reporting-Q3-earn` -> **live_dated** (page date 2025-10-29); points raw/verified 14/0
- dropped by code checks: 38 (period year 2026 does not appear in the page text or URL (likely mis-dated): 20; period_end missing or unparseable: 11; scale word 'million' not supported by quote or table header: 3; number: no number in value_as_written: 1; number: more than one number in value_as_written: 1; period year 2025 does not appear in the page text or URL (likely mis-dated): 2)

### d8 [forecasts_markets] Sell-side analysts and prediction markets

Hypothesis: Analyst notes or prediction markets before the Q3 2026 release may publish or imply a Gemini API token run-rate estimate. If available, they provide an independent forecast to compare with trend extrapolation, though they may share the same underlying Alphabet disclosures.

Queries issued by the searcher: Gemini API tokens per minute forecast 2026; Alphabet Q3 2026 Gemini token volume analyst estimate; Alphabet third quarter 2026 earnings Gemini tokens per minute; "tokens per minute" Gemini API Alphabet earnings call 2026; Google Gemini "billion tokens per minute" 2026; Alphabet Q2 2026 earnings Gemini tokens processed run-rate

- `https://huggingface.co/api/resolve-cache/spaces/amanefjt/p2workflowy/186fdf6a7e73d1f2fe6358622dd6bbb0784ac994/docs%2Fgemini_models.md?download=true&et` -> **dropped** (live page has no readable date); points raw/verified -/-
- `https://devtk.ai/en/blog/ai-api-rate-limits-comparison-2026/` -> **live_dated** (page date 2026-08-17); points raw/verified 15/14
  - p110 Gemini 2.5 Pro Tier 1 baseline input TPM (published preset) = **2,000,000** input tokens per minute (2026-07-14..2026-07-14) [DISCARD: Per-project Gemini 2.5 Pro TPM preset; not aggregate customer volume.] quote: "\| Tier 1 (2.5 Pro) \| 150 \| 2,000,000 input TPM \| 10,000 \|"
  - p111 Gemini 2.5 Flash Tier 1 baseline input TPM (published preset) = **1,000,000** input tokens per minute (2026-07-14..2026-07-14) [DISCARD: Per-project Gemini 2.5 Flash TPM preset; not aggregate customer volume.] quote: "\| Tier 1 (2.5 Flash) \| 1,000 \| 1,000,000 input TPM \| 10,000 \|"
  - p112 Gemini 2.5 Flash-Lite Tier 1 baseline input TPM (published preset) = **4,000,000** input tokens per minute (2026-07-14..2026-07-14) [DISCARD: Per-project Gemini 2.5 Flash-Lite TPM preset; not aggregate customer volume.] quote: "\| Tier 1 (2.5 Flash-Lite) \| 4,000 \| 4,000,000 input TPM \| Check AI Studio \|"
  - p113 Gemini 2.5 Pro Tier 1 RPM (published preset) = **150** requests per minute (2026-07-14..2026-07-14) [DISCARD: Per-project RPM preset; not aggregate customer volume.] quote: "\| Tier 1 (2.5 Pro) \| 150 \| 2,000,000 input TPM \| 10,000 \|"
  - p114 Gemini 2.5 Flash-Lite Tier 1 RPM (published preset) = **4,000** requests per minute (2026-07-14..2026-07-14) [DISCARD: Per-project RPM preset; not aggregate customer volume.] quote: "\| Tier 1 (2.5 Flash-Lite) \| 4,000 \| 4,000,000 input TPM \| Check AI Studio \|"
  - p115 Gemini 2.5 Pro Tier 1 RPD (published preset) = **10,000** requests per day (2026-07-14..2026-07-14) [DISCARD: Per-project RPD preset; not aggregate customer volume.] quote: "\| Tier 1 (2.5 Pro) \| 150 \| 2,000,000 input TPM \| 10,000 \|"
  - p116 Gemini 2.5 Flash-Lite Tier 1 baseline input TPM in master comparison table = **4,000,000** input tokens per minute (2026-07-14..2026-07-14) [DISCARD: Per-project TPM preset repeated in comparison table; not aggregate.] quote: "\| \| Gemini 2.5 Flash-Lite \| Tier 1 baseline \| 4,000 \| 4,000,000 input TPM \| Billing enabled \|"
  - p117 Gemini 2.5 Pro Tier 1 baseline input TPM in master comparison table = **2,000,000** input tokens per minute (2026-07-14..2026-07-14) [DISCARD: Per-project TPM preset repeated in comparison table; not aggregate.] quote: "\| \| Gemini 2.5 Pro \| Tier 1 baseline \| 150 \| 2,000,000 input TPM \| Billing enabled \|"
  - p118 Gemini 2.5 Pro baseline input TPM for startups (1K-10K requests/day) = **2,000,000** input tokens per minute (2026-07-14..2026-07-14) [DISCARD: Per-project startup TPM preset; not aggregate.] quote: "\| Gemini \| 2.5 Pro \| 150 baseline \| 2,000,000 input TPM baseline \| Pay-as-you-go; verify in AI Studio \|"
  - p119 Gemini 2.5 Flash-Lite baseline input TPM for startups (1K-10K requests/day) = **4,000,000** input tokens per minute (2026-07-14..2026-07-14) [DISCARD: Per-project startup TPM preset; not aggregate.] quote: "\| Gemini \| 2.5 Flash-Lite \| 4,000 baseline \| 4,000,000 input TPM baseline \| Pay-as-you-go; verify in AI Studio \|"
  - p120 Gemini 2.5 Flash-Lite best standard TPM at enterprise scale = **4,000,000** input tokens per minute (2026-07-14..2026-07-14) [DISCARD: Per-project enterprise-scale TPM preset; not aggregate.] quote: "\| \| Gemini 2.5 Flash-Lite \| 4,000 \| 4,000,000 input TPM baseline \|"
  - p121 Gemini 2.5 Pro best standard TPM at enterprise scale = **2,000,000** input tokens per minute (2026-07-14..2026-07-14) [DISCARD: Per-project enterprise-scale TPM preset; not aggregate.] quote: "\| \| Gemini 2.5 Pro \| 150 \| 2,000,000 input TPM baseline \|"
  - p122 Gemini RPM range cited in Mistral comparison (lower bound) = **2,000** requests per minute (2026-07-14..2026-07-14) [DISCARD: Per-project RPM comparison bound; not aggregate.] quote: "higher than Anthropic Tier 1 (50), but well below OpenAI Tier 2 (5,000) and Gemini (2,000-4,000)"
  - p123 Gemini RPM range cited in Mistral comparison (upper bound) = **4,000** requests per minute (2026-07-14..2026-07-14) [DISCARD: Per-project RPM comparison bound; not aggregate.] quote: "higher than Anthropic Tier 1 (50), but well below OpenAI Tier 2 (5,000) and Gemini (2,000-4,000)"
- `https://squigglehub.org/models/jsd/gemini-revenue-rough-guess/revisions/cmme124ng0000js0424ez2hun` -> **live_dated** (page date 2026-03-05); points raw/verified 0/0
- `https://yingtu.ai/en/blog/google-gemini-api-free-tier-limits-2026` -> **live_dated** (page date 2026-09-30); points raw/verified 15/15
  - p124 Gemini API free-tier TPM limit reported by third-party tables (January 2026) = **250,000** tokens per minute (2026-01-01..2026-01-31) [DISCARD: Free-tier per-project TPM limit; not aggregate customer volume.] quote: "third-party tables from January 2026 listed ranges of 5-15 RPM, 250,000 TPM and 100-1,000 RPD"
  - p125 Gemini API free-tier RPM lower bound reported by third-party tables (January 202 = **5** requests per minute (2026-01-01..2026-01-31) [DISCARD: Free-tier per-project RPM limit; not aggregate customer volume.] quote: "third-party tables from January 2026 listed ranges of 5-15 RPM, 250,000 TPM and 100-1,000 RPD"
  - p126 Gemini API free-tier RPM upper bound reported by third-party tables (January 202 = **15** requests per minute (2026-01-01..2026-01-31) [DISCARD: Free-tier per-project RPM limit; not aggregate customer volume.] quote: "third-party tables from January 2026 listed ranges of 5-15 RPM, 250,000 TPM and 100-1,000 RPD"
  - p127 Gemini API free-tier RPD lower bound reported by third-party tables (January 202 = **100** requests per day (2026-01-01..2026-01-31) [DISCARD: Free-tier per-project RPD limit; not aggregate customer volume.] quote: "third-party tables from January 2026 listed ranges of 5-15 RPM, 250,000 TPM and 100-1,000 RPD"
  - p128 Gemini API free-tier RPD upper bound reported by third-party tables (January 202 = **1,000** requests per day (2026-01-01..2026-01-31) [DISCARD: Free-tier per-project RPD limit; not aggregate customer volume.] quote: "third-party tables from January 2026 listed ranges of 5-15 RPM, 250,000 TPM and 100-1,000 RPD"
  - p129 Gemini 2.5 Flash free-tier requests per day reported by Reddit users (December 2 = **20** requests per day (2025-12-01..2025-12-31) [DISCARD: Anecdotal free-tier per-project request limit; not aggregate.] quote: "In December 2025, Reddit users reported that the free tier for Gemini 2.5 Flash had dropped to about 20 requests per day"
  - p130 Grounding with Google Search free allowance on Gemini 3.x models = **5,000** search requests per month (2026-09-30..2026-09-30) [DISCARD: Grounding free allowance; different product and not token volume.] quote: "Grounding with Google Search on Gemini 3.x models has its own allowance: 5,000 free search requests per month, shared across all Gemini 3.x models"
  - p131 Price per 1,000 grounding search requests beyond free allowance (as of September = **14** USD per 1,000 requests (2026-09-30..2026-09-30) [DISCARD: Grounding search price; different product and not token volume.] quote: "then $14 per 1,000 requests as of September 30, 2026"
  - p132 Tier 1 spend cap (as of September 30, 2026) = **250** USD (2026-09-30..2026-09-30) [DISCARD: Tier spend cap; not aggregate token volume.] quote: "\| Tier 1 \| Set up and link an active billing account \| $250 \| $10 \|"
  - p133 Tier 1 spend-based limit per rolling 10 minutes = **10** USD per rolling 10 minutes (2026-09-30..2026-09-30) [DISCARD: Tier spend-rate limit; not aggregate token volume.] quote: "\| Tier 1 \| Set up and link an active billing account \| $250 \| $10 \|"
  - p134 Tier 2 spend cap = **2,000** USD (2026-09-30..2026-09-30) [DISCARD: Tier spend cap; not aggregate token volume.] quote: "\| Tier 2 \| $100 paid, plus 3 days since the first successful payment \| $2,000 \| $50 \|"
  - p135 Tier 2 spend-based limit per rolling 10 minutes = **50** USD per rolling 10 minutes (2026-09-30..2026-09-30) [DISCARD: Tier spend-rate limit; not aggregate token volume.] quote: "\| Tier 2 \| $100 paid, plus 3 days since the first successful payment \| $2,000 \| $50 \|"
  - p136 Tier 3 spend cap lower bound = **20,000** USD (2026-09-30..2026-09-30) [DISCARD: Tier spend cap; not aggregate token volume.] quote: "\| Tier 3 \| $1,000 paid, plus 30 days since the first successful payment \| $20,000 to $100,000+ \| $200 \|"
  - p137 Tier 3 spend-based limit per rolling 10 minutes = **200** USD per rolling 10 minutes (2026-09-30..2026-09-30) [DISCARD: Tier spend-rate limit; not aggregate token volume.] quote: "\| Tier 3 \| $1,000 paid, plus 30 days since the first successful payment \| $20,000 to $100,000+ \| $200 \|"
  - p138 Batch API concurrent batch request limit = **100** concurrent batch requests (2026-09-30..2026-09-30) [DISCARD: Batch concurrency limit; not aggregate token volume.] quote: "Batch API jobs have separate limits: 100 concurrent batch requests, a 2 GB input file limit and 20 GB of file storage."
- dropped by code checks: 1 (scale word 'million' not supported by quote or table header: 1)

### b1 [forecasts_markets] pre-release analyst and market forecasts

Hypothesis: Independent analyst previews or prediction-market notes may imply a Q3 2026 Gemini API token run-rate, helping resolve whether growth continued near recent QoQ rates or decelerated materially; this would directly constrain m1.

Queries issued by the searcher: Alphabet Q3 2026 earnings Gemini API tokens per minute; analyst preview Alphabet third quarter 2026 results Gemini token growth; "tokens per minute" Gemini API Q3 2026 forecast "billion tokens" October 2026 preview; "billion tokens per minute" Gemini Q3 2026 estimate analysts expect

- `https://cs.bulios.com/status/273363` -> **live_dated** (page date 2026-07-23); points raw/verified 10/0
- `https://za.investing.com/news/stock-market-news/alphabet-stock-analysis-stalled-near-200day-average-ahead-of-q3-earnings-93CH-4509218` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://zeno.fm/podcast/dr-julian-hosp-ki-finanzen-unternehmertum-und-performance/episodes/1178-gemini-3-6-flash-durchbruch-oder-googles-letzter-grash` -> **live_dated** (page date 2026-07-22); points raw/verified 1/0
- `https://www.unite.ai/da/googles-ai-data-center-spending-outruns-its-cash-flow/` -> **dropped** (live http 403); points raw/verified -/-
- dropped by code checks: 11 (scale word 'billion' not supported by quote or table header: 7; period_end missing or unparseable: 2; scale word 'million' not supported by quote or table header: 1; number: unknown scale word 'Milliarden': 1)

### b2 [related_series] API revenue and token pricing

Hypothesis: If Gemini API/Vertex AI revenue or average revenue per token is found, d2 can convert Cloud AI revenue into an independent token-volume estimate and test the trend extrapolation; falling prices would imply faster token growth than revenue.

Queries issued by the searcher: Gemini API revenue Q3 2026 Alphabet tokens per minute; Vertex AI Gemini revenue run-rate 2026 tokens per minute earnings call; Alphabet third quarter 2026 results tokens per minute Gemini direct API "billion tokens per minute"; "Q3 2026" Alphabet earnings call Pichai "tokens per minute"

- `https://www.perplexity.ai/app/finance/GOOGL/earnings?eventId=657320` -> **dropped** (live http 403); points raw/verified -/-
- `https://ph.investing.com/news/company-news/alphabet-q1-2026-slides-cloud-surges-63-ai-investments-accelerate-93CH-2370226` -> **dropped** (live http 403); points raw/verified -/-
- `https://tomtunguz.com/google-earnings-q4-2025/?ref=ghost.philomaths.tech` -> **live_dated** (page date 2026-02-05); points raw/verified 15/10
  - p139 Alphabet first-party models (Gemini) tokens processed per minute via direct API  = **10,000,000,000** tokens per minute (2025-10-01..2025-12-31) [DISCARD: Duplicate of p6 direct-API 10B/min quote.] quote: "Our first-party models like Gemini now process over 10 billion tokens per minute via direct API used by our customers, up from 7 billion last quarter."
  - p140 Alphabet first-party models (Gemini) tokens processed per minute via direct API, = **7,000,000,000** tokens per minute (2025-07-01..2025-09-30) [DISCARD: Duplicate of p8 direct-API 7B/min quote.] quote: "Our first-party models like Gemini now process over 10 billion tokens per minute via direct API used by our customers, up from 7 billion last quarter."
  - p141 Year-over-year increase in Gemini tokens per minute via direct API = **52** multiple (year-over-year increase) (2025-01-01..2025-12-31) [DISCARD: 52x growth multiple is inconsistent with p142/p143 units and uses ambiguous scope.] quote: "This represents a staggering 52x increase year-over-year, up from ~8.3 trillion tokens/month in December 2024 to an annualized run rate of over 430 trillion."
  - p142 Gemini tokens per month, December 2024 baseline = **8,300,000,000,000** tokens per month (2024-12-01..2024-12-31) [DISCARD: December 2024 Gemini token baseline has unclear scope and conflicts with p141/p143 arithmetic.] quote: "up from ~8.3 trillion tokens/month in December 2024 to an annualized run rate of over 430 trillion."
  - p143 Gemini annualized token run rate, current = **430,000,000,000,000** tokens per year (annualized run rate) (2025-10-01..2025-12-31) [DISCARD: Annualized 430T token-run-rate quote is internally inconsistent with p141/p142 and other direct-API levels.] quote: "up from ~8.3 trillion tokens/month in December 2024 to an annualized run rate of over 430 trillion."
  - p144 Number of customers each processing more than 100 billion tokens = **350** customers (2025-10-01..2025-12-31) [DISCARD: Older customer token-threshold count; superseded by p33/p34 and non-binding.] quote: "Nearly 350 customers each process more than 100 billion tokens."
  - p145 Token threshold per large customer (each of ~350 customers) = **100,000,000,000** tokens per customer (2025-10-01..2025-12-31) [DISCARD: Older per-customer token threshold; not aggregate API volume.] quote: "Nearly 350 customers each process more than 100 billion tokens."
  - p146 Google backlog growth = **55** % (2025-10-01..2025-12-31) [DISCARD: Q4 2025 Cloud backlog growth; not API token volume.] quote: "Backlog grew 55% to $240 billion."
  - p147 Google backlog level = **240,000,000,000** USD (backlog) (2025-10-01..2025-12-31) [DISCARD: Q4 2025 Cloud backlog level; not API token volume.] quote: "Backlog grew 55% to $240 billion."
  - p148 Google Cloud revenue growth = **48** % (2025-10-01..2025-12-31) [DISCARD: Q4 2025 Cloud revenue growth; broad Cloud metric, not API token volume.] quote: "Google Cloud revenue grew 48% to $17.7 billion, outpacing Azure's 39% growth."
- `https://redresscompliance.com/assets/docs/research-notes/google-ai-seats-consumption-commit.pdf` -> **dropped** (live page has no readable date); points raw/verified -/-
- dropped by code checks: 5 (period_end missing or unparseable: 5)

### b3 [capacity_consumption] deployed compute and inference efficiency

Hypothesis: The capacity method m3 is limited by assumptions about Q3 2026 H100-equivalent capacity, tokens/s per accelerator, and direct-API compute share; better deployed-TPU estimates or Gemini inference benchmarks would materially tighten or falsify that route.

Queries issued by the searcher: Alphabet third quarter 2026 results tokens per minute Gemini API; Epoch AI Alphabet Google TPU H100-equivalent capacity 2026 estimate; SemiAnalysis Google TPU capacity 2026 Gemini inference share external API; Ironwood TPU Gemini inference tokens per second per chip benchmark

- `https://www.eet-china.com/mp/a515876.html` -> **dropped** (live fetch error TimeoutError); points raw/verified -/-
- `https://www.networkworld.com/article/4156949/google-owns-the-most-ai-compute-and-it-built-it-its-way.html` -> **live_dated** (page date 2026-04-09); points raw/verified 15/0
- `https://epoch.ai/data/ai-data-centers/directory/google-pryor-north` -> **live_dated** (page date 2024-07-19); points raw/verified 9/4
  - p149 Current IT power at Google Pryor (North) data center, MW = **368** MW (2026-09-06..2026-09-06) [DISCARD: Single data-center IT power; not total Alphabet owned compute.] quote: "CURRENT IT POWER 368MW"
  - p150 IT power at Google Pryor (North) Building 1 when operational, MW = **53** MW (2024-07-19..2024-07-19) [DISCARD: Single building IT power; not total Alphabet owned compute.] quote: "IT Power53MW"
  - p151 Estimated time until full operation of Building 2 at Google Pryor (North), month = **3** months (2026-05-26..2026-05-26) [DISCARD: Single building operational timeline; not aggregate capacity.] quote: "We therefore expect another 3 months until full operation."
  - p152 Size of Google TPU v4 cluster at Pryor data center, exaflops = **9** exaflops (2022..2022) [DISCARD: Older site-specific TPU cluster; not total Alphabet owned compute.] quote: "News of a 9 exaflop TPUv4 cluster in the Pryor data center, launched in 2022"
- `https://newsletter.semianalysis.com/p/tpu-inferencex-full-steam` -> **live_dated** (page date 2026-09-07); points raw/verified 15/0
- dropped by code checks: 35 (period_end missing or unparseable: 27; period_end 2031-12-31 after as_of: 2; quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1; scale word 'thousand' not supported by quote or table header: 1; value_as_written not in quote as a whole number: 2; scale word 'billion' not supported by quote or table header: 2)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['gemini tokens', 'alphabet q3', 'api volume']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p6', 'p8', 'p19', 'p86'] Alphabet's own direct-API token/min disclosures form a coherent sequence: p8 7B Q3 2025, p6 10B Q4 2025, p1 16B Q1 2026, p19 22B Q2 2026; p86 reports the Q1 QoQ growth as 60%, consistent with p6 to p1
- corroborating: ['p19', 'p51', 'p52'] p51 repeats the Q2 2026 22B/min figure and p52 the Q1 2026 16B/min figure. This is media repetition of the same Alphabet disclosure, not independent corroboration.
- corroborating: ['p20', 'p21', 'p36', 'p37', 'p56', 'p88', 'p89'] Google Cloud revenue and growth disclosures for Q1 and Q2 2026 reinforce a picture of accelerating AI/cloud demand, but they do not directly measure API token volume.
- corroborating: ['p53', 'p54', 'p55', 'p58', 'p59'] Capex figures corroborate very large AI infrastructure buildout; p55 is consistent with p54 plus p53/p58, and p59 gives the server share of Q2 capex. Shared company reporting, not independent.
- corroborating: ['p60', 'p61'] p60 is an Epoch AI estimate of TPU-only H100-equivalent compute; p61 is an implied Nvidia-GPU estimate from the same source. They are useful in sum but are not fully independent.
- corroborating: ['p13', 'p14', 'p33', 'p34', 'p65', 'p66', 'p74', 'p75'] Customer token-milestone counts corroborate growing enterprise usage: more customers crossing 1T and 10T trailing-twelve-month milestones. Definitions are trailing 12 months, not a current run-rate.
- related: ['p46', 'p47'] OpenAI API token/min trajectory is a comparable base rate for enterprise LLM API demand, but it is a different company and scope; it cannot be directly substituted for Gemini.
- contextual: ['p100', 'p101', 'p102', 'p103', 'p104', 'p105', 'p106', 'p107', 'p108', 'p109'] SDK download counts are attention/developer-activity indicators, not token volume; they can constrain direction but require an unobserved bridge to usage.
- contextual: ['p98', 'p99', 'p110', 'p111', 'p112', 'p124', 'p125', 'p126', 'p127', 'p128', 'p129', 'p130', 'p131', 'p132', 'p133', 'p134', 'p135', 'p136', 'p137', 'p138'] Model pricing, per-project rate limits and free-tier limits describe constraints and prices, not aggregate actual token throughput; using them as usage levels would be misleading.
- contextual: ['p2', 'p3', 'p7', 'p11', 'p30', 'p67'] Gemini app MAU is consumer-app scope, not direct API usage; useful for overall adoption but not for the target measure.
- contextual: ['p9', 'p10', 'p63', 'p64'] All-surface monthly token totals include consumer, internal and other surfaces and are much broader than direct API use; useful only as a broad consistency check, not a direct level.
- contextual: ['p18', 'p39', 'p72', 'p81'] Revenue growth from generative-AI products signals demand strength, but revenue and token volume are different quantities and pricing changes break proportionality.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p8', 'p6', 'p1', 'p19', 'p86'] Direct API first-party model token run-rate series: 7B/min Q3 2025, 10B/min Q4 2025, 16B/min Q1 2026, 22B/min Q2 2026. p86's Q1 2026 '+60% from last quarter' matches p1 versus p6. Same metric and sequ
- redundant: ['p139', 'p140'] Duplicate quotations of the same Q4 2025 10B/min and Q3 2025 7B/min direct-API figures already in p6 and p8; no independent information.
- different_scope: ['p2', 'p3', 'p7', 'p11', 'p30'] Gemini app monthly active users measure the consumer app, not direct API token consumption. p2 and p7 duplicate the Q4 2025 750M figure; p3 and p11 duplicate the Q3 2025 650M figure. Useful context fo
- different_scope: ['p9', 'p10'] Monthly tokens across all Google surfaces include consumer, internal, Search/AI Mode, and other workloads. They are not the direct-API customer run-rate and cannot be converted without a surface-share
- related_but_different_scope: ['p20', 'p21', 'p36', 'p57'] Google Cloud revenue, growth, and backlog are broad Cloud metrics including infrastructure and other products, not Gemini direct-API token volume. They indicate demand strength but cannot be used as a
- corroborating: ['p54', 'p55', 'p58', 'p59'] Alphabet capex: Q1 2026 $35.7B plus Q2 2026 $44.9B is consistent with H1 2026 $80.6B; Q2 capex split roughly 60% servers. This supports inference-capacity growth assumptions, not a direct token level.
- corroborating_shared_source: ['p60', 'p61'] Epoch AI Q4 2025 owned compute: TPU-only 3.1M-4.5M H100-equivalents (midpoint 3.8M), with Nvidia GPUs implied at roughly 1M. They come from the same estimate and are not independent. They require a ca
- comparable_analogue: ['p46', 'p47'] OpenAI API token usage is a different company but a useful growth analogue: 6B/min October 2025 to 15B/min March 2026, roughly 2.5x in five months. Gemini's Q2 2026 22B/min is already above the March 
- context: ['p98', 'p99'] Gemini 4 Argon list prices of $2 per million input tokens and $10 per million output tokens are relevant to any revenue-to-token conversion, but a conversion requires unknown output-token mix, discoun
- attention_context: ['p100', 'p101', 'p104', 'p105'] SDK download counts show developer attention: google-genai 216.7M PyPI and @google/genai 45.8M npm versus openai 295.9M PyPI and anthropic 119.8M PyPI. Gemini's lower SDK downloads than OpenAI coexist
- lower_bound_context: ['p33', 'p34', 'p144', 'p145'] Customer token thresholds imply large absolute usage but are far below the reported aggregate: 330 customers each >1T tokens/year and 35 each >10T/year imply roughly 350T tokens/year from those custom
- conflicting: ['p141', 'p142', 'p143'] The quoted 52x growth from ~8.3T tokens/month to an 'annualized run rate' of >430T is internally inconsistent: 52x of 8.3T/month is ~432T/month, while 430T/year is ~35.8T/month. Neither reconciles cle
- different_scope: ['p110', 'p111', 'p112', 'p113', 'p114', 'p115', 'p116', 'p117', 'p118', 'p119', 'p120', 'p121', 'p122', 'p123', 'p124', 'p125', 'p126', 'p127', 'p128', 'p129', 'p130', 'p131', 'p132', 'p133', 'p134', 'p135', 'p136', 'p137', 'p138'] Per-project or per-tier TPM/RPM/RPD limits, free-tier allowances, spend caps, and batch concurrency limits describe individual project quotas, not aggregate customer token consumption. Without custome
- site_specific_context: ['p149', 'p150', 'p151', 'p152'] These describe a single Google data center and an older TPU cluster, not total Alphabet owned compute. The p60/p61 total capacity estimates are more suitable for a capacity route.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | Q3 2026/Q2 2026 growth factor for Gemini direct API tokens per minute | 1.3 | 1.15..1.45 | 1.15..1.45 | multiple | m1 (m1) | Recent direct-API QoQ growth factors are about 1.43 (Q3 2025 to Q4 2025), 1.60 (Q4 2025 to Q1 2026), and 1.375 (Q1 2026 to Q2 2026). As the base grows, growth should decelerate modestly; Gemini 4 launched only at the very end of Q3 2026, so it should not dominate the quarter. A 30% QoQ increase is a | Q3 2026 direct-API token consumption continues the recent growth trajectory with modest deceleration and no major mid-quarter pricing/rate-limit shock. | Evidence that Q3 2026 QoQ growth was below 10% or above 55%, or that a major Gemini API launch/price cut caused a step change within Q3 2026. |
| a3 | average inference throughput per H100-equivalent serving Gemini models | 2,000 | 800..5,000 | 800..5,000 | tokens per second per H100-equivalent | m3 (m3) | An H100-equivalent accelerator running batched LLM inference can produce thousands of output tokens per second for smaller/faster models, but much less for large Gemini Pro-class models. The 2,000 token/s central value is a blended throughput across Flash/Pro serving, with a wide range for model mix | Capacity is expressed in H100-equivalents and used for a blended Gemini serving mix rather than one specific model. | Gemini inference benchmarks or capacity disclosures showing sustained throughput outside roughly 800-5,000 tokens/s per H100-equivalent. |
| a4 | average utilization of direct-API inference accelerators | 0.7 | 0.5..0.9 | 0.4743..0.9487 (widened) | fraction | m3 (m3) | Production inference fleets usually run at high average utilization because of batching and continuous serving, but need headroom for bursts, failover, and regional demand. A 70% average utilization over a quarter is plausible for a large managed API. | The capacity route estimates average quarter-level output from installed inference capacity rather than peak capacity. | Evidence that direct-API inference utilization is consistently below 50% or above 90% over the quarter. |
| a5 | share of total Alphabet owned H100-equivalent compute allocated to direct API inference | 0.05 | 0.02..0.12 | 0.02..0.12 | fraction | m3 (m3) | Alphabet's owned compute serves Search/AI Mode, the Gemini app, Workspace, internal workloads, Cloud training, and many other serving uses. Direct API is one channel, so only a minority of H100-equivalent capacity should be assigned to it. The 5% central share allows for substantial direct-API servi | p60 and p61 represent total owned Alphabet compute, including training and all serving surfaces, not dedicated Gemini API capacity. | Disclosure or credible estimate that direct-API inference uses more than ~12% or less than ~2% of total Alphabet owned H100-equivalent capacity. |
| a6 | growth factor in total owned H100-equivalent capacity from Q4 2025 to Q3 2026 | 1.5 | 1.2..2 | 1.2..2 | multiple | m3 (m3) | Alphabet spent about $80.6B on capex in H1 2026 after large Q1 and Q2 outlays, with roughly 60% of Q2 capex going to servers. Three quarters of deployment should raise owned H100-equivalent capacity meaningfully, but not all capex adds inference capacity and TPU/GPU shipments have lead times. A 1.5x | p60/p61 are Q4 2025 owned-capacity estimates and Q3 2026 capacity is approximated by applying a three-quarter growth factor. | Evidence that Alphabet's owned H100-equivalent capacity grew less than 20% or more than 100% between Q4 2025 and Q3 2026. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 28,400,129,285 | ['p19'] / ['a1'] | [] |  | 0.25 | equal |  |
| m2 | formula_mc | 30,181,511,615 | ['p19', 'p1'] / [] | [] |  | 0.25 | equal |  |
| m3 | formula_mc | 29,181,723,216 | ['p60', 'p61'] / ['a3', 'a4', 'a5', 'a6'] | [] |  | 0.25 | equal |  |
| m4 | formula_mc | 32,876,231,484 | ['p19', 'p1', 'p6', 'p8'] / [] | [] |  | 0.25 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target
- m3 coverage: the whole target
- m4 coverage: the whole target

Result: central **30,113,661,686** token/minute, 80% interval [7,669,319,280, 118,241,604,894] token/minute, basis monte_carlo (too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only), weight rule equal, weight on methods that use assumptions 0.50

## Published-value check (live use only)

Status: **no_candidates**. 0 candidate(s); entity terms ['alphabet', 'api']; measure stems ['alpha', 'first', 'minut', 'model', 'party', 'token']


## Final answer

The estimate for the number of tokens per minute that Alphabet's first-party models (primarily Gemini) process via direct API use by customers, as first stated with Q3 2026 results (period 2026-[n]-[n] to 2026-[n]-[n]), is 30,113,661,686 token/minute (80% model-based interval 7,669,319,280 to 118,241,604,894 token/minute; too few backtest years, so the interval width comes from Monte Carlo sampling of the formula inputs and reflects input uncertainty only).

The anchor is the observed Q2 2026 disclosure of 22,000,000,000 API tokens per minute, with earlier observed points 7,000,000,000 tokens per minute, 10,000,000,000 tokens per minute, and 16,000,000,000 tokens per minute tracing the growth path. Two routes extrapolate that trend (one using assumption a1 of 1.3, range 1.15 to 1.45); a third cross-checks against owned compute (3,800,000 Nvidia-H100-equivalents plus 1,000,000 Nvidia-H100-equivalents) scaled by throughput, utilization, direct-API share, and capacity growth assumptions. The four routes were combined at equal weight (25% each) because no backtest error was available to differentiate them.

The main risk is that the assumed Q3 growth factor is wrong due to a launch, pricing change, or demand shock. Better evidence would be any interim disclosure of direct-API token volume or a validated throughput benchmark.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 Q3 2026/Q2 2026 growth factor for Gemini direct API tokens per minute: 1.3 multiple, range 1.15 to 1.45; used by m1. Overturned by: Evidence that Q3 2026 QoQ growth was below [n] or above [n], or that a major Gemini API launch/price cut caused a step change within Q3 2026.
- a3 average inference throughput per H[n]-equivalent serving Gemini models: 2,000 tokens per second per H[n]-equivalent, range 800 to 5,000; used by m3. Overturned by: Gemini inference benchmarks or capacity disclosures showing sustained throughput outside roughly [n]-[n] tokens/s per H[n]-equivalent.
- a4 average utilization of direct-API inference accelerators: 0.7 fraction, range 0.4743 to 0.9487 (range widened by code); used by m3. Overturned by: Evidence that direct-API inference utilization is consistently below [n] or above [n] over the quarter.
- a5 share of total Alphabet owned H[n]-equivalent compute allocated to direct API inference: 0.05 fraction, range 0.02 to 0.12; used by m3. Overturned by: Disclosure or credible estimate that direct-API inference uses more than ~[n] or less than ~[n] of total Alphabet owned H[n]-equivalent capacity.
- a6 growth factor in total owned H[n]-equivalent capacity from Q4 2025 to Q3 2026: 1.5 multiple, range 1.2 to 2; used by m3. Overturned by: Evidence that Alphabet's owned H[n]-equivalent capacity grew less than [n] or more than [n] between Q4 2025 and Q3 2026.

# Evidence ledger: fc_googl_tokens_2026_q3

- Question: Assume today is 2026-10-19. You know nothing published after this date. Estimate the number of tokens per minute that Alphabet's first-party models (such as Gemini) process via direct API use by customers, as it will be first stated with Alphabet's third-quarter 2026 results (earnings press release or CEO earnings-call remarks); in Q2 2026 Alphabet stated this as 'Gemini models now process 22 billion API tokens per minute'. Answer in tokens per minute.
- as_of: 2026-10-19
- Pinned target: Rate at which Alphabet's first-party models (e.g. Gemini) process tokens via direct API use by customers, as first disclosed with Alphabet's Q3 2026 results (earnings release or CEO earnings-call remarks); the analogous Q2 2026 disclosure was 'Gemini models now process 22 billion API tokens per minu | unit tokens per minute | period 2026-07-01..2026-09-30 | publisher Alphabet Inc. (earnings press release / CEO earnings-call remarks)

## Directions and pages

### d1 [own_history] Alphabet investor-relations disclosures and CEO earnings-call transcripts

Hypothesis: The Q3 2026 figure is the next point in a quarterly run-rate series (e.g. prior disclosures of tokens per minute at successive earnings). Fitting the recent trajectory (level and quarter-over-quarter growth) and extrapolating one quarter gives a direct estimate; growth has been rapid and possibly decelerating, so the recent growth rate is the key input.

Queries issued by the searcher: Alphabet earnings call Gemini models process billion API tokens per minute; Sundar Pichai Gemini tokens processed per minute quarterly earnings disclosure trillion tokens per month; abc.xyz Alphabet Q2 2026 earnings call transcript Pichai "22 billion tokens per minute"; "Alphabet" Q1 2026 earnings call "16 billion tokens per minute" press release abc.xyz

- `http://alphabet2025ir.q4web.com/investor/events/event-details/2026/2026-Q2-Earnings-Call-2026-GgTAq7Is0z/` -> **live_dated** (page date 2026-07-22); points raw/verified 15/12
  - p1 Alphabet model APIs tokens processed per minute, Q2 2026 (current run-rate) = **22,000,000,000** tokens per minute (2026-04-01..2026-06-30) [keep: ] quote: "Our model APIs are now processing approximately 22 billion tokens per minute."
  - p2 Alphabet model APIs tokens processed per minute, prior quarter (Q1 2026) as cite = **16,000,000,000** tokens per minute (2026-01-01..2026-03-31) [keep: ] quote: "That's up from 16 billion just a quarter ago."
  - p3 Cloud customers each processing more than one trillion tokens in the last year ( = **500** Cloud customers (2025-07-01..2026-06-30) [keep: ] quote: "Nearly 500 Cloud customers have each processed more than one trillion tokens in the last year"
  - p4 Enterprises consuming over 100 billion tokens over the last 12 months (count of  = **2,000** enterprises (2025-07-01..2026-06-30) [keep: ] quote: "Over the last 12 months, more than 2,000 enterprises consumed over 100 billion tokens."
  - p5 Token threshold per Cloud customer (over one trillion tokens in the last year) = **1,000,000,000,000** as written "one trillion", value check pending tokens (2025-07-01..2026-06-30) [keep: ] quote: "Nearly 500 Cloud customers have each processed more than one trillion tokens in the last year"
  - p6 Token threshold per enterprise (over 100 billion tokens over last 12 months) = **100,000,000,000** tokens (2025-07-01..2026-06-30) [keep: ] quote: "Over the last 12 months, more than 2,000 enterprises consumed over 100 billion tokens."
  - p7 Developers building monthly with Alphabet models across APIs and developer produ = **9,000,000** as written "nine million", value check pending developers per month (2026-04-01..2026-06-30) [keep: ] quote: "More than nine million developers are building each month with our models across our APIs and key developer products."
  - p8 Gemini App monthly active users, Q2 2026 = **950,000,000** monthly active users (2026-04-01..2026-06-30) [keep: ] quote: "Next, the Gemini App, which now has 950 million monthly active users, with daily active users tripling in the last year."
  - p9 Gemma 4 models cumulative downloads since April launch = **300,000,000** downloads (2026-04-01..2026-06-30) [keep: ] quote: "And our latest Gemma 4 models have been downloaded over 300 million times since launching in April."
  - p10 Agent Development Kit total downloads, Q2 2026 = **70,000,000** total downloads (2026-04-01..2026-06-30) [keep: ] quote: "In Q2, Agent Development Kit, our framework for building and deploying enterprise AI agents, reached nearly 70 million total downloads."
  - p11 Google Cloud backlog, Q2 2026 = **514,000,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "Google Cloud's backlog increased by more than $50 billion sequentially, reaching $514 billion in the second quarter."
  - p12 Google Cloud revenue, Q2 2026 = **24,800,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "Cloud revenues were up 82% to $24.8 billion, driven primarily by GCP, which grew faster than Cloud overall."
- `https://stockanalysis.com/stocks/googl/transcripts/657320-q2-2026/` -> **live_dated** (page date 2026-10-16); points raw/verified 15/15
  - p13 Alphabet model APIs tokens processed per minute, Q2 2026 (current quarter run-ra = **22,000,000,000** tokens per minute (2026-04-01..2026-06-30) [DISCARD: Redundant copy of p1 (22B Q2 2026).] quote: "Our model APIs are now processing approximately 22 billion tokens per minute."
  - p14 Alphabet model APIs tokens processed per minute, prior quarter (Q1 2026) run-rat = **16,000,000,000** tokens per minute (2026-01-01..2026-03-31) [DISCARD: Redundant copy of p2 (16B Q1 2026).] quote: "That's up from 16 billion just a quarter ago."
  - p15 Number of developers building monthly with Alphabet models across APIs and devel = **9,000,000** developers (2026-04-01..2026-06-30) [DISCARD: Redundant copy of p7 (9M developers).] quote: "More than 9 million developers are building each month with our models across our APIs and key developer products."
  - p16 Cloud customers each processing more than 1 trillion tokens in the last year (co = **500** Cloud customers (2025-07-01..2026-06-30) [DISCARD: Redundant copy of p3.] quote: "Nearly 500 Cloud customers have each processed more than 1 trillion tokens in the last year"
  - p17 Enterprises consuming over 100 billion tokens over the last 12 months (count of  = **2,000** enterprises (2025-07-01..2026-06-30) [DISCARD: Redundant copy of p4.] quote: "Over the last 12 months, more than 2,000 enterprises consumed over 100 billion tokens."
  - p18 Token threshold per Cloud customer cited (over 1 trillion tokens in the last yea = **1,000,000,000,000** tokens (2025-07-01..2026-06-30) [DISCARD: Redundant copy of p5.] quote: "Nearly 500 Cloud customers have each processed more than 1 trillion tokens in the last year"
  - p19 Token threshold per enterprise cited (over 100 billion tokens over last 12 month = **100,000,000,000** tokens (2025-07-01..2026-06-30) [DISCARD: Redundant copy of p6.] quote: "Over the last 12 months, more than 2,000 enterprises consumed over 100 billion tokens."
  - p20 Gemini app monthly active users = **950,000,000** monthly active users (2026-04-01..2026-06-30) [DISCARD: Redundant copy of p8.] quote: "Next, the Gemini app, which now has 950 million monthly active users with daily active users tripling in the last year."
  - p21 AI Mode monthly active users since global expansion last October = **1,000,000,000** monthly active users (2025-10-01..2026-06-30) [keep: ] quote: "Since expanding AI Mode globally last October, we have surpassed 1 billion monthly active users."
  - p22 Agent Development Kit total downloads in Q2 2026 = **70,000,000** total downloads (2026-04-01..2026-06-30) [DISCARD: Redundant copy of p10.] quote: "In Q2, Agent Development Kit, our framework for building and deploying enterprise AI agents, reached nearly 70 million total downloads."
  - p23 Gemma family open models cumulative downloads = **900,000,000** downloads (..2026-06-30) [keep: ] quote: "These models have been downloaded over 900 million times"
  - p24 Gemma 4 model downloads since April launch = **300,000,000** downloads (2026-04-01..2026-06-30) [DISCARD: Redundant copy of p9.] quote: "our latest Gemma 4 models have been downloaded over 300 million times since launching in April"
  - p25 Antigravity agentic development platform weekly active users = **2,400,000** weekly active users (2026-04-01..2026-06-30) [keep: ] quote: "It has more than 2.4 million weekly active users."
  - p26 Google Cloud backlog at end of Q2 2026 = **514,000,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Redundant copy of p11.] quote: "Cloud backlog grew to $514 billion."
  - p27 Share of total Cloud backlog expected to be recognized as revenue over next 24 m = **50** % (2026-04-01..2026-06-30) [keep: ] quote: "we expect to recognize just over 50% of the total backlog as revenue over the next 24 months"
- `https://www.pymnts.com/news/2026/alphabet-bets-185b-on-gemini-agentic-commerce-and-enterprise-ai/` -> **live_dated** (page date 2026-02-06); points raw/verified 15/12
  - p28 Gemini tokens processed per minute via direct APIs, current quarter (Q4 2025), r = **10,000,000,000** tokens per minute (2025-10-01..2025-12-31) [keep: ] quote: "Gemini now processes more than 10 billion tokens per minute via direct APIs, up from 7 billion last quarter."
  - p29 Gemini tokens processed per minute via direct APIs, prior quarter (Q3 2025), run = **7,000,000,000** tokens per minute (2025-07-01..2025-09-30) [keep: ] quote: "Gemini now processes more than 10 billion tokens per minute via direct APIs, up from 7 billion last quarter."
  - p30 Gemini app monthly active users = **750,000,000** monthly active users (2025-10-01..2025-12-31) [keep: ] quote: "The Gemini app has surpassed 750 million monthly active users."
  - p31 Alphabet paid subscriptions across consumer services = **325,000,000** paid subscriptions (2025-10-01..2025-12-31) [keep: ] quote: "Alphabet reported more than 325 million paid subscriptions"
  - p32 Google Cloud backlog = **240,000,000,000** USD (2025-10-01..2025-12-31) [keep: ] quote: "Google Cloud backlog climbed to $240 billion, up 55% sequentially."
  - p33 Google Cloud backlog sequential growth = **55** % (2025-10-01..2025-12-31) [keep: ] quote: "Google Cloud backlog climbed to $240 billion, up 55% sequentially."
  - p34 Consolidated revenues, quarter = **113,800,000,000** USD (2025-10-01..2025-12-31) [keep: ] quote: "Consolidated revenues touched $113.8 billion in the quarter, up 18% year on year."
  - p35 Consolidated revenues year-over-year growth = **18** % (2025-10-01..2025-12-31) [keep: ] quote: "Consolidated revenues touched $113.8 billion in the quarter, up 18% year on year."
  - p36 Organizations using Gemini = **120,000** organizations (2025-10-01..2025-12-31) [keep: ] quote: "More than 120,000 organizations now use Gemini"
  - p37 Google Services revenue, quarter = **96,000,000,000** USD (2025-10-01..2025-12-31) [keep: ] quote: "Google Services revenue reached $96 billion for the quarter."
  - p38 Google Cloud revenue, quarter = **17,700,000,000** USD (2025-10-01..2025-12-31) [keep: ] quote: "Google Cloud revenue rose 48% to $17.7 billion, supported by enterprise AI infrastructure and solutions."
  - p39 Reduction in Gemini serving costs in 2025 from model optimization = **78** % (2025-01-01..2025-12-31) [keep: ] quote: "model optimization that reduced Gemini serving costs by 78% in 2025"
- `https://news.cocoloop.cn/en/2026/04/google-q1-2026-cloud-ai-earnings/` -> **live_dated** (page date 2026-04-30); points raw/verified 15/13
  - p40 Gemini API throughput, Q1 2026 (current quarter level) = **16,000,000,000** tokens per minute (2026-01-01..2026-03-31) [DISCARD: Redundant copy of p2/p66 (16B Q1 2026).] quote: "Gemini API throughput increased from 10 billion tokens per minute a quarter earlier to 16 billion."
  - p41 Google Cloud customers each processing more than 1 trillion tokens over past 12  = **330** Google Cloud customers (2025-04-01..2026-03-31) [keep: ] quote: "330 Google Cloud customers each processed more than 1 trillion tokens over the past 12 months."
  - p42 Token threshold per customer over past 12 months (lower bound) = **1,000,000,000,000** tokens (2025-04-01..2026-03-31) [keep: ] quote: "330 Google Cloud customers each processed more than 1 trillion tokens over the past 12 months."
  - p43 Gemini Enterprise paid monthly active users, QoQ growth Q1 2026 = **40** % (2026-01-01..2026-03-31) [keep: ] quote: "Gemini Enterprise paid monthly active users rose 40% from the prior quarter."
  - p44 Products built on Gemini models revenue growth, YoY Q1 2026 = **800** % (2026-01-01..2026-03-31) [keep: ] quote: "products built on Gemini models increased revenue by nearly 800% year over year"
  - p45 Google Cloud revenue, Q1 2026 = **20,030,000,000** USD (2026-01-01..2026-03-31) [keep: ] quote: "\| Google Cloud revenue \| $20.03 billion \| +63% \|"
  - p46 Google Cloud revenue YoY growth, Q1 2026 = **63** % (2026-01-01..2026-03-31) [keep: ] quote: "\| Google Cloud revenue \| $20.03 billion \| +63% \|"
  - p47 Alphabet total revenue, Q1 2026 = **109,900,000,000** USD (2026-01-01..2026-03-31) [keep: ] quote: "\| Total revenue \| $109.9 billion \| +22% \|"
  - p48 Cloud backlog, Q1 2026 = **460,000,000,000** USD (2026-01-01..2026-03-31) [keep: ] quote: "\| Cloud backlog \| $460 billion \| Nearly doubled QoQ \|"
  - p49 Cloud operating margin, Q1 2026 = **32.9** % (2026-01-01..2026-03-31) [keep: ] quote: "operating margin rose from 9.4% a year ago to 32.9%"
  - p50 Waymo autonomous rides per week = **500,000** autonomous rides per week (2026-01-01..2026-03-31) [keep: ] quote: "more than 500,000 autonomous rides a week across 11 U.S. cities"
  - p51 Paid subscriptions, Q1 2026 = **350,000,000** paid subscriptions (2026-01-01..2026-03-31) [keep: ] quote: "\| Paid subscriptions \| 350 million \| Best quarter ever \|"
  - p52 Gemma 4 downloads within weeks of release = **50,000,000** downloads (2026-01-01..2026-03-31) [keep: ] quote: "Gemma 4 passed 50 million downloads within weeks of release."
- dropped by code checks: 8 (period_end missing or unparseable: 2; value_as_written not in quote as a whole number: 2; period_end 2026-12-31 after as_of: 2; period year 2025 does not appear in the page text or URL (likely mis-dated): 2)

### d2 [related_series] Google Cloud / Vertex AI and Gemini API usage disclosures

Hypothesis: Alphabet also discloses related usage metrics (API calls, Vertex AI usage, Cloud backlog, AI model token volumes, developer counts). These broader or adjacent totals can be bridged to the token rate via a share or conversion (e.g. tokens per API call, share of tokens via direct API vs Vertex). Direction: related totals should grow similarly, constraining the plausible range.

Queries issued by the searcher: Alphabet earnings call Gemini models process tokens per minute API; Google Cloud Vertex AI tokens processed 2026; blog.google "Q2 2026" earnings call remarks Pichai 22 billion tokens per minute; blog.google Alphabet Q4 2025 earnings call remarks "10 billion tokens per minute" 350 cloud customers

- `https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q2-2026/` -> **live_dated** (page date 2026-07-22); points raw/verified 15/13
  - p53 Alphabet model APIs tokens processed per minute, Q2 2026 (CEO earnings-call rema = **22,000,000,000** tokens per minute (2026-04-01..2026-06-30) [DISCARD: Redundant copy of p1.] quote: "Our model APIs are now processing approximately 22 billion tokens per minute."
  - p54 Alphabet model APIs tokens processed per minute, prior quarter (Q1 2026), as cit = **16,000,000,000** tokens per minute (2026-01-01..2026-03-31) [DISCARD: Redundant copy of p2.] quote: "That's up from 16 billion just a quarter ago."
  - p55 Developers building each month with Alphabet models across APIs and key develope = **9,000,000** developers (2026-04-01..2026-06-30) [DISCARD: Redundant copy of p7.] quote: "More than 9 million developers are building each month with our models across our APIs and key developer products."
  - p56 Cloud customers each processing more than 1 trillion tokens in the last year = **500** Cloud customers (2025-07-01..2026-06-30) [DISCARD: Redundant copy of p3.] quote: "Nearly 500 Cloud customers have each processed more than 1 trillion tokens in the last year"
  - p57 Enterprises consuming over 100 billion tokens over the last 12 months = **2,000** enterprises (2025-07-01..2026-06-30) [DISCARD: Redundant copy of p4.] quote: "Over the last 12 months, more than 2,000 enterprises consumed over 100 billion tokens."
  - p58 Token threshold per Cloud customer (each of nearly 500 customers), last year = **1,000,000,000,000** tokens per customer per year (2025-07-01..2026-06-30) [DISCARD: Redundant copy of p5.] quote: "Nearly 500 Cloud customers have each processed more than 1 trillion tokens in the last year"
  - p59 Token threshold per enterprise (each of more than 2,000), last 12 months = **100,000,000,000** tokens per enterprise per year (2025-07-01..2026-06-30) [DISCARD: Redundant copy of p6.] quote: "Over the last 12 months, more than 2,000 enterprises consumed over 100 billion tokens."
  - p60 Google Cloud backlog, Q2 2026 = **514,000,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Redundant copy of p11.] quote: "And Cloud backlog grew to $514 billion."
  - p61 Google Cloud revenue growth year-over-year, Q2 2026 = **82** % (2026-04-01..2026-06-30) [keep: ] quote: "Cloud revenue grew 82%, powered by strong demand for AI infrastructure and AI solutions."
  - p62 Share of Fortune 100 using Gemini Enterprise = **90** % (2026-04-01..2026-06-30) [keep: ] quote: "It's great to see the wide adoption of Gemini Enterprise, with nearly 90% of the Fortune 100 using it."
  - p63 Agent Development Kit total downloads, Q2 2026 = **70,000,000** downloads (2026-04-01..2026-06-30) [DISCARD: Redundant copy of p10.] quote: "In Q2, Agent Development Kit, our framework for building and deploying enterprise AI agents, reached nearly 70 million total downloads."
  - p64 Antigravity weekly active users = **2,400,000** weekly active users (2026-04-01..2026-06-30) [DISCARD: Redundant copy of p25.] quote: "It has more than 2.4 million weekly active users."
  - p65 Gemma 4 model downloads since April launch = **300,000,000** downloads (2026-04-01..2026-06-30) [DISCARD: Redundant copy of p9.] quote: "And our latest Gemma 4 models have been downloaded over 300 million times since launching in April."
- `https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q1-2026/` -> **live_dated** (page date 2026-04-29); points raw/verified 15/12
  - p66 Alphabet first-party models tokens processed per minute via direct API use by cu = **16,000,000,000** tokens per minute (2026-01-01..2026-03-31) [keep: ] quote: "Our first-party models now process more than 16 billion tokens per minute via direct API use by our customers, up from 10 billion last quarter."
  - p67 Google Cloud customers processing over 1 trillion tokens each, trailing twelve m = **330** customers (2025-04-01..2026-03-31) [keep: ] quote: "Over the past twelve months, 330 Google Cloud customers each processed over 1 trillion tokens."
  - p68 Google Cloud customers reaching the 10-trillion-token milestone, trailing twelve = **35** as written "Thirty-five", value check pending customers (2025-04-01..2026-03-31) [keep: ] quote: "Thirty-five reached the 10-trillion-token milestone."
  - p69 Google Cloud revenue, Q1 2026 = **20,000,000,000** USD (2026-01-01..2026-03-31) [keep: ] quote: "Revenue grew 63%, exceeding $20 billion for the first time, and our backlog nearly doubled quarter-on-quarter to over $460 billion."
  - p70 Google Cloud backlog, Q1 2026 = **460,000,000,000** USD (2026-01-01..2026-03-31) [keep: ] quote: "Revenue grew 63%, exceeding $20 billion for the first time, and our backlog nearly doubled quarter-on-quarter to over $460 billion."
  - p71 Google Cloud revenue growth year-over-year, Q1 2026 = **63** % (2026-01-01..2026-03-31) [keep: ] quote: "Revenue grew 63%, exceeding $20 billion for the first time, and our backlog nearly doubled quarter-on-quarter to over $460 billion."
  - p72 Gemini Enterprise paid monthly active users growth quarter-over-quarter, Q1 2026 = **40** % (2026-01-01..2026-03-31) [keep: ] quote: "Gemini Enterprise is seeing tremendous momentum, with 40% growth quarter-over-quarter in paid monthly active users."
  - p73 Revenue from Google Cloud products built on gen AI models growth year-over-year, = **800** % (2026-01-01..2026-03-31) [keep: ] quote: "In Q1, revenue from products built on our gen AI models grew nearly 800% year-over-year."
  - p74 Gemini Enterprise seats sold with partners growth year-over-year, Q1 2026 = **9** multiple (2026-01-01..2026-03-31) [keep: ] quote: "We saw 9x year-over-year growth both in seats sold with partners, and in the number of partners adopting it for internal use."
  - p75 Gemini-powered workflows in BigQuery growth year-over-year, Q1 2026 = **30** multiple (2026-01-01..2026-03-31) [keep: ] quote: "Our strength with BigQuery and Gemini Enterprise has led Gemini-powered workflows in BigQuery to grow over 30X year-over-year."
  - p76 Google Cloud new customer acquisition growth versus same period last year, Q1 20 = **2** as written "doubling", value check pending multiple (2026-01-01..2026-03-31) [keep: ] quote: "Winning new customers faster, with new customer acquisition doubling compared to the same period last year."
  - p77 Existing Google Cloud customers' spend above initial commitments, Q1 2026 = **45** % (2026-01-01..2026-03-31) [keep: ] quote: "And we are deepening relationships with existing customers, with customers outpaced their initial commitments by 45%, accelerating over last quarter."
- `https://megaoneai.com/launches/google-io-2026-agentic-gemini-era/` -> **live_dated** (page date 2026-05-19); points raw/verified 8/5
  - p78 Year-over-year growth multiple in Google total token volume (I/O 2026 vs I/O 202 = **7** multiple (ratio of tokens per month) (2025-05-01..2026-05-31) [keep: ] quote: "Token volume grew 7x from approximately 480 trillion tokens per month at last year's I/O."
  - p79 Cumulative growth multiple in Google total token volume (I/O 2026 vs two years p = **330** multiple (ratio of tokens per month) (2024-05-01..2026-05-31) [keep: ] quote: "up roughly 330x from 9.7 trillion tokens per month two years ago"
  - p80 Developers building monthly with Google's models, announced at Google I/O 2026 = **8,500,000** developers (2026-05-01..2026-05-31) [keep: ] quote: "Over 8.5 million developers are building monthly with Google's models"
  - p81 Google model APIs tokens processed per minute, announced at Google I/O 2026 = **19,000,000,000** tokens per minute (2026-05-01..2026-05-31) [DISCARD: Redundant copy of p82 (19B I/O 2026).] quote: "model APIs process roughly 19 billion tokens per minute"
  - p82 Google model APIs tokens processed per minute (restated in Technical Details) = **19,000,000,000** tokens per minute (2026-05-01..2026-05-31) [keep: ] quote: "model APIs processing roughly 19 billion tokens per minute"
- `https://www.pymnts.com/news/2026/alphabet-bets-185b-on-gemini-agentic-commerce-and-enterprise-ai/` -> **live_dated** (page date 2026-02-06); points raw/verified 15/14
  - p83 Gemini tokens processed per minute via direct APIs, current quarter (Q4 2025) = **10,000,000,000** tokens per minute (2025-10-01..2025-12-31) [DISCARD: Redundant copy of p28 (10B Q4 2025).] quote: "Gemini now processes more than 10 billion tokens per minute via direct APIs, up from 7 billion last quarter."
  - p84 Gemini tokens processed per minute via direct APIs, prior quarter (Q3 2025) = **7,000,000,000** tokens per minute (2025-07-01..2025-09-30) [DISCARD: Redundant copy of p29 (7B Q3 2025).] quote: "Gemini now processes more than 10 billion tokens per minute via direct APIs, up from 7 billion last quarter."
  - p85 Gemini app monthly active users = **750,000,000** monthly active users (2025-10-01..2025-12-31) [keep: ] quote: "The Gemini app has surpassed 750 million monthly active users."
  - p86 Gemini Enterprise paid seats sold (cumulative, roughly four months) = **8,000,000** paid seats (..2025-12-31) [keep: ] quote: "Gemini Enterprise has already sold more than 8 million paid seats in roughly four months."
  - p87 Alphabet paid subscriptions across consumer services = **325,000,000** paid subscriptions (2025-10-01..2025-12-31) [keep: ] quote: "Alphabet reported more than 325 million paid subscriptions, while Google Cloud backlog climbed to $240 billion, up 55% sequentially."
  - p88 Google Cloud backlog = **240,000,000,000** USD (2025-12-31..2025-12-31) [keep: ] quote: "while Google Cloud backlog climbed to $240 billion, up 55% sequentially."
  - p89 Google Cloud backlog sequential growth = **55** % (2025-10-01..2025-12-31) [keep: ] quote: "while Google Cloud backlog climbed to $240 billion, up 55% sequentially."
  - p90 Organizations using Gemini = **120,000** organizations (2025-10-01..2025-12-31) [keep: ] quote: "More than 120,000 organizations now use Gemini, and Alphabet said 95% of the top 20 software-as-a-service (SaaS) companies and over 80% of the top 100 have integrated Gemini into their products or wor"
  - p91 Share of top 20 SaaS companies that integrated Gemini = **95** % (2025-10-01..2025-12-31) [keep: ] quote: "Alphabet said 95% of the top 20 software-as-a-service (SaaS) companies and over 80% of the top 100 have integrated Gemini into their products or workflows."
  - p92 Share of top 100 SaaS companies that integrated Gemini = **80** % (2025-10-01..2025-12-31) [keep: ] quote: "Alphabet said 95% of the top 20 software-as-a-service (SaaS) companies and over 80% of the top 100 have integrated Gemini into their products or workflows."
  - p93 Creative assets created by advertisers using Gemini in Q4 = **70,000,000** creative assets (2025-10-01..2025-12-31) [keep: ] quote: "Advertisers used Gemini to create nearly 70 million creative assets in Q4 alone."
  - p94 Google Cloud revenue for the quarter = **17,700,000,000** USD (2025-10-01..2025-12-31) [keep: ] quote: "Google Cloud revenue rose 48% to $17.7 billion, supported by enterprise AI infrastructure and solutions."
  - p95 Google Cloud revenue year-over-year growth = **48** % (2025-10-01..2025-12-31) [keep: ] quote: "Google Cloud revenue rose 48% to $17.7 billion, supported by enterprise AI infrastructure and solutions."
  - p96 Reduction in Gemini serving costs in 2025 from model optimization = **78** % (2025-01-01..2025-12-31) [keep: ] quote: "from model optimization that reduced Gemini serving costs by 78% in 2025 to broader productivity initiatives across engineering and finance."
- dropped by code checks: 9 (quote not found verbatim in page (elisions must skip <= 150 chars within one sentence): 1; period_end missing or unparseable: 3; period year 2025 does not appear in the page text or URL (likely mis-dated): 2; number: unknown scale word 'quadrillion': 1; period year 2024 does not appear in the page text or URL (likely mis-dated): 1; period_end 2026-12-31 after as_of: 1)

### d3 [capacity_consumption] TPU/GPU compute capacity and inference utilisation

Hypothesis: Token throughput is bounded by Alphabet's deployed inference compute (TPUs/GPUs), utilisation, and tokens per chip-second. Estimating installed AI accelerator capacity, share devoted to first-party Gemini inference, utilisation, and tokens/sec per chip gives an independent physical upper bound and central estimate.

Queries issued by the searcher: Google TPU installed base estimate 2026 units; Gemini inference tokens per second per TPU benchmark; Alphabet Q2 2026 earnings capex raised 2026 capital expenditure TPU; Epoch AI Google 3.8 million TPUs 1.3 million GPUs analysis FT April 2026

- `https://inferencex.semianalysis.com/zh/blog/tpu-inferencex-full-steam` -> **live_dated** (page date 2026-09-07); points raw/verified 15/0
- `https://tbreak.com/google-ai-compute-power-global-dominance/` -> **live_dated** (page date 2026-07-04); points raw/verified 5/0
- `https://www.trendforce.com/news/2026/07/23/news-google-raises-2026-capex-guidance-again-above-us200b-free-cash-flow-turns-negative-for-first-time/` -> **live_dated** (page date 2026-07-23); points raw/verified 12/8
  - p97 Alphabet quarterly free cash flow (negative, first time in history) = **5,900,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "free cash flow falling to negative US$5.9 billion in the quarter"
  - p98 Alphabet net cash from operating activities, trailing 12-month basis = **39,100,000,000** USD (2025-07-01..2026-06-30) [keep: ] quote: "net cash from operating activities still rose 41% year over year to US$39.1 billion on a trailing 12-month basis"
  - p99 Alphabet property and equipment purchases in the quarter = **44,900,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "property and equipment purchases doubled to US$44.9 billion"
  - p100 Google Cloud revenue in the quarter = **24,800,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "Google Cloud revenue surged 82% year over year to US$24.8 billion"
  - p101 Google Cloud operating margin in the quarter = **35.6** % (2026-04-01..2026-06-30) [keep: ] quote: "the segment's operating margin expanded to 35.6% from 20.7% a year earlier"
  - p102 Alphabet total revenue in the quarter = **119,800,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "Total revenue reached US$119.8 billion, up 24% year over year"
  - p103 Alphabet operating income in the quarter = **40,800,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "Operating income climbed 30% to US$40.8 billion"
  - p104 Alphabet operating margin in the quarter = **34** % (2026-04-01..2026-06-30) [keep: ] quote: "the operating margin expanded to 34.0% from 32.4% a year earlier"
- `https://www.ainvest.com/es/stocks/NASDAQ-GOOG/financials/earnings/` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- dropped by code checks: 24 (period_end missing or unparseable: 20; period_end 2026-12-31 after as_of: 4)

### d4 [base_rates] Developer/API customer base and per-customer usage

Hypothesis: Direct API token rate = number of active API customers/keys × average tokens per customer per minute. Developer counts (Gemini API developers, AI Studio users) times average usage per developer gives a bottom-up cross-check; average usage is highly skewed, so this mainly bounds the low end.

Queries issued by the searcher: Gemini API developers million 2026; Google AI Studio active developers 2026; Alphabet Q2 2026 earnings call Gemini models 22 billion API tokens per minute; Gemini API pricing per million tokens 2026 Gemini 3.5 Flash input output price

- `https://www.gweb-uniblog-publish-prod.appspot.com/company-news/inside-google/message-ceo/alphabet-earnings-q2-2026/` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://nagalandpost.com/8-5-million-developers-use-google-ai-monthly-190-billion-capex-planned-pichai/` -> **live_dated** (page date 2026-05-20); points raw/verified 7/0
- `https://9to5google.com/2026/07/22/alphabet-q2-2026-earnings/` -> **live_dated** (page date 2026-07-22); points raw/verified 15/15
  - p105 Gemini models API tokens processed per minute, Alphabet Q2 2026 disclosure = **22,000,000,000** API tokens per minute (2026-04-01..2026-06-30) [DISCARD: Redundant copy of p1.] quote: "Gemini models now process 22 billion API tokens per minute"
  - p106 Gemini App monthly active users, Q2 2026 = **950,000,000** monthly active users (2026-04-01..2026-06-30) [keep: ] quote: "the Gemini App has 950 million monthly active users"
  - p107 Share of Fortune 100 using Gemini Enterprise, Q2 2026 = **90** % (2026-04-01..2026-06-30) [keep: ] quote: "wide adoption of Gemini Enterprise, with nearly 90% of the Fortune 100 using it"
  - p108 Alphabet total revenue, Q2 2026 = **119,800,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "Alphabet today announced Q2 2026 earnings with $119.8 billion in revenue"
  - p109 Alphabet revenue year-over-year growth, Q2 2026 = **24** % (2026-04-01..2026-06-30) [keep: ] quote: "Revenue is up 24% from $96.4 billion in Q2 2025"
  - p110 Alphabet revenue, Q2 2025 = **96,400,000,000** USD (2025-04-01..2025-06-30) [keep: ] quote: "Revenue is up 24% from $96.4 billion in Q2 2025"
  - p111 Alphabet operating income, Q2 2026 = **40,770,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "with operating income at $40.77 billion"
  - p112 Alphabet net income, Q2 2026 = **112,100,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "net income of $112.1 billion for this quarter"
  - p113 Alphabet net income, Q2 2025 = **28,200,000,000** USD (2025-04-01..2025-06-30) [keep: ] quote: "(versus $28.2 billion a year ago)"
  - p114 Alphabet revenue, prior quarter (Q1 2026) = **109,900,000,000** USD (2026-01-01..2026-03-31) [keep: ] quote: "Alphabet reported $109.9 billion in revenue and $62.58 billion in net income last quarter"
  - p115 Alphabet net income, prior quarter (Q1 2026) = **62,580,000,000** USD (2026-01-01..2026-03-31) [keep: ] quote: "Alphabet reported $109.9 billion in revenue and $62.58 billion in net income last quarter"
  - p116 Google Cloud revenue, Q2 2026 = **24,770,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "while Cloud reported $24.77 billion (compared to $13.62 billion)"
  - p117 Google Cloud revenue, Q2 2025 = **13,620,000,000** USD (2025-04-01..2025-06-30) [keep: ] quote: "while Cloud reported $24.77 billion (compared to $13.62 billion)"
  - p118 Google Cloud revenue year-over-year growth, Q2 2026 = **82** % (2026-04-01..2026-06-30) [keep: ] quote: "Google Cloud revenues accelerating to 82% growth"
  - p119 YouTube unique viewers of World Cup-related videos during FIFA World Cup 2026 = **1,700,000,000** unique viewers (..) [keep: ] quote: "over 1.7 billion unique viewers watching World Cup-related videos during the FIFA World Cup 2026TM"
- `https://btw.media/zh/google-cloud-ai` -> **live_dated** (page date 2026-08-17); points raw/verified 5/5
  - p120 Developers using Google Cloud AI tools (Vertex AI and AI Studio), cumulative cou = **7,000,000** developers (..) [DISCARD: Redundant developer count, different scope, adds no new information.] quote: "超过 700 万开发者现在使用 Google Cloud 的 AI 工具"
  - p121 Developers using Vertex AI and AI Studio, cumulative count reported by Google Cl = **7,000,000** developers (..) [DISCARD: Redundant copy of p120.] quote: "Google Cloud 的 Maureen Costello 报告称,超过 700 万开发者正在使用 Vertex AI 和 AI Studio。"
  - p122 Gemini usage growth multiple as stated at Google Cloud London Summit = **40** times (growth multiple) (..) [DISCARD: Ambiguous '40' growth multiple with unclear definition; unusable.] quote: "Gemini 使用量增长 40 倍"
  - p123 Monthly AI-assisted actions in Google Workspace = **2,000,000,000** assists per month (..) [DISCARD: Workspace AI assists, different scope, not usable for direct-API token rate.] quote: "AI 每月辅助 Workspace 用户超过 20 亿次"
  - p124 Monthly AI assists in Google Workspace (second mention) = **2,000,000,000** assists per month (..) [DISCARD: Redundant copy of p123.] quote: "AI 每月在 Google Workspace 中提供超过 20 亿次辅助"
- dropped by code checks: 7 (period year 2026 does not appear in the page text or URL (likely mis-dated): 6; period_end 2026-12-31 after as_of: 1)

### d5 [forecasts_markets] Analyst forecasts and prediction markets on Alphabet AI usage

Hypothesis: Sell-side analysts and prediction markets may publish forecasts of Alphabet's next disclosed token rate or AI usage growth. These provide an independent expectation and a dispersion range, though they may share the same underlying disclosure history.

Queries issued by the searcher: Alphabet Q3 2026 earnings preview Gemini tokens per minute analysts; "tokens per minute" Gemini models Alphabet earnings call 22 billion; "tokens per minute" Alphabet Q3 2026 earnings preview October 2026 Gemini expected; prediction market Gemini API tokens per minute Alphabet AI metric contract

- `https://en.globes.co.il/en/zarticle.aspx?id=2997715` -> **live_dated** (page date 2026-10-01); points raw/verified 0/0
- `https://247wallst.com/investing/2026/10/16/alphabets-cloud-surge-and-ai-dominance-overshadow-capex-fears-and-keep-me-buying/` -> **live_dated** (page date 2026-10-16); points raw/verified 15/12
  - p125 Gemini models API tokens processed per minute (Q2 2026 disclosure) = **22,000,000,000** tokens per minute (2026-04-01..2026-06-30) [DISCARD: Redundant copy of p1.] quote: "Nearly 90% of the Fortune 100 use Gemini Enterprise, and Gemini models process 22 billion API tokens per minute."
  - p126 Google Cloud revenue growth rate, Q3 2025 = **34** % (2025-07-01..2025-09-30) [keep: ] quote: "Google Cloud revenue grew 34% in Q3 2025, 48% in Q4, 63% in Q1 2026 and 82% in Q2 2026, when it reached $24.77 billion."
  - p127 Google Cloud revenue growth rate, Q4 2025 = **48** % (2025-10-01..2025-12-31) [keep: ] quote: "Google Cloud revenue grew 34% in Q3 2025, 48% in Q4, 63% in Q1 2026 and 82% in Q2 2026, when it reached $24.77 billion."
  - p128 Google Cloud revenue growth rate, Q1 2026 = **63** % (2026-01-01..2026-03-31) [keep: ] quote: "Google Cloud revenue grew 34% in Q3 2025, 48% in Q4, 63% in Q1 2026 and 82% in Q2 2026, when it reached $24.77 billion."
  - p129 Google Cloud revenue growth rate, Q2 2026 = **82** % (2026-04-01..2026-06-30) [keep: ] quote: "Google Cloud revenue grew 34% in Q3 2025, 48% in Q4, 63% in Q1 2026 and 82% in Q2 2026, when it reached $24.77 billion."
  - p130 Google Cloud revenue, Q2 2026 = **24,770,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "Google Cloud revenue grew 34% in Q3 2025, 48% in Q4, 63% in Q1 2026 and 82% in Q2 2026, when it reached $24.77 billion."
  - p131 Google Cloud backlog, Q1 (nearly doubled from prior quarter) = **460,000,000,000** USD (2026-01-01..2026-03-31) [keep: ] quote: "the cloud backlog nearly doubled from the prior quarter to over $460 billion in Q1."
  - p132 Alphabet total revenue, Q2 = **119,800,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "Total Q2 revenue came in at $119.80 billion, up 24.23%."
  - p133 Alphabet total revenue growth, Q2 = **24.23** % (2026-04-01..2026-06-30) [keep: ] quote: "Total Q2 revenue came in at $119.80 billion, up 24.23%."
  - p134 Alphabet Q2 capex = **44,920,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "Q2 capex reached $44.92 billion, up 100.14%, which pushed free cash flow to negative $5.86 billion."
  - p135 Alphabet operating cash flow, Q2 = **39,070,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "Operating cash flow rose 40.8% to $39.07 billion in Q2, and debt-to-equity is only 0.143."
  - p136 Alphabet operating margin, Q2 = **34** % (2026-04-01..2026-06-30) [keep: ] quote: "Operating margin expanded by 2 points to 34%, and operating income rose 30.38% to $40.77 billion."
- `https://za.investing.com/news/stock-market-news/alphabet-stock-analysis-stalled-near-200day-average-ahead-of-q3-earnings-93CH-4509218` -> **dropped** (live fetch blocked by robots.txt); points raw/verified -/-
- `https://9to5google.com/2026/07/22/alphabet-q2-2026-earnings/` -> **live_dated** (page date 2026-07-22); points raw/verified 15/14
  - p137 Gemini models API tokens processed per minute, Q2 2026 disclosure (analogous pri = **22,000,000,000** tokens per minute (2026-04-01..2026-06-30) [DISCARD: Redundant copy of p1.] quote: "Gemini models now process 22 billion API tokens per minute and the Gemini App has 950 million monthly active users."
  - p138 Gemini App monthly active users, Q2 2026 = **950,000,000** monthly active users (2026-04-01..2026-06-30) [keep: ] quote: "Gemini models now process 22 billion API tokens per minute and the Gemini App has 950 million monthly active users."
  - p139 Alphabet total revenue, Q2 2026 = **119,800,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "Alphabet today announced Q2 2026 earnings with $119.8 billion in revenue."
  - p140 Alphabet revenue year-over-year growth rate, Q2 2026 = **24** % (2026-04-01..2026-06-30) [keep: ] quote: "Revenue is up 24% from $96.4 billion in Q2 2025, with operating income at $40.77 billion and net income of $112.1 billion for this quarter"
  - p141 Alphabet revenue, Q2 2025 (prior-year comparison) = **96,400,000,000** USD (2025-04-01..2025-06-30) [keep: ] quote: "Revenue is up 24% from $96.4 billion in Q2 2025, with operating income at $40.77 billion and net income of $112.1 billion for this quarter"
  - p142 Alphabet operating income, Q2 2026 = **40,770,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "Revenue is up 24% from $96.4 billion in Q2 2025, with operating income at $40.77 billion and net income of $112.1 billion for this quarter"
  - p143 Alphabet net income, Q2 2026 = **112,100,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "with operating income at $40.77 billion and net income of $112.1 billion for this quarter (versus $28.2 billion a year ago)"
  - p144 Alphabet net income, Q2 2025 (prior-year comparison) = **28,200,000,000** USD (2025-04-01..2025-06-30) [keep: ] quote: "with operating income at $40.77 billion and net income of $112.1 billion for this quarter (versus $28.2 billion a year ago)"
  - p145 Alphabet revenue, prior quarter (Q1 2026) = **109,900,000,000** USD (2026-01-01..2026-03-31) [keep: ] quote: "For comparison, Alphabet reported $109.9 billion in revenue and $62.58 billion in net income last quarter."
  - p146 Alphabet net income, prior quarter (Q1 2026) = **62,580,000,000** USD (2026-01-01..2026-03-31) [keep: ] quote: "For comparison, Alphabet reported $109.9 billion in revenue and $62.58 billion in net income last quarter."
  - p147 Google Cloud revenue year-over-year growth rate, Q2 2026 = **82** % (2026-04-01..2026-06-30) [keep: ] quote: "Alphabet revenues growing 24% year-over-year and Google Cloud revenues accelerating to 82% growth, driven by demand for AI infrastructure and AI solutions."
  - p148 Share of Fortune 100 using Gemini Enterprise, Q2 2026 = **90** % (2026-04-01..2026-06-30) [keep: ] quote: "It's great to see wide adoption of Gemini Enterprise, with nearly 90% of the Fortune 100 using it."
  - p149 YouTube ad revenue, Q2 2026 = **11,060,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "In Q2 2026, YouTube ad revenue was $11.06 billion (versus $9.79 billion a year ago), while Cloud reported $24.77 billion (compared to $13.62 billion)."
  - p150 Google Cloud revenue, Q2 2026 = **24,770,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "In Q2 2026, YouTube ad revenue was $11.06 billion (versus $9.79 billion a year ago), while Cloud reported $24.77 billion (compared to $13.62 billion)."
- dropped by code checks: 4 (period_end missing or unparseable: 3; period_end 2026-12-31 after as_of: 1)

### d6 [shocks] Product launches, pricing changes, and model releases affecting API demand

Hypothesis: New model releases (e.g. Gemini 3.x), price cuts, free-tier changes, or major enterprise deals between Q2 and Q3 2026 could accelerate or dampen token growth relative to the prior trend. Identifying dated events and their magnitude adjusts the extrapolation from d1.

Queries issued by the searcher: Gemini models process 22 billion API tokens per minute Q2 2026 Alphabet earnings; Gemini 3 launch API pricing 2026; Gemini 3.7 Flash launch date August 2026 Google announcement cheaper tokens; Gemini 3.8 Flash release October 2026 Google intro pricing

- `https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q2-2026/` -> **live_dated** (page date 2026-07-22); points raw/verified 15/14
  - p151 Gemini model APIs tokens processed per minute, Q2 2026 (current quarter) = **22,000,000,000** tokens per minute (2026-04-01..2026-06-30) [DISCARD: Redundant copy of p1.] quote: "Our model APIs are now processing approximately 22 billion tokens per minute."
  - p152 Gemini model APIs tokens processed per minute, prior quarter (Q1 2026) = **16,000,000,000** tokens per minute (2026-01-01..2026-03-31) [DISCARD: Redundant copy of p2.] quote: "That's up from 16 billion just a quarter ago."
  - p153 Developers building monthly with Gemini models across APIs and developer product = **9,000,000** developers (2026-04-01..2026-06-30) [DISCARD: Redundant copy of p7.] quote: "More than 9 million developers are building each month with our models across our APIs and key developer products."
  - p154 Gemma 4 model downloads since April launch = **300,000,000** downloads (2026-04-01..2026-06-30) [DISCARD: Redundant copy of p9.] quote: "our latest Gemma 4 models have been downloaded over 300 million times since launching in April"
  - p155 Increase in daily active users creating videos on Gemini app since Omni launch a = **40** % (2026-05-01..2026-06-30) [keep: ] quote: "Since launching at I/O in May, there's been a 40% increase in daily active users creating videos on the Gemini app."
  - p156 Gemini app monthly active users = **950,000,000** monthly active users (2026-04-01..2026-06-30) [keep: ] quote: "the Gemini app, which now has 950 million monthly active users"
  - p157 AI Mode monthly active users since global expansion last October = **1,000,000,000** monthly active users (..2026-06-30) [keep: ] quote: "Since expanding AI Mode globally last October, we've surpassed 1 billion monthly active users."
  - p158 Antigravity weekly active users = **2,400,000** weekly active users (2026-04-01..2026-06-30) [keep: ] quote: "It has more than 2.4 million weekly active users."
  - p159 Agent Development Kit cumulative downloads, Q2 = **70,000,000** downloads (2026-04-01..2026-06-30) [keep: ] quote: "In Q2, Agent Development Kit, our framework for building and deploying enterprise AI agents, reached nearly 70 million total downloads."
  - p160 Cloud customers each processing more than 1 trillion tokens in the last year (co = **500** Cloud customers (2025-07-01..2026-06-30) [DISCARD: Redundant copy of p3.] quote: "Nearly 500 Cloud customers have each processed more than 1 trillion tokens in the last year"
  - p161 Enterprises consuming over 100 billion tokens in the last 12 months (count) = **2,000** enterprises (2025-07-01..2026-06-30) [DISCARD: Redundant copy of p4.] quote: "Over the last 12 months, more than 2,000 enterprises consumed over 100 billion tokens."
  - p162 Fortune 100 share using Gemini Enterprise = **90** % (2026-04-01..2026-06-30) [keep: ] quote: "nearly 90% of the Fortune 100 using it"
  - p163 Cloud backlog = **514,000,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "And Cloud backlog grew to $514 billion."
  - p164 Cloud revenue year-over-year growth, Q2 2026 = **82** % (2026-04-01..2026-06-30) [keep: ] quote: "Cloud revenue grew 82%, powered by strong demand for AI infrastructure and AI solutions."
- `https://www.thehindu.com/sci-tech/technology/google-unveils-gemini-37-flash-ai-model-for-coding-agent-workflows/article71343995.ece` -> **live_dated** (page date 2026-08-14); points raw/verified 5/2
  - p165 Gap between Gemini 3.7 Flash release and Gemini 3.6 Flash release = **3** as written "three weeks", value check pending weeks (2026-08-14..2026-08-14) [keep: ] quote: "Gemini 3.7 Flash is released three weeks after Gemini 3.6 Flash."
  - p166 Countries where Gemini Spark subscription AI agent service is available to Googl = **160** countries (2026-08-14..2026-08-14) [keep: ] quote: "available to Google AI Pro and Ultra customers in more than 160 countries"
- `https://www.cnbc.com/2026/07/22/google-earnings-q2-goog-live-updates.html` -> **live_dated** (page date 2026-07-22); points raw/verified 15/13
  - p167 Gemini models token processing rate disclosed with Alphabet Q2 2026 results = **22,000,000,000** tokens per minute (2026-04-01..2026-06-30) [DISCARD: Redundant copy of p1.] quote: "Google said its Gemini App now has 950 million monthly active users and can process 22 billion tokens per minute."
  - p168 Gemini App monthly active users disclosed with Alphabet Q2 2026 results = **950,000,000** monthly active users (2026-04-01..2026-06-30) [DISCARD: Redundant copy of p8.] quote: "Google said its Gemini App now has 950 million monthly active users and can process 22 billion tokens per minute."
  - p169 Number of cheaper Gemini models debuted in the week of Alphabet Q2 2026 results = **3** as written "three", value check pending models (2026-07-01..2026-07-31) [keep: ] quote: "Google, which debuted three cheaper Gemini models this week, faced blowback earlier in the month after reportedly delaying the launch of its Gemini 3.5 Pro model"
  - p170 Google Antigravity AI coding tool weekly active users = **2,400,000** weekly active users (2026-04-01..2026-06-30) [DISCARD: Redundant copy of p25.] quote: "Google's Antigravity AI coding tool now has 2.4 million weekly active users"
  - p171 Alphabet Q2 2026 revenue = **119,800,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "Revenue: $119.80 billion vs $116.93 billion expected by LSEG"
  - p172 Alphabet Q2 2026 revenue expected by LSEG = **116,930,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "Revenue: $119.80 billion vs $116.93 billion expected by LSEG"
  - p173 Alphabet Q2 2026 adjusted earnings per share = **2.85** USD per share (2026-04-01..2026-06-30) [keep: ] quote: "Earnings per share: $2.85 adj. vs $2.89 expected by LSEG"
  - p174 Alphabet Q2 2026 adjusted earnings per share expected by LSEG = **2.89** USD per share (2026-04-01..2026-06-30) [keep: ] quote: "Earnings per share: $2.85 adj. vs $2.89 expected by LSEG"
  - p175 Alphabet Q2 2026 capex = **44,900,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "Alphabet's capex grew 100% year-over-year to $44.9 billion in Q2"
  - p176 Alphabet Q2 2026 capex year-over-year growth = **100** % (2026-04-01..2026-06-30) [keep: ] quote: "Alphabet's capex grew 100% year-over-year to $44.9 billion in Q2"
  - p177 Google Cloud Q2 2026 revenue = **24,800,000,000** USD (2026-04-01..2026-06-30) [DISCARD: Redundant copy of p12.] quote: "Google's cloud revenue jumped 82% to $24.8 billion"
  - p178 Google Cloud Q2 2026 revenue growth = **82** % (2026-04-01..2026-06-30) [DISCARD: Redundant copy of p61.] quote: "Google's cloud revenue jumped 82% to $24.8 billion"
  - p179 Alphabet Q2 2026 search revenue growth = **17** % (2026-04-01..2026-06-30) [keep: ] quote: "Search revenue grew 17%, in-line with expectations"
- `https://www.cloudzero.com/blog/google-vertex-ai-pricing/` -> **live_dated** (page date 2026-09-30); points raw/verified 15/2
  - p180 Gemini 2.5 Flash-Lite input price per million tokens (until October 16 retiremen = **0.1** USD per million input tokens (..2026-10-16) [DISCARD: Model pricing, not a token-rate input; irrelevant to target.] quote: "\| Gemini 2.5 Flash-Lite \| $0.10 \| $0.40 \| The floor, until October 16 \|"
  - p181 Gemini 2.5 Flash-Lite output price per million tokens (until October 16 retireme = **0.4** USD per million output tokens (..2026-10-16) [DISCARD: Model pricing, not a token-rate input; irrelevant to target.] quote: "\| Gemini 2.5 Flash-Lite \| $0.10 \| $0.40 \| The floor, until October 16 \|"
- dropped by code checks: 19 (period_end missing or unparseable: 8; period_end 2026-12-31 after as_of: 8; period_end 2027-01-01 after as_of: 2; value_as_written not in quote as a whole number: 1)

### b1 [own_history] Alphabet disclosure cadence

Hypothesis: If Alphabet has disclosed any intra-Q3 2026 token-rate reading (e.g. at a September developer event or Cloud summit), it would pin the within-quarter trajectory and sharply reduce extrapolation error for the Q3 endpoint.

Queries issued by the searcher: Alphabet Q2 2026 Gemini models 22 billion API tokens per minute; Google tokens per minute Gemini API September 2026 developer event; "tokens per minute" Google Gemini August 2026 Pichai model APIs; "billion tokens per minute" Google October 2026; Google Cloud Next 2026 October keynote tokens per minute Gemini API

- `https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q2-2026/?trk=article-ssr-frontend-pulse_little-text-block` -> **live_dated** (page date 2026-07-22); points raw/verified 15/14
  - p182 Alphabet model APIs tokens processed per minute, Q2 2026 (current quarter) = **22,000,000,000** tokens per minute (2026-04-01..2026-06-30) [keep: ] quote: "Our model APIs are now processing approximately 22 billion tokens per minute."
  - p183 Alphabet model APIs tokens processed per minute, prior quarter (Q1 2026) = **16,000,000,000** tokens per minute (2026-01-01..2026-03-31) [keep: ] quote: "That's up from 16 billion just a quarter ago."
  - p184 Developers building monthly with Alphabet models across APIs and key developer p = **9,000,000** developers per month (2026-04-01..2026-06-30) [keep: ] quote: "More than 9 million developers are building each month with our models across our APIs and key developer products."
  - p185 Cloud customers each processing more than 1 trillion tokens in the last year = **500** Cloud customers (2025-07-01..2026-06-30) [keep: ] quote: "Nearly 500 Cloud customers have each processed more than 1 trillion tokens in the last year"
  - p186 Enterprises consuming over 100 billion tokens over the last 12 months = **2,000** enterprises (2025-07-01..2026-06-30) [keep: ] quote: "Over the last 12 months, more than 2,000 enterprises consumed over 100 billion tokens."
  - p187 Gemma 4 model downloads since April launch = **300,000,000** downloads (2026-04-01..2026-06-30) [keep: ] quote: "our latest Gemma 4 models have been downloaded over 300 million times since launching in April"
  - p188 Antigravity weekly active users = **2,400,000** weekly active users (2026-04-01..2026-06-30) [keep: ] quote: "It has more than 2.4 million weekly active users."
  - p189 Gemini app monthly active users = **950,000,000** monthly active users (2026-04-01..2026-06-30) [keep: ] quote: "the Gemini app, which now has 950 million monthly active users"
  - p190 AI Mode monthly active users since global expansion = **1,000,000,000** monthly active users (..2026-06-30) [keep: ] quote: "Since expanding AI Mode globally last October, we've surpassed 1 billion monthly active users."
  - p191 Agent Development Kit total downloads in Q2 = **70,000,000** total downloads (2026-04-01..2026-06-30) [keep: ] quote: "In Q2, Agent Development Kit, our framework for building and deploying enterprise AI agents, reached nearly 70 million total downloads."
  - p192 Cloud backlog = **514,000,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "And Cloud backlog grew to $514 billion."
  - p193 Cloud revenue growth year-over-year, Q2 2026 = **82** % (2026-04-01..2026-06-30) [keep: ] quote: "Cloud revenue grew 82%, powered by strong demand for AI infrastructure and AI solutions."
  - p194 Fortune 100 share using Gemini Enterprise = **90** % (2026-04-01..2026-06-30) [keep: ] quote: "nearly 90% of the Fortune 100 using it"
  - p195 Increase in daily active users creating videos on Gemini app since I/O launch in = **40** % (2026-05-01..2026-06-30) [keep: ] quote: "there's been a 40% increase in daily active users creating videos on the Gemini app"
- `https://www.nasdaq.com/articles/alphabet-q2-earnings-call-highlights` -> **dropped** (live http 403); points raw/verified -/-
- `https://www.nasdaq.com/articles/alphabet-q2-earnings-call-highlights-ai-growth-cloud-momentum` -> **dropped** (live http 403); points raw/verified -/-
- `https://9to5google.com/2026/07/22/alphabet-q2-2026-earnings/?utm_campaign=DonanimHaber&utm_medium=referral&utm_source=DonanimHaber` -> **live_dated** (page date 2026-07-22); points raw/verified 15/15
  - p196 Gemini models API tokens processed per minute, Q2 2026 disclosure = **22,000,000,000** API tokens per minute (2026-04-01..2026-06-30) [keep: ] quote: "Gemini models now process 22 billion API tokens per minute"
  - p197 Gemini App monthly active users, Q2 2026 = **950,000,000** monthly active users (2026-04-01..2026-06-30) [keep: ] quote: "the Gemini App has 950 million monthly active users"
  - p198 Share of Fortune 100 using Gemini Enterprise, Q2 2026 = **90** % (2026-04-01..2026-06-30) [keep: ] quote: "wide adoption of Gemini Enterprise, with nearly 90% of the Fortune 100 using it"
  - p199 Alphabet total revenue, Q2 2026 = **119,800,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "Alphabet today announced Q2 2026 earnings with $119.8 billion in revenue."
  - p200 Alphabet revenue year-over-year growth, Q2 2026 = **24** % (2026-04-01..2026-06-30) [keep: ] quote: "Revenue is up 24% from $96.4 billion in Q2 2025"
  - p201 Alphabet revenue, Q2 2025 = **96,400,000,000** USD (2025-04-01..2025-06-30) [keep: ] quote: "Revenue is up 24% from $96.4 billion in Q2 2025"
  - p202 Alphabet operating income, Q2 2026 = **40,770,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "with operating income at $40.77 billion"
  - p203 Alphabet net income, Q2 2026 = **112,100,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "net income of $112.1 billion for this quarter"
  - p204 Alphabet net income, Q2 2025 = **28,200,000,000** USD (2025-04-01..2025-06-30) [keep: ] quote: "(versus $28.2 billion a year ago)"
  - p205 Alphabet revenue, prior quarter (Q1 2026) = **109,900,000,000** USD (2026-01-01..2026-03-31) [keep: ] quote: "Alphabet reported $109.9 billion in revenue and $62.58 billion in net income last quarter."
  - p206 Alphabet net income, prior quarter (Q1 2026) = **62,580,000,000** USD (2026-01-01..2026-03-31) [keep: ] quote: "Alphabet reported $109.9 billion in revenue and $62.58 billion in net income last quarter."
  - p207 Google Cloud revenue year-over-year growth, Q2 2026 = **82** % (2026-04-01..2026-06-30) [keep: ] quote: "Google Cloud revenues accelerating to 82% growth"
  - p208 Google Cloud revenue, Q2 2026 = **24,770,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "while Cloud reported $24.77 billion (compared to $13.62 billion)"
  - p209 Google Cloud revenue, Q2 2025 = **13,620,000,000** USD (2025-04-01..2025-06-30) [keep: ] quote: "while Cloud reported $24.77 billion (compared to $13.62 billion)"
  - p210 YouTube unique viewers of World Cup-related videos, Q2 2026 = **1,700,000,000** unique viewers (2026-04-01..2026-06-30) [keep: ] quote: "over 1.7 billion unique viewers watching World Cup-related videos"
- dropped by code checks: 1 (period_end missing or unparseable: 1)

### b2 [related_series] Growth deceleration

Hypothesis: The QoQ growth sequence (7→10→16→22B) is decelerating in absolute increments; a reliable read on Q3 Cloud/AI revenue growth or I/O-to-Q3 token growth would calibrate whether Q3 lands nearer 28B or 32B.

Queries issued by the searcher: Alphabet Q3 2026 Cloud revenue growth; Gemini models process 22 billion API tokens per minute Q2 2026; "tokens per minute" Gemini Q3 2026 Alphabet earnings preview API growth; Alphabet Q3 2026 earnings preview October 28 2026 Gemini AI usage analysts expect

- `https://www.perplexity.ai/finance/GOOG/earnings?eventId=657320` -> **dropped** (live http 403); points raw/verified -/-
- `https://247wallst.com/investing/2026/10/16/alphabets-cloud-surge-and-ai-dominance-overshadow-capex-fears-and-keep-me-buying/` -> **live_dated** (page date 2026-10-16); points raw/verified 15/12
  - p211 Google Cloud revenue growth, Q3 2025 = **34** % (2025-07-01..2025-09-30) [keep: ] quote: "Google Cloud revenue grew 34% in Q3 2025, 48% in Q4, 63% in Q1 2026 and 82% in Q2 2026, when it reached $24.77 billion."
  - p212 Google Cloud revenue growth, Q4 2025 = **48** % (2025-10-01..2025-12-31) [keep: ] quote: "Google Cloud revenue grew 34% in Q3 2025, 48% in Q4, 63% in Q1 2026 and 82% in Q2 2026, when it reached $24.77 billion."
  - p213 Google Cloud revenue growth, Q1 2026 = **63** % (2026-01-01..2026-03-31) [keep: ] quote: "Google Cloud revenue grew 34% in Q3 2025, 48% in Q4, 63% in Q1 2026 and 82% in Q2 2026, when it reached $24.77 billion."
  - p214 Google Cloud revenue growth, Q2 2026 = **82** % (2026-04-01..2026-06-30) [keep: ] quote: "Google Cloud revenue grew 34% in Q3 2025, 48% in Q4, 63% in Q1 2026 and 82% in Q2 2026, when it reached $24.77 billion."
  - p215 Google Cloud revenue, Q2 2026 = **24,770,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "Google Cloud revenue grew 34% in Q3 2025, 48% in Q4, 63% in Q1 2026 and 82% in Q2 2026, when it reached $24.77 billion."
  - p216 Gemini models API tokens processed per minute (Q2 2026 disclosure) = **22,000,000,000** API tokens per minute (2026-04-01..2026-06-30) [keep: ] quote: "Nearly 90% of the Fortune 100 use Gemini Enterprise, and Gemini models process 22 billion API tokens per minute."
  - p217 Google Cloud backlog, Q1 2026 (over) = **460,000,000,000** USD (2026-01-01..2026-03-31) [keep: ] quote: "Customers are signing long commitments: the cloud backlog nearly doubled from the prior quarter to over $460 billion in Q1."
  - p218 Alphabet total revenue, Q2 2026 = **119,800,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "Total Q2 revenue came in at $119.80 billion, up 24.23%."
  - p219 Alphabet total revenue growth, Q2 2026 = **24.23** % (2026-04-01..2026-06-30) [keep: ] quote: "Total Q2 revenue came in at $119.80 billion, up 24.23%."
  - p220 Alphabet Search and other revenue, Q2 2026 = **63,270,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "Search and other brought in $63.27 billion, up 17%, as AI features lifted query growth."
  - p221 Alphabet Search and other revenue growth, Q2 2026 = **17** % (2026-04-01..2026-06-30) [keep: ] quote: "Search and other brought in $63.27 billion, up 17%, as AI features lifted query growth."
  - p222 Alphabet operating margin, Q2 2026 = **34** % (2026-04-01..2026-06-30) [keep: ] quote: "Operating margin expanded by 2 points to 34%, and operating income rose 30.38% to $40.77 billion."
- `https://en.theblockbeats.news/news/63910` -> **live_dated** (page date 2026-10-16); points raw/verified 15/4
  - p223 JPMorgan forecast: Google Cloud Q3 2026 year-over-year revenue growth (raised fo = **100** % (2026-07-01..2026-09-30) [keep: ] quote: "The bank raised its forecast for Google Cloud's year-over-year revenue growth in the third quarter of 2026 from 88% to 100%"
  - p224 JPMorgan prior forecast: Google Cloud Q3 2026 year-over-year revenue growth (bef = **88** % (2026-07-01..2026-09-30) [keep: ] quote: "The bank raised its forecast for Google Cloud's year-over-year revenue growth in the third quarter of 2026 from 88% to 100%"
  - p225 AWS price increase for GPU reserved compute capacity starting October 7 = **15** % (2026-10-07..2026-10-07) [keep: ] quote: "AWS raised prices for GPU reserved compute capacity by 15% starting October 7"
  - p226 Cumulative price rise since start of year for H100/H200 and B200/B300 related re = **57.5** (range 40..75) as written "40% to 75%", value check pending % (2026-01-01..2026-10-07) [keep: ] quote: "prices related to H100/H200 and B200/B300 have cumulatively risen 40% to 75% since the beginning of the year"
- `https://www.beri.net/article/google-cloud-82-percent-growth-enterprise-ai-supply-constraints-2026` -> **live_dated** (page date 2026-08-02); points raw/verified 15/12
  - p227 Alphabet Gemini API tokens processed per minute, Q2 2026 (current) = **22,000,000,000** tokens per minute (2026-04-01..2026-06-30) [keep: ] quote: "Alphabet's Gemini API is now processing approximately 22 billion tokens per minute, up from 16 billion just a quarter ago."
  - p228 Alphabet Gemini API tokens processed per minute, prior quarter (Q1 2026) = **16,000,000,000** tokens per minute (2026-01-01..2026-03-31) [keep: ] quote: "Alphabet's Gemini API is now processing approximately 22 billion tokens per minute, up from 16 billion just a quarter ago."
  - p229 QoQ growth in Gemini API tokens per minute, Q2 2026 = **37** % (2026-04-01..2026-06-30) [keep: ] quote: "why Google's API is processing 22 billion tokens per minute and why that number jumped 37% in a single quarter."
  - p230 Google Cloud revenue, Q2 2026 = **24,800,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "Google cloud just posted $24.8 billion in Q2 2026 revenue - the fastest growth of any major hyperscaler this quarter."
  - p231 Google Cloud revenue growth, Q2 2026 (headline) = **82** % (2026-04-01..2026-06-30) [keep: ] quote: "The headline was 82% revenue growth."
  - p232 Google Cloud operating income, Q2 2026 = **8,800,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "Cloud operating income more than tripled to $8.8 billion."
  - p233 Google Cloud operating margin, Q2 2026 = **35** % (2026-04-01..2026-06-30) [keep: ] quote: "That's a 35% operating margin on a cloud platform that's still in aggressive growth mode."
  - p234 Google Cloud backlog (contracted work not yet delivered), Q2 2026 = **514,000,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "Cloud backlog - the value of contracted work yet to be delivered - reached $514 billion."
  - p235 Alphabet capital expenditures, Q2 2026 = **44,900,000,000** USD (2026-04-01..2026-06-30) [keep: ] quote: "Google spent $44.9 billion on capital expenditures in Q2 2026 alone."
  - p236 Share of Fortune 100 companies actively using Gemini Enterprise = **90** % (2026-04-01..2026-06-30) [keep: ] quote: "Nearly 90% of Fortune 100 companies are actively using Gemini Enterprise."
  - p237 Enterprises consuming over 100 billion tokens in the last year = **2,000** enterprises (2025-07-01..2026-06-30) [keep: ] quote: "More than 2,000 enterprises consumed over 100 billion tokens in the last year."
  - p238 Google Cloud customers processing over 1 trillion tokens each = **500** customers (2025-07-01..2026-06-30) [keep: ] quote: "Nearly 500 Google Cloud customers processed over 1 trillion tokens each."
- dropped by code checks: 17 (period_end missing or unparseable: 2; period_end 2026-12-31 after as_of: 5; period_end 2027-12-31 after as_of: 5; period_end 2028-12-31 after as_of: 4; period_end 2027-06-30 after as_of: 1)

### b3 [capacity_consumption] Physical bound

Hypothesis: An estimate of Alphabet's deployed TPU inference capacity and tokens/sec per chip would provide an independent upper bound and central estimate, resolving whether continued ~30% QoQ growth is physically plausible.

Queries issued by the searcher: Alphabet TPU fleet 2026 inference capacity; Gemini tokens per TPU second benchmark inference throughput; Alphabet Q1 2026 earnings call "tokens per minute" Gemini API; SemiAnalysis Ironwood InferenceX tokens per second per chip cost per million tokens

- `https://newsletter.semianalysis.com/p/tpu-inferencex-full-steam` -> **live_dated** (page date 2026-09-07); points raw/verified 15/0
- `https://actualitecloud.com/les-tpu-de-google-defient-nvidia-jusqua-50-de-performance-supplementaire-par-dollar/` -> **live_dated** (page date 2026-09-10); points raw/verified 15/0
- `https://thenextweb.com/news/google-inference-chips-nvidia-challenge-supply-chain` -> **live_dated** (page date 2026-04-20); points raw/verified 16/0
- `https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q1-2026/` -> **live_dated** (page date 2026-04-29); points raw/verified 15/9
  - p239 Alphabet first-party models tokens processed per minute via direct API use by cu = **16,000,000,000** tokens per minute (2026-01-01..2026-03-31) [keep: ] quote: "Our first-party models now process more than 16 billion tokens per minute via direct API use by our customers, up from 10 billion last quarter."
  - p240 Google Cloud customers processing over 1 trillion tokens each, past twelve month = **330** customers (2025-04-01..2026-03-31) [keep: ] quote: "Over the past twelve months, 330 Google Cloud customers each processed over 1 trillion tokens."
  - p241 Google Cloud customers reaching 10-trillion-token milestone, past twelve months = **35** as written "Thirty-five", value check pending customers (2025-04-01..2026-03-31) [keep: ] quote: "Thirty-five reached the 10-trillion-token milestone."
  - p242 Token threshold per customer for the 330-customer count (lower bound) = **1,000,000,000,000** tokens per customer (2025-04-01..2026-03-31) [keep: ] quote: "Over the past twelve months, 330 Google Cloud customers each processed over 1 trillion tokens."
  - p243 Reduction in Search latency over past five years = **35** % (2021-01-01..2026-03-31) [keep: ] quote: "we've reduced Search latency by more than 35% over the past five years."
  - p244 Google Cloud revenue growth year-over-year, Q1 2026 = **63** % (2026-01-01..2026-03-31) [keep: ] quote: "Revenue grew 63%, exceeding $20 billion for the first time, and our backlog nearly doubled quarter-on-quarter to over $460 billion."
  - p245 Google Cloud quarterly revenue threshold first exceeded, Q1 2026 = **20,000,000,000** USD (2026-01-01..2026-03-31) [keep: ] quote: "Revenue grew 63%, exceeding $20 billion for the first time, and our backlog nearly doubled quarter-on-quarter to over $460 billion."
  - p246 Google Cloud backlog, Q1 2026 = **460,000,000,000** USD (2026-01-01..2026-03-31) [keep: ] quote: "our backlog nearly doubled quarter-on-quarter to over $460 billion."
  - p247 Revenue growth from products built on gen AI models, year-over-year, Q1 2026 = **800** % (2026-01-01..2026-03-31) [keep: ] quote: "In Q1, revenue from products built on our gen AI models grew nearly 800% year-over-year."
- dropped by code checks: 52 (period_end missing or unparseable: 46; number: no number in value_as_written: 1; period_end 2026-12-31 after as_of: 2; period_end 2028-12-31 after as_of: 1; period year 2025 does not appear in the page text or URL (likely mis-dated): 1; scale word 'trillion' not supported by quote or table header: 1)

### markets [forecasts_markets] 

Hypothesis: prediction-market tool (code)

Market keywords ['gemini api tokens', 'alphabet q3 2026', 'gemini token growth']: no matching market created on or before as_of markets=0


## Judge

### round 1
- corroborating: ['p1', 'p13', 'p53', 'p105', 'p125', 'p137', 'p151', 'p167'] All restate the same Q2 2026 disclosure of ~22B tokens/min from Alphabet's Q2 2026 earnings call; they share one underlying source (Alphabet's own statement), so this is one measurement, not eight ind
- corroborating: ['p2', 'p14', 'p54', 'p152'] All restate the Q1 2026 level of 16B tokens/min cited in the Q2 2026 call; single underlying source.
- corroborating: ['p28', 'p29', 'p83', 'p84'] Q4 2025 = 10B and Q3 2025 = 7B tokens/min via direct APIs, from the same Q4 2025 earnings disclosure; consistent with the later 16B (Q1 2026) and 22B (Q2 2026) points, forming a coherent quarterly run
- corroborating: ['p40', 'p66'] Q1 2026 = 16B tokens/min via direct API use, matching the 'up from 16 billion' cited in Q2 2026; p66 is the primary blog wording, p40 a secondary restatement.
- corroborating: ['p81', 'p82'] I/O 2026 (May 2026) mid-quarter reading of ~19B tokens/min sits between Q1's 16B and Q2's 22B, consistent with intra-quarter growth; useful as a within-quarter trajectory check.
- corroborating: ['p78', 'p79'] Total Google token volume grew 7x YoY and 330x over two years at I/O 2026; a broader total (includes consumer/internal) that should grow at a similar order to the API rate, useful as a directional con
- corroborating: ['p3', 'p4', 'p5', 'p6', 'p56', 'p57', 'p58', 'p59', 'p160', 'p161'] Enterprise/Cloud customer token-consumption thresholds for the trailing 12 months; a different (annual, per-customer) scope, useful only as a scale sanity check, not a direct input to the per-minute r
- corroborating: ['p7', 'p15', 'p55', 'p153', 'p80'] Developer counts (~9M monthly Q2 2026, 8.5M at I/O 2026) are consistent and slowly growing; usable for a bottom-up cross-check but not a direct rate.
- corroborating: ['p97', 'p99', 'p134', 'p175', 'p176'] Q2 2026 capex ~$44.9B (doubled YoY) and negative FCF; indicates heavy inference/infrastructure buildout supporting continued token growth.
- corroborating: ['p126', 'p127', 'p128', 'p129'] Cloud revenue growth accelerating 34%→48%→63%→82% across quarters; a related demand signal consistent with accelerating AI usage, though not a token-rate measure.
- extra base-rate directions requested: ['b1', 'b2', 'b3']

### round 2
- corroborating: ['p1', 'p182', 'p196', 'p216', 'p227'] All restate the same Q2 2026 disclosure of ~22B tokens/min via direct API; they share one underlying Alphabet measurement, so they are one data point, not five independent confirmations.
- corroborating: ['p2', 'p66', 'p183', 'p228', 'p239'] All restate the Q1 2026 level of 16B tokens/min (up from 10B), same underlying disclosure; single measurement.
- corroborating: ['p28', 'p29'] Q4 2025 10B and Q3 2025 7B direct-API token rates; same series as p1/p2, giving the 7→10→16→22B trajectory. Consistent definitions (direct API, first-party Gemini).
- corroborating: ['p82'] I/O 2026 (May) mid-Q2 reading of ~19B tokens/min sits between Q1 16B and Q2 22B, consistent with intra-quarter growth; useful as a within-quarter anchor but same underlying metric.
- corroborating: ['p78', 'p79'] Total Google token volume 7x YoY and 330x vs two years prior at I/O 2026; broader scope (all Google tokens, not just direct API) but directionally consistent with rapid growth.
- corroborating: ['p61', 'p118', 'p129', 'p147', 'p164', 'p193', 'p207', 'p214', 'p231'] All report Q2 2026 Google Cloud revenue growth of 82%; same reported figure, not independent.
- corroborating: ['p223', 'p224'] JPMorgan raised Q3 2026 Cloud growth forecast from 88% to 100%, indicating continued acceleration in AI demand into Q3; supports continued token growth but is a forecast, not an outcome.
- corroborating: ['p165', 'p166', 'p169'] Q3 2026 events (Gemini 3.7 Flash release, Gemini Spark in 160 countries, three cheaper models) support continued token-volume growth via new/cheaper models and broader availability.
- corroborating: ['p97', 'p99', 'p134', 'p175', 'p235'] Q2 2026 capex ~$44.9B (doubled YoY) and negative FCF indicate heavy inference/infrastructure buildout, consistent with capacity to sustain rising token throughput.

## Assumptions (proposed by the judge, validated by code)

Rules: ids a1..a12, at most 6 per method, every formula needs an observed point; sampled lognormally with P10/P90 = low/high, widened by code to high/low >= 2.0. From judge round 2.

| id | name | value | judge range | range used (P10..P90) | unit | used by | rationale | applies when | falsified by |
|---|---|---|---|---|---|---|---|---|---|
| a1 | Q3 2026 vs Q2 2026 token-rate growth factor | 1.32 | 1.15..1.55 | 1.15..1.55 | ratio | m1 (m1) | Recent QoQ growth: 7→10 (1.43), 10→16 (1.60), 16→22 (1.375). Growth is decelerating in absolute increments; Q3 likely continues but slower. Central 1.32 (~32% QoQ) reflects deceleration from 37.5% while remaining strong given new cheaper models, Gemini 3.7 Flash, and JPMorgan's raised Cloud forecast | The Q3 2026 disclosure continues the same direct-API first-party token metric and growth decelerates modestly from Q2. | Evidence of a sharp acceleration (e.g. a >60% QoQ jump) or a plateau/stall in token growth in Q3. |
| a2 | Q3 2026 vs May 2026 (I/O) token-rate growth factor | 1.53 | 1.25..1.9 | 1.25..1.9 | ratio | m2 (m2) | I/O 2026 (May) reading of 19B is mid-Q2; Q2 end was 22B (factor ~1.16 over ~1.5 months). Extending similar monthly growth (~10%/month) through Q3 (~4.5 months from May to end-Sept) gives ~1.5x. Range reflects uncertainty in monthly compounding and deceleration. | The 19B I/O reading is a genuine mid-Q2 run-rate on the same metric and growth continues at a decelerating monthly pace. | Evidence that the 19B reading used a different scope or that monthly growth collapsed or accelerated sharply. |

## Methods (computed by code)

| id | method | estimate | inputs (points / assumptions) | backtest years | mean abs ln err | weight | weight basis | notes / error |
|---|---|---|---|---|---|---|---|---|
| m1 | formula_mc | 29,417,526,817 | ['p1'] / ['a1'] | [] |  | 0.50 | equal |  |
| m2 | formula_mc | 29,302,028,483 | ['p82'] / ['a2'] | [] |  | 0.50 | equal |  |

- m1 coverage: the whole target
- m2 coverage: the whole target

Result: central **29,359,720,855** token/minute, 80% interval [21,311,264,968, 40,447,773,043] token/minute, basis no_basis (too few backtest years, and neither method disagreement nor Monte Carlo sampling gave a wider interval, so code used its fixed default width), weight rule equal, weight on methods that use assumptions 1.00

## Published-value check (live use only)

Status: **no_candidates**. 0 candidate(s); entity terms ['alphabet', 'api']; measure stems ['alpha', 'first', 'minut', 'model', 'party', 'rate', 'token']; 2 point(s) for the target period excluded as dated before the period end or quoted as a forecast


## Final answer

Best estimate for the rate at which Alphabet's first-party models (Gemini family) process tokens via direct API use by customers, as a point-in-time run-rate to be first stated with Q3 2026 results (period 2026-[n]-[n] to 2026-[n]-[n]): 29,359,720,855 token/minute (80% model-based interval 21,311,264,968 to 40,447,773,043 token/minute).

Evidence: the Q2 2026 disclosure of 22,000,000,000 tokens per minute is the anchor for method m1 (weight 50%), which applies a decelerating QoQ growth factor 1.32 (range 1.15 to 1.55). Method m2 (weight 50%) instead grows the mid-Q2 I/O reading of 19,000,000,000 tokens per minute by factor 1.53 (range 1.25 to 1.9). Both observed points are actual disclosures; the growth factors are analyst assumptions, not observed. The two methods were combined at equal weight as a cross-check, not because they are independent.

Main risk: the I/O figure may use a different scope than the earnings disclosures, biasing m2; and growth could decelerate faster than assumed. Better evidence would be any interim Alphabet statement on token run-rate or a clearer scope definition for the I/O reading.

Key assumptions (proposed by the analyst model, not observed; code samples each one between the bounds shown):
- a1 Q3 2026 vs Q2 2026 token-rate growth factor: 1.32 ratio, range 1.15 to 1.55; used by m1. Overturned by: Evidence of a sharp acceleration (e.g. a >[n] QoQ jump) or a plateau/stall in token growth in Q3.
- a2 Q3 2026 vs May 2026 (I/O) token-rate growth factor: 1.53 ratio, range 1.25 to 1.9; used by m2. Overturned by: Evidence that the [n]B reading used a different scope or that monthly growth collapsed or accelerated sharply.

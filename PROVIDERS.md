# PROVIDERS.md — 多家模型、自带 key（BYOK）的设计记录

这份文件随阶段更新：每家 adapter 发什么、为什么、官方文档链接、已知限制。API 细节以官方文档为准，没核实的写「未核实」。

## 阶段

| tag | 内容 | 状态 |
|---|---|---|
| `v2.10a` | adapter 层 + 每次运行的 `ModelSpec`，目前只有 DeepSeek；按模型计价、没有价格的模型拒跑、方向数按模型价格缩放、余额不足立刻停、key 不落盘、BYOK 运行关掉 Jev | 本文件第 1–7 节 |
| `v2.10b` | Claude adapter（原生 Messages API，流式）和 Claude 搜索（服务端 web_search，pause_turn 续上）；用 models 列表校验 key（`llm.check_key`，DeepSeek 也有）；adapter 接口补了解码、可重试状态码、超时、回复问题、续搜索几个钩子 | 第 3、5、9 节 |
| `v2.10c` | GPT adapter（OpenAI：JSON 调用走 Chat Completions，搜索走 Responses API 的 web_search）；按官方价计价（含 cache 写入价、272K 长上下文档）；429 余额 / 额度错误立刻停；GPT key 校验 | 第 10 节 |
| `v2.10d` | Kimi adapter（国际站 / 国内站两个区域；JSON 调用走流式 Chat Completions；搜索 = 一次 JSON 调用生成查询词 + `POST /v1/tools/search`）；国内站按 CNY 官方价折算（`ModelSpec.price_id`）；429 余额不足立刻停；Kimi key 校验 | 第 11 节 |
| `v2.10e` | GLM adapter（Z.ai 国际站 / 智谱开放平台国内站两个区域；JSON 调用走非流式 Chat Completions；搜索同 Kimi：生成查询词 + `POST /web_search`）；国内站按 CNY 官方价折算；429 余额不足（1113）和用量上限 / 套餐 key 的码立刻停；只收 Standard API Key（网页提示 `GLM_KEY_NOTE`）；GLM key 校验 | 第 12 节 |
| `web-v0.9` | 网页接上 BYOK：`GET /api/providers`（provider、区域、模型、思考档位、每次运行的花费估计）、`POST /api/key/check`、`POST /api/runs` 必须带 key；key 只在这次运行的内存里，结束就清；经典界面只浏览；/verrier 控制台的「模型 · key · 上限」表单 | 第 13 节 |
| `v2.10f` | 审查修正：自带 key 的运行里预扣放不下只是因为在途时等、上限放不下一次最小运行就在服务端拒跑、Claude 默认改 Sonnet 5.5；中途停下的运行标 failed 并写原因；预扣的估计（搜索输入 p99、别家 1 字符 1 token、续接另预扣、缺 usage 按预扣记）；先 redact 再截断、GLM 形状的 key、key 字符集；等人工确认 30 分钟超时；DeepSeek 自带 key 的搜索关思考；命令行只收 DeepSeek 模型；403 的说法；GLM 1313 重试；五家的端到端测试 | 第 14 节 |

## 1. Scope and binding decisions（用户 10-20 / 10-21 定的，摘要）

- 只有网页运行自带 key；没带 key 的网页运行拒跑；网页运行永远不读服务器的 key 文件（`TRIANGULATE_KEY_FILE` / `.env`）。
  命令行、回测、三个基线臂（naive / structured / search_direct）保持「DeepSeek + key 文件」不变。
- key 只在浏览器（默认 sessionStorage）和服务器这一次运行的内存里；运行结束就清掉。不进 state.json、calls.jsonl、账本、图、日志、
  错误文字、任何 API 返回。
- DeepSeek 是默认 provider，经过现有路径时请求体逐字节不变。
- 不做 JSON 修补 / 兜底，不改提示词（G2 sha 不变），不做 JSON-schema 结构化输出，不托管（只绑 127.0.0.1）。

## 2. ModelSpec（`triangulate/providers.py`）

一次运行的设置：`provider`、`model`、`region`、`thinking`（网页档位 off / low / medium / high）、`usd_cap`（默认 $2.00），加上用户的 key。

| 规则 | 做法 |
|---|---|
| 有 spec = BYOK 运行 | `prepare_run(q, tag, spec=...)` -> `Context(spec=...)` -> `AgentLLM(spec=)`、`Searcher(spec=)`、`Budget.for_model(spec.model, usd=spec.usd_cap)`。没有 spec（命令行、回测、基线、现有测试）时和 v2.9b 完全相同 |
| 校验（`SpecError`，消息里不带 key） | provider、model 必须在白名单里（`PROVIDERS` / `MODELS`）；model 必须有价格（`config.price`，否则 `UnknownModel`）；region 必须是这家的；thinking 必须是这个模型能选的档位；usd_cap 是有限正数 |
| key 格式 | 去首尾空白（粘贴常带换行）后 8–512 个字符、中间没有空白；v2.10f 起只收字母、数字和 `. _ ~ + / = -`（第 14.4 节）。理由：urllib 拼请求头遇到 `\r\n` 会抛 `ValueError: Invalid header value b'Bearer <整把 key>'`，非 latin-1 字符会抛带字符的 `UnicodeEncodeError`（代码调查阶段在 Python 3.14.3 上实测）；入口拦下就不会走到这条路 |
| key 只有一份 | `LLM._key`、`Searcher._key` 在 spec 运行里是 `None`，每次发请求时才 `spec.key`；`save_run` 写完结果后 `run.release(h)` -> `spec.drop_key()`，之后再发请求抛 `KeyDropped` |
| 不能被顺手序列化 | `repr` / `str` / `public()` 不含 key；`pickle` / `copy` / `deepcopy` 抛 `TypeError`；spec 只挂在 `ctx` 上，不进题目 dict、不进 LangGraph state |
| 兜底 | `run_direction` 记的 `error` 文字、`LLM._log` 写的 calls.jsonl 行、`save_run` 写的 state.json / ledger.md / graph.html 都先 `spec.redact()`（把 key 换成 `***`）。正常路径上 key 本来就不会出现在这些文字里 |
| settings | `state.json` 的 `settings.run_spec` = `spec.public()`（provider、model、region、thinking、thinking_by_role、usd_cap、byok），顶层多一个 `provider`；`settings.thinking` 记这次运行实际用的档位。没有 spec 的运行 settings 不变 |
| Jev 对照臂 | spec 运行里 jev 节点直接记 `skipped`（`TYPESAFE_KEY_FILE` 是服务器主人的 key），不读 key 文件、不发请求 |

思考档位：网页的一个总档位只作用于 `plan`、`judge`、`repair` 三个角色（`config.thinking_role` 的取值）；其余角色在模型允许时关思考，
不允许关的模型用最低一档（`MODELS[m]["thinking_off"]`、`ModelSpec.effort`），而且网页不给 off。开了思考的调用 max_tokens 多给
`THINKING_EXTRA_TOKENS`（24000），不超过模型的最大输出（`MODELS[m]["max_output"]`）。spec 运行的预算预扣也按这个带余量的
max_tokens 算；没有 spec 的运行照旧只按 max_tokens 预扣（和 v2.9b 相同）。spec 运行忽略环境变量 `TRIANGULATE_THINKING`。

## 3. Adapter interface

外层循环（重试、3xx 不跟随、先查截断、JSON 解析、日志、预算）留在 `llm.LLM.json_call` 和 `agent/search.Searcher.search`，所有 provider 共用。
adapter 只管各家不同的部分：

| 方法 / 属性 | 用途 |
|---|---|
| `chat_url(region)`、`search_url(region)` | 每家固定的官方 URL（不允许用户填 base_url：会变成借服务器向任意地址发 POST） |
| `chat_request(model, key, messages, max_tokens=, effort=)` -> `(headers, payload)` | JSON 调用的请求头和请求体（dict 的键顺序就是发出去的顺序） |
| `chat_unpack(data)` | 回复骨架；形状不对抛 KeyError / IndexError / TypeError，外层记 `bad_response_body` 并重试 |
| `chat_meter(...)`、`chat_text(...)`、`chat_truncated(...)` | calls.jsonl 的计量字段（含 usd）、回复文字、是否被输出上限截断 |
| `search_request(...)`、`search_unpack(d)`、`search_meter(...)`、`search_fee_usd` | 搜索的请求、解析（查询词、结果 URL、文字块、搜索次数、搜索错误数）、token 计价、每次搜索的费用 |
| `balance_exhausted(status, body)` | 余额不足就返回一句说明，外层抛 `llm.BalanceExhausted`；`balance_hint` 是说明后面那句「怎么办」 |
| `error_body_statuses` | 哪些错误状态码要读 body 给 `balance_exhausted` 判断（DeepSeek 为空：只看 402）。读到的 body 不整段写日志：有的 provider 会回显部分 key |
| v2.10b：`chat_decode(raw)` | 回复 body -> dict。DeepSeek 是 `json.loads`（不变）；Claude 是 `parse_sse_message`（流式回复拼回完整 Message） |
| v2.10b：`chat_problem(unpacked)` | 不解析 JSON 就先报的回复问题：`None` 或 `(日志 error, 说明)`。DeepSeek 只有截断（文字和 v2.9b 相同）；Claude 另有拒答、暂停 |
| v2.10b：`retry_statuses`、`honor_retry_after` | 哪些状态码退避重试（DeepSeek 和 v2.9b 的 `RETRY_STATUS` 相同；Claude 多 529），要不要按 `retry-after` 等（`llm.retry_wait`，最多 60 秒） |
| v2.10b：`log_server_error` | 读过的错误 body 里 `error.type` 和 `error.message` 前 200 字记进日志和异常文字（`llm.server_error`；DeepSeek 关） |
| v2.10b：`chat_timeouts` | `LLM._post` 的单次读 / 整次超时（DeepSeek 为空 = 180 / 1200 秒不变） |
| v2.10b：`search_continue(payload, d)`、`max_search_continuations` | 搜索回复要不要续（Claude 的 pause_turn）；DeepSeek 返回 None、0 次（不变） |
| v2.10b：`key_check_request(region, key)`、`models_unpack(d)` | `llm.check_key(spec)` 用：models 列表接口的 GET 和解析 |
| v2.10c：`llm.server_error` 另记 `server_error_code` | 读过的错误 body 有 `error.code`（OpenAI）时记下，异常文字写成 `(type/code: message)`（`llm.server_error_detail`）；message 里像 key 的片段（`sk-...`）换成 `sk-***`。Claude 的错误没有 `code`，文字不变 |
| v2.10c：`Budget.reserve_rates(model, prompt_tokens)` | 预扣用的单价：`peak_rates`，默认会写缓存的模型（`prompt_cache = "implicit_write"`，GPT）输入按 30 分钟写入价。DeepSeek / Claude 和 `peak_rates` 相同 |
| v2.10d：`ModelSpec.price_id`、`providers.price_id(model, region, ad)` | 计价 id（`config.PRICES` 的键）：这家的默认区域就是模型名（DeepSeek / Claude / GPT 只有一个区域，不变），别的区域是 `模型@区域`（Kimi 国内站 `kimi-k3@cn`）。`LLM.price_model`、`Searcher` 的计量、`Budget.for_model`、`ModelSpec` 的价格校验都用它；请求里发的仍是模型名，calls.jsonl 的 `model` 也仍是模型名 |
| v2.10d：`providers.search_fee_usd(price_id)` | 价格表里写了 `search_fee_usd` 的（Kimi，按区域）用它，否则用这家 adapter 的 `search_fee_usd`（其余三家不变） |
| v2.10d：`search_mode`、`tools_search_request(key, query, limit=)`、`tools_search_unpack(d)` | `search_mode = "queries"`（Kimi）：`Searcher.search` 不走 `search_request` 那条路，改走 `_search_by_queries`（第 11.5 节）。没有这个属性的 adapter 照旧（`"model"`） |
| v2.10d：`reset_header`、`llm.retry_after(ad, headers)` | 出错时要等多少秒：先看 `retry-after`；没有、且 adapter 指定了 `reset_header`（Kimi 搜索接口的 `X-RateLimit-Reset`，Unix 秒）时换成距现在的秒数。`honor_retry_after = False`（DeepSeek）时照旧不看；Claude / OpenAI 没有 `reset_header`，行为不变 |
| v2.10d：`region_labels`、`MODELS[m]["thinking_param"]` / `["thinking_depth"]` | 网页用：区域的说明；这个模型用哪个字段控制思考、有没有深度档位（K2.6 没有：low / medium / high 都是「开」） |
| v2.10e：`tools_search_request(key, query, limit=, region=)`、`search_settings(region)` | 搜索请求按区域建（GLM 两站的引擎和必填字段不同；Kimi 不用 region）；`run_settings` 的 `search_queries` 里记哪些搜索设置（Kimi 仍是 `timeout_seconds`，GLM 是引擎等） |
| v2.10e：`search_bills_every_ok_response` | 「查询词」模式的计费：没有这个属性（Kimi）= 只有结果非空才记一次；GLM 为 True = 每个 HTTP 200 都记一次（含空结果、形状不对的） |
| v2.10e：`parse_error(raw)` | adapter 有它时 `llm.server_error` 用它解析错误 body（GLM：只有 `code` / `message`，可能没有外层 `error`），日志记 `server_error_code` / `server_error`、不记 `server_error_type`；`llm.server_error_detail` 对这种记录写 `(code 1214: message)`。其余 provider 没有这个钩子，文字不变 |
| v2.10e：`models_unpack` 第二项可以是 `None` | 「列表全不全不知道」（GLM 的 models 接口没有文档）：所选模型不在里面时 `check_key` 的 `model_listed` 是 None，message 写「没核对」而不是「不在列表里」 |
| v2.10e：`key_note`、`key_pages`（GLM） | 网页上要显示的 key 说明（只收 Standard API Key、不收 Coding Plan key）和两站建 key 的页面；`PROVIDERS["glm"]["key_note"]` 是同一段 |

`ModelSpec.tokens_for(role, max_tokens)`（v2.10b）：这个角色的思考档位和实际发出的 max_tokens（开思考 +`THINKING_EXTRA_TOKENS`，不超过模型最大输出），
JSON 调用、搜索、预扣都用它。`Budget.search_tokens`：spec 运行里搜索实际发出的 max_tokens（Opus 5.5 / Fable 5.1 的搜索也开思考，预扣跟着变大）。

`llm.check_key(spec)`（v2.10b）：用这次运行的 key GET models 列表，返回给网页看的 dict：`ok`、`status`、`error`（key_rejected / balance /
redirect / http_<code> / bad_response_body / network）、`message`、`model_listed`（所选模型在不在列表里；列表不完整又没找到时是 None）、`n_models`。
不含 key、不含服务端原文。网页阶段接。

没有 spec 时 `LLM` / `Searcher` 用 `providers.DEEPSEEK`，URL 仍取 `llm.API_URL` / `search.SEARCH_URL`（测试 patch 这两个名字的做法照旧有效），key 仍由 `read_key()` 从 key 文件读。

## 4. DeepSeek adapter（`DeepSeekAdapter`）

| 调用 | 发什么 | 为什么 |
|---|---|---|
| JSON 调用 | `POST https://api.deepseek.com/chat/completions`，`Authorization: Bearer <key>`；body 依次是 `model`、`messages`、`thinking: {type: enabled/disabled}`、`response_format: {type: json_object}`、`temperature: 0`、`max_tokens`、`stream: false`，开思考时末尾加 `reasoning_effort` | 和 v2.9b 的 `llm.py` 逐字节相同（v2.9a 的思考开关、frozen-v2.8r 的默认请求） |
| 搜索 | `POST https://api.deepseek.com/anthropic/v1/messages`，`x-api-key`、`anthropic-version: 2023-06-01`；body `model`、`max_tokens`（8192）、`tools: [web_search_20250305, max_uses]`、`messages` | 和 v2.9b 的 `agent/search.py` 逐字节相同 |
| key 校验（下一阶段用） | `GET https://api.deepseek.com/models` | 官方 List Models；不带 key 时回 401 纯文本 `Authentication Fails (governor)`（代码调查阶段实测）。带有效 key 是否计费：文档没写，未核实 |

思考档位（DeepSeek Thinking Mode 文档：`reasoning_effort` 只有 low / high / max，medium 按 high 处理；默认开思考、默认 high；思考模式下
temperature 不生效但不报错）：

| 网页档位 | plan / judge / repair 发的 `reasoning_effort` | 其余角色 |
|---|---|---|
| off | 不发，`thinking.type = disabled` | 关 |
| low | `low` | 关 |
| medium | `high`（官方映射） | 关 |
| high | `high`（和 v2.9 思考实验的 high 相同；不用 max） | 关 |

DeepSeek 两个模型都能关思考，所以四档都给。max_output 记 384,000（价格页写「最大 384K」，按 1000 算，偏保守）。
temperature 照旧发 0（用户决定 5：DeepSeek 保留 temperature 0）。

价格（`config.PRICES`，USD / 百万 token：cache hit、cache miss、output；https://api-docs.deepseek.com/quick_start/pricing ，2026-10-21 查看）：

| 模型 | 闲时 | 峰时（UTC 周一至周五 01–04、06–10 点） |
|---|---|---|
| `deepseek-flash`（DeepSeek-V4.1-Flash-1017） | 0.003 / 0.15 / 0.60 | 0.006 / 0.30 / 1.20 |
| `deepseek-v4-pro`（DeepSeek-V4-Pro-0813） | 0.022 / 0.66 / 1.98 | 0.044 / 1.32 / 3.96 |

中国法定假日也算闲时，代码忽略（只会高估）。搜索费：价格页列了独立的 Search API（$0.75 / 1000 次成功请求，2026-11-01 北京时间零点起按次计费），
没有单列 Anthropic 兼容接口里服务端 web_search 工具的价格；预算照旧按 Anthropic 公开价 $0.01 / 次记账（`DEEPSEEK_SEARCH_FEE_ASSUMED_USD`，保守假设）。

余额不足：官方错误码 402 = Insufficient Balance（https://api-docs.deepseek.com/quick_start/error_codes）。JSON 调用和搜索遇到 402 都不重试，
记一行和 v2.9b 相同的 `http_402` 日志，抛 `BalanceExhausted`。

## 5. Pricing, directions and the cap

Claude 的价格（v2.10b，USD / 百万 token；https://platform.claude.com/docs/en/about-claude/pricing ，2026-10-21 查看；没有分时价，
`peak` = `offpeak` = (cache hit, base input, output)，另记 5 分钟 / 1 小时 cache 写入价）：

| 模型 | base input | 5m cache 写 | 1h cache 写 | cache hit | output |
|---|---|---|---|---|---|
| `claude-haiku-5-5`（prompt ≤ 100K） | 0.10 | 0.125 | 0.20 | 0.01 | 0.50 |
| `claude-haiku-5-5`（prompt > 100K，整次请求） | 0.50 | 0.625 | 1.00 | 0.05 | 2.50 |
| `claude-sonnet-5-5` | 2.00 | 2.50 | 4.00 | 0.10 | 10.00 |
| `claude-opus-5-5` | 4.00 | 5.00 | 8.00 | 0.20 | 20.00 |
| `claude-fable-5-1` | 10.00 | 12.50 | 20.00 | 0.25 | 50.00 |

Haiku 5.5 的 prompt 长度 = input + cache 读 + cache 写（官方 Long context pricing）。web search $10 / 1,000 次（每次 $0.01，出错的不计费），
搜索结果按 input token 另计。回复的 `usage.inference_geo` 是 `"us"` 时乘 1.1（Data residency pricing；请求里不写，默认 global）。

- **没有价格就不跑**：`config.price(model)` 找不到就抛 `UnknownModel`；`usd_cost`、`Budget`、`LLM()` / `Searcher()` 的构造、`ModelSpec` 都经过它。
  v2.9b 的 `PRICES.get(model, PRICES["deepseek-flash"])` 静默回落已删（命令行设了没价格的 `TRIANGULATE_MODEL` 现在在读 key 之前就报错）。
- **方向数按模型价格缩放**：`Budget.typical_direction_usd(model)` = 0.06（deepseek-flash 实测）×（这个模型 / flash 按峰时价算的一个方向的价格比）。
  一个方向的 token 构成 `DIRECTION_PROFILE` 取自已存的 1251 个 deepseek-flash 方向的平均（搜索 + 抽取：cache hit 13,600、miss 25,700、
  输出 3,600 token，4 次搜索），只用来算比例。flash 仍是 0.06（`Budget().directions` 仍是 10）；v4-pro 约 $0.102 / 方向：
  $1 上限 5 个方向、$2 上限 10 个（页数上限 40 / 4）。
- 预扣（`llm_reserve`、`search_reserve`）用这次运行的模型的峰时价和这家的搜索费。v2.10f：自带 key 的运行里输入的 token 估计、
  搜索输入、续接、等在途的规则见第 14.1 / 14.3 节（命令行不变）。
- v2.10b Claude：请求里不写 `cache_control` 就没有缓存（`prompt_cache: "explicit"`），所以 `DIRECTION_PROFILE` 里 DeepSeek 自动命中的
  13,600 token 在 Claude 上按 base input 算。Haiku 5.5 的预扣在估计的 prompt（字符数 / 2）超过 100,000 token 时按高价（`Budget.peak_rates`）。
  `$2` 上限下的方向数和几个典型预扣见第 9.8 节。

## 6. Insufficient balance stop

`BalanceExhausted` 是 `TransportError` 的子类：基线（`forecast.py`、`runner.py` 只接 `TransportError`）照旧跳过这道题、不保存。
agent 里 `AgentLLM.ask` 和 `run_direction` 的搜索把它变成 `Budget.halt(原因)` + `BudgetExceeded`：之后每次预扣都抛 `BudgetExceeded`，
各节点按已有的预算中止路径收尾（和网页的「取消」同一条路），`save_run` 照常写 state.json，`aborted` 是
「insufficient balance: DeepSeek HTTP 402 Insufficient Balance (...); the run was stopped without retrying. Top up the DeepSeek account and run again.」

## 7. Verification（v2.10a）

- 金样本：`tests/golden_deepseek.py` 的 `capture()` 用假 urlopen 跑 24 组固定输入（json_call 的各种回复和错误、思考开关、AgentLLM.ask 带错误重问、
  Searcher、基线 DirectClient），记 URL、请求头、请求体、超时、calls.jsonl 行（at / latency 换成占位符）和返回值。
  `tests/golden/deepseek_requests_head.json` 是在 HEAD `ec3e929` 的导出上生成的（`git archive ec3e929 triangulate | tar -x -C probes/out/_old_v2_9b`，
  再 `python tests/golden_deepseek.py probes/out/_old_v2_9b tests/golden/deepseek_requests_head.json`），重生成逐字节相同。
  `tests/test_providers.py` 在新代码上逐字节比较：24 组的请求和日志全部相同；只有 `json_402`、`search_402` 两组的返回值有意不同（改成抛 `BalanceExhausted`）。
  变异检查：只调换请求体两个键的顺序、或改一个请求头的一个字符，测试都失败。
- spec 路径：`deepseek-flash` + off 的请求体、请求头和默认路径完全相同（key 换成 spec 里的）。
- G2（`probes/compare_continuous_prompts.py`）：HEAD 和 v2.10a 都是 `365b06515d8caef8257020c2e5d574de7724be2f2270c122e6e21952517f78c4`
  （NEXT.md 的 G2 表停在 U1 时期，没登记过这个值；这里只证明本阶段没改 prompt）。

## 8. Known limits / open items

（v2.10b 起 Claude 相关的限制在第 9.8 节；下面是 v2.10a 记的，「key 校验」一条已在 v2.10b 实现。）

- ~~**DeepSeek 搜索角色的思考没关**~~（v2.10f 已改，只改自带 key 的路径，第 14.6 节）：搜索请求不带 `thinking` 字段（v2.9b 原样），服务端默认；`search_direct.py` 的注释记过这个接口默认返回 thinking 块。
  用户决定 6 说「其余角色能关就关」，但关掉要往搜索请求体里加字段（改变冻结的请求体），而且 DeepSeek 的 Anthropic 兼容文档只写了 `thinking`
  「Supported」、没写 `type: disabled` 的效果（未核实）。本阶段没动，等用户定。
- ~~**网页还没接**~~：web-v0.9 已接（第 13 节）。
- 搜索遇到 401 / 403 仍然只记 `http_401` 返回空 URL（v2.9b 原样），不像 JSON 调用那样抛 `KeyRejected`。
- ~~key 校验（models 列表接口）还没实现。~~ v2.10b：`llm.check_key`（DeepSeek `GET /models`、Claude `GET /v1/models`）；web-v0.9 网页已接（`POST /api/key/check`）。
- ~~其他四家（Claude、GPT、Kimi、GLM）的 adapter、价格、模型清单还没加~~：Claude 见第 9 节（v2.10b），GPT 见第 10 节（v2.10c），
  Kimi 见第 11 节（v2.10d），GLM 见第 12 节（v2.10e）。

## 9. Claude adapter（`ClaudeAdapter`，v2.10b）

走原生 Messages API，不用 OpenAI 兼容层（官方说它会忽略 `response_format` 和 `reasoning_effort`、不支持缓存、不适合生产）。
用标准库 urllib 直接发 HTTP，不装官方 Python SDK：项目里所有 provider 共用一套外层循环（重试、不跟随跳转、日志、预算、假 urlopen 的测试），
SDK 自带重试和 httpx 传输层，D9「不跟随跳转」和现有测试的拦截都得重做（代码调查阶段的结论），也是一个新依赖。

### 9.1 JSON 调用发什么

`POST https://api.anthropic.com/v1/messages`，请求头 `Content-Type: application/json`、`Authorization: Bearer <key>`、`anthropic-version: 2023-06-01`
（Authentication 页：直接发 HTTP 时用 Bearer，`x-api-key` 是 legacy、仍支持）。body 依次是：

| 字段 | 值 | 为什么 |
|---|---|---|
| `model` | `claude-haiku-5-5` / `claude-sonnet-5-5` / `claude-opus-5-5` / `claude-fable-5-1` | 用户决定 9 的清单 |
| `max_tokens` | 角色的 `MAX_TOKENS`，开思考 +24,000，最多 128,000 | 原生 API 只有这一个上限，思考 + 正文共用（Thinking 页）；四个模型同步请求最大输出 128K |
| `system` | 开头的 system 消息（原样） | 原生 API 没有 system 角色的输入消息，放顶层 |
| `messages` | 其余的 user / assistant 消息；内容为空的 assistant 消息不发 | `TextBlockParam.text` 最少 1 个字；两条 user 由 API 合并成一轮（Messages API）。最后一条总是 user（5.5 代不支持 prefill） |
| `thinking` | 开思考 `{"type": "adaptive"}`；关思考 Haiku `{"type": "disabled"}`、Sonnet `{"type": "between_tools"}` | 见 9.2 |
| `output_config` | `{"effort": ...}` | 见 9.2；不写 `format`（用户决定 10：不用 JSON schema） |
| `stream` | `true` | Errors 页 Long requests：max_tokens 大的请求用流式或 Batch，避免长时间空闲的连接被网络断开；官方 SDK 在非流式请求预计超过 10 分钟时直接拒绝 |

不发 `temperature` / `top_p` / `top_k`：这四个模型上传非默认值一律 400（Messages API：Models released after Claude Opus 4.6 do not support setting temperature …）。
不写 `cache_control`（没要求做缓存）、不写 `inference_geo`、不加任何 beta 头。

回复：流式事件按 Streaming 页拼回完整的 Message（`providers.parse_sse_message`：message_start -> content_block_start / delta / stop -> message_delta（usage 累计）
-> message_stop；ping 和未知事件忽略）。只拼 `type == "text"` 的块（thinking 块在 display 默认 omitted 时是空字符串），直接 `json.loads`；
不剥代码块、不修补（用户决定 4：照原样报错）。流里来了 `error` 事件（如 `overloaded_error`）或没收到 `message_stop`：记 `bad_response_body`
（`stream_error` = 错误类型 / `incomplete_stream`），按已有逻辑重试。单次读最多等 600 秒、整次 3600 秒（`chat_timeouts`）。

### 9.2 思考档位

| 模型 | 网页可选 | plan / judge / repair | 其余角色 |
|---|---|---|---|
| Haiku 5.5 | off / low / medium / high | off：`disabled` + effort `medium`；其余：`adaptive` + 同名 effort | `disabled` + effort `medium` |
| Sonnet 5.5 | off / low / medium / high | off：`between_tools` + effort `high`；其余：`adaptive` + 同名 effort | `between_tools` + effort `high` |
| Opus 5.5 | low / medium / high（思考关不掉，不给 off） | `adaptive` + 同名 effort | `adaptive` + `low`（最低一档） |
| Fable 5.1 | low / medium / high（同上） | `adaptive` + 同名 effort | `adaptive` + `low` |

依据：Errors 页 Thinking cannot be disabled（Opus 5.5 / Fable 5.1 发 disabled 在任何 effort 下 400；Sonnet 5.5 发 disabled 400，要关用 between_tools；
Haiku 5.5 接受 disabled；between_tools / disabled 在 xhigh / max 下 400）；Effort 页（effort 作用于所有输出 token，开不开思考都有效；
Opus 5.5、Haiku 5.5 默认 medium，其余默认 high；把 effort 设成默认值等于不写）。关思考的调用把 effort 显式写成模型默认值，
是为了换模型、官方改默认值时请求不悄悄变（Effort 页 Best practices 第 1 条：Set effort explicitly）。网页档位 high 对应 `high`，不用 xhigh / max。
开了思考的调用（含 Opus / Fable 的所有调用）max_tokens +24,000（不超过 128,000）；between_tools / disabled 的调用不加。

### 9.3 stop_reason

| stop_reason | 处理 |
|---|---|
| `end_turn`、`stop_sequence` | 解析 JSON |
| `max_tokens`、`model_context_window_exceeded` | 报截断（`truncated`，说明里写 stop_reason），不解析；`AgentLLM.ask` 照旧要求「短一点再答一次」 |
| `refusal` | 报 `refusal`（日志记 `stop_category` = `stop_details.category`），不解析；`AgentLLM.ask` 照旧带错误重问一次。拒答也计费（按 usage） |
| `pause_turn` | JSON 调用不带工具，正常不会出现；出现就报 `paused` |
| 搜索的 `pause_turn` | 见 9.5：续上 |

### 9.4 错误、重试、余额

| 情况 | 处理 | 依据 |
|---|---|---|
| 401 / 403 | `KeyRejected`，不重试，不读 body | Errors 页；10-21 实测假 key 401 `invalid x-api-key`、`x-should-retry: false` |
| 429 rate_limit_error、500、502、503、504、529 overloaded_error | 最多 3 次；有 `retry-after` 就等那么久（最多 60 秒），否则 2 / 4 秒（搜索 3 / 6 秒） | Errors 页、Rate limits 页 |
| 402 billing_error | `BalanceExhausted`，不重试 | Errors 页 |
| 400，message 以 `You have reached your specified API usage limits` / `... workspace API usage limits` 开头 | `BalanceExhausted`（用户在 Console 设的 spend limit） | Rate limits 页 Setting your own spend limit |
| 429，`error.details.error_code = enforced_spend_limit_reached` | `BalanceExhausted`（用量档的月度上限；没有 retry-after，重试没用） | Rate limits 页 Reaching your spend cap |
| message 以 `Your credit balance is too low to access the Anthropic API` 开头（400 / 402 / 429 都认） | `BalanceExhausted` | API credits 页给了原文；**状态码文档没写**（未核实） |
| 其余 4xx（参数不对、组织关了 web search、身份绑定的 key 没带 workspace id 等） | 不重试；`error.type` 和 message 前 200 字进日志和异常文字 | Errors 页、Authentication 页、Web search tool 页 |
| 3xx | 不跟随（D9），`TransportError` | 同 v2.6g |

`BalanceExhausted` 的文字：`insufficient balance: Claude <原因> (...); the run was stopped without retrying. Check Plans & Billing and the spend limits in the Claude Console, then run again.`
（不含服务端原文。）agent 运行里它照旧变成 `Budget.halt`，整次运行停下（第 6 节）。

### 9.5 搜索

`POST https://api.anthropic.com/v1/messages`（非流式），请求头同上；body：`model`、`max_tokens`（8192，开思考 +24,000）、
`tools: [{"type": "web_search_20250305", "name": "web_search", "max_uses": 3}]`、`messages`（一条 user）、`thinking`、`output_config`（规则同 9.2，
搜索不是 plan / judge / repair：Haiku / Sonnet 关思考，Opus / Fable 用 low）。

- 工具版本：`web_search_20250305`（基础版）。所有当前模型都能用、ZDR-eligible、结果块直接在顶层 content 里；带 dynamic filtering 的
  `web_search_20260209` / `20260318` 会在内部跑 code execution，结果块嵌套、带 `caller` 字段，默认不算 ZDR。这里只要 URL，用不上过滤。
- 解析（`anthropic_search_unpack`，和 DeepSeek 共用）：`server_tool_use.input.query` -> 查询词；`web_search_tool_result.content`（列表）的
  `url`、`title` -> 结果；出错时 content 是一个错误对象（HTTP 仍是 200）-> 记一个搜索错误；`text` 块 -> 模型挑的 URL。
  标题解析出来但不出 Searcher（分析角色只看得到 URL，设计同 v2.9b）。
- 计价：token 按 9.6；搜索费 = `usage.server_tool_use.web_search_requests` × $0.01（官方价，字段名仍叫 `usd_search_fee_assumed`）。
- `pause_turn`（Server tools 页）：把这次的 content 原样作为 assistant 消息接在后面，工具不变，再发；最多续 2 次（`max_search_continuations`）。
  每次请求各记一行日志（续的那行带 `continuation: n`），查询词、URL、搜索次数、费用合并；续的时候失败就用已经拿到的结果，
  返回里加 `error: "continuation n: ..."`。
- 余额不足同 9.4（抛 `BalanceExhausted`）；组织关了 web search 时是 400 invalid_request_error，照原样记在 `error` 里。

### 9.6 用量和成本

`claude_usage_cost`：`input_tokens × base + cache_read × hit + 5 分钟写 × 1.25 倍价 + 1 小时写 × 2 倍价 + output_tokens × output`
（`usage.cache_creation` 有分档就按分档，没有就全按 5 分钟）。总 prompt = input + cache 读 + cache 写（Messages API usage 说明）。
Haiku 5.5 总 prompt > 100,000 整次按高价；`inference_geo == "us"` 乘 1.1。calls.jsonl 每行：`finish_reason`（= stop_reason）、`prompt_tokens`（总 prompt）、
`input_tokens`、`cache_read_input_tokens`、`cache_creation_input_tokens`、`completion_tokens`（= output_tokens，含思考）、`usd`，
开思考时 `reasoning_tokens`（= `usage.output_tokens_details.thinking_tokens`），拒答时 `stop_category`。`report.py` 按 prompt / completion / finish_reason 汇总照样能用。

### 9.7 key 校验

`GET https://api.anthropic.com/v1/models?limit=1000`（List Models：limit 1–1000，默认 20），请求头 Bearer + anthropic-version。不生成 token；
带有效 key 是否完全免费，官方页没写价格（未核实，按「免费的 models 列表」用，用户决定 2）。
10-21 实测（`probes/claude_key_probe.py`，没花钱）：不带 key -> 401 `{"type":"error","error":{"type":"authentication_error","message":"x-api-key header is required"},...}`、
`x-should-retry: false`；假 key（Bearer）走 `check_key` -> `{"ok": false, "status": 401, "error": "key_rejected", "message": "Claude rejected the API key (HTTP 401)"}`
（服务端 message 是 `invalid x-api-key`，不进返回值）。

### 9.8 已知限制、没做的、要你定的

- **`$2` 上限下贵的模型几乎跑不起来（最要紧，要你定）**。预扣按最坏情况（输入字符数 / 2 个 token × 输入价 + 发出的 max_tokens × 输出价），
  而且一次预扣放不下就把整次运行标成中止（`Budget.hold`，DeepSeek 时代的设计，本阶段没改）。按现在的价格和余量算（`$2` 上限、默认思考档）：

  | 模型 | 一个方向 | `$2` 方向数 | 一次搜索预扣 | plan（2 万字符） | 抽取（4 万字符） | 抽取（40 万字符） | judge（10 万字符） |
  |---|---|---|---|---|---|---|---|
  | deepseek-flash | $0.060 | 10 | $0.099 | $0.010 | $0.025 | $0.079 | $0.029 |
  | claude-haiku-5-5（off） | $0.053 | 10 | $0.087 | $0.004 | $0.010 | $0.140 | $0.011 |
  | claude-sonnet-5-5（off） | $0.178 | 6 | $0.222 | $0.080 | $0.200 | $0.560 | $0.220 |
  | claude-opus-5-5（low） | $0.310 | 3 | $0.844 | $0.640 | $0.880 | $1.600 | $0.920 |
  | claude-fable-5-1（low） | $0.706 | 1 | $1.990 | $1.600 | $2.200 | $4.000 | $2.300 |

  Opus：第一轮 3 个方向同时搜索，预扣合计 $2.53 > $2，第三个搜索就会让整次运行中止；Fable：一次 4 万字符的抽取预扣就超过 $2。
  Sonnet 在 8 个并发抽取时也很可能撞上。可选的修法（没做，等你定）：自带 key 的运行里，预扣放不下只是因为「在途的预扣」时就等在途调用结束，
  只有「已花 + 这一次」放不下才中止；或者给贵模型更高的默认上限 / 更低的并发。~~上限本身照样守得住（预扣是最坏情况）。~~
  **更正（v2.10f）**：这句不对。预扣不是严格的最坏情况（搜索输入按估计的 token 数、字符数换 token 是估计、续接没另预扣），上限可能被
  在途调用的超出部分超过（第 14.3 节）。等在途、拒跑、默认模型已在 v2.10f 改（第 14.1 节）。
- **没开 refusal fallback**。claude-api 参考建议 Opus 5.5 / Sonnet 5.5 / Fable 5.1 默认带服务端 `fallbacks: "default"`（beta 头
  `server-side-fallback-2026-07-01`）：被安全分类器拒答时 API 自动换别的模型重跑。没开的理由：它会换到别的模型、按那个模型的价格计费，
  和「按所选模型的官方价计价」（用户决定 7）、「照原样报错」（决定 4）冲突，也是 beta。要开随时说。
- **没开 prompt caching**（没要求）。抽取的 system prompt 每页都一样，写 `cache_control` 可以省钱，但要改请求体、改计价假设，留给你定。
- 流式回复里 ping 事件多久一次，官方只写「may include any number of ping events」；display omitted 时思考期间可能长时间没有字节。
  单次读超时设 600 秒（同官方 SDK 默认的 10 分钟），没实测。
- 搜索是非流式的；Opus / Fable 的搜索开思考，max_tokens 是 32,192，超过官方 SDK 允许的非流式上限（约 21,333）。服务端的工具循环跑得长时会
  自己回 pause_turn，单次请求时长应该有界；socket 超时 600 秒。没实测。
- 身份绑定、又没限定到单个 workspace 的 key：每个请求都要 `anthropic-workspace-id` 头，否则 400（Authentication 页）。没做 workspace id 输入，
  这种 key 会在第一个调用报 400（message 原文进错误文字）。网页上应提示用户建单 workspace 的 key。
- 「Your credit balance is too low」的状态码文档没写；按 message 原文认。
- Haiku 5.5 的 100K 门槛在服务端工具循环（一次搜索请求内多轮）里怎么算没写；这里按整次请求的 usage 合计判断，可能高估。
- ~~预扣的 token 估计仍是「字符数 / 2」~~（v2.10f：别家按 1 个字符 1 个 token，第 14.3 节）；官方说 4.7 以后的 tokenizer 同样文字多约 30% token，和 DeepSeek 的差距没测。
- `DIRECTION_PROFILE` 是 DeepSeek 实测的 token 构成；Claude 的 tokenizer、Opus / Fable 关不掉的思考会让真实的一个方向更贵（未测）。上限靠预扣守住。
- Claude 没有中国区 endpoint；Supported Regions Policy 不含中国大陆、香港、澳门（research 记录），网页阶段要写明。
- 网页还没接（同第 8 节）：`check_key`、Claude 选项、key 输入框都留给网页阶段。

### 9.9 Verification（v2.10b）

- `tests/test_claude.py`（31 个）全部对着 127.0.0.1 上的假 Anthropic 服务（`tests/fake_claude.py`）跑，真实走 urllib + `urlopen_no_redirect`：
  请求头 / 请求体（逐字段）、四个模型 × 档位 × 角色的 thinking / effort / max_tokens、空 assistant 消息不发、流式解析（多个 text 块、思考块、ping、
  未知事件、input_json_delta、CRLF、usage 累计）、各种 stop_reason、529 / 流内 error / 断流重试、retry-after、四种余额 / 额度停下、普通 400 照原样报、
  401 / 403、3xx 不跟随、cache 两档 / Haiku 长上下文 / geo 计价、方向数、预扣、搜索请求体、URL / 标题 / 搜索费、错误对象、pause_turn 续两次和续失败、
  搜索 400 / 402 / 529、key 校验（含 10-21 实测的两种 401 body）、DeepSeek key 校验、端到端（prepare_run -> 图 -> save_run，402 干净停下，结果目录没有 key）。
- DeepSeek 默认路径：`tests/test_providers.py` 的 24 组金样本仍逐字节相同（adapter 接口加钩子以后）。
- G2（`probes/compare_continuous_prompts.py`）：`365b06515d8caef8257020c2e5d574de7724be2f2270c122e6e21952517f78c4`，和 v2.10a 相同。
- 真实网络只发了不花钱的请求（`probes/claude_key_probe.py`：不带 key、假 key 调 `/v1/models`，都是 401）。没有真 key，没有发过 `/v1/messages`。

## 10. GPT adapter（`OpenAIAdapter`，v2.10c）

只用官方 `api.openai.com`（global）。JSON 调用走 Chat Completions；搜索走 Responses API（hosted `web_search` 工具只在 Responses 里有，
Chat Completions 只能换专用搜索模型 `gpt-5-search-api`）。同 Claude：标准库 urllib，不装官方 SDK（SDK 自带重试，和外层循环、不跟随跳转、
假服务测试冲突）。没有用 data residency 端点（`us.` / `eu.api.openai.com`：Pricing 页写明 2026-03-05 以后发布的模型加价 10%，还要项目有资格），
所以 region 只有 `global`。

### 10.1 JSON 调用发什么

`POST https://api.openai.com/v1/chat/completions`，请求头 `Content-Type: application/json`、`Authorization: Bearer <key>`（不发
`OpenAI-Organization` / `OpenAI-Project`：API Overview 页说只有属于多个组织、或用 legacy user API key 访问项目时才需要；没做这两个输入，网页上应建议用户建一个 project key，最好设 hard spend limit）。body 依次是：

| 字段 | 值 | 为什么 |
|---|---|---|
| `model` | `gpt-6-luna` / `gpt-6.1-sol` / `gpt-6-astra` | 用户决定 9 的清单 |
| `messages` | 开头的 system 消息改成 `role: "developer"`，内容不变；其余原样 | API 参考：With o1 models and newer, use `developer` messages for this purpose instead（GPT-6 都是推理模型）。不改提示词文字，G2 sha 不变 |
| `reasoning_effort` | 见 10.2；关思考时显式写 `"none"` | Reasoning 指南：Luna 省略时默认 medium |
| `response_format` | `{"type": "json_object"}` | 用户决定 4 / 10：各家文档里的普通 JSON 写法，不用 json_schema。JSON mode 要求上下文里出现字符串 "JSON"，所有走 json_call 的提示词都有（逐个查过） |
| `temperature` | 只有 effort 是 `none` 时发 `0` | GPT-6 迁移指南：When reasoning effort is not `none`, remove `temperature`, `top_p`, and `top_logprobs`（发了会怎样文档没写，未核实）；Luna 在 none 时可以带，照 DeepSeek 发 0（用户决定 5） |
| `max_completion_tokens` | 角色的 `MAX_TOKENS`，开思考 +24,000，最多 128,000 | API 参考：含可见输出和 reasoning token 的上限；`max_tokens` 已 deprecated、和推理模型不兼容。三个模型最大输出都是 128,000（模型页）。Reasoning 指南建议起步至少留 25,000 给推理 + 输出 |
| `store` | `false` | API 参考的可选参数（存下来给 distillation / evals 用）；默认值参考页没写明，显式写 false |

不发 `stream`（非流式；见 10.8）、`tools`（6.1 Sol / Astra 在 Chat Completions 里不能 tool calling，本来也不用）、`prompt_cache_options`（见 10.6）、
`service_tier`（默认 auto = 项目设置）、`seed`、`logprobs`。

回复：`choices[0]`；`message` 不是对象就按形状不对（`bad_response_body`）重试。先查回复本身的问题（Structured Outputs 指南 JSON mode 一节要求
先处理这几种情况），不解析 JSON：

| 情况 | 处理 |
|---|---|
| `message.refusal` 有值 | 报 `refusal`（日志记 `refusal: true`，拒答文字不记）；`AgentLLM.ask` 照旧带错误重问一次。拒答也按 usage 计费 |
| `finish_reason = "length"` | 报截断（`truncated`，说明文字和 DeepSeek 相同）；`AgentLLM.ask` 照旧要求「短一点再答一次」 |
| `finish_reason = "content_filter"` | 报 `content_filter` |
| `finish_reason = "stop"` | `json.loads(message.content)`，不剥代码块、不修补（用户决定 4） |

### 10.2 思考档位

| 模型 | 网页可选 | plan / judge / repair | 其余角色（含搜索） |
|---|---|---|---|
| GPT-6 Luna | off / low / medium / high | off：`none` + `temperature: 0`；其余同名 | `none` + `temperature: 0` |
| GPT-6.1 Sol | low / medium / high（不支持 none 和 minimal，不给 off） | 同名 | `low`（最低一档） |
| GPT-6 Astra | low / medium / high（不支持 none，发了 HTTP 400） | 同名 | `low` |

依据：Reasoning 指南（GPT-6 Astra does not support `none` … returns HTTP 400；GPT-6.1 Sol does not support `none` or `minimal` and defaults to `medium`；
6.1 Sol、6 Sol、Luna 默认 medium）、GPT-6 迁移指南 Limitations、三个模型页。网页 high 对应 `high`，不用 xhigh / max（官方：只在评测证明值得时用）。
effort 不是 none 的调用（含 Sol / Astra 的所有调用）max_completion_tokens +24,000（不超过 128,000）。OpenAI 不返回原始 reasoning token，
Chat Completions 也不给 reasoning summary；只有 `completion_tokens_details.reasoning_tokens` 计数（记进日志）。

### 10.3 错误、重试、余额

| 情况 | 处理 | 依据 |
|---|---|---|
| 401 / 403 | `KeyRejected`，不重试，**不读 body** | Error codes 页（401 Incorrect API key / Invalid Authentication；403 Country, region, or territory not supported）。10-21 实测：假 key 的 401 message 回显打了码的 key（`sk-proj-****…0000`），所以不读 |
| 429 且 `error.code` 是 `credit_balance_exhausted` / `organization_spend_limit_exceeded` / `project_spend_limit_exceeded` / `organization_usage_limit_exceeded`，或 `error.type` / `code` 是 `insufficient_quota` | `BalanceExhausted`，不重试，整次运行停下（第 6 节） | Error codes 页：For billing-related errors, inspect `error.code` … The broader `error.type` can still be `insufficient_quota`；Retrying billing, spend, or quota errors won't restore API access |
| 其余 429（`rate_limit_exceeded`、`slow_down`）、500、502、503（`server_is_overloaded`）、504 | 最多 3 次；有 `Retry-After` 就至少等那么久（最多 60 秒），否则 2 / 4 秒（搜索 3 / 6 秒） | Rate limits 页：Retry-After 是 minimum number of seconds；只对临时限流和 503 过载有意义 |
| 其余 4xx（参数不对等） | 不重试；`error.type`、`error.code`、message 前 200 字进日志和异常文字 | Error codes 页 BadRequestError |
| 3xx | 不跟随（D9），`TransportError` | 同 v2.6g |

`BalanceExhausted` 的文字：`insufficient balance: OpenAI HTTP 429 credit_balance_exhausted (no prepaid credits left) (...); the run was stopped without retrying.
Add credits or raise the spend limits in the OpenAI Platform settings (Billing / Limits), then run again.`（不含服务端原文。）
没加没有文档依据的「随机抖动」：Rate limits 页建议没有 Retry-After 时加 jitter，这里沿用现有的固定退避（同 DeepSeek / Claude）。

### 10.4 搜索

`POST https://api.openai.com/v1/responses`（非流式），请求头同上；body：

```json
{"model": "<所选模型>", "input": "<SEARCH_USER>", "tools": [{"type": "web_search"}], "tool_choice": "required",
 "max_tool_calls": 3, "include": ["web_search_call.action.sources"], "reasoning": {"effort": "none|low"},
 "max_output_tokens": 8192, "store": false}
```

- `{"type": "web_search"}`：web search 指南 For new Responses API integrations；`web_search_preview` 是旧版。不设 `search_context_size`（默认 medium）、
  `filters`、`user_location`（省略时默认美国，同 Claude 搜索不设地区）。
- `tool_choice: "required"`：指南 Limitations：With `tool_choice: "auto"`, search is optional. Use `tool_choice: "required"` … when search must run。
  搜索角色就是为了搜。和 DeepSeek / Claude 的搜索（不写 tool_choice）不一样，理由是 OpenAI 文档明写了。required 下服务端的工具循环怎么收尾，未实测。
- `max_tool_calls` = `max_uses`（3）：Responses 参考：所有内置工具调用合计的上限（含 open_page / find_in_page），超出的调用被忽略。比 Claude 的
  `max_uses`（只数搜索）更紧。
- `include`：sources（完整的 URL 列表，只有 url）默认不返回。
- `reasoning.effort`：搜索不是 plan / judge / repair，Luna 用 `none`，Sol / Astra 用 `low`（+24,000 余量）。web search 指南只写了 gpt-5 的 minimal
  不支持、gpt-5.4 的 none 结果可能变差，GPT-6 Luna 的 none 没写限制（未实测）。不发 temperature（同其他两家的搜索请求）。
- `store: false`：Responses 参考：Defaults to true when omitted，保存至少 30 天。
- 搜索用所选的模型（同 Claude），没有固定用 Luna。调研建议固定用 Luna 省钱（搜索内容 token 按模型 input 价计），那是「换模型」，没做，见 10.8。

解析（`openai_search_unpack`）：`output[]` 里 `web_search_call` 的 `action`：`search` -> 查询词（`queries`，没有就 `query`）和 `sources[].url`；
`open_page` -> url；`find_in_page` 不取。`message` 的 `output_text` -> 文字（模型挑的 URL，`parse_urls` 取）和 `url_citation` 注解的 url、title。
结果 URL 的顺序：引用的 -> sources -> open_page（Searcher 照旧先用文字里的 URL，不够再按这个顺序补）。标题只有引用有，不出 Searcher。
`web_search_call.status = failed` 记一个搜索错误；`status = incomplete`（如撞到 max_output_tokens）照样用已有的文字和 sources，日志 `stop` 记
`incomplete:max_output_tokens`。没有 pause_turn，不续（`max_search_continuations = 0`）。

计价：token 按 10.6；搜索费 = search 动作数 × $0.01（Pricing 页 Tools：Web search $10.00 / 1k calls；web search 指南：Search actions incur a
tool call cost）。open_page / find_in_page 不计次（文档只说 search 动作收费；未核实它们是否另收）。没有 action 的调用、failed 的调用也按一次算（保守）。

### 10.5 key 校验

`GET https://api.openai.com/v1/models`，`Authorization: Bearer`（List models 参考：返回 `{"object": "list", "data": [{"id", "created", "object",
"owned_by", "shutdown_date"}]}`，没有分页，所以列表是完整的：所选模型不在里面就是 `model_listed: false`）。不生成 token；有效 key 是否完全免费，
参考页没写价格（未核实）。10-21 实测（`probes/openai_key_probe.py`，没花钱）：

| 请求 | 状态 | body |
|---|---|---|
| 不带 key | 401 | `{"error": {"message": "Missing bearer authentication in header", "type": "invalid_request_error", "param": null, "code": null}}` |
| 假 key | 401 | `{"error": {"message": "Incorrect API key provided: sk-proj-**********************0000. You can find your API key at https://platform.openai.com/account/api-keys.", "type": "invalid_request_error", "param": null, "code": "invalid_api_key"}}` |
| 假 key 走 `check_key` | — | `{"provider": "gpt", "model": "gpt-6-luna", "ok": false, "status": 401, "error": "key_rejected", "message": "OpenAI rejected the API key (HTTP 401)"}` |

调研的推断（未核实）：余额为 0 的 key 可能能通过 `/v1/models`，要到真正调用时才报 429 `credit_balance_exhausted`。所以 key 校验通过不代表有钱，
网页上要写明。

### 10.6 价格和成本

`config.PRICES`（USD / 百万 token；https://developers.openai.com/api/docs/pricing ，Standard 档，2026-10-21 查看；没有分时价，`peak` = `offpeak`
= (cached input, input, output)）：

| 模型 | input | cached input | 30 分钟写 | 12 小时写 | output | input > 272K 的整次请求（input / cached / 30m / 12h / output） |
|---|---|---|---|---|---|---|
| `gpt-6-luna` | 0.10 | 0.01 | 0.125 | 0.25 | 0.50 | 0.20 / 0.02 / 0.25 / 0.50 / 0.75 |
| `gpt-6.1-sol` | 2.00 | 0.10 | 2.50 | 5.00 | 10.00 | 4.00 / 0.20 / 5.00 / 10.00 / 15.00 |
| `gpt-6-astra` | 10.00 | 1.00 | 12.50 | 25.00 | 50.00 | 20.00 / 2.00 / 25.00 / 50.00 / 75.00 |

`openai_usage_cost`（Prompt caching 页的算法）：普通 input = input − `cached_tokens` − `cache_write_tokens`；`cached_tokens` 按 cached input 价；
写入按 30 分钟写入价（Responses 有 `cache_write_tokens_details.ttl_30m_tokens` / `ttl_12h_tokens` 分档就分开算；Chat Completions 只有 30 分钟一档）；
output（含 reasoning token）按 output 价。input（Chat 的 `prompt_tokens`、Responses 的 `input_tokens`）超过 272,000 整次按长上下文价。
calls.jsonl 每行：`finish_reason`、`prompt_tokens`、`cached_tokens`、`cache_write_tokens`、`completion_tokens`、`usd`，开思考时 `reasoning_tokens`，
拒答时 `refusal: true`；搜索行：`input_tokens`、`cached_tokens`、`cache_write_tokens`、`output_tokens`、`reasoning_tokens`。`report.py` 照样能汇总。

**缓存写入（要你定）**：GPT-5.6 及以后，默认的 implicit 模式在最后一条 user 消息末尾写缓存，写入的 token 按 1.25 倍 input 价计（不是另加的费用，
是这部分 input 改按写入价算）。本项目每次调用的 user 消息都不同（网页、题目），写进去的大多不会被再读到（Prompt caching 页 gotcha：A shared prefix
is not always a cached prefix），所以 GPT 的输入大约贵 25%。本阶段**没改默认**（没要求做缓存，也不加没要求的参数），计价照实际 usage 算，
预扣和方向数按最坏情况（输入全按 30 分钟写入价）算。可选的改法：请求里加 `prompt_cache_options: {"mode": "explicit"}` 且不放断点 =
不用缓存、不产生写入（API 参考：If there are no explicit breakpoints, the request does not use prompt caching），或者在 developer 消息上放一个
explicit 断点只缓存固定的提示词（要改请求体的消息格式）。

预扣（`Budget.reserve_rates`）：输入按 30 分钟写入价（超过 272K 按长上下文的写入价），输出按发出的 max_completion_tokens / max_output_tokens。
方向数（`typical_direction_usd`）：`DIRECTION_PROFILE` 的 cache hit 和 miss 两部分都按 30 分钟写入价算（不指望命中缓存，保守），加 4 次 × $0.01。

### 10.7 `$2` 上限下的方向数和预扣（默认档位：Luna off，Sol / Astra low）

| 模型 | 一个方向 | `$2` 方向数 | 一次搜索预扣 | plan（2 万字符） | 抽取（4 万字符） | 抽取（40 万字符） | judge（10 万字符） |
|---|---|---|---|---|---|---|---|
| deepseek-flash（对照） | $0.060 | 10 | $0.099 | $0.010 | $0.025 | $0.079 | $0.029 |
| gpt-6-luna（off） | $0.054 | 10 | $0.088 | $0.004 | $0.011 | $0.033 | $0.012 |
| gpt-6-luna（high） | $0.054 | 10 | $0.088 | $0.016 | $0.011 | $0.033 | $0.024 |
| gpt-6.1-sol（low） | $0.201 | 5 | $0.477 | $0.325 | $0.450 | $0.900 | $0.485 |
| gpt-6-astra（low） | $0.819 | 1 | $2.065 | $1.625 | $2.250 | $4.500 | $2.425 |

- **Astra 在 `$2` 下跑不起来**：一次搜索的预扣（$2.07）就超过上限，第一轮第一个搜索就会让整次运行中止。
- **6.1 Sol 在 `$2` 下第一轮会中止**：5 个方向同时搜索，预扣合计 $2.39 > $2（同 v2.10b 记的 Opus 问题，第 9.8 节）。大头是思考余量：
  搜索的 max_output_tokens 32,192 × $10 / 百万 = $0.32。
- 修法同第 9.8 节（自带 key 的运行里预扣只是因为在途调用放不下时等在途调用结束；或者贵模型默认上限更高、并发更低），等你定。
- 默认模型用 Luna（`PROVIDERS["gpt"]["default_model"]`）：只有它在 `$2` 下能跑满，也是三个里唯一能关思考的（`ModelSpec` 的默认档位是 off）。
  官方文档的说法是「新项目从 gpt-6-astra 开始」。Claude 那边默认是 Opus 5.5（v2.10b 按官方推荐定的），两家口径不一致，要统一随时说。

### 10.8 已知限制、没做的

- **缓存写入的默认行为没改**（10.6，要你定）。
- **搜索没有固定用 Luna**：搜索内容 token 按所选模型的 input 价计，Astra 的搜索比 Luna 贵约 100 倍（调研的建议是 Searcher 固定用 Luna）。
  固定用 Luna 等于「用户选了 Astra，搜索却换成 Luna」，和「按所选模型」不一致，没做，要不要做你定。
- 每次搜索的内容 token 数文档没给；搜索上下文窗口最大 128K（web search 指南）。预扣照旧假设每次搜索输入 30,000 token（DeepSeek 实测；v2.10f 起自带 key 的运行按 p99 72,000，第 14.3 节），
  Sol / Astra 的真实搜索可能更贵，超出部分事后计入（`Budget.add`），上限可能被一次搜索超过一点。
- 非流式：生成完才回 body。单次读超时设 1,200 秒、整次 1,800 秒（`chat_timeouts`）；Astra / Sol 开 high 的长回复要多久，没实测。读超时后会重试，
  而服务端那次请求可能已经计费。搜索沿用 600 秒（Searcher 共用）。
- `tool_choice: "required"` + `max_tool_calls` 的收尾行为、Luna 在 `none` 下用 web_search 的效果、json_object 在 GPT-6 Chat Completions 上的
  表现，都只按文档写，没有真 key 实测。
- `temperature` 在 effort 不是 none 时发了会 400 还是被忽略，文档没写（未核实）；代码不发，所以不影响。
- 中国大陆、香港、澳门不在 OpenAI supported countries 列表里（调研记录；官方警告 accessing or offering access 可能导致封号），网页阶段要写明。
- 调研说 Free 档能不能用 GPT-6、reasoning summary 要不要组织验证，没查到（未核实）；本项目不请求 summary。
- ~~预扣的 token 估计仍是「字符数 / 2」~~（v2.10f：按 1 个字符 1 个 token，第 14.3 节）；OpenAI 的 tokenizer 英文约 4 字符 / token，偏保守。`DIRECTION_PROFILE` 是 DeepSeek 不开思考时的输出量，
  Sol / Astra 关不掉思考，真实的一个方向会更贵（未测），靠预扣守住上限。
- 网页还没接（同第 8 节）。

### 10.9 Verification（v2.10c）

- `tests/test_openai.py`（28 个）全部对着 127.0.0.1 上的假 OpenAI 服务（`tests/fake_openai.py`，复用 `fake_claude.py` 的脚本化服务）跑，
  真实走 urllib + `urlopen_no_redirect`：请求头 / 请求体（逐字段、键顺序）、三个模型 × 档位 × 角色的 reasoning_effort / temperature /
  max_completion_tokens、developer 角色、余量封顶 128K、usage 计价（cached、cache_write、reasoning、272K 门槛、Responses 的 30m / 12h 分档）、
  拒答 / 截断 / content_filter、不修 JSON、形状不对重试、六种余额 / 额度 429 不重试、限流 / slow_down / 503 按 Retry-After 重试、普通 400 照原样报
  （带 code）、401 / 403 不读 body、打码 key 不进日志、3xx 不跟随、方向数、预扣、搜索请求体、URL / 查询词 / 标题 / 搜索费、open_page /
  find_in_page / failed / incomplete、搜索的余额 / 503 / 400、key 校验（含 10-21 实测的两种 401 body）、端到端（prepare_run -> 图 -> save_run，
  429 credit_balance_exhausted 干净停下，结果目录没有 key，key 已清掉）。
- 变异检查 18 处（去掉 store、错发 temperature、漏认 credit_balance_exhausted、不改 developer、tool_choice 改 auto、漏 include、计价不扣写入、
  272K 用 >=、open_page 计次、URL 顺序、预扣不用写入价、方向数不用写入价、不打码、不看 Retry-After、关思考发 low、不认拒答、读 401 body 等）：全部被测试抓到
  （读 401 body 那一处是补了 `read_error_body` 没被调用的断言后抓到的）。
- DeepSeek 默认路径：`tests/test_providers.py` 的 24 组金样本仍逐字节相同；Claude 的 31 个测试不变。
- G2（`probes/compare_continuous_prompts.py`）：HEAD（v2.10b）和本阶段都是 `365b06515d8caef8257020c2e5d574de7724be2f2270c122e6e21952517f78c4`。
- 真实网络只发了 3 次不花钱的 GET（`probes/openai_key_probe.py`：不带 key、假 key 直接发、假 key 走 check_key，都是 401）。没有真 key，
  没发过 `/v1/chat/completions`、`/v1/responses`。
- 测试改动：`tests/test_providers.py` 里两个「没有价格的模型」测试原来拿 `gpt-6-luna` 当例子，现在它有价格了，换成 `no-such-model-x`。

## 11. Kimi adapter（`KimiAdapter`，v2.10d）

Moonshot AI 开放平台。同前两家：标准库 urllib，不装 SDK（官方示例用 OpenAI SDK 换 base_url；这里直接发 HTTP，和其余 provider 共用外层循环、
不跟随跳转、假服务测试）。JSON 调用走 OpenAI 兼容的 Chat Completions；Responses / Anthropic Messages 兼容接口文档里只支持 `kimi-k3`，不用
（K2.6 只能走 Chat Completions）。API 细节在 2026-10-21 对照官方 `.md` 原文（页面地址加 `.md`）逐条核过，价格表是 JS 渲染的，数字取自页面 HTML
里编译后的表格（见 11.6）。

### 11.1 区域和 key

| `region` | 平台（控制台） | API 地址 | 计价 |
|---|---|---|---|
| `global`（默认） | 国际站 platform.kimi.ai（旧域名 platform.moonshot.ai 会 301 过去） | `https://api.moonshot.ai/v1` | USD |
| `cn` | 国内站 platform.kimi.com（旧域名 platform.moonshot.cn） | `https://api.moonshot.cn/v1` | CNY，按 2026-10-21 人民币汇率中间价 1 USD = 6.7192 CNY 折成 USD |

- 两站的账户、余额、key 完全独立，混用返回 401（Common Error Codes 页 Platform key isolation；List Models 页）。网页上用户自己选区域。
  调研里提到的「401 时换另一站自动判断」没做（等于拿用户的 key 去另一个地址试）。
- 计价 id：国际站就是模型名（`kimi-k2.6`、`kimi-k3`），国内站 `kimi-k2.6@cn`、`kimi-k3@cn`（`ModelSpec.price_id`）。请求里发的、calls.jsonl 里记的
  `model` 都是模型名；`state.json` 的 `settings.run_spec` 在国内站另记 `price_id` 和 `fx`（汇率、来源、日期）。
- 汇率来源：中国人民银行授权中国外汇交易中心公布的 2026-10-21 人民币汇率中间价（https://www.pbc.gov.cn/zhengcehuobisi/125207/125217/125925/2026102108513972558/index.html ）。
  固定常数 `config.CNY_PER_USD`，不随行情更新；汇率变动 1% 时成本估计差 1%。
- 调研记录（本阶段没再核实）：Kimi Code 订阅的 key 不能用在开放平台；美国用户能否用信用卡给国际站充值文档没写清。

### 11.2 JSON 调用发什么

`POST {base}/chat/completions`，请求头 `Content-Type: application/json`、`Authorization: Bearer <key>`。body 依次是：

| 字段 | 值 | 为什么 |
|---|---|---|
| `model` | `kimi-k2.6` / `kimi-k3` | 用户决定 9 的清单 |
| `messages` | 原样（Kimi 收 `system` 角色）；内容为空的 assistant 消息不发 | Chat API：content must not be empty（AgentLLM.ask 重问时，回复被思考用完、正文为空，就会出现空的 assistant 消息） |
| `thinking`（K2.6） | `{"type": "disabled"}` / `{"type": "enabled"}` | K2.6 默认 enabled，要关必须显式写；不支持 `reasoning_effort`（Model Parameter Reference） |
| `reasoning_effort`（K3） | `low` / `high` / `max` | K3 永远在想，顶层 `reasoning_effort`，省略时默认 `max`（最贵），所以每次都显式写；文档：K3 不发 `thinking` |
| `response_format` | `{"type": "json_object"}` | 用户决定 4 / 10：普通 JSON 写法，不用 json_schema。文档要求在 prompt 里写明 JSON 的字段（现有 prompt 都写了） |
| `max_completion_tokens` | 角色的 `MAX_TOKENS`，开思考 +24,000，最多 K2.6 262,144 / K3 1,048,576 | Chat API：`max_tokens` 已 Deprecated；思考 token 和正文共用这个上限（Thinking 指南：the sum of tokens in reasoning_content and content must be less than or equal to max_tokens） |
| `stream` | `true` | Common Error Codes 页：服务端 900 秒没回就 504，Common with long non-streaming requests. Use streaming output；Thinking 指南也建议思考模型开流式 |
| `stream_options` | `{"include_usage": true}` | 不写就拿不到 usage（Chat API：usage 在 `[DONE]` 之前的最后一个 chunk） |

不发：`temperature`、`top_p`、`n`、`presence_penalty`、`frequency_penalty`（Model Parameter Reference：三个模型上都是固定值，"passing any other value returns
an error, so do not pass it explicitly"；用户决定 5）；`prompt_cache_options`（省略 = 默认 5 分钟档的隐式缓存写入，没要求做缓存）；`tools`、`tool_choice`、
`partial`（文档：Partial Mode 不要和 json_object 混用）、`prompt_cache_key`、`safety_identifier`。

回复（`providers.parse_chat_sse`）：每个事件一行 `data: <chunk>`，`choices[0].delta.content` 累加，`finish_reason` 取最后一个非空值，`usage` 取带 usage 的 chunk，
`data: [DONE]` 结束；`delta.reasoning_content`（思考内容，总在 content 之前）不拼、不记；`:` 开头的注释行和 CRLF 都认。只 `json.loads(content)`，不剥代码块、不修补。

| 情况 | 处理 |
|---|---|
| `finish_reason = "stop"` | 解析 JSON |
| `finish_reason = "length"` | 报截断（`truncated`，说明文字和 DeepSeek 相同）；`AgentLLM.ask` 照旧要求「短一点再答一次」 |
| 其余（不带工具时出现 `tool_calls`、流里没给 finish_reason） | 报 `unexpected_finish`，不解析（Chat API 的枚举只有 stop / length / tool_calls） |
| 没收到 `[DONE]`、流里来了 `error` 对象 | `StreamError` -> `bad_response_body`（`stream_error` 记类型），按已有逻辑重试 |
| 收到 `[DONE]` 却没有 usage | 照常用回复，日志 `usage_missing: true`（文档：流被打断时可能收不到 usage；重试会重复计费）。v2.10f：`usd` 按这次调用的预扣记（`usd_basis: "reserve (usage missing)"`），不再记 0 |
| 内容审核 | HTTP 400 `content_filter`（不是 finish_reason），照原样报 |

单次读最多 600 秒、整次 3,600 秒（`chat_timeouts`，没实测）。

### 11.3 思考档位

| 模型 | 网页可选 | plan / judge / repair | 其余角色（含生成查询词） |
|---|---|---|---|
| K2.6 | off / low / medium / high（没有深度：low / medium / high 都是「开」，`thinking_depth = False`，网页合并显示） | off：`disabled`；其余：`enabled` + 24,000 | `disabled` |
| K3 | low / medium / high（永远在想，不给 off） | low -> `low`、medium -> `high`、high -> `max`（+24,000） | `low`（+24,000） |

- K3 的映射按调研的建议（`providers_research.json` 的 suggested_mapping：medium -> high，high -> max）。**和另外三家不一样**：DeepSeek / Claude / GPT 的网页 high
  都对应 `high`、不用 max / xhigh。K3 只有三档、默认就是 max，所以这里 high 用了 max；要统一成「high -> high」随时说（medium 和 high 会变成同一档）。
- Model Parameter Reference：切换档位会让前缀缓存失效。本项目各角色的 prompt 本来就不同，影响不大。
- K3 的多轮对话要求把 API 返回的完整 assistant 消息（含 `reasoning_content`）原样传回（Reasoning Effort 页）。`AgentLLM.ask` 带错误重问时只传正文的前 2,000 字（所有
  provider 共用的协议，本阶段没改），K3 上这样做会怎样文档没写（未核实）。

### 11.4 错误、重试、余额

| 情况 | 处理 | 依据 |
|---|---|---|
| 401 / 403 | `KeyRejected`，不重试，不读 body | Common Error Codes 页（401 invalid_authentication_error / incorrect_api_key_error；403 permission_denied_error：API 没开放、IP 不在白名单）。10-21 实测见 11.8 |
| 429 `exceeded_current_quota_error` | `BalanceExhausted`，不重试，整次运行停下（第 6 节） | Common Error Codes 页：Account balance is insufficient or the account has been disabled / Token quota is insufficient -> Top up |
| 429 `engine_overloaded_error`、`rate_limit_reached_error`；500、502、503、504 | 最多 3 次；有 `Retry-After` 就至少等那么久（最多 60 秒），否则 2 / 4 秒 | 同上页：overloaded 按 Retry-After 退避；组织并发 / RPM / TPM / TPD 超限等一会儿再试 |
| 其余 4xx（400 参数不对、输入 + max_completion_tokens 超过上下文、content_filter；404 模型不存在或账户没权限，例如 K3 没解锁） | 不重试；`error.type` 和 message 前 200 字进日志和异常文字 | 同上页 |
| 3xx | 不跟随（D9），`TransportError` | 同 v2.6g |

`BalanceExhausted` 的文字：`insufficient balance: Kimi HTTP 429 exceeded_current_quota_error (balance insufficient, account in arrears or disabled, or token quota used up)
(...); the run was stopped without retrying. Top up the Kimi account on the platform where the key was created (platform.kimi.ai or platform.kimi.com), then run again.`（不含服务端原文。）
Kimi 文档里没有 402；也没有像 OpenAI 那样分「用户自设的消费上限」的错误码（国际站项目可设每日预算，到额后拒绝请求，调研记录有约 10 分钟延迟；返回什么错误没查到，未核实）。

### 11.5 搜索：生成查询词 + `POST /v1/tools/search`

为什么不用模型自己搜：内置工具 `$web_search` 在 2026-10-20 下线（WebSearch Pricing 页：expected to be deprecated on October 20, 2026；For new integrations, please use the
`/v1/tools/search` endpoint）；Anthropic 兼容接口文档里没有 web_search 服务端工具（调研记录）；Responses API 的 web_search 只支持 K3、计费页没列价格（调研记录）；官方工具 `web-search`
的结果是加密的、拿不到 URL（调研记录）。所以搜索由代码驱动（`search_mode = "queries"`，`Searcher._search_by_queries`）：

1. **生成查询词**：一次 `LLM.json_call`（同一个 adapter、同一套重试和日志，日志交给 Searcher 的 log，agent 里就是写 calls.jsonl 并计入预算），arm 是 `search:<方向>:queries`
   （思考角色还是 `search`：K2.6 关思考、K3 用 low），`max_completion_tokens` = `SEARCH_QUERIES_MAX_TOKENS`（2,000，开思考 +24,000）。只调一次，不像 `AgentLLM.ask` 那样
   带错误重问（调用方 `run_direction` 已经占着并发名额和预扣；在里面再拿名额可能死锁）。失败（不是合法 JSON、截断、没有 `queries` 列表、列表为空、传输错误、key 被拒）就没有 URL，
   `error` 以 `queries:` 开头，不发搜索请求；余额不足照样抛 `BalanceExhausted`。查询词只做最少的整理：去首尾空白、去掉空的 / 重复的 / 非字符串的，最多 `max_uses`（3）个。
2. **搜索**：每个查询词 `POST {base}/tools/search`，Bearer，body `{"text_query": <查询词>, "limit": <cap，即 urls_per_direction 4>, "timeout_seconds": 30}`
   （Web Search Basic 页：`text_query` 必填；`limit` 1–20，默认 5；`timeout_seconds` 1–60，省略 = 不限时；`include_content` 用默认 false，页面由 fetch 自己取）。
   查询词按顺序一个一个发（不并发：Tier0 的搜索 QPS 只有 1）。一个失败不影响其余的，原因合在 `error` 里（`query 2: http_400 (invalid_request: ...)`）。
3. **合并**：`search_results[].url`（和 `title`）按名次交替合并（每个查询词的第 1 名，再第 2 名……），经 `parse_urls` 去重、去 `#fragment`，取 `cap` 个。标题解析出来但不出 Searcher
   （分析角色只拿得到 URL，同其他 provider）；snippet 不用。返回的字段同其他 provider（`queries` 是生成的查询词，照旧进 state.json 审计和回测的泄漏检查）。

生成查询词的 prompt（`agent/prompts.py`，新加的，只有这类 provider 用；搜索角色收到的仍是 `SEARCH_USER` 填好的那段，原样放进 `{brief}`；DeepSeek / Claude / GPT 的搜索、G2 都不经过它）：

```text
SEARCH_QUERIES_SYSTEM:
You write web search queries for a research assistant. In this step you cannot browse: a search engine will run your queries exactly as written, and code will collect the result URLs. Reply with one JSON object only.

SEARCH_QUERIES_USER:
Below is a research brief written for an assistant that searches the web itself. Here your only job is to write the searches: up to {n} queries that, run as written in a web search engine, are most likely to return the pages the brief asks for.

- Write each query as a search engine query (keywords and names), not as a question addressed to a person.
- Make the queries differ from one another: different sources, terms, or angles taken from the brief.
- Ignore the brief's final instruction about listing URLs; code collects the URLs from the search results.

Research brief:
<<<
{brief}
>>>

Reply with one JSON object: {"queries": ["first query", "second query"]}
```

（`{n}` = `max_uses` = 3。brief 末尾那句「After searching, reply with at most N URLs ...」是给会自己搜的模型的，这里让模型忽略。）

计费和日志：生成查询词那次按 token 计价（11.6）；搜索按次：只有 HTTP 200 且 `search_results` 非空才收（Web Search Basic 页、WebSearch Pricing 页），国际站 $0.002 / 次、
国内站 ¥0.01 / 次（折 USD）。calls.jsonl：一行 `search:<方向>:queries`（同 JSON 调用的字段），每个查询词一行 `kind: "search"`、`query_n`、`web_search_requests`（0 或 1）、
`n_result_urls`、`usd: 0.0`、`usd_search_fee_assumed`（字段名沿用，值是官方价）。

重试：搜索接口的 429 `rate_limited` 带 `X-RateLimit-Limit` / `Remaining`，按秒限速时还有 `X-RateLimit-Reset`（Unix 秒）：没有 `Retry-After` 时等到 reset（`llm.retry_after`，
至少 3 / 6 秒，最多 60 秒）；`rate_limit_unavailable`、500 `internal_error`、502 `upstream_failed`、504 `timeout` 退避重试。401 / 403 没有 body（文档；10-21 实测 401 的
Content-Length 是 0），不读、不抛，记 `http_401`（和其他 provider 的搜索一样，见第 8 节）。搜索接口的错误码表没列余额不足；按聊天接口的规则（429 `exceeded_current_quota_error`）认，
未核实它是不是用同一个 type。

预扣：`run_direction` 照旧在整个 `Searcher.search` 外面 `hold(search_reserve())`。Kimi 的 `Budget.search_tokens` = 生成查询词那次发出的 max_completion_tokens（K2.6 2,000，K3 26,000），
输入照旧按 30,000 token 估，搜索费按 `(2 × max_uses + 2)` 次，都偏保守。

### 11.6 价格和成本

`config.PRICES`（每百万 token；不含税；没有分时价，`peak` = `offpeak` = (cache hit, cache miss, output)）。国际站 https://platform.kimi.ai/docs/pricing/chat 、
国内站 https://platform.kimi.com/docs/pricing/chat ，2026-10-21 查看。K3 表的列：Cache Write Price (TTL 5min) / (TTL 1h) / Cached Input Price / Input Price / Output Price；
K2 表的列：Input Price (Cache Hit) / (Cache Miss) / Output Price。

| 计价 id | cache hit | cache miss | 5 分钟写入 | 1 小时写入 | output | 搜索 / 次 |
|---|---|---|---|---|---|---|
| `kimi-k3` | $0.30 | $3.00 | $3.00 | $6.00 | $15.00 | $0.002 |
| `kimi-k2.6` | $0.16 | $0.95 | —（不单列，按 miss） | — | $4.00 | $0.002 |
| `kimi-k3@cn` | ¥2.00 | ¥20.00 | ¥20.00 | ¥40.00 | ¥100.00 | ¥0.01 |
| `kimi-k2.6@cn` | ¥1.10 | ¥6.50 | — | — | ¥27.00 | ¥0.01 |

CNY 原价存在 `PRICES[...]["listed"]`，`peak` / `search_fee_usd` 是除以 6.7192 以后的 USD。K3 的价格另由 Context Caching 指南正文核对（$3.00 / $3.00 / $6.00 / $0.30）；
搜索价由 WebSearch Pricing 页正文核对（$0.002；国内站表格 ￥0.01）。

`kimi_usage_cost`（Chat API usage 说明）：`prompt_tokens` 是全部输入；`prompt_tokens_details.cached_tokens`（命中）、`cache_write_tokens`（写入）和未缓存部分互斥、相加等于
`prompt_tokens`。命中按 hit 价，写入按 5 分钟写入价（不写 `prompt_cache_options` 就是 5 分钟档；K2 没有单列写入价，按 miss），其余按 miss，`completion_tokens`（含思考）按 output。
没有 `prompt_tokens_details` 时用顶层 `cached_tokens`。calls.jsonl：`finish_reason`、`prompt_tokens`、`cached_tokens`、`cache_write_tokens`、`completion_tokens`、`usd`；
`completion_tokens_details.reasoning_tokens` 有才记（Chat API 的 usage 没写这个字段）。

方向数：`prompt_cache = "implicit"`：服务端自动缓存，但这个 agent 在 Kimi 上的命中率没测过，`DIRECTION_PROFILE` 的 hit 和 miss 两部分都按 miss（K3 的 5 分钟写入价同 miss）算，
加 4 次 × 每次搜索费。预扣（`Budget.reserve_rates`）：输入按 miss 和 5 分钟写入价中较高的。

### 11.7 `$2` 上限下的方向数和预扣

| 计价 id（档位） | 一个方向 | `$2` 方向数 | 一次搜索预扣 | plan（2 万字符） | 抽取（4 万字符） | 抽取（40 万字符） | judge（10 万字符） |
|---|---|---|---|---|---|---|---|
| deepseek-flash（对照） | $0.060 | 10 | $0.099 | $0.010 | $0.025 | $0.079 | $0.029 |
| kimi-k2.6（off） | $0.069 | 10 | $0.052 | $0.034 | $0.083 | $0.254 | $0.096 |
| kimi-k2.6（high） | $0.069 | 10 | $0.052 | $0.130 | $0.083 | $0.254 | $0.192 |
| kimi-k3（low / high 相同） | $0.207 | 5 | $0.496 | $0.480 | $0.660 | $1.200 | $0.690 |
| kimi-k2.6@cn（off） | $0.067 | 10 | $0.049 | $0.034 | $0.084 | $0.258 | $0.097 |
| kimi-k3@cn（low） | $0.203 | 5 | $0.488 | $0.476 | $0.655 | $1.191 | $0.685 |

- **K3 在 `$2` 下第一轮会中止**（同第 9.8 / 10.7 节的 Opus / 6.1 Sol 问题）：5 个方向同时搜索，预扣合计约 $2.48 > $2。大头是思考余量：K3 关不掉思考，每次调用都 +24,000 token × $15 / 百万 = $0.36。
  修法同前（自带 key 的运行里预扣只是因为在途调用放不下时等在途调用结束；或者贵模型默认上限更高、并发更低），等你定。
- 默认模型 K2.6（`PROVIDERS["kimi"]["default_model"]`）：`$2` 下跑满 10 个方向、能关思考（同 GPT 选 Luna 的理由）；调研记录官方 FAQ 讲成本时也推荐它（本阶段没再核实）。K3 还要先充值才解锁（K3 quickstart：minimum $1）。

### 11.8 key 校验

`GET {base}/models`，Bearer（List Models 页：返回 `{"object": "list", "data": [{"id", "context_length", "supports_reasoning", ...}]}`，没有分页，所以列表是完整的）。
不生成 token；有效 key 是否完全免费，文档没写价格（未核实）。余额为 0 的 key 能不能通过 `/models` 没查到（未核实）；K3 没解锁时校验也可能通过，到调用时才 404。
10-21 实测（`probes/kimi_key_probe.py`，没花钱）：

| 请求 | 状态 | body |
|---|---|---|
| 国际站 `GET /v1/models` 不带 key | 401 | `{"error":{"message":"Incorrect API key provided","type":"incorrect_api_key_error"}}` |
| 国际站 `GET /v1/models` 假 key | 401 | `{"error":{"message":"Invalid Authentication","type":"invalid_authentication_error"}}` |
| 国内站 `GET /v1/models` 假 key | 401 | 同上 |
| 国际站 `POST /v1/tools/search` 假 key | 401 | 空（Content-Length 0，带 `X-Msh-Track-Id` / `X-Msh-Chat-Id`） |
| 国际站 `POST /v1/chat/completions` 假 key | 401 | 同 `/models` 假 key |
| 假 key 走 `check_key`（国际站、国内站） | — | `{"provider": "kimi", "model": ..., "ok": false, "status": 401, "error": "key_rejected", "message": "Kimi rejected the API key (HTTP 401)"}` |

两个 API 主机都没有跳转。服务端的 401 message 没有回显 key。

### 11.9 已知限制、没做的、要你定的

- **K3 在 `$2` 下第一轮中止**（11.7，要你定，和 Opus / Sol 同一个问题）。
- **K3 的 high -> max 映射**和另外三家的口径不同（11.3，要你定）。
- **新账户（Tier0：累计充值 $1）基本跑不动**：并发 1、RPM 3、TPD 150 万、搜索 QPS 1（Recharge and Rate Limits 页）。agent 默认并发 8，会连续撞 429 `rate_limit_reached_error`，
  3 次重试后这些调用失败；调研估计一次运行约 100 万 token，一天大约只够一次。Tier1（累计 $10：并发 15、RPM 100、QPS 3）以上才正常。没做自动降并发 / 本地排队，网页上要写明。
- K2.6 的上下文是 262,144：输入 + max_completion_tokens 超过就 400（照原样报）。抽取最多发 40 万字符，中文页按官方「1 token 约 1.5–2 个汉字」可能接近或超过上限；预扣仍按「字符数 / 2」估。
- ~~流式回复收到 `[DONE]` 却没有 usage 时，这次调用的成本按 0 记~~（v2.10f：按这次调用的预扣记，第 14.3 节）；文档说只有流被打断才会这样。
- 生成查询词只调一次、失败就没有 URL；搜索结果只按名次交替合并，没有像其他 provider 那样由模型在看过结果之后挑 URL（只允许一次小的 JSON 调用）。这一步的效果没有真 key 实测。
- 搜索接口的余额不足错误没写在文档里（11.5）；搜索接口的 403（Account inactive or suspended）照原样记，不停整次运行。
- json_object + 流式 + K3 思考的组合、K2.6 关思考时的 json_object 表现、`timeout_seconds: 30` 是否够，都只按文档写，没有真 key 实测。
- 国内站的价格按固定汇率折算（11.1）。
- 网页还没接（同第 8 节）：区域选择、K2.6「没有深度」的提示、Tier0 的提示都留给网页阶段。

### 11.10 Verification（v2.10d）

- `tests/test_kimi.py`（33 个）全部对着 127.0.0.1 上的假 Kimi 服务（`tests/fake_kimi.py`，复用 `fake_claude.py` 的脚本化服务；国内站接在 `/cn/...`）跑，真实走 urllib +
  `urlopen_no_redirect`：请求头 / 请求体（键顺序、禁发的采样参数）、两个模型 × 档位 × 角色的 `thinking` / `reasoning_effort` / `max_completion_tokens`、余量封顶、区域路由、
  空 assistant 消息、流式拼接（CRLF、注释行、思考内容不进返回值和日志）、usage 计价（命中、写入、K2 写入按 miss、国内站折算）、截断 / 意外 finish_reason / 断流 / 流内 error / 缺 usage、
  不修 JSON、余额 429 不重试、overload / rate limit / 503 重试、400 / 404 照原样报、401 / 403 不读 body、3xx 不跟随、价格表、方向数、预扣、按区域的搜索费、
  查询词调用的 prompt 和参数、搜索请求体、交替合并、空结果不计费、单个查询词失败、`X-RateLimit-Reset` 等待、搜索 401 / 形状不对、生成查询词的六种失败、查询词整理、
  两处余额不足、一个方向的端到端（查询词 -> 搜索 -> 取页 -> 抽取 -> 核对，三次调用计入预算）、key 校验（含 10-21 实测的两种 401 body）、ModelSpec、
  整次运行端到端（国内站 K3，429 余额不足干净停下，结果目录没有 key，key 已清掉，settings 记 price_id / 汇率 / 搜索设置）。
- 变异检查 26 处（发 temperature、去掉 stream_options、K3 high 改 high、K2.6 总开思考、认错余额 type、写入按命中价、未缓存不扣写入、合并改成拼接、空结果也计费、计量不用 price_id、
  预算不用 price_id、搜索费不分区域、不看 X-RateLimit-Reset、保留空 assistant、把思考拼进正文、没有 [DONE] 也接受、意外 finish_reason 照样解析、搜索预扣用 8192、读 401 body、
  查询词调用用 8192、不发 timeout_seconds、国内站地址写错、方向估价算缓存命中、吞掉查询词调用的余额错误、不整理查询词、不限查询词个数）：全部被测试抓到。
- DeepSeek 默认路径：`tests/test_providers.py` 的 24 组金样本仍逐字节相同；Claude、GPT 的测试不变（`llm.retry_after` 对它们的行为和以前相同）。
- G2（`probes/compare_continuous_prompts.py`）：HEAD（v2.10c）和本阶段都是 `365b06515d8caef8257020c2e5d574de7724be2f2270c122e6e21952517f78c4`。新加的 `SEARCH_QUERIES_*` 不在 G2 的路径上。
- 真实网络只发了 7 个不花钱的请求（`probes/kimi_key_probe.py`，全部 401）。没有真 key，没有发过成功的 `/chat/completions`、`/tools/search`。
- 本阶段对其他代码的改动：`config.MAX_TOKENS` 没动（新常数 `SEARCH_QUERIES_MAX_TOKENS` 放在 `agent/search.py`，免得 DeepSeek 运行的 settings 变）；
  `ModelSpec` 先校验区域再查价格（按 price_id）。

## 12. GLM adapter（`GLMAdapter`，v2.10e）

Z.ai 国际站和智谱开放平台国内站。同前几家：标准库 urllib，不装官方 SDK（`zai-sdk`）：和其余 provider 共用外层循环、不跟随跳转、假服务测试。
JSON 调用走 OpenAI 兼容的 Chat Completions（两站的 API 参考都写明）；Anthropic Messages 兼容端点和 Responses 兼容端点支持哪些参数没写全（调研记录），不用。
API 细节在 2026-10-21 对照两站官方 `.md` 原文（页面地址加 `.md`）逐条核过；国际站和国内站的同名页面有出入时分开写。

### 12.1 区域和 key

| `region` | 平台（控制台） | API 地址（通用端点） | 计价 |
|---|---|---|---|
| `global`（默认） | Z.ai（z.ai） | `https://api.z.ai/api/paas/v4` | USD（价格页：All prices are in USD） |
| `cn` | 智谱开放平台（bigmodel.cn） | `https://open.bigmodel.cn/api/paas/v4` | CNY，按 2026-10-21 中间价 1 USD = 6.7192 CNY 折成 USD（同 Kimi，`config.CNY_PER_USD`） |

- **只收 Standard API Key**。两站 10-16 的公告（API Key Management Guide / API Key 分类管理说明）：从 2026-10-16 起标准 API 的 key 和 GLM Coding Plan 的 key
  分开管理，key 的类型决定计费方式（换端点不改变）；Coding Plan 的使用规范：只能在官方支持的工具里用，违规可能被限流、冻结，多次违规封号。
  所以：只用通用端点 `/api/paas/v4`，代码里没有 Coding Plan 端点 `/api/coding/paas/v4`（测试检查 regions 里没有 `coding`）；网页上显示 `GLM_KEY_NOTE`
  （`providers.GLM_KEY_NOTE`，也挂在 `GLMAdapter.key_note` 和 `PROVIDERS["glm"]["key_note"]`）：

  > Use a Standard API Key: on Z.ai, API Keys -> Standard API Key (https://z.ai/manage-apikey/apikey-list); on bigmodel.cn, the standard API Keys page
  > (https://bigmodel.cn/usercenter/proj-mgmt/apikeys). GLM Coding Plan keys (Personal / Team Coding Plan) are not allowed: since 2026-10-16 they are a
  > separate key type, and the usage policy limits them to officially supported coding tools (violations can lead to rate limiting or a frozen account).
  > This app only calls the general endpoint /api/paas/v4, never the Coding Plan endpoint /api/coding/paas/v4.

  有人填了 Coding Plan 的 key：服务端如果回 429 + 1309 / 1311 / 1314 / 1315（套餐过期、套餐不含这个模型、企业套餐 key），整次运行停下并提示换 Standard API Key（12.4）。
  文档没写 Coding Plan key 打通用端点会怎样（是否直接拒绝），未核实。
- 两站的 key 能不能互通没写（调研记录），按两个独立平台处理；用户自己选区域。计价 id：国际站是模型名，国内站 `glm-5.3@cn` 等（`ModelSpec.price_id`），
  `state.json` 的 `run_spec` 在国内站另记 `price_id` 和 `fx`。
- 国际站 FAQ：账单按天显示前一天（n-1）的消费，刚跑完看不到扣费是正常的；信用卡充值不支持 3DS。网页阶段要写明。

### 12.2 JSON 调用发什么

`POST {base}/chat/completions`，请求头 `Content-Type: application/json`、`Authorization: Bearer <key>`（两站的 HTTP API 页；可选的 `Accept-Language` 不发）。body 依次是：

| 字段 | 值 | 为什么 |
|---|---|---|
| `model` | `glm-4.7-flashx` / `glm-5.2` / `glm-5.3` | 用户决定 9 的清单 |
| `messages` | 原样（GLM 收 `system` 角色） | API 参考没要求 assistant 的 content 非空（不像 Kimi / Claude），所以 `AgentLLM.ask` 重问时的空 assistant 消息照原样发 |
| `thinking` | `{"type": "enabled"}` / `{"type": "disabled"}` | ChatThinking：默认 enabled；5.3 只能 enabled（disabled 报错）；5.2 和 4.7 系列能 disabled |
| `reasoning_effort`（5.3 / 5.2，开思考时） | 5.3：`low` / `high` / `max`；5.2：`high` / `max` | 只在 thinking 为 enabled 时生效、默认 max（最贵），所以每次都显式写；4.7 系列没有这个参数（只有 5.2 及以上有） |
| `response_format` | `{"type": "json_object"}` | 用户决定 4 / 10：普通 JSON 写法（enum 只有 text / json_object，没有 json_schema）。结构化输出指南的做法是 prompt 里写明格式（现有 prompt 都写了） |
| `max_tokens` | 角色的 `MAX_TOKENS`，开思考 +24,000，最多 131,072 | API 参考 / Core Parameters：参数名是 `max_tokens`（没有 max_completion_tokens），1–131,072，不写默认 65,536。思考 token 算不算进 `max_tokens` 文档没写（未核实），按 DeepSeek 的做法给余量 |
| `stream` | `false` | 非流式：文档没写非流式请求的服务端超时（不像 Kimi 的 900 秒）；而流式调用时推理中途出错不回错误码、只在 `finish_reason` 里写原因（错误码页的注），非流式出错直接是 HTTP 状态 + 业务码，好处理 |

不发：`temperature`、`top_p`、`do_sample`（默认 temperature 1.0、top_p 0.95 就是迁移指南推荐的值，建议两个只调一个；temperature 的说明同时写了「[0.0, 1.0]」和
「must be a positive number」，0 能不能用有歧义；Claude / Kimi / GPT 推理档也都用默认采样）；`tools`、`tool_choice`、`stop`、`request_id`、`user_id`、`tool_stream`。

回复：`choices[0].message.content` 是最终答案，只对它 `json.loads`（不剥代码块、不修补）；思考在 `message.reasoning_content`（Deep Thinking 指南的示例），不拼、不记。

| `finish_reason`（API 参考） | 处理 |
|---|---|
| `stop` | 解析 JSON |
| `length` / `model_context_window_exceeded` | 报截断（`truncated`，`reply was truncated (finish_reason=...)`）；`AgentLLM.ask` 照旧要求「短一点再答一次」（同 Claude 的 model_context_window_exceeded） |
| `sensitive` | 报 `sensitive`：被内容安全审核拦截，不解析 |
| `network_error`（推理异常）、`tool_calls`（不带工具时不该出现）、没给 | 报 `unexpected_finish`，不解析；`AgentLLM.ask` 照旧带着错误重问一次 |
| 没有 `choices`、`message` 不是对象 | `bad_response_body`，按已有逻辑重试 |

单次读最多 1,200 秒、整次 1,800 秒（`chat_timeouts`，同 OpenAI，没实测）。

### 12.3 思考档位

| 模型 | 网页可选 | plan / judge / repair | 其余角色（含生成查询词） |
|---|---|---|---|
| GLM-5.3 | low / medium / high（永远在想，不给 off） | low -> `low`、medium -> `high`、high -> `max`（+24,000） | `low`（+24,000） |
| GLM-5.2 | off / low / medium / high | off：`disabled`；low、medium -> `high`；high -> `max`（+24,000） | `disabled` |
| GLM-4.7-FlashX | off / low / medium / high（没有深度：low / medium / high 都是「开」，`thinking_depth = False`，网页合并显示） | off：`disabled`；其余 `enabled`（+24,000） | `disabled` |

- GLM-5.3：Deep Thinking 指南 / 模型页：thinking 只能 enabled，reasoning_effort 只收 low / high / max（其他值报错），迁移提示写明「原来用 disabled 的改成 enabled +
  low」，所以其余角色用 low。映射同 Kimi K3（调研的建议；**和 DeepSeek / Claude / GPT 的「high -> high」不一样**，K3 的同一个问题还等你定）。
- GLM-5.2：reasoning_effort 收 7 个值，但 low / medium 映射成 high、xhigh 映射成 max、none / minimal 等于不思考，实际只有关 / high / max。这里发映射后的值
  （网页 low 也发 `high`），日志和 settings 里看得到实际档位；所以网页的 low 和 medium 是同一档。enabled 时 5.2「由模型自动决定要不要思考」（ChatThinking）。
- GLM-4.7 系列：enabled 时强制思考（ChatThinking），没有 reasoning_effort。

### 12.4 错误、重试、余额

错误 body 有两种写法：错误码页（两站）和 10-21 实测都是 `{"error": {"code": "1000", "message": "..."}}`（code 是字符串），API 参考的 Error schema 却是
`{"code": 1214, "message": "..."}`（没有外层 error、code 是整数）。`providers.glm_error` 两种都认，code 统一成字符串。GLM 的错误没有 type：日志记
`server_error_code` 和 `server_error`（message 前 200 字），异常文字写成 `http_400 (code 1214: Parameter ... is invalid ...)`。

| 情况 | 处理 | 依据（错误码页，两站同表） |
|---|---|---|
| 401（1000 / 1001 / 1003 / 1005）、403（1220） | `KeyRejected`，不重试，不读 body | 1000 Authentication Failed 等；10-21 实测见 12.8 |
| 429 **1113** | `BalanceExhausted`，不重试，整次运行停下（第 6 节） | Insufficient balance or no resource package. Please recharge.（国内站：您的账户已欠费，请充值后重试） |
| 429 1308 / 1310 / 1316–1321 | 同上（我定的，见 12.9）；v2.10f 起说明开头是 `usage limit reached`，不写成余额不足 | 用量上限（要到服务端给的重置时间）、5 小时 / 7 天上限且余额或月消费上限不允许超额：重试都没用 |
| 429 1313 | v2.10f 起按限流重试（以前和余额不足一样停下） | 公平使用策略下的频率限制（调研只把 1113 列为余额不足） |
| 429 1309 / 1311 / 1314 / 1315 | 同上，说明里提示换 Standard API Key；v2.10f 起说明开头是 `key or plan not accepted` | Coding Plan 过期、套餐不含这个模型、企业套餐过期、key 只限企业编程套餐 |
| 429 1302（限流）、1305（过载）；500（1200 / 1230 / 1234）、502、503、504 | 最多 3 次，2 / 4 秒退避（搜索接口 3 / 6 秒）；服务端给了 `Retry-After` 就至少等那么久（最多 60 秒；文档没写这个头） | Rate limit reached / service may be temporarily overloaded / network error, please try again later |
| 其余 4xx（1210 / 1213 / 1214 / 1215 参数、1211 模型不存在、1261 prompt 超长、1301 内容安全） | 不重试；业务码和 message 进日志和异常文字 | 同上表 |
| 3xx | 不跟随（D9），`TransportError` | 同 v2.6g |

`BalanceExhausted` 的文字：`insufficient balance: GLM HTTP 429 code 1113 (insufficient balance or no resource package) (...); the run was stopped without retrying.
Top up the GLM account (or check its limits) on the platform where the key was created (z.ai/manage-apikey/billing or bigmodel.cn), make sure it is a Standard API Key,
then run again.`（不含服务端原文。）

### 12.5 搜索：生成查询词 + `POST {base}/web_search`

为什么不用模型自己搜：Chat Completions 的内置 `web_search` 工具是「检索结果喂给模型再生成」，不像 Anthropic 的服务端工具那样多轮自主搜，而且 API 参考写的引擎
`search_pro_jina` 和指南示例的 `search-prime` 对不上（调研记录）；独立的 Web Search API 直接给结构化结果（title / link / content），正好只要 URL。
所以走 Kimi 那条路（`search_mode = "queries"`，`Searcher._search_by_queries`，第 11.5 节）：一次 JSON 调用生成最多 3 个查询词（同一个 `SEARCH_QUERIES_*` prompt，
没改），再逐个调搜索接口，按名次交替合并 URL。

| 区域 | body | 依据 |
|---|---|---|
| `global` | `{"search_engine": "search-prime", "search_query": <查询词>, "count": <cap，即 4>}` | 国际站 Web Search API：`search_engine`（必填，enum 只有 search-prime）、`search_query`（必填）、`count`（1–50，默认 10；字段说明写「Supported search engines: search_pro_jina」，但指南的 search-prime 示例用了 count=15） |
| `cn` | `{"search_query": <查询词，最多 70 个字符>, "search_engine": "search_std", "search_intent": false, "count": 4}` | 国内站网络搜索：`search_query`（必填，maxLength 70、建议不超过 70 个字符）、`search_engine`（必填：search_std 基础版 / search_pro / search_pro_sogou / search_pro_quark）、`search_intent`（必填；false = 跳过意图识别、直接搜：查询词已经是写好的搜索词）、`count`（1–50） |

- 国内站查询词超过 70 个字符时截到 70 以内最后一个空格（没有合适的空格就直接截，例如中文）。截的是发出去的那份；返回的 `queries`（进 state.json 审计）仍是生成的原文。国际站没写长度上限，不截。
- `search_domain_filter`、`search_recency_filter`、`content_size` 用默认（不限域名、不限时间；摘要不用）。回复 `search_result[]` 取 `link`（和 `title`），标题不出 Searcher。
- 计费：国际站价格页只列了 Built-in Tools 的「Web Search $0.01 / use」，没说是否就是独立接口 search-prime 的价（未核实，按它记）；国内站「搜索工具按照实际调用次数计费」，
  Search-Std ¥0.01 / 次。文档没说空结果免费，所以每个 HTTP 200 都按一次记（`search_bills_every_ok_response`，含空结果、形状不对的；Kimi 只记结果非空的），失败的请求不记。
- 错误：同 12.4（429 1113 停下，1302 / 1305 重试；搜索接口的 401 和其他 provider 的搜索一样只记 `http_401`、不抛）。国内站另列了 1701（搜索并发到上限，稍后重试）、1702（没有可用的搜索引擎）、
  1703（搜索引擎没返回有效数据），没写对应的 HTTP 状态：是 429 / 5xx 就按状态重试，其余照原样记在 `error` 里。
- 预扣：同 Kimi，`Budget.search_tokens` = 生成查询词那次发出的 max_tokens（5.2 / 4.7-FlashX 关思考 2,000；5.3 26,000），输入按 30,000 token 估，搜索费按 `(2 × max_uses + 2)` 次。
- `run_settings` 的 `search_queries`：`max_tokens`、`endpoint`，加 `search_engine`（国内站另有 `search_intent: false`、`query_max_chars: 70`）。

### 12.6 价格和成本

`config.PRICES`（每百万 token；没有分时价，`peak` = `offpeak` = (cached input, input, output)）。国际站 https://docs.z.ai/guides/overview/pricing 、
国内站 https://docs.bigmodel.cn/cn/guide/start/pricing ，2026-10-21 查看。

| 计价 id | cached input | input | output | 搜索 / 次 |
|---|---|---|---|---|
| `glm-5.3` | $0.26 | $1.4 | $4.4 | $0.01 |
| `glm-5.2` | $0.26 | $1.4 | $4.4 | $0.01 |
| `glm-4.7-flashx` | $0.01 | $0.07 | $0.4 | $0.01 |
| `glm-5.3@cn` | ¥2 | ¥8 | ¥28 | ¥0.01 |
| `glm-5.2@cn` | ¥2 | ¥8 | ¥28 | ¥0.01 |
| `glm-4.7-flashx@cn` | ¥0.1 | ¥0.5 | ¥3 | ¥0.01 |

- 缓存是隐式自动的（Context Caching 指南），没有写入费；缓存存储两站都写「限时免费」，不计（免费期结束后的价格没公布）。国际站 FAQ：缓存机制还在公测，命中规则和保留时长没公布。
- `glm_usage_cost`：`prompt_tokens - cached_tokens` 按 input 价，`prompt_tokens_details.cached_tokens` 按 cached input 价，`completion_tokens` 按 output 价。usage 里没有 reasoning_tokens，
  思考 token 是否就计在 `completion_tokens` 里文档没写（未核实；按它计价）。calls.jsonl：`finish_reason`、`prompt_tokens`、`cached_tokens`、`completion_tokens`、`usd`；
  `completion_tokens_details.reasoning_tokens` 有才记。
- 方向数和预扣：`prompt_cache = "implicit"`（同 Kimi）：这个 agent 在 GLM 上的命中率没测过，`DIRECTION_PROFILE` 的输入全按 input 价算；预扣的输入也按 input 价。

### 12.7 `$2` 上限下的方向数和预扣

| 计价 id（档位） | 一个方向 | `$2` 方向数 | 一次搜索预扣 | plan（2 万字符） | 抽取（4 万字符） | 抽取（40 万字符） | judge（10 万字符） |
|---|---|---|---|---|---|---|---|
| deepseek-flash（对照） | $0.060 | 10 | $0.099 | $0.010 | $0.025 | $0.079 | $0.029 |
| glm-4.7-flashx（off） | $0.051 | 10 | $0.083 | $0.003 | $0.008 | $0.020 | $0.008 |
| glm-4.7-flashx（high） | $0.051 | 10 | $0.083 | $0.013 | $0.008 | $0.020 | $0.018 |
| glm-5.2（off） | $0.128 | 9 | $0.131 | $0.040 | $0.098 | $0.350 | $0.123 |
| glm-5.2（high） | $0.128 | 9 | $0.131 | $0.146 | $0.098 | $0.350 | $0.228 |
| glm-5.3（low / high 相同） | $0.128 | 9 | $0.236 | $0.146 | $0.204 | $0.456 | $0.228 |
| glm-5.2@cn（off） | $0.078 | 10 | $0.056 | $0.037 | $0.090 | $0.305 | $0.110 |
| glm-5.3@cn（low） | $0.078 | 10 | $0.156 | $0.137 | $0.190 | $0.405 | $0.210 |

- **国际站 GLM-5.3 在 `$2` 下很紧**（同第 9.8 / 10.7 / 11.7 节的问题）：第一轮 8 个方向同时搜索（并发 8），预扣合计 $1.89，加上规划已花的钱接近 $2；之后 8 个并发抽取每个预扣 $0.20–0.46，
  很可能撞上「已花 + 在途 + 这一次 > 上限」而中止。大头是关不掉的思考：每次调用 +24,000 token × $4.4 / 百万 ≈ $0.11。修法同前，等你定。
- 默认模型 GLM-5.2（`PROVIDERS["glm"]["default_model"]`）：国际站 API 参考的 model enum 里有它、能关思考（ModelSpec 的默认档位是 off），`$2` 下 9 个方向。
  最便宜的 4.7-FlashX（10 个方向）国际站 id 没核实（12.9），5.3 是官方的默认旗舰但关不掉思考。要改随时说。

### 12.8 key 校验

`GET {base}/models`（Bearer）。两站的文档（`llms.txt` 索引和 API 参考）都没有这个接口，但它存在：10-21 实测（`probes/glm_key_probe.py`，没花钱，全是 401）：

| 请求 | 状态 | body |
|---|---|---|
| 国际站 `GET /models` 不带 key | 401 | `{"error":{"code":"1001","message":"Authentication parameter not received in Header, unable to authenticate"}}` |
| 国际站 `GET /models` 假 key | 401 | `{"error":{"code":"1000","message":"Authentication Failed"}}` |
| 国内站 `GET /models` 假 key | 401 | `{"error":{"code":"1000","message":"身份验证失败。"}}` |
| 两站 `POST /chat/completions`、`POST /web_search` 假 key | 401 | 同上（国际站英文、国内站中文） |
| 假 key 走 `check_key`（国际站 4.7-FlashX、国内站 5.3） | — | `{"provider": "glm", "model": ..., "ok": false, "status": 401, "error": "key_rejected", "message": "GLM rejected the API key (HTTP 401)"}` |

两个 API 主机都没有跳转；服务端的 401 没有回显 key（探针检查了 key 和 key 的 id 段）。有效 key 的回复形状没核实（手上没有 key）：是 OpenAI 的形状（`data` 列表、每项有 `id`）就看
所选模型在不在里面；列表全不全不知道（`models_unpack` 第二项是 None），不在里面时 `model_listed` 是 None、message 写「没核对」；形状不认识也照样算 key 通过（HTTP 200 本身说明 key 被接受）。
`GET /models` 查不出余额：余额不足要到第一次计费调用才报 429 1113（调研记录）。

### 12.9 已知限制、没做的、要你定的

- **国际站 GLM-5.3 在 `$2` 下很紧**（12.7，要你定，和 Opus / Sol / K3 同一个问题）。
- **5.3 的 high -> max 映射**同 Kimi K3，和另外三家的口径不同（12.3，要你定）。
- **1113 以外的 429 码也停下整次运行**（12.4）：这是我定的；v2.10f：1313 改成重试，停下的说明和余额不足分开写（第 14.9 节）。任务只写了「1113 停、1302 / 1305 重试」；1308–1321 是用量上限和套餐的问题，重试几秒没用（要等服务端给的重置时间、续订或换 key），
  照 OpenAI 那边把 spend / usage limit 当成停下的先例处理。只按原样报、不停也可以（每个调用会先重试 3 次再失败），要改随时说。
- **GLM-4.7-FlashX 的国际站 id 没核实**：`glm-4.7-flashx` 取自国内站 API 参考的 model enum；国际站 API 参考的 enum 只有 5.3 / 5.2 / 5.1 / 5 / 4.7 / 4.6，国际站价格页的 Other Pricing 里有 GLM-4.7-FlashX。
  国际站要是不收这个 id，第一个调用会报 400 1211（Unknown Model），照原样显示。它的上下文只有 200K：抽取最多发 40 万字符，可能超出（400 1261 Prompt too long，照原样报）。
- 思考 token 算不算进 `max_tokens`、算不算进 `completion_tokens` 计费，文档都没写（未核实）。
- 国际站搜索的单价按 Built-in Tools 的 $0.01 / use 记（12.5，未核实）；空结果也按一次记（保守）。
- 文档没写 Coding Plan key 打通用端点会怎样（12.1）；只能在网页上提示、在收到 1309 / 1311 / 1314 / 1315 时停下。
- 国内站的价格按固定汇率折算（同 Kimi）。
- 并发和限流额度不公开，要到控制台看（调研记录）；agent 默认并发 8，额度低的账户会连续撞 1302，3 次重试后这些调用失败。没做自动降并发。
- json_object + 思考的组合、5.2 关思考时的 json_object 表现、非流式长请求的超时，都只按文档写，没有真 key 实测。
- 网页还没接（同第 8 节）：区域选择、`GLM_KEY_NOTE`、4.7-FlashX「没有深度」和 5.2「low = medium」的提示、账单 n-1 延迟的提示都留给网页阶段。

### 12.10 Verification（v2.10e）

- `tests/test_glm.py`（31 个）全部对着 127.0.0.1 上的假 GLM 服务（`tests/fake_glm.py`，复用 `fake_claude.py` 的脚本化服务；国内站接在 `/cn/...`）跑，真实走 urllib +
  `urlopen_no_redirect`：请求头 / 请求体（键顺序、禁发的采样参数、不发 max_completion_tokens）、三个模型 × 档位 × 角色的 `thinking` / `reasoning_effort` / `max_tokens`、余量封顶、
  区域路由、思考内容不进返回值和日志、usage 计价（命中、国内站折算）、六种 finish_reason、不修 JSON、形状不对重试、两种错误 body 形状、1113 不重试（两种形状、中英文）、
  1308–1321 / 1309–1315 停下、1302 / 1305 / 500 重试、Retry-After、400 照原样报（业务码和 message）、401 / 403 不读 body、3xx 不跟随、价格表、方向数、预扣、按区域的搜索费、
  查询词调用的 prompt 和参数、两站的搜索请求体、国内站 70 字符截断、交替合并、空结果 / 形状不对也计费、单个查询词失败、搜索 401 / 1302 / 1113、生成查询词的六种失败、
  一个方向的端到端（查询词 -> 搜索 -> 取页 -> 抽取 -> 核对，三次调用计入预算）、key 校验（含 10-21 实测的三种 401 body、models 列表形状不认识）、ModelSpec、key 说明、
  整次运行端到端（国内站 5.3，429 1113 干净停下，结果目录没有 key，key 已清掉，settings 记 price_id / 汇率 / 搜索设置）。
- 变异检查 36 处（发 temperature、stream true、改成 max_completion_tokens、5.3 high 改 high、5.2 low 发 low、开思考不写 thinking、5.2 关思考发 none、4.7 发 reasoning_effort、
  命中按 input 价、没扣命中部分、context window 当成 stop、不认 sensitive、network_error 照样解析、只认带外层 error 的形状、code 不转字符串、1113 不算余额、1305 算余额、
  套餐码重试、429 不重试、读 401 body、国内站不发 search_intent、国际站引擎写错、国内站不截断、空结果不计费、取 url 不取 link、国内站写成 Coding 端点、models 列表当成完整、
  llm 不用 parse_error、异常文字不写业务码、国内站价格写错、Searcher 不传 region、形状不对不计费、把思考拼进正文、key 说明不提 Coding Plan、settings 记 Kimi 的字段、默认模型改成 4.7-FlashX）：
  全部被测试抓到。
- 其他 provider：DeepSeek 默认路径的 24 组金样本仍逐字节相同；Kimi 的 33 个测试不变（`tools_search_request` 多收一个不用的 `region`，`run_settings` 改由 `search_settings` 给字段，值相同）。
- G2（`probes/compare_continuous_prompts.py`）：v2.10d 的导出和本阶段都是 `365b06515d8caef8257020c2e5d574de7724be2f2270c122e6e21952517f78c4`。
- 真实网络只发了不花钱的请求（`probes/glm_key_probe.py`，跑了两次，全部 401）。没有真 key，没有发过成功的 `/chat/completions`、`/web_search`。
- 本阶段对其他代码的改动：`llm.server_error`（`parse_error` 钩子）、`llm.server_error_detail`（只有 code 的记录）、`llm.check_key`（列表全不全不知道时的文字）、
  `Searcher._search_by_queries`（传 region、按 adapter 计费）、`run.run_settings`（`search_settings`）、`KimiAdapter`（`region` 参数、`search_settings`）。

## 13. Web layer（web-v0.9）

网页（`triangulate/web/`）接上自带 key。只在本机单用户用（照旧只绑 127.0.0.1，`TrustedHostMiddleware` 只认本机 Host 头，POST 只收 JSON）。

### 13.1 接口

| 接口 | 做什么 |
|---|---|
| `GET /api/providers[?usd_cap=2]` | `web/catalog.py` 的 `providers_view(cap)`：五家的 id / 名字 / 默认模型 / 区域（Kimi、GLM 有国际站 / 国内站，`region_choice`）/ 说明（中英，`PROVIDER_NOTES`）/ GLM 建 key 的页面；每个模型的思考档位（`levels`、`can_turn_off`、`default`、`sends` = 各档位下 plan / judge / repair 的请求体里控制思考的字段、`sends_other_roles`、说明）和每个区域的价格（官方价、来源、查看日期，CNY 原价和汇率）、第一轮方向数、每个档位的花费估计（13.4）。全部取自 `providers.py` 和 `config.PRICES`，不另写一份清单；没有 key、没有任何秘密。`usd_cap` 不是有限正数回 400 |
| `POST /api/key/check` `{provider, region, model?, api_key}` | 用这几项建一个 `ModelSpec`（没给模型用这家的默认模型），调 `llm.check_key`（这家免费的 models 列表接口，第 9.7 / 10.5 / 11.8 / 12.8 节），返回 `ok` / `error`（key_rejected、balance、network……）/ `message`；结果先过 `spec.redact_obj`，返回后马上 `drop_key()`。`create_app(key_checker=...)` 可以换校验函数（假演示服务用） |
| `POST /api/runs` `{question, as_of, provider, model, region, thinking, usd_cap, api_key}` | `app.spec_from_body`：没有 `api_key`（缺、null、空白）就 400，消息是中英两句 `runs.NEED_KEY`（「需要你自己的 API key：网页运行只用你填的 key，从不使用服务器上的 key 文件。」）；其余字段没给就用默认值（DeepSeek、这家的默认模型、这个模型的默认档位：能关就 off，否则 low；上限 $2.00）；不合法的组合（模型不属于这家、这个模型没有这个档位、区域不对、上限不是正数、key 格式不对）都是 400，消息里不带 key。spec 交给 `Registry.start(question, as_of, spec=spec)` |
| 422（请求体不是 JSON 对象） | FastAPI 默认的 422 会把收到的 body 原样放在 `input` 里（请求体里有 `api_key` 时就是回显 key）。`create_app` 换了 `RequestValidationError` 的处理：只回 `loc` / `type` / `msg` |

### 13.2 key 在服务器上的一生

1. `spec_from_body` -> `ModelSpec`（`clean_key`：去首尾空白，8–512 个可打印 ASCII）。
2. `Registry.start` 必须有 spec（没有就 `ValueError(NEED_KEY)`，防别的调用方绕过 app）；登记之前任何一步出错（题目不合法、`Busy`）先 `spec.drop_key()` 再抛。
3. `WebRun._spec` 和 `prepare_run(q, tag, spec=spec)` 的 `ctx.spec`：只在内存里。默认的 prepare 就是命令行同一个 `run.prepare_run`，所以 LLM / Searcher / Budget 走的都是 v2.10a–e 的 spec 路径，**不读 key 文件**（测试把 `config.read_key`、`llm.read_key`、`search.read_key` 换成直接报错来证明）；Jev 对照臂照 v2.10a 跳过。
4. 停在人工确认时 key 留着（批准后还要用）；v2.10f：超过 30 分钟没批准就按「不批准」结束、清 key（第 14.5 节）。
5. 运行结束（完成 / 失败 / 取消，都经过 `_guard` 的 `finally`）：`WebRun._release()` 先把内存里已存的文字（题目、错误、目标、方向、裁判摘要、计算结果、批准记录……）过一遍 `spec.redact_obj`，再 `drop_key()`。
   `_after_stream` 调 `save_run(h, approvals, keep_key=True)`：`save_run` 新加的 `keep_key` 参数让它写完文件不清 key，由 `_release` 统一清（不然 save 先清了 key，之后就认不出文字里的 key 了）。命令行照旧 `keep_key=False`。
6. 错误文字（`_guard` 的异常、`state.aborted`）经 `WebRun._clip`：先 redact 再截到 500 字（先截的话，截在 key 中间的半截就认不出来了）。
7. 每个状态视图（`status_view`、`brief`）返回前加上 `run_spec`（`spec.public()`，不含 key）和 `key_in_memory`（布尔），整个 dict 过一遍 `redact_obj`。

`providers.ModelSpec.redact_obj(obj)`（新）：`redact` 的深层版，dict（含键）/ list / tuple 里的每个字符串都换，返回新对象。
`providers.effort_for(model, level, role)` / `tokens_for_model(...)`（新）：从 `ModelSpec.effort` / `tokens_for` 里提出来的同一段逻辑（行为不变），网页的估计在没有 key 时也能用。

### 13.3 前端

- **经典界面（`/`，`static/app.js` + `index.html`）只浏览**：首页的提问表单去掉了，换成「去 Verrier 控制台发起」的说明；还能看这次服务启动后的网页运行（进度、批准 / 取消已有的运行）、已保存的运行和回测。导航「新问题」改名「网页运行」。
- **共享控制台（`static/verrier_console.js`，/verrier、/verrier/aero、/verrier/apple、/verrier/manuscript 都用）**：提问页加了「模型 · key · 上限」：
  provider、区域（只有 Kimi / GLM 显示）、模型（选项里带每次运行的估计花费，第一轮会中止的标 ⚠）、API key（`type=password`）+「在这台设备上记住」+「校验 key」、思考深度（off / low / medium / high，这个模型没有的档位 disabled，下面写各档实际发什么和说明）、花费上限（默认 2.00，改了就重新取 `/api/providers?usd_cap=`）。下面三格读数：估计花费、上限、第一轮方向数，以及超上限 / 第一轮会中止的提示。中英两套文字照旧用 `T()` 的 span；`<option>` 里放不了 span，档位写成「off · 关」这种双语。
  旧的「需要 key 文件、上限 $1.00」说明换成了「自带 key：只用你填的 key，从不用服务器的 key 文件；key 只在浏览器和这次运行的服务器内存里，结束就清，不写盘」。
- **key 在浏览器里**：按「provider + 区域」分开存（`verrier-key:<provider>:<region>`），默认 `sessionStorage`（关掉标签页就没了）；勾了「记住」才放 `localStorage`，旁边写明是明文、能用这个浏览器配置的人都读得到；取消勾选就从 `localStorage` 删掉。换 provider / 区域时自动填上那个组合存过的 key。非秘密的选择（provider、区域、模型、档位、上限）存 `localStorage` 的 `verrier-run-cfg`。
- 运行页题 id 那一行加了「provider / 模型 / 区域 · 思考档位 · key 在服务器内存里 / 已清掉」。
- 样式：原版 /verrier（`verrier_console.html` 的内联 CSS）按工业规格表做了 `.cx-cfg`（黑铭牌条、左栏标签右栏控件、底部三格读数）；另外三个页面没加样式，能用但朴素。
- **假演示服务**（`probes/web_demo_fake.py`，端口 8773）：「校验 key」换成不发请求、总是通过的 `fake_check_key`；prepare 收 spec（假模型不管选了哪家），key 照真实路径只在内存里、结束就清。10-21 在浏览器里走了一遍：选 GLM、填 key、记住 / 取消记住（存储位置对）、校验、发起、批准、完成，运行页显示「key 已从服务器内存清掉」，临时结果目录里 grep 不到 key。

### 13.4 每次运行的花费估计

只是给人看的粗估，不参与预算（上限照旧靠预扣守住）。`catalog.estimate(model, region, level, cap)`：

- token 构成（`RUN_PROFILE`）：`results/agent/**/calls.jsonl` 里 2026-10-18 起 50 次 deepseek-flash 运行（不开思考）的平均：plan / judge / repair 合计 cache hit 19,400、miss 28,400、输出 14,900 token；其余角色合计 5,000 / 18,700 / 3,100、15 次调用；
  实际方向数 = 第一轮上限 × 1.13（含第二轮 base-rate），每个方向 3.1 次调用，每个方向的 token 用 `Budget.DIRECTION_PROFILE`。思考：22 次 v2.9 思考实验运行里 plan / judge / repair 开 high 多出 47,300 个思考 token（所有非 off 档位都按它算，偏保守）；audit / unit_arbiter 开 low 每次调用 870 个，关不掉思考的模型其余角色按它乘调用次数。
- 计价：`Budget.profile_usd(price_id, profile)`（新，从 `typical_direction_usd` 里提出来，算法不变）：峰时价，缓存的处理同方向数缩放（Claude 不写 cache_control 按 base input；GPT 输入按 30 分钟写入价；Kimi / GLM 按 miss 价），思考 token 按输出价。
- 方向数：`Budget.for_model(price_id, usd=cap).directions`（和真正运行的预算同一个函数）。
- 对照：deepseek-flash 估 $0.62，50 次实测平均 $0.52（峰时价 + 方向数按上限算，偏高约 20%）。
- ~~**第一轮会不会因为预扣放不下而中止**~~（v2.10f 起 `stops_early` 换成「一次最小运行放不放得下」，见第 14.1 节）（`stops_early`）：第一轮同时在途的搜索预扣合计（min(方向数, 8) × `search_reserve`）或抽取一个 4 万字符页面的预扣（`llm_reserve`，含思考余量）超过上限就标出来，并从当前上限往上按 $0.5 一档找放得下的最小上限（`min_cap_usd`）。只往上找：上限低到只剩一个方向时也可能放得下，但那不是「调高上限」的建议。

`$2` 上限下（默认档位；「估计（high）」是 plan / judge / repair 开 high）：

| 计价 id（默认档位） | 第一轮方向数 | 估计 | 估计（high） | 第一轮搜索预扣合计 | 抽取一页预扣 | 第一轮会中止 | 放得下的最小上限 |
|---|---|---|---|---|---|---|---|
| deepseek-flash（off） | 10 | $0.62 | $0.68 | $0.79 | $0.03 | 否 | — |
| deepseek-v4-pro（off） | 10 | $1.14 | $1.33 | $1.22 | $0.09 | 否 | — |
| claude-haiku-5-5（off） | 10 | $0.53 | $0.56 | $0.70 | $0.01 | 否 | — |
| claude-sonnet-5-5（off） | 6 | $1.37 | $1.84 | $1.33 | $0.20 | 否 | — |
| claude-opus-5-5（low） | 3 | $2.95 | $2.95 | $2.53 | $0.88 | 是 | $7.00 |
| claude-fable-5-1（low） | 1 | $5.48 | $5.48 | $1.99 | $2.20 | 是 | $16.00 |
| gpt-6-luna（off） | 10 | $0.55 | $0.57 | $0.70 | $0.01 | 否 | — |
| gpt-6.1-sol（low） | 5 | $2.10 | $2.10 | $2.38 | $0.45 | 是 | $4.00 |
| gpt-6-astra（low） | 1 | $5.77 | $5.77 | $2.06 | $2.25 | 是 | $2.50 |
| kimi-k2.6（off） | 10 | $0.81 | $1.00 | $0.42 | $0.08 | 否 | — |
| kimi-k2.6@cn（off） | 10 | $0.80 | $0.99 | $0.39 | $0.08 | 否 | — |
| kimi-k3（low） | 5 | $2.63 | $2.63 | $2.48 | $0.66 | 是 | $4.00 |
| kimi-k3@cn（low） | 5 | $2.60 | $2.60 | $2.44 | $0.65 | 是 | $4.00 |
| glm-4.7-flashx（off） | 10 | $0.51 | $0.53 | $0.66 | $0.01 | 否 | — |
| glm-4.7-flashx@cn（off） | 10 | $0.13 | $0.15 | $0.12 | $0.01 | 否 | — |
| glm-5.2（off） | 9 | $1.31 | $1.51 | $1.05 | $0.10 | 否 | — |
| glm-5.2@cn（off） | 10 | $0.93 | $1.12 | $0.45 | $0.09 | 否 | — |
| glm-5.3（low） | 9 | $1.69 | $1.69 | $1.89 | $0.20 | 否 | — |
| glm-5.3@cn（low） | 10 | $1.30 | $1.30 | $1.25 | $0.19 | 否 | — |

Astra 的 $2.50 是「只剩 1 个方向时放得下」的上限（往上找到的第一档）；Astra 在 $10 下有 7 个方向，又放不下，要 $17。这张表就是 v2.10b–e 一直说的「贵模型在 $2 下跑不起来」，网页现在把它直接显示出来；预算本身的做法没改（等你定）。

### 13.5 已知限制、没做的

- ~~**贵模型在 $2 下第一轮就中止**~~（v2.10f：等在途 + 服务端拒跑 + 默认 Sonnet，第 14.1 节）。
- 估计用的是 DeepSeek 的 token 数：别家的 tokenizer、思考长度、搜索带进来的内容 token 都没测；Kimi / GLM 的搜索不经过模型，按 DeepSeek 的搜索 token 算是高估。思考 token 不分档位（low 也按 high 的实测量算）。
- ~~「第一轮会中止」只查了第一轮同时搜索和抽取一个 4 万字符页面两种预扣~~（v2.10f：改成规划 + 搜索 + 抽取 + 裁判，第 14.1 节；更长的页面照旧没查）。
- ~~停在人工确认的运行一直占着 key（在内存里），直到你批准、取消或者服务退出；没有超时自动清。~~（v2.10f：30 分钟超时，第 14.5 节）
- 浏览器里的 key：sessionStorage / localStorage 对这个页面的任何脚本都可读。页面只加载本仓库的脚本和 Google Fonts 的 CSS，所有服务端文字都经过 `esc()`；没有做 CSP。勾「记住」时是明文。
- key 从浏览器发到本机服务走的是 `http://127.0.0.1`（没有 TLS；只在本机回环上）。
- 服务器内存里的 key 是 Python 字符串，`drop_key()` 只是去掉引用，不能保证内存里的那份立刻被覆盖（Python 做不到）。
- 「校验 key」只说明这家接受这把 key：余额够不够、K3 是否解锁、GLM 的 key 是不是 Standard API Key，都要到第一次计费调用才知道（第 11.8 / 12.8 节）。
- 经典界面的运行页还能批准 / 取消已有的运行（不发起新运行）。
- aero / apple / manuscript 三个页面的表单没有专门的样式。
- ~~DeepSeek 搜索角色的思考没关（第 8 节），仍等你定。~~（v2.10f 已改，第 14.6 节）

### 13.6 Verification（web-v0.9）

- `tests/test_web_byok.py`（15 个）：目录和 providers.py 一致、各档位发的字段、估计跟着上限 / 预算走（含 Opus $7、Fable 抽取放不下）、上限校验；key 校验对着假服务（真走 urllib，请求头里是去了空白的 key，返回里没有 key）、校验完清 key、各种 400 不回显；没有 key 拒跑（4 种写法）、15 种不合法的组合都是 400 且不回显、4 种 422 不回显；设置一路传到运行（Kimi 国内站 K3、high、$3.5）、默认值；整次运行（假模型）后 key 已清、写出的每个文件和每个 API 返回都没有 key；模型回复里带 key 时状态视图和结束后的视图都是 `***`；取消、prepare 抛带 key 的异常（key 跨在 500 字截断处）、没有 spec、题目不合法、Busy 都会清 key；经典界面不能发起运行；控制台表单的静态检查。
  **端到端（`TestRealPathEndToEnd`）**：默认的 `Registry()`（真实的 `prepare_run` / `AgentLLM` / `Searcher` / `save_run`），DeepSeek 的 URL 换成 127.0.0.1 上按 system prompt 回复的假服务；POST /api/runs（deepseek-flash、high、$1.5）-> 人工确认 -> 批准 -> 完成：每个请求都带着用户的 key（Bearer / x-api-key），plan 发 `thinking enabled` + `reasoning_effort high` + `max_tokens` 30000、抽取关思考；key 文件一次都没读；结果目录（state.json、calls.jsonl、ledger.md、graph.html）和 7 个 API 返回里都没有 key；key 已从内存清掉。
- 旧测试：`tests/test_web.py`、`tests/test_unit_display.py` 的网页运行改成带假 key（`TW.BYOK` / `TW.byok_spec()`），`make_prepare` 收 spec；`tests/test_verrier_page.py` 的路由清单加上两个新接口。
- 变异检查 19 处（`_release` 不清 key、先截断再 redact、状态视图不 redact、清 key 前不 scrub、save 自己清 key、没有 spec 也能跑、登记失败不清 key、422 回显 input、校验后不清 key、校验结果不 redact、没 key 时用服务器的 key、忽略上限、最小上限从 0 找、不查抽取预扣、思考不计价、方向数写死、经典界面又能发起、「记住」不放 localStorage、`redact_obj` 漏掉 dict 的值）：全部被测试抓到（「先截断再 redact」第一次没抓到：测试里截断只留下 key 的前 6 个字符，改成留 16 个后抓到）。
- DeepSeek 默认路径的 24 组金样本仍逐字节相同（`tests/test_providers.py`）；G2（`probes/compare_continuous_prompts.py`）仍是 `365b06515d8caef8257020c2e5d574de7724be2f2270c122e6e21952517f78c4`。
- 浏览器（假演示服务，10-21）：/verrier 上切 DeepSeek / Kimi / GLM / Claude、K3 的 off 是 disabled、上限 2 -> 4 -> 2 时估计和提示跟着变、GLM 两站分别存 key、记住 / 取消记住、校验、发起 -> 批准 -> 完成；/verrier/aero、/verrier/apple、/verrier/manuscript 表单能用、没有脚本错误；经典界面首页只剩浏览。
- 没有真 key。真实网络只有一处意外：前两轮变异检查里，「没 key 时用服务器的 key」那处变异让 `test_classic_page_is_browse_only` 用默认的 `Registry()` 真的发起了运行，向 `api.deepseek.com/chat/completions` 发了 2 次带假 key（`sk-server-default-key`）的请求，都是 401、不花钱，在 `results/agent/` 下多出的目录已删。之后测试的 client 默认改成 prepare 直接报错的 Registry（保护失效时只会测试失败、不会连真 API），再跑变异检查没有再发真实请求。

## 14. 审查修正（v2.10f）

10-21 的对抗式审查（自己写的端到端：真实的 Registry -> prepare_run -> AgentLLM / Searcher -> save_run，接 127.0.0.1 上的假服务，用假 key）
找出 1 个 high、2 个 medium、8 个 low。全部按审查给的修法改了，各条的做法和没做的部分如下。命令行、回测、三个基线臂（没有 ModelSpec）
的请求体和预算行为都没变（24 组 DeepSeek 金样本逐字节相同，`TestCommandLineBudgetUnchanged`）。

### 14.1 预算：等在途的调用、放不下就拒跑、Claude 默认模型（high）

问题：方向数按「典型花费」缩放，真正让运行中止的却是按最坏情况的预扣（`Budget.hold`：已花 + 在途 + 这一次 > 上限就中止整次运行）。
Claude 的默认组合（Opus 5.5 + $2）第一轮就中止（规划和两次搜索的钱已经花了，没有估计）；Fable 第一个搜索就中止；6.1 Sol、Astra、K3 同理。

做法（审查给的 (b) + (c)）：

- **等在途的调用**（`Budget.wait_for_room`，只在自带 key 的运行里开，`pipeline.configure_byok` 设）：预扣放不下、但「已花 + 这一次」放得下、而且有在途的
  预扣时，等（`threading.Condition`：预扣退回、花费记入、中止都会叫醒；另外每 0.5 秒醒一次）。只有「已花 + 这一次」放不下，或者没有在途的调用可等时
  才中止，原因的文字和以前相同。等过几次、等了多久记在 state.json 的 `budget.waited_for_room` / `wait_s`（只有自带 key 的运行有这两项）。
  - 为什么不会死锁：`hold` 不嵌套（只有 `AgentLLM.ask` 和 `run_direction` 的搜索两处；Kimi / GLM 搜索里生成查询词的那次调用不另预扣）；在途的预扣
    都在发 HTTP，一定会结束；续接的 `renew_current` 先退回自己那份再等（14.3），不会等自己。等的线程占着并发名额，名额照旧最多 8 个。
  - 网页取消、余额不足（`Budget.halt`）会叫醒等着的预扣，它们马上放弃。`WebRun._abort_budget` 改成经 `halt`（保留第一个原因，同以前）。
- **放不下一次最小运行就拒跑**：`web/catalog.run_floor(model, region, level)` = 规划（2 万字符的 prompt）+ 一次搜索 + 抽取一页（4 万字符）+ 裁判一次
  （10 万字符：已存 355 次裁判调用 prompt 的 p99 约 2.5 万 token）各自的最坏情况预扣之和。预扣是一步一步拿的，每一步都要「已花 + 这一次」放得下，
  合计放不下上限的组合在最坏情况下拿不到裁判那一步。`Registry.start` 在登记之前算（`check_spec_cap`），超过上限就抛 `CapTooLow`（ValueError，
  网页回 400，中英两句，写出最小上限），不发任何请求，key 清掉。目录接口的 `stops_early` 改成同一个判据（`run_floor_usd`、各步的 `run_floor`），
  `min_cap_usd` = 合计按 $0.5 往上取整。原来的「第一轮同时在途的搜索预扣合计」只剩提示 `round1_queues`（会排队，不会中止）。
- **Claude 默认改成 Sonnet 5.5**（`PROVIDERS["claude"]["default_model"]`）：和 GPT / Kimi 选默认模型的口径一致（默认上限下跑得完、能关思考）。
  官方推荐的默认模型是 Opus 5.5，要用它把上限调到 $4 以上。
- 没做审查的 (a)（方向数再按预扣缩放）：有了等待，第一轮同时在途的预扣不会再让运行中止；按预扣缩放会让贵模型在高上限下也只剩很少的方向
  （Opus $7 只剩 3 个方向）。

`$2` 上限、默认档位（`catalog.estimate`，v2.10f 的预扣估计）：

| 计价 id（档位） | 第一轮方向数 | 估计 | 一次最小运行的最坏情况预扣 | 拒跑 | 最小上限 | 第一轮搜索排队 |
|---|---|---|---|---|---|---|
| deepseek-flash（off） | 10 | $0.62 | $0.18 | 否 | — | 否 |
| deepseek-v4-pro（off） | 10 | $1.14 | $0.45 | 否 | — | 否 |
| claude-haiku-5-5（off） | 10 | $0.53 | $0.12 | 否 | — | 否 |
| claude-sonnet-5-5（off，新默认） | 6 | $1.37 | $0.97 | 否 | — | 否 |
| claude-opus-5-5（low） | 3 | $2.95 | $3.77 | 是 | $4.00 | 是 |
| claude-fable-5-1（low） | 1 | $5.48 | $9.31 | 是 | $9.50 | 是 |
| gpt-6-luna（off） | 10 | $0.55 | $0.13 | 否 | — | 否 |
| gpt-6.1-sol（low） | 5 | $2.10 | $2.04 | 是 | $2.50 | 是 |
| gpt-6-astra（low） | 1 | $5.77 | $9.89 | 是 | $10.00 | 是 |
| kimi-k2.6 / kimi-k2.6@cn（off） | 10 | $0.81 / $0.80 | $0.34 / $0.34 | 否 | — | 否 |
| kimi-k3 / kimi-k3@cn（low） | 5 | $2.63 / $2.60 | $2.57 / $2.54 | 是 | $3.00 | 是 |
| glm-4.7-flashx / @cn（off） | 10 | $0.51 / $0.13 | $0.11 / $0.04 | 否 | — | 否 |
| glm-5.2 / glm-5.2@cn（off） | 9 / 10 | $1.31 / $0.93 | $0.50 / $0.39 | 否 | — | 否 |
| glm-5.3 / glm-5.3@cn（low） | 9 / 10 | $1.69 / $1.30 | $0.93 / $0.79 | 否 | — | 否 |

### 14.2 中途停下的运行：网页状态和终稿（medium）

问题：子 agent 阶段（搜索、抽取）余额不足或预扣放不下时，只有 `budget.aborted` 有原因，图 state 的 `aborted` 是空的，网页把运行标成 done，
error 为空，终稿写「no estimation method could be computed from the verified evidence」。

做法：
- `graph.judge`：预算已中止时，返回值里也写 `aborted`（同 `budget.aborted`）。
- `WebRun._after_stream`：原因取 `state.aborted`，没有就取 `budget.aborted`；没有估计就标 failed，error 写原因（先 redact 再截断）。有估计但后面的调用
  停了（终稿等）照旧 done，原因另记在状态视图的 `stopped`（运行页显示「中途停下」）。运行列表（`brief`）也带 `error`，控制台的列表显示前 160 字。
- 终稿（连续值和离散目标）：没有估计、运行又被中止时写「No estimate: the run was stopped before an estimate could be made (<原因>).」。

### 14.3 预扣的估计（medium）

问题：预扣不是最坏情况，上限可能被超过。本阶段改了四处（只在自带 key 的运行里；命令行的预扣不变）：

| 处 | 以前 | v2.10f | 依据 |
|---|---|---|---|
| 搜索输入（模型自己搜的 DeepSeek / Claude / GPT） | 每次 30,000 token | 72,000 token（`Budget.SEARCH_INPUT_TOKENS_BYOK`） | 已存 1,262 次 DeepSeek 搜索的 input + cache read：中位 27,719、p90 44,283、p99 71,669、最大 265,681，42% 超过 30,000 |
| Claude 的 pause_turn 续接 | 同一份预扣下最多 3 次请求 | 每次续接之前另预扣一份（`Searcher.renew` -> `Budget.renew_current`：换掉已用掉的那份）；放不下就不续，用已有的结果，`error` 写 `continuation n: not sent: ...`，不中止整次运行 | 审查发现 |
| JSON 调用输入的 token 估计 | 字符数 / 2 | 别家按 1 个字符 1 个 token（adapter 的 `reserve_chars_per_token`；DeepSeek 照旧 2） | 别家的 tokenizer 没测过；中文按 2 个字符算会低估 |
| Kimi 流式回复没给 usage | 这次调用记 $0 | 按这次调用的预扣记（`usd_basis: "reserve (usage missing)"`） | 审查发现 |

Kimi / GLM（生成查询词 + 搜索接口）的搜索预扣照旧按 30,000 token 输入：唯一的模型调用是生成查询词，输入是几千字符的 brief，30,000 已是上界。

**上限能不能守住（更正第 9.8 节的说法）**：每次调用之前按这次调用的估计最坏情况预扣，放不下就不发；实际花费超出预扣的部分（搜索输入超过 72,000 token，
约 1% 的搜索；tokenizer 让一个字符超过一个 token；GLM 的思考 token 是否计入 max_tokens 未核实）事后才记入，`Budget.add` 一旦发现超过上限就中止之后的调用。
所以上限可能被**在途调用的超出部分之和**超过，不是严格的硬上限。

### 14.4 key 不留在文字里（low）

- `llm.scrub_server_text`：服务端的说明先 `spec.redact`（这次运行的整把 key）、再换像 key 的片段（`sk-...`，和新加的 GLM 形状 `<32 位 hex>.<16 位>`），
  最后才截到 200 字。`llm.server_error(ad, raw, redact)`、`json_call` 的 bad_response_body 分支、`Searcher._request` 都经过它；`GLMAdapter.parse_error`
  不再自己截断。审查的「leaky」场景（400 的 message 是 185 个 x + key，截断落在 key 中间）：GLM 以前在 calls.jsonl、state.json、/api/result 里留下 key
  的前 10 个字符，现在哪里都没有（`test_server_message_quoting_the_key_leaves_no_fragment`，GLM / Claude / Kimi）。
- 网页：`WebRun._on_update` 先 `redact_obj` 整个更新，再做裁判摘要（摘要会截断）。
- `clean_key` 只收 `KEY_CHARS`（字母、数字和 `. _ ~ + / = -`）：兜底的 redact 是在序列化之后的文字上找 key，带 `"`、`\`、`&`、`<`、`>`、`'` 的 key
  经 JSON / HTML 转义以后就找不到了。各家真实的 key（`sk-...` 的 base64url、GLM 的 hex.secret）都在这个字符集里。

### 14.5 等人工确认的超时（low）

停在人工确认超过 `runs.APPROVAL_TIMEOUT_S`（30 分钟）：`WebRun._approval_expired` 走已有的取消路径（`cancel(by="web-timeout")`），按「不批准」结束，
状态 cancelled，error 写「not approved within 30 minutes: ...」，key 随 `_release` 清掉，名额退回。批准或取消时计时器停掉。`Registry(approval_timeout_s=...)`
可以改（测试用 0.5 秒）。

### 14.6 DeepSeek 自带 key 的搜索关思考（low）

Thinking Mode 文档（2026-10-21 看了页面 HTML 的表格，WebFetch 的摘要分不清列）：开关 `{"thinking": {"type": "enabled/disabled"}}` 这一格横跨
OpenAI / Anthropic 两种格式（colspan=2），Anthropic 格式的深度是 `output_config.effort`；思考默认开、默认 high。Anthropic 兼容接口的页面写 thinking
「Supported (budget_tokens is ignored)」。所以 `DeepSeekAdapter.search_request_spec`（只有自带 key 的运行用，Searcher 有 spec 时选它）在请求体末尾加
`"thinking": {"type": "disabled"}`（搜索不是 plan / judge / repair，DeepSeek 两个模型都能关）。命令行的 `search_request` 不变（金样本逐字节相同）。
没有真 key，这个字段的实际效果没测（有效 key 时会不会被拒、会不会真的不思考，未核实）。

### 14.7 命令行只收 DeepSeek 模型（low）

没有 spec 时 `LLM()` / `Searcher()`（含基线的 `DirectClient`）用 `config.require_deepseek`：没有价格抛 `UnknownModel`（同以前），有价格但不是 DeepSeek 的
模型抛 `UnsupportedModel`（`UnknownModel` 的子类），都在读 key 之前。以前 `TRIANGULATE_MODEL=claude-haiku-5-5` 会带着 DeepSeek 的 key 把 Claude 的模型 id
发到 api.deepseek.com，预算又按 Claude 的价格算。

### 14.8 403 的说法（low）

401 照旧「X rejected the API key (HTTP 401)」。403 改成「X rejected the API key or the request (HTTP 403[: type/code])」：OpenAI 的 403 可能是地区不支持
（Error codes 页），Claude 的 403 是 permission_error（Errors 页），不一定是 key 错了。Claude、OpenAI 把 403 放进 `error_body_statuses`，`llm.forbidden_info`
只取 `error.type` / `error.code`（不取 message）。Kimi / GLM / DeepSeek 的 403 照旧不读 body，只改说法。`check_key` 对 403 返回 `error: "forbidden"`。

### 14.9 GLM 1313（low）

1313（公平使用策略下的频率限制）从「停下整次运行」改成按限流重试（2 / 4 秒，同 1302 / 1305）；3 次仍是 1313 就照原样报传输错误。1308 / 1310 / 1316–1321
（`GLM_LIMIT_CODES`）和 1309 / 1311 / 1314 / 1315（`GLM_PLAN_CODES`）照旧停下，但说明的开头分别是 `usage limit reached` / `key or plan not accepted`，
只有 1113 写 `insufficient balance`（`GLMAdapter.stop_prefix`；`llm.balance_message`、`check_key` 都用 `providers.stop_prefix`，其余 provider 的文字不变）。

### 14.10 Verification（v2.10f）

- `tests/test_providers_e2e.py`（8 个，审查脚本 e2e_all.py 整理而来）：一个 127.0.0.1 上的假服务接五家的所有 URL，走 POST /api/runs -> Registry ->
  真实的 prepare_run / AgentLLM / Searcher / save_run。11 个组合（DeepSeek high、Haiku / Sonnet off、Opus high、Luna off、Sol medium、K2.6 off、K3 国内站 high、
  GLM-5.2 off、5.3 国内站 low、4.7-FlashX high）全部 done、估计 1210；每个请求都带着用户的 key；Claude / Kimi / GLM 不发 temperature、GPT 只在 none 时发、
  max tokens 不超过模型上限、DeepSeek 自带 key 的搜索带 thinking disabled；写出的文件和 7 个 API 返回里没有 key（整把和三段半截）；搜索阶段余额不足
  （五家各自文档写的 402 / 429）-> failed、error 和运行列表里有说明、终稿写明停下；中途花费超过上限 -> failed；Opus / Fable / Astra / Sol / K3 在 $2 下被拒（400，
  一个请求都没发）；Opus 6 个方向、$5、搜索慢：排队跑完（`waited_for_room > 0`，不中止）；服务端说明里带 key（截断落在 key 中间）不留半截；等确认超时自动结束、
  按时批准不受影响。
- `tests/test_budget_wait.py`（12 个）：命令行的预算行为不变；等在途、放不下就中止、没有在途不等、等的时候在途的花掉了就中止、取消叫醒等着的预扣、20 个并发
  预扣不超过上限也不死锁；`renew_current`（换掉已用掉的那份、放不下返回 False 不中止、等别的线程）；Claude 续接另预扣、放不下不续；各家的搜索输入估计。
- `tests/test_review_v210f.py`（11 个）：key 字符集；命令行拒收别家模型（读 key 之前）；先 redact 再截断（GLM 形状、parse_error 不截断、网页裁判摘要）；
  DeepSeek 自带 key 的搜索请求体；原因只在 budget.aborted 时的网页状态（failed / done + stopped）；拒跑并清 key。
- 改过的旧测试：Claude / GPT / Kimi / GLM 的预扣测试（1 字符 1 token、72,000）、403 的说法、Kimi 缺 usage 按预扣、GLM 1313 重试和说明开头、Claude 默认模型、
  DeepSeek 自带 key 搜索的请求体（末尾多一个 thinking，其余和默认路径相同）、网页估计（新判据：Opus $2 拒跑、最小上限 $4.00；五家的默认组合在 $2 下都不拒跑）。
- 变异检查 26 处（关掉等待、裁判不写 aborted、网页只看 state.aborted、有估计时不记 stopped、终稿不写原因、先截断再 redact、去掉 GLM 形状的正则、parse_error 先截断、
  不续接预扣、renew 不先退回自己那份、搜索输入回到 30,000、别家回到 2 字符 / token、旧的 key 字符集、缺 usage 记 0、不启动 / 不停掉确认计时器、不拒跑、
  最小运行不算裁判、命令行不拦别家模型、1313 又算停下、用量上限写成余额不足、DeepSeek 自带 key 的搜索不关思考、网页摘要不先 redact、OpenAI 403 不读 body、
  403 用旧说法、运行列表不带 error）：全部被测试抓到。第一轮有 2 处没抓到（「网页只看 state.aborted」：裁判已经把原因写进 state，两处修正互相兜底；「不停掉确认计时器」：
  计时器到时 cancel 会因为状态不对而什么都不做），补了 `TestWebStatusAfterBudgetStop` 和计时器的断言后抓到。「renew 不先退回自己那份」表现为测试卡死（自己等自己，正是设计里要避免的死锁），手动结束进程后记为抓到。
- DeepSeek 默认路径的 24 组金样本仍逐字节相同；G2（`probes/compare_continuous_prompts.py`）：`365b06515d8caef8257020c2e5d574de7724be2f2270c122e6e21952517f78c4`（和 v2.10e 相同，没改提示词）。
- 没有真 key，没有任何付费请求。本阶段的真实网络只有不带 key 的 GET：DeepSeek 两页文档（WebFetch）和 `probes/deepseek_thinking_doc_probe.py`（打印 Thinking Mode 页的表格）。
- 全套测试：674 个通过（v2.10e + web-v0.9 时 643 个）。

### 14.11 已知限制、没做的

- 上限不是严格的硬上限（14.3 最后一段）。
- 第一轮可能把上限花到裁判放不下：方向数按典型花费只用上限的 60%，但第一轮的调用只要「已花 + 这一次」放得下就会发，最坏情况下会把钱花到裁判那一步
  放不下（没有给裁判单独留钱）。`run_floor` 只保证一个方向的最小运行放得下。
- 一页很长（最多 40 万字符）的抽取预扣可能放不下，这时整次运行停下（预扣放不下就中止的规则没变，只是不再因为在途的调用中止）。
- 等在途会让贵模型的运行变慢（第一轮的搜索几个几个地跑）；没有给网页显示「正在等预扣」。
- 拒跑的判据用固定的 prompt 长度（规划 2 万、抽取 4 万、裁判 10 万字符），不是这道题的实际长度。
- DeepSeek 搜索的 thinking disabled、各家的 403 body、GLM 1313 的重试效果，都只按文档写，没有真 key 实测。
## Official docs（Claude，2026-10-21 查看）

- Messages API（请求字段、stop_reason、usage、流式事件类型）：https://platform.claude.com/docs/en/api/messages/create
- Streaming：https://platform.claude.com/docs/en/build-with-claude/streaming
- Errors：https://platform.claude.com/docs/en/api/errors
- Rate limits（spend cap、spend limit、retry-after）：https://platform.claude.com/docs/en/api/rate-limits
- API credits（credit balance too low 原文）：https://platform.claude.com/docs/en/about-claude/api-credits-for-subscribers
- Authentication：https://platform.claude.com/docs/en/manage-claude/authentication
- Effort：https://platform.claude.com/docs/en/build-with-claude/effort
- Thinking：https://platform.claude.com/docs/en/build-with-claude/thinking
- Pricing：https://platform.claude.com/docs/en/about-claude/pricing
- Web search tool：https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool
- Server tools（pause_turn、allowed_callers）：https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools
- List Models：https://platform.claude.com/docs/en/api/models/list
- OpenAI SDK 兼容层（为什么不用）：https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/openai-sdk

## Official docs（DeepSeek，2026-10-21 查看）

- Models & Pricing：https://api-docs.deepseek.com/quick_start/pricing
- Thinking Mode：https://api-docs.deepseek.com/guides/thinking_mode
- Anthropic API 兼容：https://api-docs.deepseek.com/guides/anthropic_api
- Error Codes：https://api-docs.deepseek.com/quick_start/error_codes
- List Models：https://api-docs.deepseek.com/api/list-models

## Official docs（OpenAI，2026-10-21 查看；页面加 `.md` 可取原始 markdown）

- Using GPT-6（模型选择、迁移：none 档、temperature、Chat Completions 的 tool calling）：https://developers.openai.com/api/docs/guides/latest-model
- 模型页：https://developers.openai.com/api/docs/models/gpt-6-luna 、https://developers.openai.com/api/docs/models/gpt-6.1-sol 、https://developers.openai.com/api/docs/models/gpt-6-astra
- Reasoning（effort 取值、默认档、reasoning token、max_output_tokens、incomplete）：https://developers.openai.com/api/docs/guides/reasoning
- Create chat completion（messages / developer、max_completion_tokens、reasoning_effort、response_format、store、usage、finish_reason、refusal）：https://developers.openai.com/api/reference/resources/chat
- Create response（include、max_output_tokens、max_tool_calls、store、tool_choice、web_search 工具、output 项、usage）：https://developers.openai.com/api/reference/resources/responses/methods/create
- Web search tool（tool_choice required、sources、search 动作计费、Limitations）：https://developers.openai.com/api/docs/guides/tools-web-search
- Structured Outputs / JSON mode（"JSON" 字符串要求、edge cases）：https://developers.openai.com/api/docs/guides/structured-outputs
- Prompt caching（implicit / explicit、写入 1.25 倍 / 2.5 倍、usage 字段和计价算法）：https://developers.openai.com/api/docs/guides/prompt-caching
- Pricing（Standard 档、272K 长上下文、Web search $10 / 1k calls）：https://developers.openai.com/api/docs/pricing
- Error codes（429 credit_balance_exhausted / spend limit / usage limit、503 server_is_overloaded）：https://developers.openai.com/api/docs/guides/error-codes
- Rate limits（Retry-After、slow_down）：https://developers.openai.com/api/docs/guides/rate-limits
- List models：https://developers.openai.com/api/reference/resources/models/methods/list
- Your data（store、Responses 默认保存 30 天）：https://developers.openai.com/api/docs/guides/your-data

## Official docs（Kimi，2026-10-21 查看；页面加 `.md` 可取原始 markdown，价格 / 限速表要看页面 HTML）

- Chat Completions API（请求字段、流式格式、stream_options、usage、prompt_tokens_details、finish_reason、JSON mode、Partial Mode）：https://platform.kimi.ai/docs/api/chat
- Model Parameter Reference（thinking / reasoning_effort / 固定的 temperature、top_p、n、penalty）：https://platform.kimi.ai/docs/api/models-overview
- Reasoning Effort（K3：low / high / max，默认 max）：https://platform.kimi.ai/docs/guide/use-reasoning-effort
- Thinking Mode（reasoning_content、思考 token 计入 max_tokens、建议流式）：https://platform.kimi.ai/docs/guide/use-thinking-models
- Kimi K3 quickstart（解锁条件、流式、结构化输出）：https://platform.kimi.ai/docs/guide/kimi-k3-quickstart
- Kimi K2.6 quickstart（默认 max_tokens 32K、thinking 开关、固定采样参数）：https://platform.kimi.ai/docs/guide/kimi-k2-6-quickstart
- Common Error Codes（400 / 401 / 403 / 404 / 429 exceeded_current_quota_error / 504）：https://platform.kimi.ai/docs/api/errors
- Web Search Basic（/v1/tools/search 的请求、返回、错误码、计费条件）：https://platform.kimi.ai/docs/api/tools-search
- WebSearch Pricing（$0.002 / 次，$web_search 2026-10-20 下线）：https://platform.kimi.ai/docs/pricing/websearch
- Model Inference Pricing（K3 / K2 价格表）：https://platform.kimi.ai/docs/pricing/chat
- Context Caching（缓存写入 5m / 1h、K3 价格正文）：https://platform.kimi.ai/docs/guide/context-caching
- Recharge and Rate Limits（Tier0–Tier5）：https://platform.kimi.ai/docs/pricing/limits
- List Models：https://platform.kimi.ai/docs/api/list-models
- 国内站同名页面：https://platform.kimi.com/docs/api/chat 、https://platform.kimi.com/docs/api/tools-search 、https://platform.kimi.com/docs/api/errors 、
  https://platform.kimi.com/docs/pricing/chat 、https://platform.kimi.com/docs/pricing/websearch
- 人民币汇率中间价（2026-10-21，1 美元对人民币 6.7192 元）：https://www.pbc.gov.cn/zhengcehuobisi/125207/125217/125925/2026102108513972558/index.html

## Official docs（GLM，2026-10-21 查看；页面加 `.md` 可取原始 markdown）

- 国际站 API Introduction（通用端点 /api/paas/v4、Bearer、Standard API Key）：https://docs.z.ai/api-reference/introduction
- 国际站 Chat Completion（请求字段、thinking、reasoning_effort、response_format、max_tokens、usage、finish_reason、Error schema）：https://docs.z.ai/api-reference/llm/chat-completion
- 国际站 Errors（业务码、错误 body 形状）：https://docs.z.ai/api-reference/api-code
- 国际站 Web Search API（search-prime、count）：https://docs.z.ai/api-reference/tools/web-search ；指南：https://docs.z.ai/guides/tools/web-search
- 国际站 Deep Thinking（各模型的 thinking / reasoning_effort）：https://docs.z.ai/guides/capabilities/thinking
- 国际站 Core Parameters（max_tokens 默认 / 最大、采样参数）：https://docs.z.ai/guides/overview/concept-param
- 国际站 Migrate to GLM-5.3（采样参数推荐、disabled 改成 enabled + low）：https://docs.z.ai/guides/overview/migrate-to-glm-new
- 国际站模型页：https://docs.z.ai/guides/llm/glm-5.3 、https://docs.z.ai/guides/llm/glm-5.2 、https://docs.z.ai/guides/llm/glm-4.7
- 国际站 Structured Output（json_object）：https://docs.z.ai/guides/capabilities/struct-output ；Context Caching：https://docs.z.ai/guides/capabilities/cache
- 国际站 Pricing：https://docs.z.ai/guides/overview/pricing ；FAQ（缓存公测、账单 n-1、3DS）：https://docs.z.ai/help/faq
- 国际站 API Key Management Guide（10-16 起 Standard / Coding Plan key 分开）：https://docs.z.ai/devpack/notice/api-key-management ；Coding Plan Usage Policy：https://docs.z.ai/devpack/usage-policy
- 国内站对话补全：https://docs.bigmodel.cn/api-reference/模型-api/对话补全 ；网络搜索：https://docs.bigmodel.cn/api-reference/工具-api/网络搜索
- 国内站错误码：https://docs.bigmodel.cn/cn/faq/api-code ；API 定价：https://docs.bigmodel.cn/cn/guide/start/pricing ；模型概览：https://docs.bigmodel.cn/cn/guide/start/model-overview
- 国内站深度思考：https://docs.bigmodel.cn/cn/guide/capabilities/thinking ；核心参数：https://docs.bigmodel.cn/cn/guide/start/concept-param ；HTTP API 调用：https://docs.bigmodel.cn/cn/guide/develop/http/introduction
- 国内站 API Key 分类管理说明：https://docs.bigmodel.cn/cn/coding-plan/notice/api-key-management ；Coding Plan 使用须知：https://docs.bigmodel.cn/cn/coding-plan/usage-notes

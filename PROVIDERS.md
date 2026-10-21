# PROVIDERS.md — 多家模型、自带 key（BYOK）的设计记录

这份文件随阶段更新：每家 adapter 发什么、为什么、官方文档链接、已知限制。API 细节以官方文档为准，没核实的写「未核实」。

## 阶段

| tag | 内容 | 状态 |
|---|---|---|
| `v2.10a` | adapter 层 + 每次运行的 `ModelSpec`，目前只有 DeepSeek；按模型计价、没有价格的模型拒跑、方向数按模型价格缩放、余额不足立刻停、key 不落盘、BYOK 运行关掉 Jev | 本文件第 1–7 节 |
| `v2.10b` | Claude adapter（原生 Messages API，流式）和 Claude 搜索（服务端 web_search，pause_turn 续上）；用 models 列表校验 key（`llm.check_key`，DeepSeek 也有）；adapter 接口补了解码、可重试状态码、超时、回复问题、续搜索几个钩子 | 第 3、5、9 节 |
| `v2.10c` | GPT adapter（OpenAI：JSON 调用走 Chat Completions，搜索走 Responses API 的 web_search）；按官方价计价（含 cache 写入价、272K 长上下文档）；429 余额 / 额度错误立刻停；GPT key 校验 | 第 10 节 |
| 之后 | Kimi、GLM 的 adapter；网页（填 key、选模型、校验 key、每次运行的花费估计） | 未开始 |

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
| key 格式 | 去首尾空白（粘贴常带换行）后 8–512 个可打印 ASCII 字符、中间没有空白。理由：urllib 拼请求头遇到 `\r\n` 会抛 `ValueError: Invalid header value b'Bearer <整把 key>'`，非 latin-1 字符会抛带字符的 `UnicodeEncodeError`（代码调查阶段在 Python 3.14.3 上实测）；入口拦下就不会走到这条路 |
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
- 预扣（`llm_reserve`、`search_reserve`）用这次运行的模型的峰时价和这家的搜索费。
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

- **DeepSeek 搜索角色的思考没关**：搜索请求不带 `thinking` 字段（v2.9b 原样），服务端默认；`search_direct.py` 的注释记过这个接口默认返回 thinking 块。
  用户决定 6 说「其余角色能关就关」，但关掉要往搜索请求体里加字段（改变冻结的请求体），而且 DeepSeek 的 Anthropic 兼容文档只写了 `thinking`
  「Supported」、没写 `type: disabled` 的效果（未核实）。本阶段没动，等用户定。
- **网页还没接**：`web/runs.py` 的 `prepare(q, tag)` 还不传 spec；运行失败（`_guard`）时还没调 `run.release(h)` 和 `spec.redact`；
  `app.py` 不收 provider / model / key；网页没有 key 输入框、模型选择、花费估计。留给网页阶段。
- 搜索遇到 401 / 403 仍然只记 `http_401` 返回空 URL（v2.9b 原样），不像 JSON 调用那样抛 `KeyRejected`。
- ~~key 校验（models 列表接口）还没实现。~~ v2.10b：`llm.check_key`（DeepSeek `GET /models`、Claude `GET /v1/models`），网页还没接。
- ~~其他四家（Claude、GPT、Kimi、GLM）的 adapter、价格、模型清单还没加~~：Claude 见第 9 节（v2.10b），GPT 见第 10 节（v2.10c）；
  Kimi、GLM 还没加，调研结果在 `providers_research.json`（2026-10-20）。

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
  只有「已花 + 这一次」放不下才中止；或者给贵模型更高的默认上限 / 更低的并发。上限本身照样守得住（预扣是最坏情况）。
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
- 预扣的 token 估计仍是「字符数 / 2」；官方说 4.7 以后的 tokenizer 同样文字多约 30% token，和 DeepSeek 的差距没测，中文页面可能低估。
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
- 每次搜索的内容 token 数文档没给；搜索上下文窗口最大 128K（web search 指南）。预扣照旧假设每次搜索输入 30,000 token（DeepSeek 实测），
  Sol / Astra 的真实搜索可能更贵，超出部分事后计入（`Budget.add`），上限可能被一次搜索超过一点。
- 非流式：生成完才回 body。单次读超时设 1,200 秒、整次 1,800 秒（`chat_timeouts`）；Astra / Sol 开 high 的长回复要多久，没实测。读超时后会重试，
  而服务端那次请求可能已经计费。搜索沿用 600 秒（Searcher 共用）。
- `tool_choice: "required"` + `max_tool_calls` 的收尾行为、Luna 在 `none` 下用 web_search 的效果、json_object 在 GPT-6 Chat Completions 上的
  表现，都只按文档写，没有真 key 实测。
- `temperature` 在 effort 不是 none 时发了会 400 还是被忽略，文档没写（未核实）；代码不发，所以不影响。
- 中国大陆、香港、澳门不在 OpenAI supported countries 列表里（调研记录；官方警告 accessing or offering access 可能导致封号），网页阶段要写明。
- 调研说 Free 档能不能用 GPT-6、reasoning summary 要不要组织验证，没查到（未核实）；本项目不请求 summary。
- 预扣的 token 估计仍是「字符数 / 2」；OpenAI 的 tokenizer 英文约 4 字符 / token，偏保守。`DIRECTION_PROFILE` 是 DeepSeek 不开思考时的输出量，
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

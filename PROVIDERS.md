# PROVIDERS.md — 多家模型、自带 key（BYOK）的设计记录

这份文件随阶段更新：每家 adapter 发什么、为什么、官方文档链接、已知限制。API 细节以官方文档为准，没核实的写「未核实」。

## 阶段

| tag | 内容 | 状态 |
|---|---|---|
| `v2.10a` | adapter 层 + 每次运行的 `ModelSpec`，目前只有 DeepSeek；按模型计价、没有价格的模型拒跑、方向数按模型价格缩放、余额不足立刻停、key 不落盘、BYOK 运行关掉 Jev | 本文件第 1–7 节 |
| 之后 | Claude、GPT、Kimi、GLM 的 adapter；网页（填 key、选模型、校验 key、每次运行的花费估计） | 未开始 |

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
| `balance_exhausted(status, body)` | 余额不足就返回一句说明，外层抛 `llm.BalanceExhausted` |
| `error_body_statuses` | 哪些错误状态码要读 body 给 `balance_exhausted` 判断（DeepSeek 为空：只看 402）。读到的 body 不写日志：有的 provider 会回显部分 key |

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

- **没有价格就不跑**：`config.price(model)` 找不到就抛 `UnknownModel`；`usd_cost`、`Budget`、`LLM()` / `Searcher()` 的构造、`ModelSpec` 都经过它。
  v2.9b 的 `PRICES.get(model, PRICES["deepseek-flash"])` 静默回落已删（命令行设了没价格的 `TRIANGULATE_MODEL` 现在在读 key 之前就报错）。
- **方向数按模型价格缩放**：`Budget.typical_direction_usd(model)` = 0.06（deepseek-flash 实测）×（这个模型 / flash 按峰时价算的一个方向的价格比）。
  一个方向的 token 构成 `DIRECTION_PROFILE` 取自已存的 1251 个 deepseek-flash 方向的平均（搜索 + 抽取：cache hit 13,600、miss 25,700、
  输出 3,600 token，4 次搜索），只用来算比例。flash 仍是 0.06（`Budget().directions` 仍是 10）；v4-pro 约 $0.102 / 方向：
  $1 上限 5 个方向、$2 上限 10 个（页数上限 40 / 4）。
- 预扣（`llm_reserve`、`search_reserve`）用这次运行的模型的峰时价和这家的搜索费。

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

- **DeepSeek 搜索角色的思考没关**：搜索请求不带 `thinking` 字段（v2.9b 原样），服务端默认；`search_direct.py` 的注释记过这个接口默认返回 thinking 块。
  用户决定 6 说「其余角色能关就关」，但关掉要往搜索请求体里加字段（改变冻结的请求体），而且 DeepSeek 的 Anthropic 兼容文档只写了 `thinking`
  「Supported」、没写 `type: disabled` 的效果（未核实）。本阶段没动，等用户定。
- **网页还没接**：`web/runs.py` 的 `prepare(q, tag)` 还不传 spec；运行失败（`_guard`）时还没调 `run.release(h)` 和 `spec.redact`；
  `app.py` 不收 provider / model / key；网页没有 key 输入框、模型选择、花费估计。留给网页阶段。
- 搜索遇到 401 / 403 仍然只记 `http_401` 返回空 URL（v2.9b 原样），不像 JSON 调用那样抛 `KeyRejected`。
- key 校验（models 列表接口）还没实现。
- 其他四家（Claude、GPT、Kimi、GLM）的 adapter、价格、模型清单还没加；调研结果在 `providers_research.json`（2026-10-20）。

## Official docs（DeepSeek，2026-10-21 查看）

- Models & Pricing：https://api-docs.deepseek.com/quick_start/pricing
- Thinking Mode：https://api-docs.deepseek.com/guides/thinking_mode
- Anthropic API 兼容：https://api-docs.deepseek.com/guides/anthropic_api
- Error Codes：https://api-docs.deepseek.com/quick_start/error_codes
- List Models：https://api-docs.deepseek.com/api/list-models

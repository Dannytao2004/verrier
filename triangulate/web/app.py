"""本地网页：发起运行（停在人工确认方向）、看进度、看任何一次保存的运行、回测表。

启动：.venv/Scripts/python.exe -m triangulate serve [--port 8770]，只绑定 127.0.0.1。
浏览保存的运行完全离线；前端是 static/ 里的原生 HTML + JS，没有构建步骤。
web-v0.9：发起新运行要用户自己的 key（自带 key，BYOK）：POST /api/runs 带 provider / model / region / thinking / usd_cap / api_key，
没有 api_key 就拒跑；网页运行永远不读服务器的 key 文件（TRIANGULATE_KEY_FILE / .env）。key 只进这次运行内存里的 ModelSpec，
运行结束就清掉；任何返回（状态、校验结果、错误）都不含 key。只在 /verrier 系列页面上发起；经典界面（/）只浏览。
GET /api/providers：可选的 provider、区域、模型、思考档位和每次运行的花费估计（web/catalog.py）。
POST /api/key/check：用这把 key 调这家免费的 models 列表接口（llm.check_key），只回 ok / 被拒 / 出错。
"""
from pathlib import Path

from fastapi import Body, FastAPI, HTTPException, Query
from fastapi.exceptions import RequestValidationError
from fastapi.responses import FileResponse, JSONResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.trustedhost import TrustedHostMiddleware

from .. import llm
from .. import providers as PV
from ..agent.outputs import dep_graph
from ..agent.run import RES
from . import catalog as CAT
from . import results as R
from .runs import NEED_KEY, BadState, Busy, Registry

STATIC = Path(__file__).resolve().parent / "static"
HOST = "127.0.0.1"
DEFAULT_PORT = 8770
FILES = {"graph.html": "text/html; charset=utf-8", "ledger.md": "text/plain; charset=utf-8"}
SPEC_FIELDS = ("provider", "model", "region", "thinking")   # 字符串字段；usd_cap 是数，api_key 单独处理


def spec_from_body(body: dict) -> PV.ModelSpec:
    """网页请求里的 provider / model / region / thinking / usd_cap / api_key -> ModelSpec。没给的字段用默认值（provider 默认 DeepSeek，
    模型用这家的默认模型，档位用这个模型的默认档，上限 $2.00）；api_key 没给就拒（NEED_KEY）。抛 ValueError，消息里不带 key。"""
    key = body.get("api_key")
    if key is None or (isinstance(key, str) and not key.strip()):
        raise ValueError(NEED_KEY)
    for f in SPEC_FIELDS:
        if body.get(f) is not None and not isinstance(body[f], str):
            raise ValueError(f"{f} must be a string")
    provider = body.get("provider") or PV.DEFAULT_PROVIDER
    if provider not in PV.PROVIDERS:
        raise ValueError(f"unknown provider {provider!r}; choose one of {', '.join(PV.PROVIDERS)}")
    model = body.get("model") or PV.PROVIDERS[provider]["default_model"]
    if model not in PV.MODELS:
        raise ValueError(f"model {model!r} is not offered for {PV.PROVIDERS[provider]['label']}; choose one of "
                         f"{', '.join(PV.PROVIDERS[provider]['models'])}")
    thinking = body.get("thinking") or CAT.default_thinking(model)
    cap = CAT.parse_cap(body["usd_cap"]) if body.get("usd_cap") is not None else PV.DEFAULT_USD_CAP
    # SpecError / config.UnknownModel 都是 ValueError
    return PV.ModelSpec(provider, model, key, region=body.get("region") or None, thinking=thinking, usd_cap=cap)


def create_app(registry: Registry | None = None, res: Path = RES, allowed_hosts=("127.0.0.1", "localhost"),
               key_checker=None) -> FastAPI:
    """key_checker：POST /api/key/check 用的校验函数（默认 llm.check_key；假演示服务换成「什么 key 都接受」的）。"""
    app = FastAPI(title="triangulate-agent", docs_url=None, redoc_url=None, openapi_url=None)
    # 只认本机的 Host 头（挡 DNS rebinding）；POST 只收 application/json（FastAPI 默认），别的网页不能用表单替你开运行
    app.add_middleware(TrustedHostMiddleware, allowed_hosts=list(allowed_hosts))
    reg = registry or Registry()
    app.state.registry = reg
    check = key_checker or llm.check_key

    @app.exception_handler(RequestValidationError)
    async def validation_error(request, exc):
        # FastAPI 默认的 422 会把收到的 body 原样放进 "input"：请求体里有 api_key 时就回显了 key。这里只回错误的位置和类型
        return JSONResponse(status_code=422, content={"detail": [{"loc": list(e.get("loc", ())), "type": e.get("type"),
                                                                  "msg": e.get("msg")} for e in exc.errors()]})

    def run_or_404(run_id: str):
        try:
            return reg.get(run_id)
        except KeyError:
            raise HTTPException(404, f"没有这个运行：{run_id}（服务重启后内存里的运行会丢失，结果在「已保存的运行」里）") from None

    @app.get("/")
    def index():
        return FileResponse(STATIC / "index.html", media_type="text/html; charset=utf-8")

    @app.get("/verrier")
    def verrier():
        # Verrier 宣传页 + 控制台（提问 → 人工确认 → 进度 → 结果），和经典界面用同一套 API
        return FileResponse(STATIC / "verrier_console.html", media_type="text/html; charset=utf-8")

    @app.get("/verrier/aero")
    def verrier_aero():
        # 并列的新版界面（航天宣传风草稿）：同一套 API 和共享 JS，旧版 /verrier 不变；照片在 static/aero_assets/（不进 git）
        return FileResponse(STATIC / "verrier_aero.html", media_type="text/html; charset=utf-8")

    @app.get("/verrier/apple")
    def verrier_apple():
        # 第三版并列界面（浅色产品页风格草稿）：同一套 API 和共享 JS；首屏结果卡实时读 /api/result，读不到用页面里的快照
        return FileResponse(STATIC / "verrier_apple.html", media_type="text/html; charset=utf-8")

    @app.get("/verrier/manuscript")
    def verrier_manuscript():
        # 第四版并列界面（欧洲古典天文学手稿风草稿）：同一套 API 和共享 JS；首屏账页实时读 /api/result，读不到用页面里的快照
        return FileResponse(STATIC / "verrier_manuscript.html", media_type="text/html; charset=utf-8")

    @app.get("/verrier/halo")
    def verrier_halo():
        # 第五版并列界面：HALOFLUX（Ryder191，PolyForm Noncommercial 1.0.0，仅限非商业用途）的派生版，
        # 整套流程（提问 → 人工确认 → 进度 → 结果）由我们自己的 static/verrier_halo_flow.js 驱动，同一套 API。
        # 署名和条款在页面里和 static/haloflux_LICENSE.txt；项目若转向商用，删掉这个路由和 verrier_halo.html、haloflux_LICENSE.txt
        return FileResponse(STATIC / "verrier_halo.html", media_type="text/html; charset=utf-8")

    # ---------- 模型、key ----------
    @app.get("/api/providers")
    def providers(usd_cap: float | None = Query(None)):
        try:
            cap = PV.DEFAULT_USD_CAP if usd_cap is None else CAT.parse_cap(usd_cap)
        except ValueError as e:
            raise HTTPException(400, str(e)) from None
        return CAT.providers_view(cap)

    @app.post("/api/key/check")
    def key_check(body: dict = Body(...)):
        try:
            spec = spec_from_body({k: body.get(k) for k in ("provider", "model", "region", "api_key")})
        except ValueError as e:
            raise HTTPException(400, str(e)) from None
        try:
            return spec.redact_obj(check(spec))
        finally:
            spec.drop_key()

    # ---------- 网页运行 ----------
    @app.post("/api/runs")
    def start_run(body: dict = Body(...)):
        try:
            spec = spec_from_body(body)
        except ValueError as e:
            raise HTTPException(400, str(e)) from None
        try:
            run = reg.start(body.get("question", ""), body.get("as_of"), spec=spec)   # 出错时 Registry.start 清 key
        except ValueError as e:
            raise HTTPException(400, str(e)) from None
        except Busy as e:
            raise HTTPException(429, str(e)) from None
        return R.clean(run.status_view())

    @app.get("/api/runs")
    def list_web_runs():
        return {"runs": reg.list(), "max_active": reg.max_active}

    @app.get("/api/runs/{run_id}")
    def get_run(run_id: str):
        return R.clean(run_or_404(run_id).status_view())

    @app.post("/api/runs/{run_id}/approve")
    def approve(run_id: str, body: dict | None = Body(None)):
        run = run_or_404(run_id)
        keep = (body or {}).get("keep_direction_ids")
        if keep is not None and not (isinstance(keep, list) and all(isinstance(x, str) for x in keep)):
            raise HTTPException(400, "keep_direction_ids 必须是字符串列表")
        use = (body or {}).get("use_existing")   # v2.11f：选用一个现成数据候选（id），不跑路线
        if use is not None and not isinstance(use, str):
            raise HTTPException(400, "use_existing 必须是字符串")
        try:
            run.approve(keep, use)
        except BadState as e:
            raise HTTPException(409, str(e)) from None
        except ValueError as e:
            raise HTTPException(400, str(e)) from None
        return R.clean(run.status_view())

    @app.post("/api/runs/{run_id}/cancel")
    def cancel(run_id: str):
        run = run_or_404(run_id)
        try:
            run.cancel()
        except BadState as e:
            raise HTTPException(409, str(e)) from None
        return R.clean(run.status_view())

    # ---------- 保存的运行（只读、离线） ----------
    @app.get("/api/saved")
    def saved():
        return {"runs": R.list_runs(res)}

    @app.get("/api/result")
    def result(qid: str = Query(...), tag: str = Query("")):
        try:
            return R.load_result(qid, tag, res)
        except R.NotFound as e:
            raise HTTPException(404, str(e)) from None

    @app.get("/api/graph")
    def graph(qid: str = Query(...), tag: str = Query("")):
        # 控制台的依赖图（#console/graph/...）：和 graph.html 同一个 outputs.dep_graph，按保存的 state.json 现算
        try:
            return R.clean(dep_graph(R.load_state(qid, tag, res)))
        except R.NotFound as e:
            raise HTTPException(404, str(e)) from None

    @app.get("/api/file")
    def run_file(qid: str = Query(...), tag: str = Query(""), name: str = Query(...)):
        if name not in FILES:
            raise HTTPException(404, f"只提供 {sorted(FILES)}")
        try:
            p = R.run_dir(qid, tag, res) / name
        except R.NotFound as e:
            raise HTTPException(404, str(e)) from None
        if not p.is_file():
            raise HTTPException(404, f"{qid}/{tag} 没有 {name}")
        if name.endswith(".md"):
            return PlainTextResponse(p.read_text(encoding="utf-8"), media_type=FILES[name])
        # graph.html 加载 CDN 上的 vis-network：放进 sandbox（opaque origin），它就拿不到本机 API 的同源权限（审查发现）
        return FileResponse(p, media_type=FILES[name], headers={"Content-Security-Policy": "sandbox allow-scripts"})

    @app.get("/api/backtests")
    def backtests():
        return R.backtests(res)

    app.mount("/static", StaticFiles(directory=STATIC), name="static")
    return app


def serve(port: int = DEFAULT_PORT):
    import uvicorn
    print(f"triangulate web: http://{HOST}:{port}/  (Ctrl+C to stop)", flush=True)
    uvicorn.run(create_app(), host=HOST, port=port, log_level="warning")

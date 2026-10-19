"""本地网页：发起运行（停在人工确认方向）、看进度、看任何一次保存的运行、回测表。

启动：.venv/Scripts/python.exe -m triangulate serve [--port 8770]，只绑定 127.0.0.1。
浏览保存的运行完全离线；发起新运行需要 key 文件（TRIANGULATE_KEY_FILE）和网络。前端是 static/ 里的原生 HTML + JS，没有构建步骤。
"""
from pathlib import Path

from fastapi import Body, FastAPI, HTTPException, Query
from fastapi.responses import FileResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.trustedhost import TrustedHostMiddleware

from ..agent.outputs import dep_graph
from ..agent.run import RES
from . import results as R
from .runs import BadState, Busy, Registry

STATIC = Path(__file__).resolve().parent / "static"
HOST = "127.0.0.1"
DEFAULT_PORT = 8770
FILES = {"graph.html": "text/html; charset=utf-8", "ledger.md": "text/plain; charset=utf-8"}


def create_app(registry: Registry | None = None, res: Path = RES, allowed_hosts=("127.0.0.1", "localhost")) -> FastAPI:
    app = FastAPI(title="triangulate-agent", docs_url=None, redoc_url=None, openapi_url=None)
    # 只认本机的 Host 头（挡 DNS rebinding）；POST 只收 application/json（FastAPI 默认），别的网页不能用表单替你开运行
    app.add_middleware(TrustedHostMiddleware, allowed_hosts=list(allowed_hosts))
    reg = registry or Registry()
    app.state.registry = reg

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

    # ---------- 网页运行 ----------
    @app.post("/api/runs")
    def start_run(body: dict = Body(...)):
        try:
            run = reg.start(body.get("question", ""), body.get("as_of"))
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
        try:
            run.approve(keep)
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

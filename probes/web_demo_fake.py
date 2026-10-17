"""网页演示服务（假模型、假搜索、假网页；不联网、不调模型、不花钱）：用来在浏览器里走一遍控制台的完整流程。

用法：.venv/Scripts/python.exe probes/web_demo_fake.py [端口，默认 8773]
打开 http://127.0.0.1:8773/verrier#console 提问（任意问题）→ 停在人工确认 → 批准 → 进度 → 结果。
结果写进临时目录（不碰 results/）；假组件来自 tests/test_web.py，每次模型调用和取页多等一会儿，进度才看得见。
"""
import sys
import tempfile
import time
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tests import test_web as TW  # noqa: E402
from triangulate.agent import graph as G  # noqa: E402
from triangulate.agent import pipeline as P  # noqa: E402
from triangulate.web.app import HOST, create_app  # noqa: E402
from triangulate.web.runs import Registry  # noqa: E402

DELAY_S = 1.2
ROLE_DELAY_S = {"plan": 5.0, "judge": 3.0, "final": 2.0}   # 按角色多等一会儿，接近真实运行的节奏（真实的 plan 约 13 s）


class SlowLLM(TW.FakeLLM):
    def ask(self, system, user, *, role, qid, **k):
        time.sleep(next((v for r, v in ROLE_DELAY_S.items() if role.startswith(r)), DELAY_S))
        return super().ask(system, user, role=role, qid=qid, **k)


class SlowSearcher(TW.FakeSearcher):
    def search(self, *a, **k):
        time.sleep(DELAY_S)
        return super().search(*a, **k)


def slow_fetch(url, as_of, qid, **kw):
    time.sleep(DELAY_S / 2)
    return TW.fake_fetch(url, as_of, qid, **kw)


def main(port: int = 8773):
    import uvicorn
    tmp = Path(tempfile.mkdtemp(prefix="verrier_demo_"))
    base = TW.make_prepare(tmp)

    def prepare(q, tag=""):
        h = base(q, tag)
        h["ctx"].llm, h["ctx"].searcher = SlowLLM(), SlowSearcher()
        h["g"] = G.build(h["ctx"])
        return h

    with mock.patch.object(P, "fetch_page", slow_fetch), \
            mock.patch.object(G, "search_markets", lambda k, a: {"keywords": k, "markets": [], "points": [], "note": "demo: no markets"}):
        print(f"verrier demo (fake model, results in {tmp}): http://{HOST}:{port}/verrier#console", flush=True)
        uvicorn.run(create_app(Registry(prepare=prepare), res=tmp), host=HOST, port=port, log_level="warning")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 8773)

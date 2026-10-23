"""网页演示服务（假模型、假搜索、假网页；不联网、不调模型、不花钱）：用来在浏览器里走一遍控制台的完整流程。

用法：.venv/Scripts/python.exe probes/web_demo_fake.py [端口，默认 8773]
打开 http://127.0.0.1:8773/verrier#console 提问（任意问题）→ 停在人工确认 → 批准 → 进度 → 结果。
结果写进临时目录（不碰 results/）；假组件来自 tests/test_web.py，每次模型调用和取页多等一会儿，进度才看得见。
web-v0.9：表单要选 provider / 模型、填 key。这里任何 key（8–512 个可打印 ASCII 字符，同真实的格式检查）都接受：
「校验 key」换成不发请求、总是通过的假校验；运行用假模型，不管选了哪家。key 照真实路径只留在这次运行的内存里，结束就清掉。
v2.11f：也走一遍现成数据前置步骤（真实使用的开关 check_published 打开）：前置搜索的那一页有一个 13 位的第三方估计，判定模型认它
是 estimate，人工确认里多一个「用这个数」（选用后结果页的大数字就是它；13 位用来看 fitBig 的缩放）。问题的 as_of 要不早于 2026-06-30。
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


EXISTING_URL = "https://analyst.example.org/widgets-june-2026"
EXISTING_QUOTE = "Analysts estimate that 1,234,567,890,123 widgets were sold in June 2026."
EXISTING_POINT = {"name": "Analyst estimate of widgets sold, June 2026", "value_as_written": "1,234,567,890,123", "unit": "widgets",
                  "period_start": "2026-06-01", "period_end": "2026-06-30", "quote": EXISTING_QUOTE}


class SlowLLM(TW.FakeLLM):
    def ask(self, system, user, *, role, qid, **k):
        time.sleep(next((v for r, v in ROLE_DELAY_S.items() if role.startswith(r)), DELAY_S))
        if role == "extract:existing":   # v2.11f：前置步骤那一页的点
            return {"points": [EXISTING_POINT]}, None
        if role == "existing:published":
            return {"candidates": [{"id": "x1", "verdict": "different", "reason": "demo: an analyst estimate"}]}, None
        if role == "existing:check":
            return {"matches": [{"id": "x1", "label": "estimate", "reason": "demo: an estimate of the target itself"}]}, None
        return super().ask(system, user, role=role, qid=qid, **k)


class SlowSearcher(TW.FakeSearcher):
    def search(self, *a, **k):
        time.sleep(DELAY_S)
        if k.get("role") == "existing:search":
            return {"queries": ["widgets June 2026 estimate"], "urls": [EXISTING_URL], "web_search_requests": 1}
        return super().search(*a, **k)


def slow_live(url, as_of, qid, **kw):   # v2.11f：前置步骤直接抓 live 页（同真实使用）
    time.sleep(DELAY_S / 2)
    return {"url": url, "status": "live_dated", "snapshot_ts": None, "page_date": "2026-07-15",
            "text": "Widget market note, July 2026. " + EXISTING_QUOTE}


def slow_fetch(url, as_of, qid, **kw):
    time.sleep(DELAY_S / 2)
    return TW.fake_fetch(url, as_of, qid, **kw)


def fake_check_key(spec) -> dict:
    """假的「校验 key」：不发任何请求，什么 key 都接受（形状同 llm.check_key 的返回，不含 key）。"""
    return {"provider": spec.provider, "model": spec.model, "ok": True, "status": 200, "model_listed": True, "n_models": 1,
            "message": f"demo: the fake {spec.adapter.label} server accepts any key (no request was sent)"}


def main(port: int = 8773):
    import uvicorn
    tmp = Path(tempfile.mkdtemp(prefix="verrier_demo_"))
    base = TW.make_prepare(tmp)

    def prepare(q, tag="", spec=None):
        h = base(q, tag, spec=spec)
        h["ctx"].llm, h["ctx"].searcher = SlowLLM(), SlowSearcher()
        h["ctx"].check_published = True   # v2.11f：真实使用的开关（假的 ctx 没有它），前置步骤才会跑
        h["g"] = G.build(h["ctx"])
        return h

    with mock.patch.object(P, "fetch_page", slow_fetch), mock.patch.object(P, "fetch_live", slow_live), \
            mock.patch.object(G, "search_markets", lambda k, a: {"keywords": k, "markets": [], "points": [], "note": "demo: no markets"}):
        print(f"verrier demo (fake model, results in {tmp}): http://{HOST}:{port}/verrier#console", flush=True)
        uvicorn.run(create_app(Registry(prepare=prepare), res=tmp, key_checker=fake_check_key), host=HOST, port=port,
                    log_level="warning")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 8773)

"""v2.8o 探针：真实模型做数的核对（value_check.VALUE_CHECK_*），固定用例，每个跑 REPEATS 次。
应为 true 的读数（单词、分数、百分数、倍数词、区间、中文数词、表头倍数；倍数词由代码从写法里去掉）和故意读错的（大 10 倍、倍数漏了 / 重复、区间读成一个数）
都要判对。结果写进 probes/out/value_check/probe.json。"""
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from triangulate.agent import evidence as ev  # noqa: E402
from triangulate.agent import value_check as VC  # noqa: E402
from triangulate.agent.pipeline import AgentLLM, Budget  # noqa: E402

OUT = ROOT / "probes" / "out" / "value_check"
REPEATS = 3
NHANES = "Overall, males had four and females had three slices of pizza (see definition of a slice, p.8) at an eating occasion"
CASES = [  # (期望, value_as_written, scale_word, reading, quote)
    (True, "four", "", {"number": 4}, NHANES),
    (True, "three", "", {"number": 3}, NHANES),
    (True, "1/6", "", {"number": 0.16667}, "One slice of pizza is approximately 1/6 of 14-inch fast food/restaurant cheese pizza"),
    (True, "11%", "", {"number": 11}, "On any given day, pizza was consumed by 11% of the population overall"),
    (True, "4.8 million", "million", {"number": 4.8}, "Shipments reached 4.8 million cases in 2024"),
    (True, "4.8 million", "", {"number": 4.8}, "Shipments reached 4.8 million cases in 2024"),   # 倍数由代码从写法里取
    (True, "3-4", "", {"low": 3, "high": 4}, "An estimated 3-4 slices are eaten per occasion by adolescents"),
    (True, "two-thirds", "", {"number": 0.66667}, "two-thirds of adults ate pizza at least once a month"),
    (True, "one-quarter", "", {"number": 0.25}, "about one-quarter was from grocery stores"),
    (True, "a dozen", "", {"number": 12}, "the shop sells a dozen pies an hour"),
    (True, "三百", "", {"number": 300}, "目前在全国共有三百家门店"),
    (True, "4,774.10", "万", {"number": 4774.1}, "外贸 4,774.10 8.37% 5,201.33"),
    (True, "519万548", "", {"number": 5190548}, "人口为519万548人"),
    (True, "12", "", {"number": 12}, "The chain opened 12 stores"),
    (False, "four", "", {"number": 40}, NHANES),
    (False, "three", "", {"number": 4}, NHANES),
    (False, "one-quarter", "", {"number": 0.26}, "about one-quarter was from grocery stores"),
    (False, "4.8 million", "million", {"number": 4800000}, "Shipments reached 4.8 million cases in 2024"),
    (False, "4.8 million", "", {"number": 4800000}, "Shipments reached 4.8 million cases in 2024"),   # 代码再乘 million 就重复了
    (False, "3-4", "", {"number": 3.5}, "An estimated 3-4 slices are eaten per occasion by adolescents"),
    (False, "3-4", "", {"low": 3, "high": 5}, "An estimated 3-4 slices are eaten per occasion by adolescents"),
    (False, "11%", "", {"number": 0.11}, "On any given day, pizza was consumed by 11% of the population overall"),
    (False, "1/6", "", {"number": 0.125}, "One slice of pizza is approximately 1/6 of 14-inch fast food/restaurant cheese pizza"),
    (False, "三百", "", {"number": 3000}, "目前在全国共有三百家门店"),
    (False, "4,774.10", "万", {"number": 477410}, "外贸 4,774.10 8.37% 5,201.33"),
    (False, "two-thirds", "", {"number": 0.5}, "two-thirds of adults ate pizza at least once a month"),
    (False, "12", "", {"low": 12, "high": 13}, "The chain opened 12 stores"),
]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    llm = AgentLLM(OUT / "calls.jsonl", Budget(usd=2.0))
    jobs = [(i, k) for i in range(len(CASES)) for k in range(REPEATS)]

    def one(job):
        i, k = job
        want, vw, sw, reading, quote = CASES[i]
        p = {"id": f"p{i + 1}", "quote": quote, "value_as_written": vw, "scale_word": sw}
        try:   # 代码先查（区间写法、倍数冲突）；代码就拒的不调用模型，记为 false
            ev.read_reading(reading, vw, sw)
        except ValueError as e:
            return {"case": i + 1, "repeat": k + 1, "want": want, "got": False, "error": f"code: {e}"}
        got, err = VC._match(llm, f"probe{k}", p, reading)
        return {"case": i + 1, "repeat": k + 1, "want": want, "got": got, "error": err}

    with ThreadPoolExecutor(8) as ex:
        rows = list(ex.map(one, jobs))
    (OUT / "probe.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    bad = [r for r in rows if r["got"] is not r["want"]]
    for i, (want, vw, sw, reading, _) in enumerate(CASES):
        gots = [r["got"] for r in rows if r["case"] == i + 1]
        mark = "ok " if all(g is want for g in gots) else "BAD"
        print(f"{mark} case {i + 1:2} want {str(want):5} got {gots}  {vw!r} sw={sw!r} reading={json.dumps(reading)}")
    print(f"\n{len(rows) - len(bad)}/{len(rows)} judged as expected; usd {llm.budget.usd_spent():.4f}" if hasattr(llm.budget, "usd_spent")
          else f"\n{len(rows) - len(bad)}/{len(rows)} judged as expected")


if __name__ == "__main__":
    main()

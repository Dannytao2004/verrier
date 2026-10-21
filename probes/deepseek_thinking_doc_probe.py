"""v2.10f 探针（不带 key、不花钱）：取 DeepSeek Thinking Mode 文档页的 HTML，原样打印里面的表格（单元格的 colspan / rowspan 一起打）。
用途：核实 Anthropic 兼容接口里关思考的字段名。WebFetch 的摘要分不清这张表的列；页面 HTML 里开关那一格 colspan=2，横跨 OpenAI 和 Anthropic
两种格式：{"thinking": {"type": "enabled/disabled"}}；Anthropic 格式的深度是 {"output_config": {"effort": ...}}（2026-10-21 运行结果见 PROVIDERS.md 14.6）。
用假 key 直接调接口核实不了：鉴权先失败（401），看不到字段是否被接受。

用法：.venv/Scripts/python.exe probes/deepseek_thinking_doc_probe.py
"""
import html
import re
import urllib.request

URL = "https://api-docs.deepseek.com/guides/thinking_mode"


def main():
    req = urllib.request.Request(URL, headers={"User-Agent": "triangulate-agent docs probe"})
    with urllib.request.urlopen(req, timeout=30) as r:   # 文档站会 302 到同一路径，urllib 跟随（GET、不带 key）
        page = r.read().decode("utf-8", "replace")
    for table in re.findall(r"<table.*?</table>", page, re.S):
        for row in re.findall(r"<tr.*?</tr>", table, re.S):
            cells = re.findall(r"<t[hd]([^>]*)>(.*?)</t[hd]>", row, re.S)
            print(" | ".join((a.strip() + ": " if a.strip() else "") + html.unescape(re.sub(r"<[^>]+>", "", c)).strip()
                             for a, c in cells))
        print("-----")
    for line in re.findall(r"[^<>]*(?:enabled by default|default effort)[^<>]*", page):
        print(html.unescape(line).strip())


if __name__ == "__main__":
    main()

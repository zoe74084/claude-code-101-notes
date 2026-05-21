#!/usr/bin/env python3
"""Replace non-Taiwan tech terms with Taiwan-standard equivalents in all handout files."""

import os, re

BASE = "/Users/ding/Desktop/Claude code 101/handouts"

# Ordered replacements (more specific first to avoid double-replacement)
REPLACEMENTS = [
    # 編程 → 程式設計
    ("Agentic 編程工具",           "Agentic 程式設計工具"),
    ("代理式編程工具",              "代理式程式設計工具"),
    ("編程工具",                    "程式設計工具"),
    ("編程",                        "程式設計"),

    # 技術棧 → 技術堆疊
    ("Tech Stack 技術棧",           "Tech Stack 技術堆疊"),
    ("技術棧、",                    "技術堆疊、"),
    ("技術棧說明",                  "技術堆疊說明"),
    ("技術棧",                      "技術堆疊"),

    # 腳本 → 指令稿（shell/script 語境，非劇本）
    ("執行建置腳本",                "執行建置指令稿"),
    ("自訂腳本",                    "自訂指令稿"),

    # 工作流（未接「程」）→ 工作流程
    ("工作流中",                    "工作流程中"),
    ("工作流的",                    "工作流程的"),

    # 子代理 → 子代理程式（不重複替換已有「程式」的）
    ("子代理程式",                  "子代理程式"),   # passthrough to protect existing correct form
    ("子代理</td>",                 "子代理程式</td>"),
    ("子代理，",                    "子代理程式，"),
    ("子代理：",                    "子代理程式："),
    ("子代理（",                    "子代理程式（"),
    ("Sub Agent | 子代理 |",        "Sub Agent | 子代理程式 |"),
    ("Sub Agent</td><td>子代理</td>","Sub Agent</td><td>子代理程式</td>"),

    # 服務商托管 → 服務商代管
    ("服務商托管",                  "服務商代管"),
]

def apply_replacements(text):
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    return text

exts = (".html", ".md")
changed = []

for fname in sorted(os.listdir(BASE)):
    if not any(fname.endswith(e) for e in exts):
        continue
    path = os.path.join(BASE, fname)
    with open(path, encoding="utf-8") as f:
        original = f.read()
    updated = apply_replacements(original)
    if updated != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(updated)
        changed.append(fname)
        print(f"  updated: {fname}")
    else:
        print(f"  no change: {fname}")

print(f"\nDone. {len(changed)} files updated.")

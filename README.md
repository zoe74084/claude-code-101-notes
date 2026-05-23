# Claude Code 101 學習筆記

整理自 [Claude Youtube 官方頻道課程 Claude-Code-101](https://youtube.com/playlist?list=PLmWCw1CzcFilebjK89WLb5cAvM8K0cLB3&si=6K86NWePoZl9vmu5)，共 9 堂課。

## 閱讀方式

| 格式 | 連結 |
|------|------|
| 網頁版（GitHub Pages） | https://zoe74084.github.io/claude-code-101-notes/ |
| PDF 下載 | [handouts/Claude-Code-101-notes.pdf](handouts/Claude-Code-101-notes.pdf) |
| Markdown 純文字 | [handouts/Claude-Code-101-notes.md](handouts/Claude-Code-101-notes.md) |

## 課程內容

| # | 主題 |
|---|------|
| 01 | What is Claude Code? — 定義、Agentic Loop、Tools、Context Window |
| 02 | Installing Claude Code — 各平台安裝方式與指令速查 |
| 03 | How Claude Code Works — 代理循環、工具呼叫、Permission Modes |
| 04 | Your First Claude Code Prompt — Prompt 寫法、Plan Mode、Auto Accept |
| 05 | The CLAUDE.md File — 專案設定檔結構與使用方式 |
| 06 | Explore → Plan → Code → Commit — 標準工作流程 |
| 07 | Context Management — 情境視窗管理與 Compaction |
| 08 | MCP — 整合外部工具的方式 |
| 09 | Hooks in Claude Code — 事件驅動的確定性自動化 |

## 延伸學習

- [官方入門課程 Claude Code 101 — Anthropic Skilljar](https://anthropic.skilljar.com/claude-code-101)（官方認證課程，完成後可取得證照）
- [Claude Code 官方文件](https://code.claude.com/docs/en/overview)

## 檔案結構

```
├── index.html          # 網頁版（GitHub Pages 服務）
├── handouts/
│   ├── *.pdf           # PDF 版（含筆記欄）
│   └── *.md            # Markdown 純文字版
└── _dev/
    ├── build_pdf.py    # PDF 產生器（Chrome headless）
    └── fix_terms.py    # 台灣用語批次替換
```

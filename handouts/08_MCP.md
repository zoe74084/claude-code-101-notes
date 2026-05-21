# 08 | MCP in Claude Code  MCP 整合外部工具

---

## 本節重點 Key Takeaways

1. **MCP（Model Context Protocol）** = 讓 Claude Code 連接外部工具與資料來源的開放標準。
2. 兩種 server 類型：**HTTP**（遠端服務）、**stdio**（本機程式）。
3. 三種 scope：local（本機本專案）、user（個人跨專案）、project（MCP.json，團隊共用）。
4. MCP server 的工具定義**佔用 context window**，不用的要停用。
5. 工具佔用超過 10% context 時，Claude 自動切換 **tool search mode**（效果較差）。

---

## 兩種 MCP Server 類型

| 類型 | 連接方式 | 範例 |
|------|----------|------|
| HTTP Server | 遠端服務，透過網路連接 | Notion、GitHub、Linear |
| stdio Server | 本機程式，在你的電腦上執行 | 本地資料庫、自訂程式化腳本 |

---

## 三種 Scope（作用範圍）

```
Local（本機本專案）       → 只有你，只在這個專案
User（使用者）            → 只有你，所有專案都能用
Project（專案級）         → 整個團隊共用（透過 .mcp.json）
```

---

## 常用 MCP 操作

```bash
# 新增 MCP server
claude mcp add [server-name]

# 在 session 內管理 servers
/mcp                        # 查看連接狀態、停用不用的 server
```

---

## 何時用 MCP，何時用 CLI？

| 情境 | 建議 |
|------|------|
| GitHub 操作 | 用 `gh` CLI（更節省 context） |
| AWS 操作 | 用 `aws` CLI（更節省 context） |
| 沒有 CLI 的服務（Notion、Linear）| 用 MCP server |
| 需要跨 session 持久配置 | 用 project scope + `.mcp.json` |

---

## 推薦 MCP Server 範例

| MCP Server | 用途 |
|------------|------|
| Linear | 拉取專案管理 issue 詳情 |
| Context7 | 取得最新依賴套件文件 |
| claude.com/connectors | 數百種連接器可選 |

---

## 關鍵詞彙 Vocabulary

| 英文 | 中文 | 說明 |
|------|------|------|
| MCP | Model Context Protocol | 連接外部工具的開放標準 |
| HTTP Server | HTTP 伺服器 | 遠端服務提供的 MCP server |
| stdio Server | 標準 I/O 伺服器 | 在本機執行的 MCP server |
| Scope | 作用範圍 | local / user / project 三種設定層級 |
| Tool Search Mode | 工具搜尋模式 | 工具太多時的自動備用模式（效果較差） |
| .mcp.json | — | 存放 project scope MCP 設定的檔案 |

---

## 我的筆記 My Notes

&nbsp;

___

___

___

___

___

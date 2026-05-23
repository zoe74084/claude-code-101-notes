# Claude Code 101 學習筆記

整理自 [Claude 官方 YouTube 課程](https://youtube.com/playlist?list=PLmWCw1CzcFilebjK89WLb5cAvM8K0cLB3)

---

# 01 | What is Claude Code？什麼是 Claude Code？

---

## 本節重點 Key Takeaways

1. Claude Code 是 **Agentic 程式設計工具**，可直接存取你的檔案、終端機與程式碼庫，不需要複製貼上。
2. 與 Claude AI 的差異：Claude Code 能「自己進去做事」，而非只輸出文字讓你自己操作。
3. **AI Agent** = 能與環境互動、自主執行行動來達成目標的軟體。
4. **Context Window（情境視窗）** = Claude 的工作記憶，有容量上限，無法存放所有內容。
5. 預設行為：執行操作前會詢問許可；Claude Code 並非完美，可能誤解意圖或引入錯誤。

---

## 核心概念 Core Concepts

### Agentic Loop 代理循環
Claude Code 運作方式：接收 prompt → 收集情境 → 呼叫模型 → 執行行動 → 驗證結果 → 若未達標則循環重試。

### Tools 工具
讓 Agent 能「做事」的能力模組，例如讀取檔案、搜尋網頁、執行建置程式化腳本等。

### Context Window 情境視窗
Claude 的工作記憶，存放對話記錄、檔案內容、指令輸出等。容量有限，需策略性管理。

---

## 關鍵詞彙 Vocabulary

| 英文 | 中文 | 說明 |
|------|------|------|
| Agentic Coding Tool | 代理式程式設計工具 | 能自主執行多步驟任務的 AI 工具 |
| AI Agent | AI 代理 | 能與環境互動、執行行動來完成目標的軟體 |
| Context Window | 情境視窗 | Claude 的工作記憶，存放對話、檔案等內容 |
| Permission Mode | 許可模式 | 控制 Claude 執行操作前是否需要詢問確認 |
| Tools | 工具 | 讓 Agent 執行程式碼、搜尋等行動的功能模組 |
| Codebase | 程式碼庫 | 整個專案的程式碼集合 |

---

## 可用平台 Platforms

- **Terminal（終端機）** — 功能最完整，功能最快上線
- **VS Code** — 與編輯器整合
- **JetBrains IDEs** — 與 IDE 整合
- **Claude Desktop** — 適合背景執行
- **Claude.ai/code（Web）** — 可在瀏覽器直接執行任務，不限 GitHub；支援桌面瀏覽器與 iOS app

---

## 我的筆記 My Notes

&nbsp;

___

___

___

___

___

---

# 02 | Installing Claude Code 安裝 Claude Code

---

## 本節重點 Key Takeaways

1. **Mac/Linux/WSL**：用 `curl` 指令安裝（支援自動更新）；Homebrew 可用但**不自動更新**。
2. **Windows**：PowerShell `Invoke-RestMethod`、`curl` 或 `winget`（winget 不自動更新）。
3. 啟動方式：進入專案目錄後執行 `claude`，首次需設定色彩主題並登入帳號。
4. Claude 可存取你執行指令的目錄及其**所有子資料夾**。
5. 帳號類型：Pro、Max、Enterprise（選擇組織帳號）或 API Key 皆可。

---

## 安裝指令速查 Install Commands

### Mac / Linux / WSL
```bash
# 推薦（支援自動更新）
curl -fsSL https://claude.ai/install.sh | sh

# Homebrew（不自動更新）
brew install --cask claude-code
```

### Windows
```powershell
# PowerShell
Invoke-RestMethod -Uri https://claude.ai/install.ps1 | Invoke-Expression

# cmd / curl
curl -fsSL https://claude.ai/install.bat -o install.bat && install.bat
```

---

## 各平台安裝方式 Platform Setup

| 平台 | 步驟 | 備註 |
|------|------|------|
| Terminal | `claude` 啟動 | 功能最完整 |
| VS Code | Extensions → 搜尋 "Claude Code" → Anthropic（藍色勾選）| 可能需重啟 |
| JetBrains | JetBrains Marketplace → 安裝後重啟 | 側邊欄可見 Claude logo |
| Desktop | 安裝 Claude Desktop 後，頂部切換 "Code" 分頁 | 適合背景執行 |
| Web | claude.ai/code | 可在瀏覽器直接執行任務，不限 GitHub；支援桌面瀏覽器與 iOS app |

---

## 關鍵詞彙 Vocabulary

| 英文 | 中文 | 說明 |
|------|------|------|
| Auto Update | 自動更新 | 安裝後自動取得最新版本 |
| Project Directory | 專案目錄 | 你要讓 Claude 操作的資料夾 |
| API Key | API 金鑰 | 無帳號時可用此方式驗證身份 |

---

## 我的筆記 My Notes

&nbsp;

___

___

___

___

___

---

# 03 | How Claude Code Works  Claude Code 如何運作

---

## 本節重點 Key Takeaways

1. **Agentic Loop（代理循環）**：Prompt → 收集情境 → 呼叫模型 → 執行行動 → 驗證結果 → 未達標則循環。
2. **Tools（工具）** 是 Agent 的核心骨架，讓 Claude 能「做事」而非只輸出文字。
3. 情境視窗接近上限時，Claude 會自動 **compact（壓縮）**，可能遺失部分細節。
4. 三種許可模式：預設（每次詢問）、Auto Accept（自動接受編輯）、Plan Mode（唯讀規劃）。
5. Claude Code 使用**語意搜尋（Semantic Search）** 判斷何時該呼叫哪個工具。

---

## Agentic Loop 代理循環

```
使用者輸入 Prompt
       ↓
收集所需情境 (Context)
       ↓
呼叫 LLM（回傳文字或工具呼叫）
       ↓
執行行動（編輯檔案、執行指令...）
       ↓
驗證結果
       ↓
 達標？ → Yes → 等待下一個 Prompt
         → No  → 回到循環頂端
```

---

## 三種許可模式 Permission Modes

| 模式 Mode | 說明 | 切換方式 |
|-----------|------|----------|
| Default 預設 | 每次操作（編輯檔案、執行指令）前詢問許可 | 預設狀態 |
| Auto Accept 自動接受 | 自動接受檔案編輯；執行指令仍需確認 | Shift + Tab |
| Plan Mode 規劃模式 | 僅唯讀工具，先規劃再執行 | Shift + Tab |

---

## 關鍵詞彙 Vocabulary

| 英文 | 中文 | 說明 |
|------|------|------|
| Agentic Loop | 代理循環 | Claude 自主執行任務的反覆循環機制 |
| Tool Call | 工具呼叫 | Claude 決定使用特定工具（如讀檔）的行動 |
| Compaction | 壓縮 | 情境視窗接近上限時，自動摘要舊內容釋放空間 |
| Semantic Search | 語意搜尋 | 根據語義判斷何時呼叫哪個工具 |
| Verification | 驗證 | Claude 確認執行結果是否達到 prompt 目標 |

---

## 我的筆記 My Notes

&nbsp;

___

___

___

___

___

---

# 04 | Your First Claude Code Prompt  第一個 Prompt

---

## 本節重點 Key Takeaways

1. 用**自然語言**與 Claude Code 對話，如同對人類說話。
2. `Shift + Tab` 切換模式：Auto Accept（自動接受）↔ 手動確認 ↔ Plan Mode。
3. **Plan Mode（規劃模式）**：用唯讀工具分析程式碼庫 → 回傳詳細計畫 → 確認後才執行。
4. Prompt 原則：**越具體越好**，說清楚目標、現有限制、預期結果。
5. Plan Mode 的計畫可以修改後再 Approve，是最佳的「開始執行前修正」節點。

---

## Prompt 寫作技巧 How to Write Good Prompts

| 做 ✅ | 不做 ❌ |
|-------|--------|
| 說明「我需要達成什麼」| 只說「幫我改這個」 |
| 描述現有系統的限制與偏好 | 不說明使用的框架/風格 |
| 指定預期結果的樣子 | 留下模糊的成功標準 |
| 一次聚焦一個目標 | 塞太多功能到一個 prompt |

---

## Plan Mode 使用流程

```
Shift + Tab（進入 Plan Mode）
       ↓
輸入詳細 Prompt（說清楚目標與限制）
       ↓
Claude 分析程式碼庫，返回計畫
       ↓
你審視計畫，確認 / 修改
       ↓
Approve（核准）→ Claude 開始執行
```

---

## 實際案例 Example

**好的 Prompt 範例**：
> "My app needs a dark mode implemented across the entire app. Create a toggle switch on the header that allows user to toggle between light and dark mode. Find a good contrast color that works based on my existing light theme."

**包含了**：目標（dark mode）、位置（header toggle）、限制（配合現有 light theme）

---

## 關鍵詞彙 Vocabulary

| 英文 | 中文 | 說明 |
|------|------|------|
| Plan Mode | 規劃模式 | 唯讀分析，先給計畫再執行 |
| Auto Accept | 自動接受 | 自動核准所有檔案編輯 |
| Approve | 核准 | 確認 Plan Mode 的計畫並開始執行 |
| Prompt | 提示詞 | 你給 Claude 的指令或問題 |

---

## 我的筆記 My Notes

&nbsp;

___

___

___

___

___

---

# 05 | The CLAUDE.md File  CLAUDE.md 檔案

---

## 本節重點 Key Takeaways

1. **CLAUDE.md = Claude Code 的持久記憶**，每次 session 啟動時自動讀取，不需再重新探索。
2. 沒有 CLAUDE.md 時，Claude 每次都要從頭理解程式碼庫，容易做出假設與錯誤。
3. `/init` 指令：讓 Claude 根據你的程式碼庫自動生成初始 CLAUDE.md。
4. 層級結構：**專案級**（根目錄，團隊共用）> **使用者級**（個人設定，跨所有專案）。
5. 最佳實踐：先不加，觀察需要反覆糾正的地方，再精簡加入。

---

## CLAUDE.md 層級 Hierarchy

```
~/.claude/CLAUDE.md          ← 使用者級（個人偏好，跨所有專案）
                                  只有你看得到
                                  
/your-project/CLAUDE.md      ← 專案級（根目錄，check in 版本控制）
                                  整個團隊共用
```

---

## CLAUDE.md 建議填入內容

```markdown
## Tech Stack 技術堆疊
- Next.js 15 (App Router)
- Tailwind CSS
- Drizzle ORM

## Commands 常用指令
- dev: npm run dev
- test: npm test
- lint: npm run lint

## Code Style 程式碼風格
- 2 space indentation
- Named exports only
- API routes → /app/api/

## Rules 規則
- Use server actions instead of API routes
```

---

## 三個使用技巧

1. **糾正 Claude 的行為後**，告訴他：「把這個規則存進 CLAUDE.md」
2. **引用文件**：用 `@檔案路徑` 讓 Claude 參考特定文件
3. **從 `/init` 開始**，然後根據實際需要精簡

---

## 關鍵詞彙 Vocabulary

| 英文 | 中文 | 說明 |
|------|------|------|
| CLAUDE.md | — | Claude Code 的持久記憶設定檔（Markdown 格式） |
| Persistent Memory | 持久記憶 | 跨 session 保留的知識 |
| `/init` | — | 讓 Claude 自動生成 CLAUDE.md 的指令 |
| Project-level | 專案級 | 放在根目錄，整個團隊共用 |
| User-level | 使用者級 | 放在個人設定資料夾，只有自己用 |
| Version Control | 版本控制 | Git 等追蹤程式碼變更的工具 |

---

## 我的筆記 My Notes

&nbsp;

___

___

___

___

___

---

# 06 | Explore → Plan → Code → Commit  核心工作流程

---

## 本節重點 Key Takeaways

1. **核心工作流程**：Explore（探索）→ Plan（規劃）→ Code（編碼）→ Commit（提交）
2. 多數人直接跳到 Code，導致大量事後修正；計畫前才是最佳修正節點。
3. Plan Mode 可同時完成 Explore + Plan，是進入前兩步最快的方式。
4. 給 Claude **可驗證的成功標準**（測試套件、Claude in Chrome），讓他自己確認完成。
5. Commit 前用 sub agent 做 code review，再讓 Claude 生成 commit message。

---

## 工作流程圖

```
Explore（探索）          →  了解程式碼庫現狀
    ↓
Plan（規劃）             →  ✅ 最佳修正節點（計畫確認前）
    ↓
Code（編碼）             →  Claude 執行 + 你 course-correct
    ↓
Commit（提交）           →  Sub agent review → 生成 commit message
    ↓
下一個功能
```

> **備注：名稱差異**
> 本講義依課程影片使用「**Code**」；Anthropic 官方文件（code.claude.com）將同一步驟標示為「**Implement**」。兩者指相同流程，「Implement」語意較廣，泛指所有實作工作——不限於程式設計，修改設定、資料遷移、撰寫文件等皆屬之。

---

## 各步驟操作說明

### Step 1 & 2 — Explore + Plan
進入 Plan Mode（`Shift + Tab`），輸入目標 prompt，Claude 會：
- 讀取相關檔案
- 搜尋必要文件
- 提出問題請你澄清
- 回傳詳細計畫

**審視計畫 → 修改 → Approve**

### Step 3 — Code
- 讓 Claude 持續執行計畫項目
- 隨時 course-correct（調整方向）
- 把反覆發生的修正存進 CLAUDE.md

### Step 4 — Commit
```
1. 用 sub agent 做 code review
2. 讓 Claude 生成 commit message
3. Push → 開始下一個功能
```

---

## 讓 Claude 自我驗證的工具

| 工具 | 用途 |
|------|------|
| 測試套件 (Test Suite) | Claude 跑測試確認功能正確 |
| Claude in Chrome 擴充 | Claude 控制瀏覽器測試 UI |
| Lint / Type Check | 確保程式碼品質 |

---

## 關鍵詞彙 Vocabulary

| 英文 | 中文 | 說明 |
|------|------|------|
| Explore | 探索 | 了解程式碼庫現狀，收集情境 |
| Plan | 規劃 | 生成執行計畫，確認後才動手 |
| Course Correct | 修正方向 | 執行過程中調整 Claude 的做法 |
| Sub Agent | 子代理程式 | 獨立執行特定任務的 Claude 實例 |
| Code Review | 程式碼審查 | 確認程式碼品質與正確性 |
| Commit Message | 提交訊息 | Git commit 的描述文字 |

---

## 我的筆記 My Notes

&nbsp;

___

___

___

___

___

---

# 07 | Context Management  情境視窗管理

---

## 本節重點 Key Takeaways

1. **Context Window = Claude 的工作記憶**，所有輸入、工具執行結果、對話都佔空間。
2. `/compact`：壓縮對話並保留摘要，繼續當前功能開發用。
3. `/clear`：完全清除，開始全新任務或新功能時使用。
4. `/context`：查看目前情境使用狀況、佔用分佈與視覺化圖表。
5. 減少 context 消耗的技巧：提示詞具體、關掉不用的 MCP server、善用 sub agent。

---

## 指令速查 Commands

| 指令 | 用途 | 使用時機 |
|------|------|----------|
| `/compact` | 壓縮對話，保留摘要 | 功能還沒做完，但 context 快滿 |
| `/clear` | 完全清除，從頭開始 | 功能做完，要開始新功能 |
| `/context` | 查看 context 使用狀況 | 想了解哪些東西佔了最多空間 |

---

## 什麼時候用 compact，什麼時候用 clear？

```
還在同一個功能？
  ↓
  Yes → /compact（壓縮，保留摘要繼續工作）
  No  → /clear（清除，全新開始）
```

---

## 減少 Context 消耗的 5 個技巧

1. **提示詞要具體**：模糊 prompt 迫使 Claude 探索更多檔案，消耗更多 context
2. **停用不需要的 MCP server**：每個 server 的工具定義都佔 context
3. **用 sub agent 委派任務**：sub agent 有獨立 context，只回傳摘要給主 agent
4. **把常用規則放進 CLAUDE.md**：不需要 Claude 每次重新探索
5. **定期 `/compact`**：大 session 中途就壓縮，避免自動壓縮遺失細節

---

## 關鍵詞彙 Vocabulary

| 英文 | 中文 | 說明 |
|------|------|------|
| Context Window | 情境視窗 | Claude 的工作記憶容量 |
| Compaction | 壓縮 | 自動或手動摘要舊內容，釋放空間 |
| `/compact` | — | 手動壓縮指令 |
| `/clear` | — | 完全清除情境的指令 |
| Sub Agent | 子代理程式 | 有獨立 context 的 Claude 實例 |
| Token | — | 衡量 context 佔用量的單位 |

---

## 我的筆記 My Notes

&nbsp;

___

___

___

___

___

---

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

---

# 09 | Hooks in Claude Code  Hooks 確定性自動化

---

## 本節重點 Key Takeaways

1. **Hooks = 確定性執行的自動化**，不像 CLAUDE.md 的「建議」，Hooks 每次都一定執行。
2. 常見用途：自動格式化（prettier/gofmt）、記錄指令、封鎖危險操作、完成通知。
3. 設定在 **settings.json**，可 check in 版本控制讓整個團隊共用。
4. Exit code 規則：`0` = 繼續執行，`2` = 阻擋並把 stderr 回傳給 Claude。
5. 「如果某件事必須**每次**都發生 → 放進 Hook，不要放進 prompt 或 CLAUDE.md」。

---

## 5 種 Hook 事件

| 事件 | 觸發時機 |
|------|----------|
| `UserPromptSubmit` | 你送出 prompt 時（Claude 處理前） |
| `PreToolUse` | 工具呼叫**前** |
| `PostToolUse` | 工具呼叫**後** |
| `Notification` | Claude 發送通知時 |
| `Stop` | Claude 完成回應時 |

---

## 最常用 Hook：自動格式化

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|MultiEdit",
        "command": "bash -c 'ext=${TOOL_INPUT_FILE##*.}; case $ext in ts|tsx) prettier --write $TOOL_INPUT_FILE;; go) gofmt -w $TOOL_INPUT_FILE;; py) ruff format $TOOL_INPUT_FILE;; esac'"
      }
    ]
  }
}
```

---

## Exit Code 規則

```
Exit Code 0 → 繼續執行（proceed）
Exit Code 2 → 阻擋（block）
             → stderr 內容回傳給 Claude
             → Claude 知道原因，可以調整
```

---

## 用 PreToolUse 封鎖危險操作範例

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "command": "bash -c 'echo $TOOL_INPUT | grep -q \"rm -rf\" && exit 2 || exit 0'"
      }
    ]
  }
}
```

封鎖 `rm -rf`，Claude 會收到 stderr 訊息並調整指令。

---

## CLAUDE.md vs Hooks 比較

| | CLAUDE.md | Hooks |
|--|-----------|-------|
| 執行方式 | 建議（Claude 決定是否遵循） | 確定性（每次都執行） |
| 適合場景 | 偏好、風格、技術堆疊說明 | 格式化、封鎖操作、通知 |
| 設定位置 | 根目錄 Markdown 檔 | settings.json |
| 可程式化 | 否 | 是（shell script） |

---

## 關鍵詞彙 Vocabulary

| 英文 | 中文 | 說明 |
|------|------|------|
| Hook | 鉤子 | 在特定事件觸發時執行的命令 |
| Deterministic | 確定性的 | 每次都保證執行，無例外 |
| Matcher | 匹配器 | 指定 Hook 作用於哪個工具 |
| Exit Code | 退出碼 | 0=繼續，2=阻擋 |
| settings.json | — | Claude Code 的設定檔 |
| PreToolUse | 工具呼叫前 | 可用來驗證或阻擋某些操作 |
| PostToolUse | 工具呼叫後 | 常用於格式化、記錄 |

---

## 我的筆記 My Notes

&nbsp;

___

___

___

___

___

---
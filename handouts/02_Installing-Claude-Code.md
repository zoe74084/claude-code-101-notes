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

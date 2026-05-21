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

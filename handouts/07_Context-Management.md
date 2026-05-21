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

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

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

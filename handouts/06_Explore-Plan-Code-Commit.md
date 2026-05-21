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

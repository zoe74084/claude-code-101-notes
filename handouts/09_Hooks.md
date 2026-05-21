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

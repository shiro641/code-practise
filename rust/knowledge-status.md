# Rust 学习状态

状态文件用于控制每日 Rust 语法自动化是否推送新内容。

## 规则

- `pending` 表示已推送但尚未确认学完。
- `done` 表示用户已回复 `finish learning`、`学完了`、`完成学习`、`记完了` 或等价表达。
- 每次自动化触发前，先检查本文件。
- 只要存在任意 `pending` 条目，就不要推送新的 Rust 知识点；只提醒用户继续学习最早的 pending 条目。
- 用户确认完成后，更新对应条目为 `done`，并同步更新 PersonalOS habit `每日学习 Rust 常用语法`。

## 当前状态

- 最近完成日期: 2026-06-08
- 当前待完成: 2026-06-09

## 知识点记录

| 日期 | 知识点 | 状态 | 来源代码 | 完成日期 | 备注 |
|---|---|---|---|---|---|
| 2026-06-09 | trait 里的 `impl Future + Send` | pending | `/Users/bytedance/Desktop/codecli/codex-rs/rmcp-client/src/stdio_server_launcher.rs` |  | 已推送，尚未确认学完 |
| 2026-06-10 | `ok_or_else` 和 `?` 的组合 | pending | `/Users/bytedance/Desktop/codecli/codex-rs/lmstudio/src/client.rs` |  | 在新规则建立前已推送 |

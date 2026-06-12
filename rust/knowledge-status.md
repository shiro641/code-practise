# Rust 学习状态

状态文件用于控制 Rust 每日练习助手是否推送新内容，并记录学习进度、优先级和完成状态。

## 规则

- `pending` 表示已推送但尚未确认学完。
- `done` 表示用户已回复 `finish learning`、`学完了`、`完成学习`、`记完了` 或等价表达。
- `planned` 表示进入本周学习计划，但尚未推送。
- `backlog` 表示后续可学，但暂未进入本周计划。
- 每次自动化触发前，先检查本文件。
- 只要存在任意 `pending` 条目，就不要推送新的 Rust 知识点；只提醒用户继续学习最早的 pending 条目。
- 用户确认完成后，更新最早的 `pending` 条目为 `done`，写入完成日期，并同步更新 PersonalOS habit `每日学习 Rust 常用语法`。
- 用户针对某个知识点反复追问时，在“追问次数”中累加，并提高该知识点后续复习/再讲解优先级。
- 本周没学完的 `planned` 或 `pending` 条目，会自动流转到下一周学习计划。
- 每日推送必须包含：知识点具体说明、例子、一道简单练习题。

## 当前状态

- 最近完成日期: 2026-06-08
- 当前待完成: 2026-06-09
- 当前最早 pending: trait 里的 `impl Future + Send`
- 当前周计划文件: `weekly-plan.md`
- 问题与回答日志: `question-log.md`

## 知识点记录

| 日期 | 知识点 | 状态 | 优先级 | 追问次数 | 来源代码 | 完成日期 | 备注 |
|---|---|---|---:|---:|---|---|---|
| 2026-06-09 | trait 里的 `impl Future + Send` | pending | 95 | 0 | `/Users/bytedance/Desktop/codecli/codex-rs/rmcp-client/src/stdio_server_launcher.rs` |  | 已推送，尚未确认学完 |
| 2026-06-10 | `ok_or_else` 和 `?` 的组合 | pending | 90 | 0 | `/Users/bytedance/Desktop/codecli/codex-rs/lmstudio/src/client.rs` |  | 在新规则建立前已推送 |
| 2026-06-12 | ownership 与 move 的基本规则 | planned | 100 | 0 | 自包含示例 |  | 基础、高频，等待 pending 完成后推送 |
| 2026-06-12 | 借用与引用 `&T` / `&mut T` | planned | 99 | 0 | 自包含示例 |  | 基础、高频，等待 pending 完成后推送 |
| 2026-06-12 | `Option` / `Result` 的基础错误处理 | planned | 98 | 0 | 自包含示例 |  | 基础、高频，等待 pending 完成后推送 |

## 优先级规则

优先级分数越高越先学习。每次周日生成周计划时按以下规则调整：

- 基础程度：越简单、越基础，分数越高。
- 常用程度：日常 Rust 代码越常见，分数越高。
- 依赖关系：能帮助理解后续知识点的内容优先。
- 追问次数：用户每追问一次相关知识点，给该知识点或其前置知识点提高优先级。
- 流转规则：上一周没学完的 `pending` 和 `planned` 自动排到下一周前面。

# Rust 每周学习计划

本文件由周日 6:00 自动化维护，用来控制“一周能学完”的 Rust 知识点范围。

## 规则

- 每周日生成或更新本周计划。
- 本周计划优先包含上周未完成的 `pending` / `planned`。
- 每周知识点数量控制在 3 到 5 个。
- 知识点按优先级排序：简单、基础、常用优先；用户反复追问的知识点优先。
- 每日 6:00 只从本周计划中抽取一个未掌握知识点。
- 如果存在 `pending`，每日自动化只提醒继续学习该知识点，不推送新的知识点。
- 推送内容必须循序渐进：每次只引入一个新 Rust 学习目标，示例代码中的其他 Rust 语法必须是已学过内容。

## 当前周计划：2026-W27

周期：2026-06-29 至 2026-07-05

本次生成日期：2026-06-28。恢复状态时优先采用 `knowledge-status.md`：最近完成日期为 2026-06-27，当前没有 `pending`，`struct` 字段与配置对象已完成。因此本周不流转未完成的 `pending`，而是从 backlog 中选择 3 个前置已满足、且能直接服务 Codex CLI 入口阅读链的 ready 条目。考虑到本周主题开始从基础错误处理过渡到“类型与命令入口”，概念密度高于上周，因此本周控制为 3 项，不额外塞入 `Vec<T>`、`async` 或共享状态主题。

| 顺序 | 知识点 | 状态 | 优先级 | 为什么本周学 |
|---:|---|---|---:|---|
| 1 | `enum` 表示命令和事件分支 | done | 86 | `struct` 已完成后，先补“一个值可以是多种分支之一”的建模方式；它直接对应 Codex CLI 里的 `Subcommand`、`Op`、`EventMsg`，也是后续命令入口理解的最低前置 |
| 2 | `derive` 宏基础：`Debug`、`Clone`、`Parser` | done | 84 | 入口类型上常见 `#[derive(...)]`；先只建立“编译器帮你自动生成常见实现”的直觉，不展开宏展开细节，为后续读 `Parser` 和调试输出做准备 |
| 3 | `clap` 命令行参数解析基础 | done | 72 | 前两项完成后，就可以把 `struct` / `enum` / `derive(Parser)` 串起来，看懂 CLI 如何把命令行参数解析成 Rust 值；这会直接打通 `main.rs` 的入口阅读路径 |

## 前置关系说明

- `struct` 字段与配置对象已在 2026-06-27 完成，因此本周可以自然进入 `enum`，不需要再回退。
- `enum` 先于 `derive`，因为需要先理解“这个类型有多个分支”，再看 `#[derive(Debug, Clone, Parser)]` 给这种类型自动补什么能力。
- `derive` 先于 `clap`，因为 `clap` 当前阶段主要通过 `#[derive(Parser)]`、字段属性和枚举分支来建模命令行；如果先跳到 `clap`，会把“宏做什么”和“命令行解析做什么”绑在一起，概念密度过高。
- `Vec<T>` 与 `HashMap` 虽然很常用，但不是读入口分发链的最小前置，因此继续留在 backlog，等入口链跑通后再进入。
- `Arc<T>`、`Mutex<T>`、`async fn`、channel、`trait` 里的 `impl Future + Send` 仍然依赖更多前置概念，本周不排入计划。

## 流转说明

- 上周结束时 `knowledge-status.md` 中没有未完成的 `pending` 或 `planned`；最近完成项是 2026-06-27 的 `struct` 字段与配置对象。
- 旧版 `weekly-plan.md` 仍保留了“`struct` 为 `pending`”的描述，但这与 `knowledge-status.md` 当前摘要和知识点表冲突。按 state protocol，本次已以 `knowledge-status.md` 为准恢复状态，并重建本周周计划。
- 因此本周实际流转结果是：没有遗留 `pending` 进入新周，只有从 backlog 提升的 3 个 ready 条目进入 `planned`。
- 2026-06-28 用户补充确认昨天已学完 `struct`，因此本次 daily workflow 直接把第 1 项 `enum` 表示命令和事件分支 提升为新的 `pending`；只有在该条目确认完成后，才会继续推送第 2 项。
- 用户已于 2026-06-28 回复“学完了”，第 1 项 `enum` 表示命令和事件分支 已从 `pending` 更新为 `done`。
- 2026-06-29 daily workflow 已将第 2 项 `derive` 宏基础：`Debug`、`Clone`、`Parser` 从 `planned` 提升为新的 `pending`。只有在该条目确认完成后，才会继续推送第 3 项 `clap` 命令行参数解析基础。
- 用户已于 2026-06-30 回复“记完了”，第 2 项 `derive` 宏基础：`Debug`、`Clone`、`Parser` 已从 `pending` 更新为 `done`；下一次 daily workflow 才可推进第 3 项 `clap` 命令行参数解析基础。
- 2026-07-01 daily workflow 已将第 3 项 `clap` 命令行参数解析基础 从 `planned` 提升为新的 `pending`。只有在该条目确认完成后，才会进入下一次周计划或新的 ready 条目。
- 用户已于 2026-07-02 回复“今天的学完了”，第 3 项 `clap` 命令行参数解析基础 已从 `pending` 更新为 `done`；本周 2026-W27 的 3 个计划条目已全部完成。

## backlog 保留说明

- `Vec<T>` 与 `HashMap` 基础：前置满足，但本周优先让入口建模链闭环，避免同周并行两条主线。
- `serde` 序列化与反序列化基础：更适合放在入口链和基础集合之后，再进入协议/配置读取。
- `Arc<T>`、`Mutex<T>`、`async fn`、`tokio::spawn`、channel：都属于异步与共享状态链，必须等类型和入口链更稳定后再排。
- `trait 里的 impl Future + Send`：前置链仍明显不完整，继续保留在 backlog。

## 周日生成清单时的输出要求

周日推送给用户时，输出：

- 本周要学的知识点列表。
- 每个知识点为什么值得学。
- 建议学习顺序。
- 上周未完成内容的流转说明。
- 提醒用户：每日只会在前一个知识点学完后再推送下一个。

## Codex CLI 源码导向路线

从 2026-06-28 的周计划开始，在不改变每日练习约束的前提下，把 `/Users/zhangjie/Desktop/codexcli` 的源码阅读需求作为优先级来源之一。

编排规则：

- 仍然每周只选 3 到 5 个知识点。
- 仍然每天只推送 1 个新 Rust 学习目标。
- 如果存在 `pending`，仍然只提醒继续当前知识点，不推送新的知识点。
- 示例代码优先使用自包含小例子；只有当真实源码片段不引入多个未学概念时，才引用 Codex CLI 源码。
- 每个知识点都要说明它对应 Codex CLI 哪条阅读链路，例如入口分发、会话状态、异步主循环、工具调用、配置协议或 TUI。
- 不直接跳到 `trait 里的 impl Future + Send`、MCP 完整协议、TUI 渲染细节这类高密度主题；先拆成 trait、async、Arc、Mutex、channel、serde 等前置小目标。

推荐阶段：

1. 入口与类型阶段：`struct`、`enum`、`derive`、`clap`。
2. 错误与数据阶段：`anyhow::Result`、集合、`serde`。
3. 共享状态阶段：`Arc<T>`、`Mutex<T>`。
4. 异步流程阶段：`async fn`、`.await`、`tokio::spawn`、channel。
5. 源码流程阶段：读懂 `run_turn`、工具调用流程、TUI 事件循环。

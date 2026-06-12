# Rust 学习问题与回答日志

本文件记录用户在学习某个 Rust 知识点时问过的问题，以及助手给出的回答。后续每日推送必须读取本文件，把相关追问自然融入解释、例子或练习题里。

## 记录规则

- 用户围绕某个知识点提问时，追加一条记录。
- 同时在 `knowledge-status.md` 对应知识点的“追问次数”加 1。
- 如果问题暴露出前置知识薄弱，给前置知识点提高优先级。
- 每次每日推送时，优先复用最近追问过的困惑点来设计例子和练习。

## 已归档问题

### 2026-06-07：`if let` 链 + `let ... else`

问题：

- `Some` 是什么？
- `match` 怎么返回值？
- `let ... else` 的 `else` 为什么必须退出？
- Rust 里不加分号是不是等于提前退出？
- 为什么不能直接写 `let Some(user) = maybe_user;`？

回答摘要：

- `Some` 是 `Option<T>` 的有值分支，`None` 表示没有值。
- `match` 是表达式，会返回命中分支的值，所有分支类型必须一致。
- `let ... else` 的 `else` 块必须让当前流程退出，例如 `return`、`break`、`continue`、`panic!`。
- 不加分号表示代码块返回该表达式的值，但不等于提前退出函数。
- `let Some(user) = maybe_user;` 不行，因为 `Some(user)` 不是一定能匹配成功。

后续融入方式：

- 讲解 `Option` / `Result` 时，继续用 `Some` / `None` 和提前返回做例子。

### 2026-06-08：`filter_map` 和迭代器链

问题：

- `into_iter()` 是什么？
- `|value| value` 是什么？
- 为什么 `Vec` 不能直接用 `filter_map`？

回答摘要：

- `into_iter()` 把集合变成迭代器，通常会消耗原集合。
- `|value| value` 是闭包，表示接收 `value` 并原样返回。
- `Vec` 是容器，`Iterator` 才能使用 `filter_map`、`map`、`filter`、`collect` 等流水线操作。

后续融入方式：

- 讲所有权时，重点解释 `into_iter()` 为什么会消耗集合。
- 讲借用时，对比 `iter()`、`iter_mut()`、`into_iter()`。

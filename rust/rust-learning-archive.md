# Rust 学习会话归档

来源旧线程：`019e9f09-34e6-71d2-82fa-0ade897ca288`

旧线程目录：`/Users/bytedance/Desktop/codecli`

恢复后目录：`/Users/zhangjie/Desktop/code-practise/rust`

新主线程：`019eb617-1421-72b1-a1e3-79044af9c5b3`

自动化 ID：`rust`

Habit：`每日学习 Rust 常用语法`

PersonalOS 仓库：`/Users/zhangjie/Desktop/daily-routine`

## 自动化规则

- 每天北京时间 6:00 触发。
- 每次先读取 `knowledge-status.md`。
- 如果存在 `pending` 条目，不推新知识点，只提醒继续学习最早的 `pending`。
- 如果没有 `pending` 条目，再推送一个新的 Rust 常用语法点。
- 用户回复 `finish learning`、`学完了`、`完成学习`、`记完了` 或等价表达时：
  - 更新 PersonalOS habit：`每日学习 Rust 常用语法`
  - 将 `knowledge-status.md` 中最早的 `pending` 改为 `done`
  - 写入完成日期
  - 总结 git diff

## 当前状态

- 最近完成日期：2026-06-24
- 当前待完成：无
- 最早 pending：无
- 本周计划：当前流转周前 5 项已全部完成；下一次每日推送需等待新的 `planned` 或下周计划生成。

### 2026-06-25：推进 `Option` 到 `Result` 的桥接

恢复状态结果：

- `knowledge-status.md` 中不存在旧的 `pending`。
- `weekly-plan.md` 当前周剩余 `planned` 中，最高优先级且前置已满足的是“`Option` 转 `Result`：`ok_or` 基础”。

处理决定：

- 按每日卡片 workflow，从本周 `planned` 中提升最靠前且 ready 的条目。
- 将“`Option` 转 `Result`：`ok_or` 基础”标记为新的 `pending`。
- 今日只引入一个目标：理解 `ok_or` 会把 `Option` 里的 `Some(v)` 保留为成功值，把 `None` 改造成一个 `Err(...)`，为后续 `ok_or_else` 和 `?` 组合做前置。

状态更新：

- `knowledge-status.md` 当前待完成已更新为“`Option` 转 `Result`：`ok_or` 基础”。
- `weekly-plan.md` 已将该知识点从 `planned` 更新为 `pending`。

完成确认：

- 用户已回复“学完了”，已将“`Option` 转 `Result`：`ok_or` 基础”从 `pending` 更新为 `done`，完成日期 2026-06-25。
- 已按项目规则执行 PersonalOS habit 同步命令，记录 `每日学习 Rust 常用语法` 在 2026-06-25 完成。

今日收获：

- `ok_or` 会把 `Option` 里的 `Some(v)` 转成 `Ok(v)`，把 `None` 转成你提供的 `Err(...)`。
- 这一步把“可能没值”和“可能报错”顺利接起来，后面就能更自然地进入 `ok_or_else`。

### 2026-06-24：切回 `Option` 分支处理

恢复状态结果：

- `knowledge-status.md` 中不存在旧的 `pending`。
- `weekly-plan.md` 当前周剩余 `planned` 中，最高优先级且前置已满足的是“用 `match` 处理 `Option` 的 `Some` / `None`”。

处理决定：

- 按每日卡片 workflow，从本周 `planned` 中提升最靠前且 ready 的条目。
- 将“用 `match` 处理 `Option` 的 `Some` / `None`”标记为新的 `pending`。
- 今日只引入一个目标：看懂 `Option` 如何通过 `match` 分成 `Some(...)` 和 `None` 两种情况分别处理，为后面的 `ok_or` 做准备。

状态更新：

- `knowledge-status.md` 当前待完成已更新为“用 `match` 处理 `Option` 的 `Some` / `None`”。
- `weekly-plan.md` 已将该知识点从 `planned` 更新为 `pending`。

完成确认：

- 用户已回复“学完了”，已将“用 `match` 处理 `Option` 的 `Some` / `None`”从 `pending` 更新为 `done`，完成日期 2026-06-24。
- 已按项目规则执行 PersonalOS habit 同步命令，记录 `每日学习 Rust 常用语法` 在 2026-06-24 完成。

今日收获：

- `Option` 可以通过 `match` 明确拆成 `Some(...)` 和 `None` 两种情况分别处理。
- 后续学习 `ok_or` 时，可以把它理解成“把 `None` 这条分支改造成一个 `Err(...)`”。

## 时间线

### 2026-06-23：完成 `Result` 与 `?` 基础

恢复状态结果：

- `knowledge-status.md` 中不存在旧的 `pending`。
- `weekly-plan.md` 当前周剩余 `planned` 中，最高优先级且前置已满足的是 `Result` 与 `?` 基础。

处理决定：

- 按每日卡片 workflow，将 `Result` 与 `?` 基础 从 `planned` 提升为新的 `pending`。
- 今日只引入一个目标：理解 `?` 在返回 `Result` 的函数里如何把 `Err` 自动向外传递。
- 围绕用户追问，补清了三层判断：`?` 和手写 `match` 的关系、`main` 里能否使用 `?`、`main` 返回 `Err` 时程序会如何结束。

完成确认：

- 用户已回复“记完了”，已将 `Result` 与 `?` 基础 从 `pending` 更新为 `done`，完成日期 2026-06-23。
- 已按项目规则执行 PersonalOS habit 同步命令，记录 `每日学习 Rust 常用语法` 在 2026-06-23 完成。

今日收获：

- `?`：在返回为 `Result` 的函数中，可以通过 `?` 自动把 `Err` 结果向外传递。
- 最外层 `main` 如果遇到 `Err`，会把失败结果交出去，并结束程序。

### 2026-06-22：推进手动传播错误这一步

恢复状态结果：

- `knowledge-status.md` 中不存在 `pending`。
- `weekly-plan.md` 当前周仍有 4 个剩余 `planned`，其中最高优先级且前置已满足的是“返回 `Result` 的函数里手动传播错误”。

处理决定：

- 按每日卡片 workflow，不引入新链路，直接从本周 `planned` 中提升最靠前且 ready 的条目。
- 将“返回 `Result` 的函数里手动传播错误”标记为新的 `pending`。
- 今日教学继续围绕 `Result` 返回值展开，先把 `?` 背后的手动 `match` / `return Err(...)` 看清，再进入 `?`。

状态更新：

- `knowledge-status.md` 当前待完成已更新为“返回 `Result` 的函数里手动传播错误”。
- `weekly-plan.md` 已将该知识点从 `planned` 更新为 `pending`。

完成确认：

- 用户已回复“学完了”，已将“返回 `Result` 的函数里手动传播错误”从 `pending` 更新为 `done`，完成日期 2026-06-22。
- 已按项目规则执行 PersonalOS 同步命令，`每日学习 Rust 常用语法` 已记录到 2026-06-22。

### 2026-06-21：补上 `?` 之前的函数返回值前置课

恢复状态结果：

- `knowledge-status.md` 中不存在 `pending`。
- `weekly-plan.md` 里本周前 7 个条目均已 `done`，没有剩余可直接发送的 `planned`。

处理决定：

- 不直接推送 `Result` 与 `?` 基础，因为它仍会把“函数返回 `Result`”和“`?` 提前返回错误”绑在同一天。
- 继续按低概念密度拆分，先新增 `函数返回 Result<T, E>` 作为今日单一目标。
- 将该条目标记为 `pending`，等用户学完后，再进入 `?` 相关语法。

状态更新：

- `knowledge-status.md` 当前待完成已更新为 `函数返回 Result<T, E>`。
- `weekly-plan.md` 已将该知识点追加为本周第 8 项，并标记为 `pending`。

完成确认：

- 用户已回复“学完了”，已将 `函数返回 Result<T, E>` 从 `pending` 更新为 `done`，完成日期 2026-06-21。
- 已按项目规则执行 PersonalOS 同步命令，`每日学习 Rust 常用语法` 已记录到 2026-06-21。

### 2026-06-20：推进 `match` 处理 `Result`

恢复状态结果：

- `knowledge-status.md` 中不存在 `pending`。
- `weekly-plan.md` 里本周前 6 个条目均已 `done`，没有剩余可直接发送的 `planned`。

处理决定：

- 不直接推送 `Result` 与 `?` 基础，因为它仍同时包含“手动处理分支”和“错误传播语法”两个目标。
- 继续按低概念密度拆分，先新增 `用 match 处理 Result 的 Ok / Err` 作为今日单一目标。
- 将该条目标记为 `pending`，等用户学完后，再进入 `?` 相关语法。

状态更新：

- `knowledge-status.md` 当前待完成已更新为 `用 match 处理 Result 的 Ok / Err`。
- `weekly-plan.md` 已将该知识点追加为本周第 7 项，并标记为 `pending`。

完成确认：

- 用户已回复“学完了”，已将 `用 match 处理 Result 的 Ok / Err` 从 `pending` 更新为 `done`，完成日期 2026-06-20。
- 已按项目规则执行 PersonalOS 同步命令，`每日学习 Rust 常用语法` 已记录到 2026-06-20。

### 2026-06-19：拆分 `Result` 前置课并推送

恢复状态结果：

- `knowledge-status.md` 中不存在 `pending`。
- `weekly-plan.md` 当前周的原 5 个条目均已 `done`，没有可直接晋升的 `planned`。

处理决定：

- 不直接推送原 backlog `Result` 与 `?` 基础，因为它把 `Result` 结构和 `?` 错误传播绑在同一天，概念密度过高。
- 先拆出更基础的 `Result` 的 `Ok` / `Err` 作为单独一课，并加入本周计划。
- 将该条目标记为 `pending`，等待用户学完后再进入后续错误处理语法。

状态更新：

- 用户已确认“学完了”，已将 `Result` 的 `Ok` / `Err` 从 `pending` 更新为 `done`，完成日期 2026-06-19。

用户总结与校正：

- `Result` 用来表示成功 / 失败；`Option` 用来表示有值 / 无值。
- `String` 是拥有字符串数据的类型，通常拥有堆上的字符串内容，不只是“管理一个引用”。
- `str` 是字符串内容本体，通常不单独裸用；`&str` 是对字符串内容的引用，变量本身通常在栈上，指向的数据可能在静态区，也可能在堆上。
- `&'static str` 是生命周期为 `'static` 的 `&str`，常见于字符串字面量。
- `&String` 是对 `String` 的引用；很多时候 Rust 会让 `&String` 自动当成 `&str` 用，但它们不是同一种类型。
- 可以通过 `as_str()` 从 `String` 借出 `&str`；这个 `&str` 不能活得比原来的 `String` 更久，原 `String` 销毁后，借出的 `&str` 不能继续存活。

PersonalOS 同步：

- 已确认当前线程具备 `/Users/zhangjie` 下目标文件写权限。
- 已通过 `personal-execution-skill` 的完成流程同步 PersonalOS：`/Users/zhangjie/Desktop/daily-routine/dailies/2026-06-19.md` 今日 Habit 已勾选，`今日复盘 -> 收获` 已写入 Rust 学习总结。
- 已同步 `/Users/zhangjie/Desktop/daily-routine/state/habits.md`、`logs/execution-log.md` 和 `state/stats.md` 中的完成记录。

### 2026-06-07：创建自动化与 habit

用户请求：

```text
我希望创建一个自动化：每天早上6点，帮我推送一个rust的常用语法让我学习，并在这个项目中截取一段代码作为示例并进行解释。
use skill, add this to my daily plan (as a habit), when I response finish learning, update its status
```

处理结果：

- 创建自动化：`rust`
- 创建 PersonalOS habit：`每日学习 Rust 常用语法`
- 当用户回复学习完成表达时，同步更新 PersonalOS

### 2026-06-07：`if let` 链 + `let ... else`

来源代码：

`/Users/bytedance/Desktop/codecli/codex-rs/rollout-trace/src/reducer/thread.rs`

片段：

```rust
if let Some(event_thread_id) = thread_id.as_deref()
    && let Some(turn) = self.rollout.codex_turns.get(&codex_turn_id)
    && turn.thread_id != event_thread_id
{
    bail!(
        "codex turn end for {codex_turn_id} used thread {event_thread_id}, \
         but the turn belongs to {}",
        turn.thread_id
    );
}

let Some(turn) = self.rollout.codex_turns.get_mut(&codex_turn_id) else {
    bail!("codex turn end for missing turn {codex_turn_id}");
};
```

学习点：

- `if let Some(x) = ...` 用来只在 `Option` 是 `Some` 时取值。
- `if let` 链可以把多个匹配和条件写在同一个判断里。
- `let Some(x) = value else { ... };` 用来做“匹配成功继续，失败提前退出”。
- `bail!(...)` 常用于返回错误。

用户追问与解释：

- `Some` 是 `Option<T>` 的“有值”分支；`None` 表示没有值。
- `match` 是表达式，会返回命中分支的值，所有分支类型必须一致。
- `let ... else` 的 `else` 块必须让当前流程退出，例如 `return`、`break`、`continue`、`panic!`。
- Rust 中“不加分号”表示代码块返回该表达式的值，但不等于提前退出函数。
- `let Some(user) = maybe_user;` 不行，因为 `Some(user)` 不是一定能匹配成功。

完成记录：

- 用户表示“今天的我学完了”
- PersonalOS 已标记 2026-06-07 完成

### 2026-06-08：`filter_map` 和迭代器链

来源代码：

`/Users/bytedance/Desktop/codecli/codex-rs/codex-mcp/src/tools.rs`

片段：

```rust
pub fn declared_openai_file_input_param_names(
    meta: Option<&Map<String, JsonValue>>,
) -> Vec<String> {
    let Some(meta) = meta else {
        return Vec::new();
    };

    meta.get(META_OPENAI_FILE_PARAMS)
        .and_then(JsonValue::as_array)
        .into_iter()
        .flatten()
        .filter_map(JsonValue::as_str)
        .filter(|value| !value.is_empty())
        .map(str::to_string)
        .collect()
}
```

学习点：

- `filter_map` 一边转换，一边过滤掉失败项。
- `JsonValue::as_str` 返回 `Option<&str>`。
- `filter_map(JsonValue::as_str)` 会保留 `Some` 里的字符串，丢掉 `None`。
- `map(JsonValue::as_str)` 会得到 `Iterator<Item = Option<&str>>`。
- `filter_map(JsonValue::as_str)` 会得到 `Iterator<Item = &str>`。

用户练习：

```rust
result = values.filter_map(JsonValue::as_str)
```

纠正：

```rust
let values = vec![Some("a"), None, Some("b")];

let result: Vec<&str> = values
    .into_iter()
    .filter_map(|value| value)
    .collect();
```

也可以写成：

```rust
let result: Vec<&str> = values.into_iter().flatten().collect();
```

补充解释：

- `into_iter()` 把集合变成迭代器，通常会消耗原集合。
- `|value| value` 是闭包，表示接收 `value` 并原样返回。
- `Vec` 是容器，`Iterator` 才能使用 `filter_map`、`map`、`filter`、`collect` 等流水线操作。

完成记录：

- 用户回复“记完了”
- PersonalOS 已标记 2026-06-08 完成

### 2026-06-09：trait 里的 `impl Future + Send`

来源代码：

`/Users/bytedance/Desktop/codecli/codex-rs/rmcp-client/src/stdio_server_launcher.rs`

片段：

```rust
impl Transport<RoleClient> for StdioServerTransport {
    type Error = io::Error;

    fn send(
        &mut self,
        item: TxJsonRpcMessage<RoleClient>,
    ) -> impl Future<Output = std::result::Result<(), Self::Error>> + Send + 'static {
        match &mut self.inner {
            StdioServerTransportInner::Local(transport) => transport.send(item).boxed(),
            StdioServerTransportInner::Executor(transport) => transport.send(item).boxed(),
        }
    }

    fn receive(&mut self) -> impl Future<Output = Option<RxJsonRpcMessage<RoleClient>>> + Send {
        match &mut self.inner {
            StdioServerTransportInner::Local(transport) => transport.receive().boxed(),
            StdioServerTransportInner::Executor(transport) => transport.receive().boxed(),
        }
    }
}
```

学习点：

- trait 方法可以返回 `impl Future<Output = ...>` 来表达异步行为。
- `impl Future` 表示返回某种实现了 `Future` 的具体类型，但调用者不需要知道具体类型。
- `Output = Result<(), Self::Error>` 表示 future 完成后的结果。
- `Send` 表示 future 可以在线程间安全移动。
- `'static` 表示 future 不依赖短生命周期引用。
- `.boxed()` 可以把不同分支返回的 future 统一成同一种 boxed future 类型。

状态：

- pending，尚未确认学完。

### 2026-06-10：`ok_or_else` 和 `?` 的组合

状态文件中已有记录：

```text
2026-06-10 | `ok_or_else` 和 `?` 的组合 | pending
```

状态：

- pending，尚未确认学完。
- 该条目是在新状态规则建立前已推送。

### 2026-06-11：`serde` 的枚举标签序列化

片段：

```rust
#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "snake_case", tag = "type")]
pub enum ToolCallKind {
    Function {
        name: String,
    },
    Custom {
        name: String,
    },
}
```

学习点：

- `Serialize` 表示 Rust 值可以转成 JSON 等格式。
- `Deserialize` 表示 JSON 等格式可以解析回 Rust 值。
- `rename_all = "snake_case"` 会把枚举变体名转成 snake_case。
- `tag = "type"` 表示内部标签枚举，JSON 里会多一个 `type` 字段标识变体。

示例：

```rust
ToolCallKind::Function {
    name: "shell".to_string(),
}
```

大致序列化为：

```json
{
  "type": "function",
  "name": "shell"
}
```

注意：

- 该条是在状态文件有 pending 的情况下推送的，后来恢复规则改为：有 pending 时不再推新知识点。

## 后续建议

建议先补完最早的 pending：

```text
2026-06-09 | trait 里的 impl Future + Send
```

学完后在 Rust 学习线程中回复：

```text
finish learning
```

然后再继续 2026-06-10 的 `ok_or_else` 和 `?`。

### 2026-06-12：升级为 Rust 每日练习助手

用户请求：

```text
请你在这个工作区内，帮我搭建一个简单的rust每日练习助手
```

处理结果：

- 新增运行说明：`rust-practice-assistant.md`
- 新增每周学习计划：`weekly-plan.md`
- 新增问题与回答日志：`question-log.md`
- 扩展 `knowledge-status.md`：
  - 增加 `planned` / `backlog` 状态说明
  - 增加优先级和追问次数
  - 明确 pending 未完成时不推送下一个知识点
  - 明确本周未完成内容自动流转到下一周
- 更新每日自动化：
  - 自动化 ID：`rust`
  - 每天 6:00 触发
  - 有 pending 时只提醒继续学习最早 pending
  - 没有 pending 时从本周计划中抽取下一个 planned 知识点
  - 用户提问时记录问题与回答，并提高追问相关优先级
  - 用户确认学完后更新状态和 PersonalOS habit
- 新增每周自动化：
  - 自动化 ID：`rust-2`
  - 每周日 6:00 触发
  - 生成 3 到 5 个一周可学完的 Rust 知识点
  - 自动流转上周未完成内容

### 2026-06-12：手动触发周清单和日清单

用户请求：

```text
你先触发一次周清单和日清单，由于这周只有两天了，所以周清单的内容需要对应减少
```

处理结果：

- 本周只剩 2026-06-12 和 2026-06-13 两个可学习日。
- 将 `weekly-plan.md` 的当前周计划从 5 个知识点缩减为 2 个：
  - trait 里的 `impl Future + Send`
  - `ok_or_else` 和 `?` 的组合
- 将以下知识点保留为下周自动流转候选：
  - ownership 与 move 的基本规则
  - 借用与引用 `&T` / `&mut T`
  - `Option` / `Result` 的基础错误处理
- 日清单遵守 pending 规则：继续学习最早 pending，不推送新知识点。

### 2026-06-12：重置为循序渐进学习路线

用户反馈：

```text
我希望你在给我rust知识点的时候，遵循循序渐进的原则，即你推送给我的学习任务，除了这次学习目标本身外，其他rust的代码逻辑必须是我已经学过的。
例如这次学习trait 里的 impl Future + Send，里面包含了太多我没学过的东西，这就是不好的例子
你先删除之前pending的任务，我们从头开始
```

处理结果：

- 删除当前学习队列里的旧 pending 阻塞项：
  - trait 里的 `impl Future + Send`
  - `ok_or_else` 和 `?` 的组合
- 旧 pending 没有丢失，已移动到 `backlog`，等待前置知识完成后再学。
- 新学习路线从基础开始：
  - ownership 与 move 的基本规则
  - 借用与引用 `&T`
  - 可变借用 `&mut T`
  - `Option` 的 `Some` / `None`
  - `Result` 与 `?` 基础
- 增加最高优先级教学规则：每次推送只能引入一个新的 Rust 学习目标；示例代码里的其他 Rust 语法必须是用户已经学过的内容。

### 2026-06-13：ownership 与 move 的基本规则

状态：

- 已完成，完成日期：2026-06-13。
- 本次从基础路线重新开始。
- 示例只使用变量绑定、字符串和打印，避免引入未学过的 Rust 概念。

学习目标：

- 理解 Rust 中一个值默认只有一个所有者。
- 理解把 `String` 赋给另一个变量时会发生 move。
- 理解 move 之后，旧变量不能继续使用。

用户总结：

1. 所有权：所有权发生转移后，原变量不可访问。
2. 常用类型：数字、浮点、布尔、字符串字面量 `&str`、字符串 `String`、数组、元组；其中没有实现 `Copy` trait 的，会发生所有权转移。
3. Rust 变量默认不可变，如果想中途修改某个变量，需要显式声明 `mut`。

校正：

- 第 1 条正确。
- 第 2 条大方向正确，但“没有实现 `Copy` 就一定会发生所有权转移”需要加条件：当发生赋值、传参、返回等移动位置时，非 `Copy` 类型通常会 move；如果只是借用 `&T` / `&mut T`，所有权不会转移。
- 第 3 条正确。拼写是“显式声明 `mut`”。

PersonalOS 同步：

- 已更新 habit：`每日学习 Rust 常用语法`。
- 已将校正后的总结记录到 2026-06-13 日报“今日复盘 -> 收获”。
- 后续安排：下一个知识点详细讲 `借用与引用 &T`，先只讲不可变借用，不提前引入 `&mut`。

### 2026-06-14：借用与引用 `&T`

状态：

- 已完成，完成日期：2026-06-14。
- 本次只讲不可变借用 `&T`，不引入 `&mut`。
- 示例只使用已经学过的变量绑定、`String`、`println!`、`{}`、ownership 与 move。

学习目标：

- 理解借用是不拿走所有权，只临时看一下值。
- 理解 `&a` 会创建对 `a` 的不可变引用。
- 理解不可变引用可以读取值，但不能修改值。

用户练习结论：

- `other = &name` 没有拿走所有权，只是借用了 `name`。
- `println!("{}", name)` 可以，因为 `name` 没有失去字符串 `"codex"` 的所有权。

本次追问与收获：

- 借用可以粗略理解成复制一份“指向原值的位置”，但 Rust 引用不是裸地址；引用类型还带有类型信息和借用规则。
- 不可变引用 `&T` 通常是 `Copy`，复制引用不会复制底层数据。
- 普通 `&T` 底层通常保存目标位置；`&String` 常指向栈上的 `String` 结构体，而 `&str` 通常包含字符串数据位置和长度。
- Rust 引用底层通常靠地址/指针值实现；安全性主要来自编译期借用检查。

PersonalOS 同步：

- 已更新 habit：`每日学习 Rust 常用语法`。
- 已将本次收获记录到 2026-06-14 日报“今日复盘 -> 收获”。

### 2026-06-16：`可变借用 &mut T`

状态：

- 已完成，完成日期：2026-06-16。
- 本次只讲 `&mut T` 这个单一目标，不提前展开借用冲突规则。
- 示例继续只使用已经学过的变量绑定、`String`、不可变借用和打印。

学习目标：

- 理解 `&mut T` 表示“临时拿到修改原值的权限”，不是拿走所有权。
- 理解想通过 `&mut` 修改值时，原变量本身也必须是 `mut`。
- 理解“引用变量可重新绑定”和“通过可变借用修改底层值”是两件不同的事。

本次推送设计：

- 复用用户之前“怎样声明可变变量”“Rust 是强类型的吗”“能不能像 C 指针那样改值”的困惑。
- 个性化提醒重点区分：
  - `let mut x = ...` 是让变量绑定的值可改。
  - `let r = &mut x` 是借用阶段拿到独占修改权限。
  - `mut` 不会让变量类型改变。

后续安排：

- 用户确认学完后，再进入“不能同时存在 `&T` 和 `&mut T`”的借用冲突规则。

用户总结与校正：

- 通过 `&mut` 拿到对原变量的可变借用，可以借此修改原变量。
- 可变借用活跃时，不能直接访问原变量。
- 可变借用是独占的，不能和同一值的只读借用同时活跃。

PersonalOS 同步：

- 已执行 habit 完成命令：`每日学习 Rust 常用语法`。
- 已将优化后的总结记录到 2026-06-16 日报“今日复盘 -> 收获”。

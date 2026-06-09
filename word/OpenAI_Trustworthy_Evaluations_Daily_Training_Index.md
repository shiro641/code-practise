# OpenAI Trustworthy Evaluations Daily Training Index

Source PDF: `/Users/bytedance/Downloads/OpenAI_Trustworthy_Evaluations_Deep_Reading_Notes_CN.pdf`

Use this phrase bank in daily vocabulary training, review items, example sentences, and Chinese-to-English exercises. Focus on AI evaluation, safety, validity, and third-party assessment writing.

## Evaluation Core

- claim: 主张、待验证结论，需要 evidence 支持。
- result: 评测输出，如分数、成功率、攻击成功率。
- interpretation: 对结果意义的解释，从 result 推向 claim 的过程。
- provide evidence: 提供证据，正式评测报告常用搭配。
- valid evidence: 能有效支持结论的证据。
- evaluation setup: 评测方案、实验设置。
- evaluation content: 评测任务、任务分布、技能、行为或失败模式。
- tested system: 被测系统，不只是模型名，也包括 tools、harness、safeguards。
- validity checks: 有效性检查，用来判断结果是否真的支持 claim。
- trustworthy interpretation: 可信解释，而不是无可置疑的证明。

## Harness And Agentic Systems

- harness: 模型外部运行框架，包括 prompts、tools、control logic、memory、retries、validators。
- agentic system: 能跨多步使用工具、维护状态、在环境中行动的系统。
- scaffolding: 辅助执行结构，如计划、反思、重试、状态管理。
- tool access: 模型可用的外部工具权限。
- interface: 系统交互方式，不只是 UI。
- stripped-down model interface: 精简模型接口，通常没有工具、记忆或 agent loop。
- trajectory: 任务执行路径、步骤链。
- longer trajectories: 更长的多步骤任务执行过程。

## Elicitation And Capability

- elicitation: 能力或行为激发，通过 prompt、tools、harness、budget 等引出能力。
- capability elicitation: 能力激发，评测模型是否能合理展现某能力。
- strong elicitation: 充分激发。
- maximum elicitation: 在定义预算内寻找最强可信表现或失败模式。
- under-elicitation: 能力激发不足，导致低估真实能力。
- capability ceiling: 能力上限估计。
- lower-bound estimate: 下界估计，不应误读成能力上限。
- plausibly: 合理可能地。
- credible: 现实可信、合理可能。

## Safety And Threat Modeling

- safeguard: 安全防护措施，如过滤、监控、阻断系统。
- safeguard testing: 安全防护测试。
- robustness: 鲁棒性，面对攻击或异常仍能保持有效。
- threat model: 威胁模型，假设攻击者有什么能力、资源、动机和限制。
- adversary model: 攻击者模型。
- relevant adversary model: 与 claim 相匹配的攻击者模型。
- end-to-end attack strategy: 端到端攻击策略。
- red teaming: 红队测试。
- jailbreak: 越狱，绕过安全限制。
- universal jailbreak: 跨多任务有效的通用越狱模式。
- severity: 严重程度、风险等级。

## Validity Hazards

- reward hacking: 通过评价者意图之外的方式拿高分。
- shortcut: 捷径、钻空子的路径。
- exploit: 利用漏洞、钻空子。
- contamination: 训练数据或评测中可找到答案造成的污染。
- close variants: 高度相似的变体。
- refusal: 拒答，可能掩盖被测行为。
- broken problems: 无效题目或有缺陷任务。
- sandbagging: 策略性隐藏能力、故意装弱。
- strategic underperformance: 有策略地表现低于真实水平。
- evaluation awareness: 模型意识到或似乎意识到自己正在被评测。
- reasoning traces: 推理轨迹。
- intermediate artifacts: 中间过程产物，如工具调用记录、计划、搜索日志。
- harness artifacts: harness 引入的偏差或假象。

## Interpretation Verbs And Modifiers

- assess: 系统评估、衡量并判断。
- specify: 明确且具体指出。
- explicitly: 明确地、直接写出。
- beyond the result itself: 不只是结果本身。
- account for: 将某因素纳入分析、控制或校正。
- materially affect: 实质性影响结果或结论。
- distort results: 使结果失真，方向可能高也可能低。
- inflate scores: 使分数虚高。
- understate capability/risk: 低估能力或风险。
- overinterpret: 过度解读，推出超出证据支持范围的结论。
- disqualify apparent successes: 排除表面成功案例。
- subject to security or confidentiality concerns: 在安全或保密限制前提下。

## Useful Contrast Groups

- result vs interpretation vs claim
- assess vs evaluate vs test
- explicitly vs clearly
- specify vs explain
- provide evidence vs give evidence vs offer evidence
- valid vs correct
- credible vs unlimited
- equivalent vs identical vs similar
- serious vs severe vs severity
- unintended vs unexpected
- impact vs materially affect

# 06 - Git 基础工作流

目标：熟悉最小可用的 Git 操作链路。

## 你会用到

```sh
git status
git init
git add
git commit
git log
git diff
```

## 任务

请完成：

1. 如果当前目录还不是 Git 仓库，运行 `git init`。
2. 运行 `git status`，观察哪些文件还没有提交。
3. 创建 `answers/06-git.txt`，写入 `git practice started`。
4. 运行 `git diff` 看看改动。
5. 暂存所有文件。
6. 提交一次，提交信息为 `Add terminal practice exercises`。
7. 用 `git log --oneline -3` 查看最近提交。

## 提示

```sh
git init
echo "git practice started" > answers/06-git.txt
git status
git add .
git commit -m "Add terminal practice exercises"
git log --oneline -3
```

## 注意

如果 Git 提示你没有配置用户名或邮箱，可以先配置：

```sh
git config user.name "Your Name"
git config user.email "you@example.com"
```


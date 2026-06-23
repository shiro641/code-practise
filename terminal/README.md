# 命令行快速熟悉练习场

这个项目是一套循序渐进的命令行练习。目标不是背命令，而是通过真实的小任务，快速建立“我知道该怎么找、怎么看、怎么改”的手感。

## 推荐练习顺序

1. `exercises/01-navigation.md`：目录导航与查看文件
2. `exercises/02-files.md`：创建、复制、移动、删除
3. `exercises/03-search.md`：搜索文件和内容
4. `exercises/04-pipes-redirection.md`：管道、重定向、组合命令
5. `exercises/05-permissions-processes.md`：权限、脚本、进程基础
6. `exercises/06-git-basics.md`：Git 基础工作流

## 怎么开始

先进入项目目录：

```sh
cd /Users/zhangjie/Desktop/code-practise/terminal
```

然后打开第一关：

```sh
less exercises/01-navigation.md
```

每完成一关，可以运行检查脚本：

```sh
./scripts/check.sh 01
```

如果提示脚本没有执行权限，先运行：

```sh
chmod +x scripts/check.sh
```

## 练习原则

- 每一关都尽量自己先试。
- 不确定时先用 `pwd`、`ls -la`、`cat`、`less` 看现场。
- 删除命令 `rm` 要慢一点，先确认路径。
- 做错没关系，这个项目就是拿来折腾的。


# 05 - 权限、脚本、进程基础

目标：理解可执行权限，并能查看简单进程信息。

## 你会用到

```sh
chmod
ls -l
./script.sh
ps
grep
sleep
kill
```

## 任务

请完成：

1. 查看 `practice/scripts/hello.sh` 的权限。
2. 给它添加执行权限。
3. 运行它，并把输出保存到 `answers/05-hello.txt`。
4. 在后台启动一个 60 秒的 sleep：`sleep 60 &`
5. 用 `ps` 找到它。
6. 用 `kill` 结束它。
7. 在 `answers/05-process.txt` 写入 `killed`。

## 提示

```sh
chmod +x practice/scripts/hello.sh
./practice/scripts/hello.sh > answers/05-hello.txt
sleep 60 &
ps aux | grep "sleep 60"
kill <PID>
```

## 检查

```sh
./scripts/check.sh 05
```


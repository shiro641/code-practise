# 03 - 搜索文件和内容

目标：学会在一堆文件里快速定位线索。

## 你会用到

```sh
find
grep
rg
which
wc
```

如果你的电脑有 `rg`，优先用 `rg`；没有的话用 `grep -r`。

## 任务

请完成：

1. 找出 `practice/logs` 目录下所有 `.log` 文件。
2. 在 `practice/logs` 里搜索 `ERROR`。
3. 在 `practice/recipes` 里搜索包含 `salt` 的文件。
4. 统计 `practice/recipes/noodles.txt` 有多少行。
5. 把第 2 步搜到的那一整行写入 `answers/03-error-line.txt`。
6. 把包含 `salt` 的文件名写入 `answers/03-salt-file.txt`。

## 提示

可以试试：

```sh
rg "ERROR" practice/logs
rg -l "salt" practice/recipes
```

## 检查

```sh
./scripts/check.sh 03
```


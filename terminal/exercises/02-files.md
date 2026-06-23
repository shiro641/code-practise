# 02 - 创建、复制、移动、删除

目标：掌握最常见的文件整理动作。

## 你会用到

```sh
mkdir
touch
cp
mv
rm
ls
cat
```

## 任务

请在项目根目录完成：

1. 创建目录 `workspace/notes`。
2. 创建文件 `workspace/notes/today.txt`。
3. 向 `today.txt` 写入一行：`learn terminal commands`
4. 复制 `practice/templates/checklist.txt` 到 `workspace/notes/checklist.txt`。
5. 把 `workspace/notes/today.txt` 重命名为 `workspace/notes/day-1.txt`。
6. 创建一个临时文件 `workspace/notes/delete-me.txt`，然后删除它。
7. 在 `answers/02-files.txt` 写入 `done`。

## 提示

写入文件可以用：

```sh
echo "learn terminal commands" > workspace/notes/today.txt
```

## 检查

```sh
./scripts/check.sh 02
```


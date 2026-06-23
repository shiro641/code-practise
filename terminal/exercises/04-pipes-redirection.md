# 04 - 管道、重定向、组合命令

目标：把多个简单命令连起来，完成更有用的事。

## 你会用到

```sh
|
>
>>
sort
uniq
wc
grep
cut
```

## 任务

请完成：

1. 查看 `practice/data/fruits.txt`。
2. 统计这个文件一共有多少行。
3. 生成去重并排序后的水果列表，保存到 `workspace/fruits-unique.txt`。
4. 从 `practice/data/people.csv` 中筛选出城市是 `Shanghai` 的行，保存到 `workspace/shanghai-people.csv`。
5. 把 `workspace/fruits-unique.txt` 的行数写入 `answers/04-unique-count.txt`。

## 提示

```sh
sort practice/data/fruits.txt | uniq > workspace/fruits-unique.txt
grep "Shanghai" practice/data/people.csv > workspace/shanghai-people.csv
wc -l workspace/fruits-unique.txt > answers/04-unique-count.txt
```

## 检查

```sh
./scripts/check.sh 04
```


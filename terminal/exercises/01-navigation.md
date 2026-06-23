# 01 - 目录导航与查看文件

目标：熟悉你现在在哪、目录里有什么、文件里写了什么。

## 你会用到

```sh
pwd
ls
ls -la
cd
cat
less
head
tail
```

## 任务

请在项目根目录完成这些操作：

1. 用 `pwd` 确认当前位置。
2. 用 `ls` 查看项目里有哪些目录。
3. 进入 `practice/world/cities`。
4. 查看这个目录下的所有文件，包括隐藏文件。
5. 用 `cat` 查看 `tokyo.txt`。
6. 用 `head` 查看 `shanghai.txt` 的前 3 行。
7. 用 `tail` 查看 `new-york.txt` 的最后 2 行。
8. 回到项目根目录。
9. 在项目根目录创建文件 `answers/01-navigation.txt`，写入你当前的绝对路径。

## 提示

创建答案目录和文件可以这样做：

```sh
mkdir -p answers
pwd > answers/01-navigation.txt
```

## 检查

```sh
./scripts/check.sh 01
```


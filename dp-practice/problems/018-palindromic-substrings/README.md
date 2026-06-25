# 018. 回文子串

- 日期：2026-06-25
- 题目：`647. Palindromic Substrings`
- 类型：区间 DP / 回文判断计数
- 状态：已完成
- 来源：daily-practice-2026-06-25

## 题目

给你一个字符串 `s`，请你返回 `s` 中回文子串的数量。

子串是连续的字符序列。单个字符也算回文子串。

## 示例

```text
示例 1：
输入：s = "abc"
输出：3
解释："a"、"b"、"c"
```

```text
示例 2：
输入：s = "aaa"
输出：6
解释："a"、"a"、"a"、"aa"、"aa"、"aaa"
```

## 限制

```text
1 <= s.length <= 1000
s 只包含小写英文字母
```

## 用户解答

你提交的是 Python 实现：

```python
s = "aac"


def getHuiCount(s):
    dp = [[True if i == j else False for j in range(len(s))] for i in range(len(s))]

    for i in range(len(s) - 2, -1, -1):
        for j in range(i + 1, len(s)):
            if j - i + 1 == 2:
                dp[i][j] = s[i] == s[j]
            else:
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]

    return sum([1 for i in range(len(dp)) for j in range(len(dp[i])) if dp[i][j]])


if __name__ == "__main__":
    print(getHuiCount(s))
```

## 评价

通过。

这份代码的区间 DP 建模是正确的：

- `dp[i][j]` 表示子串 `s[i..j]` 是否为回文。
- 当 `s[i] != s[j]` 时，`dp[i][j] = False`。
- 当 `s[i] == s[j]` 时：
  - 若区间长度为 `2`，则 `dp[i][j] = True`。
  - 若区间长度大于 `2`，则看内部子串是否回文：`dp[i][j] = dp[i + 1][j - 1]`。

遍历顺序也正确：

- `i` 从大到小枚举。
- `j` 从 `i + 1` 到末尾枚举。
- 这样在计算 `dp[i][j]` 时，`dp[i + 1][j - 1]` 一定已经算过。

边界处理正确：

- 所有单字符子串默认是回文，因此初始化 `dp[i][i] = True`。
- 长度为 `2` 的区间单独判断，避免访问越界或错误依赖未定义状态。

复杂度正确：

```text
时间复杂度：O(n^2)
空间复杂度：O(n^2)
```

额外验证通过的边界 case：

- `"a"` -> `1`
- `"aa"` -> `3`
- `"ab"` -> `2`
- `"aac"` -> `4`
- `"aaa"` -> `6`
- `"abba"` -> `6`

## 后续强化

- 这题已经能稳定写对区间 DP 了，下一步继续训练“看到题先识别模型”的速度。
- 后续可以继续对比这题和“最长回文子序列”的区别：一个是子串、一个是子序列，状态定义和转移目标都不一样。

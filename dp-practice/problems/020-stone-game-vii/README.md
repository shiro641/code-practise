# 020. 石子游戏 VII

- 日期：2026-06-27
- 题目：`1690. Stone Game VII`
- 类型：区间 DP / 博弈型分差 DP
- 状态：已完成
- 来源：daily-practice-2026-06-27

## 题目

给你一个整数数组 `stones` 。游戏中，Alice 和 Bob 轮流进行自己的回合，Alice 先开始。

每个回合，玩家可以移除最左边或最右边的一块石子，并获得剩余石子总和的分数。Bob 总是尽可能缩小自己和 Alice 之间的分差，Alice 总是尽可能扩大分差。

请你返回两人的最终得分差 `Alice - Bob` 。

## 示例

```text
示例 1：
输入：stones = [5,3,1,4,2]
输出：6
```

```text
示例 2：
输入：stones = [7,90,5,1,100,10,10,2]
输出：122
```

## 限制

```text
2 <= stones.length <= 1000
1 <= stones[i] <= 1000
```

## 用户解答

你提交的是 Python 实现：

```python
input = [7, 90, 5, 1, 100, 10, 10, 2]


def competition(input):
    dp = [
        [float("inf") if i != j else 0 for i in range(len(input))]
        for j in range(len(input))
    ]

    for i in range(len(input) - 2, -1, -1):
        initSum = input[i]
        for j in range(i + 1, len(input)):
            initSum += input[j]
            """dp[i][j]: 先手用户与后手用户之间分差的最大值"""
            dp[i][j] = initSum - min(input[i] + dp[i + 1][j], input[j] + dp[i][j - 1])

    print(dp[0][len(input) - 1], dp)

    return dp[0][len(input) - 1]


if __name__ == "__main__":
    print(competition(input))
```

## 评价

通过。

这份代码的核心算法是正确的：

- 状态定义正确：`dp[i][j]` 表示当前区间 `stones[i..j]` 上，轮到当前先手时，先手相对后手能取得的最大分差。
- 遍历顺序正确：外层 `i` 从大到小，内层 `j` 从小到大，能保证 `dp[i + 1][j]` 和 `dp[i][j - 1]` 先于 `dp[i][j]` 计算完成。
- 转移逻辑正确：你使用的是等价写法

```text
dp[i][j] = sum(i..j) - min(stones[i] + dp[i+1][j], stones[j] + dp[i][j-1])
```

它与更常见的

```text
max(sum(i+1..j) - dp[i+1][j], sum(i..j-1) - dp[i][j-1])
```

本质等价。

- 复杂度也已优化到可接受范围：你把原先循环里的 `sum(input[i:j+1])` 改成了 `initSum` 滚动维护区间和，因此总时间复杂度回到 `O(n^2)`，空间复杂度为 `O(n^2)`。

这次按你的要求，只检查核心算法正确性，不额外要求变量命名或风格调整。

# 017. 买卖股票的最佳时机 III

- 日期：2026-06-24
- 题目：`123. Best Time to Buy and Sell Stock III`
- 类型：股票状态机 DP / 最多两笔交易
- 状态：已完成
- 来源：daily-practice-2026-06-24

## 题目

给定一个数组 `prices`，它的第 `i` 个元素 `prices[i]` 表示一支给定股票第 `i` 天的价格。

你最多可以完成 `2` 笔交易。你不能同时参与多笔交易，也就是说你必须在再次购买前出售掉之前的股票。

返回你能获得的最大利润。

## 用户解答

```python
input = [3, 3, 5, 0, 0, 3, 1, 4]
target = 4


def getMaxProfits_(input):
    """dp[i][j][k]: 第i天出售次数为k，持有(j=1)/未持有(j=0)股票时的最大利润"""
    dp = [[[0, 0, 0], [0, 0, 0]] for _ in range(len(input))]

    dp[0][1] = [-input[0], float('-inf'), float('-inf')]
    dp[0][0] = [0, float('-inf'), float('-inf')]

    for i in range(1, len(input)):

        dp[i][0] = [
            dp[i - 1][0][0],
            max(dp[i - 1][0][1], dp[i - 1][1][0] + input[i]),
            max(dp[i - 1][0][2], dp[i - 1][1][1] + input[i]),
        ]
        dp[i][1] = [
            max(dp[i - 1][1][0], dp[i - 1][0][0] - input[i]),
            max(dp[i - 1][1][1], dp[i - 1][0][1] - input[i]),
            float('-inf'),
        ]

    print(dp, max([dp[len(input)-1][0][k] for k in range(3)]))
    return max([dp[len(input)-1][0][k] for k in range(3)])


if __name__ == "__main__":
    print(getMaxProfits_(input))
```

## 评价

通过。

这次做得好的地方，不只是把结果算对了，而是你把状态语义一步步抠清楚了。

- 状态定义最终对齐为：`dp[i][j][k]` 表示第 `i` 天结束时，持有/未持有股票，且恰好卖出 `k` 次时的最大利润。
- 初始化正确：第 0 天只有 `dp[0][0][0] = 0` 和 `dp[0][1][0] = -prices[0]` 合法，其余状态都设为 `-inf`，避免混入不可达状态。
- 卖出次数增加的时机正确：只有在卖出时，`k` 才会从 `k - 1` 转移到 `k`；买入不会增加卖出次数。
- 不可达状态处理正确：`dp[i][1][2]` 始终保持为 `-inf`，因为已经卖出 2 次后再持有，等价于开启第 3 笔交易，不符合题意。
- 复杂度正确：时间复杂度 `O(n)`，空间复杂度 `O(n)`；如果后续愿意，还可以继续压成常数状态。

## 后续强化

- 继续保持先对齐“状态语义”再写初始化，这对股票状态机题特别重要。
- 之后可以把这题进一步压缩成 4 个状态：`hold1 / sold1 / hold2 / sold2`，训练把三维状态机映射成常数状态写法。

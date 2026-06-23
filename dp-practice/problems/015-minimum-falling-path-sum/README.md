# 015. 下降路径最小和

- 日期：2026-06-22
- 题目：`931. Minimum Falling Path Sum`
- 类型：二维路径 / 网格 DP
- 状态：已完成
- 来源：daily-practice-2026-06-22

## 题目

给你一个 `n x n` 的整数矩阵 `matrix` ，请你找出并返回通过 `matrix` 的下降路径的最小和。

下降路径可以从第一行中的任何元素开始，并从每一行选择一个元素。在下一行选择的元素，必须是正下方或者左下方、右下方相邻的元素。

## 用户解答

```python
input = [[-19,57],[-40,-5]]

def getMinPath(matrix):
    dp = [[0] * len(matrix[0]) for row in matrix]

    if len(matrix[0]) == 1:
        return sum(row[0] for row in matrix)

    dp[0] = matrix[0][:]

    for i in range(1, len(matrix)):
        for j in range(len(matrix[0])):
            if j == 0:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1]) + matrix[i][j]
            elif j == len(matrix[0]) - 1:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + matrix[i][j]
            else:
                dp[i][j] = (
                    min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1]) + matrix[i][j]
                )

    return min(dp[len(dp) - 1])

if __name__ == "__main__":
    print(getMinPath(input))
```

## 评价

- 代码正确，状态设计和转移方向都对。
- 第一行直接初始化为原矩阵值，符合“路径从第一行任意位置开始”的语义。
- 对最左列、最右列和中间列分别处理，边界没有漏。
- 最终取最后一行最小值，符合题意。
- 时间复杂度 `O(n^2)`，空间复杂度 `O(n^2)`。

## 后续强化

- 这类题可以继续训练成一句话识别：`dp[i][j]` 表示“走到当前位置的最优值”，当前格子只从上一行允许到达的位置转移。
- 后续可以再尝试把二维 `dp` 压成一维，继续练空间优化。

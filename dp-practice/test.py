def getMinPath(input):
    dp = [[float("inf")] * len(input[-1]) for _ in input]

    dp[0][0] = input[0][0]

    for i in range(1, len(input)):
        for j in range(len(input[i])):
            dp[i][j] = (
                dp[i - 1][j] if j == 0 else min(dp[i - 1][j], dp[i - 1][j - 1])
            ) + input[i][j]

    print(dp)
    return min(dp[-1])


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

input = [3, 3, 5, 0, 0, 3, 1, 4]
target = 4


def getMaxProfits(input):
    dp = [[0] * 3 for _ in range(len(input))]

    dp[0][0] = 0
    dp[0][1] = -input[0]

    for i in range(1, len(input)):
        if dp[i][2] > 2:
            continue
        if dp[i-1][1] + input[i] > dp[i-1][0]:
            dp[i][0] = dp[i-1][1] + input[i]
            dp[i][2] += 1
        # dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + input[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - input[i])

    print(dp)
    return dp[len(input)-1][0]

if __name__ == "__main__":
    print(getMaxProfits(input))

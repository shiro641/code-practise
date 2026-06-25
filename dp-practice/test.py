input = [3, 3, 5, 0, 0, 3, 1, 4]
target = 4


def getMaxProfits_(input):
    """dp[i][j][k]: 第i天出售次数为k，持有(j=1)/未持有(j=0)股票时的最大利润"""
    dp = [[[0, 0, 0], [0, 0, 0]] for _ in range(len(input))]

    dp[0][1] = [-input[0], float("-inf"), float("-inf")]
    dp[0][0] = [0, float("-inf"), float("-inf")]

    for i in range(1, len(input)):

        dp[i][0] = [
            dp[i - 1][0][0],
            max(dp[i - 1][0][1], dp[i - 1][1][0] + input[i]),
            max(dp[i - 1][0][2], dp[i - 1][1][1] + input[i]),
        ]
        dp[i][1] = [
            max(dp[i - 1][1][0], dp[i - 1][0][0] - input[i]),
            max(dp[i - 1][1][1], dp[i - 1][0][1] - input[i]),
            float("-inf"),
        ]

    print(dp, max([dp[len(input) - 1][0][k] for k in range(3)]))
    return max([dp[len(input) - 1][0][k] for k in range(3)])


s = "aac"


def getHuiCount(s):
    dp = [[True if i == j else False for j in range(len(s))] for i in range(len(s))]

    for i in range(len(s) - 2, -1, -1):
        # print(i)
        for j in range(i + 1, len(s)):
            # print(i, j)
            if j - i + 1 == 2:
                dp[i][j] = s[i] == s[j]
            else:
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]

    return sum([1 for i in range(len(dp)) for j in range(len(dp[i])) if dp[i][j]])


if __name__ == "__main__":
    print(getHuiCount(s))

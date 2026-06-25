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

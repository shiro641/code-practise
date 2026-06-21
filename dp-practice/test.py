nub_ = 13


def getMinCount(nub):
    
    items = [x * x for x in range(nub) if x * x <= nub]
    print(items)

    dp = [float('inf')] * (nub+1)
    dp[0] = 0

    print(dp)

    for i in range(len(items)):
        for j in range(items[i], nub+1):
            dp[j] = min(dp[j-items[i]] + 1, dp[j])

    print(dp)
    return dp[nub]

if __name__ == "__main__":
    print(getMinCount(nub_))

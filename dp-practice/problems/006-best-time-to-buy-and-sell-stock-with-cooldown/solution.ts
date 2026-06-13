const maxProfit = (prices: number[]): number => {
  const n = prices.length;
  const dp = Array.from({ length: n }, () => [0, 0]);

  if (n <= 1) return 0;
  if (n <= 2) {
    return Math.max(0, prices[1] - prices[0]);
  }

  dp[0][0] = 0;
  dp[0][1] = -prices[0];
  dp[1][0] = Math.max(0, prices[1] - prices[0]);
  dp[1][1] = Math.max(-prices[1], -prices[0]);

  for (let i = 2; i < n; i++) {
    dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1] + prices[i]);
    dp[i][1] = Math.max(dp[i - 1][1], dp[i - 2][0] - prices[i]);
  }

  return dp[n - 1][0];
};

export { maxProfit };

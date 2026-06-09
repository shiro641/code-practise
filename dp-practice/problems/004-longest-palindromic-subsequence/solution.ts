const s = "bbbab";

const getHuiStr = (s: string) => {
  const dp = Array.from({ length: s.length }, (_, i) =>
    Array.from({ length: s.length }, (_, j) => (i === j ? 1 : 0)),
  );

  // 倒着遍历，因为 j 很快就遍历到底了，所以可以先算出小区间的状态。
  for (let i = s.length - 1; i >= 0; i--) {
    for (let j = i + 1; j < s.length; j++) {
      if (s[i] === s[j]) {
        dp[i][j] = i + 1 > j - 1 ? 2 : dp[i + 1][j - 1] + 2;
      } else {
        dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);
      }
    }
  }

  return dp[0][s.length - 1];
};

getHuiStr(s);

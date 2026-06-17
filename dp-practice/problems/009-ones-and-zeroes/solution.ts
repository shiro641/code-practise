const strs = ["10", "0", "1"];
const m = 1;
const n = 1;

const getMaxStrCount = (strs: string[], m: number, n: number) => {
  const dp = Array.from({ length: m + 1 }, () =>
    Array.from({ length: n + 1 }, () => 0),
  );

  for (let i = 0; i < strs.length; i++) {
    const [count0, count1] = strs[i]
      .split("")
      .reduce(
        (acc, cur) =>
          cur === "0" ? [acc[0] + 1, acc[1]] : [acc[0], acc[1] + 1],
        [0, 0],
      );

    for (let j = m; j >= count0; j--) {
      for (let k = n; k >= count1; k--) {
        dp[j][k] = Math.max(dp[j - count0][k - count1] + 1, dp[j][k]);
      }
    }
  }

  return dp[m][n];
};

console.log(getMaxStrCount(strs, m, n));

const num = [31, 26, 33, 21, 40];

const getMaxCount = (num: Array<number>) => {
  const sum = num.reduce((acc, cur) => acc + cur, 0);
  const bag = Math.ceil(sum / 2);
  const dp = new Array(bag + 1).fill(0);

  for (let i = 0; i < num.length; i++) {
    for (let j = bag; j >= num[i]; j--) {
      // dp[j] = num[i] + dp[j - num[i]] > bag ? dp[j - num[i]] : num[i] + dp[j - num[i]]
      dp[j] = Math.max(dp[j - num[i]] + num[i], dp[j]);
    }
  }

  return dp[bag];
};

const part = getMaxCount(num);

Math.abs(num.reduce((acc, cur) => acc + cur, 0) - 2 * part);

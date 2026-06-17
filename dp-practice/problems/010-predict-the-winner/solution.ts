const nums = [1, 5, 233, 7];

const getWinner = (nums: Array<number>) => {
  const dp = Array.from({ length: nums.length }, (_, index0) =>
    Array.from({ length: nums.length }, (_, index1) =>
      index0 === index1 ? nums[index1] : 0,
    ),
  );

  for (let i = nums.length - 1; i >= 0; i--) {
    for (let j = i + 1; j < nums.length; j++) {
      dp[i][j] = Math.max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1]);
    }
  }

  return dp[0][nums.length - 1] >= 0;
};

console.log(getWinner(nums));

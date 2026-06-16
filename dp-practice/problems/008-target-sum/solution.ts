const nums = [1, 1, 1, 1, 1];
const target = 3;

const getWays = (nums: Array<number>, target: number) => {
  const sum = nums.reduce((acc, cur) => acc + cur, 0);

  if ((sum + target) % 2 !== 0) return 0;
  if (Math.abs(target) > sum) return 0;
  const packet = (sum + target) / 2;

  const dp = new Array(packet + 1).fill(0);
  dp[0] = 1;
  for (let i = 0; i < nums.length; i++) {
    for (let j = packet; j >= nums[i]; j--) {
      // dp[j] 表示：从前 i 个数里选若干个数，凑出和为 j 的方案数。
      dp[j] = dp[j - nums[i]] + dp[j];
    }
  }
  return dp[packet];
};

console.log(getWays(nums, target));

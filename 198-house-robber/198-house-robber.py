class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums) + 1)]
        
        for i in range(1, len(dp)):
            curr = nums[i - 1]
            if i >= 2:
                curr += dp[i - 2]
            dp[i] = max(curr, dp[i - 1])
        return dp[-1]
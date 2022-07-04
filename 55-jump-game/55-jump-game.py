class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp(i) = max(dp[i - 1], 1 + dp[j])
        
        dp = [0 for _ in range(len(nums) + 1)]
        dp[0] = 1
        
        for i in range(1, len(dp)):
            if dp[i - 1] < i:
                return False
            dp[i] = max(dp[i - 1], i + nums[i - 1])
        
        return True
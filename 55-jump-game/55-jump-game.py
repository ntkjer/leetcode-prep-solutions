class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        dp = [0 for _ in range(len(nums) + 1)]
        dp[0] = 1
        
        for i in range(1, len(dp)):
            if dp[i - 1] < i:
                return False
            
            dp[i] = max(nums[i - 1] + i, dp[i - 1])
            
        return dp[-1]
        
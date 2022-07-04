class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp(i) = max(dp[i - 1], 1 + dp[j])
        n = len(nums) - 1
        last_idx = n
        
        for i in range(n, -1, -1):
            if i + nums[i] >= last_idx:
                last_idx = i
                
        return last_idx == 0
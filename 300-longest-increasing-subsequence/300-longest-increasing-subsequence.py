class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # dp[i] = max(dp[j] + 1, dp[i]) iff dp[j] < dp[i]
        dp = [1 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], 1 + dp[i])
                    
        return max(dp)
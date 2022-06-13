class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
    
        dp = [1] * len(nums)
        
        for i in range(len(dp)):
            for j in range(i + 1):
                if nums[j] < nums[i]:
                    dp[i] = max(1 + dp[j], dp[i])
        
        return max(dp)
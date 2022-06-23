class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # LIS(0) = 0
        # LIS(i) = max(LIS(i - 1), LIS(j) + 1 if nums[j] < nums[i]) 
        
        dp = [1] * (len(nums))
        
        for i in range(len(dp)):
            for j in range(i + 1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    
        return max(dp)
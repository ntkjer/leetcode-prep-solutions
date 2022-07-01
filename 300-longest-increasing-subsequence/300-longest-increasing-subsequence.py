class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # LIS(i) = max(LIS(i - 1), 1 + LIS(j) if nums[i] >= nums[j])
        
        dp = [1] * (len(nums))
        
        for i in range(len(dp)):
            for j in range(i + 1):
                if nums[j] < nums[i]:
                    dp[i] = max(1 + dp[j], dp[i])
        return max(dp)
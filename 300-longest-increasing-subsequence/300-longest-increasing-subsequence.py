class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # dp[i] = max(dp[i - 1], dp[j] + 1) if nums[j] > nums[i]
        
        dp = [1 for _ in range(len(nums))]
        
        for i in range(len(dp)):
            for j in range(i + 1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
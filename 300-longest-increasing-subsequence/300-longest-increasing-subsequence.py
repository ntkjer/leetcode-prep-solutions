class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1 for _ in range(len(nums))]
        for i in range(len(dp)):
            for j in range(i + 1, len(dp)):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[i] + 1, dp[j])
        
        return max(dp)
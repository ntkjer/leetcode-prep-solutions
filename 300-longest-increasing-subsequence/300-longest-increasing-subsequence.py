class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1 for _ in range(len(nums))]
        
        for i in range(1, len(dp)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(1 + dp[j], dp[i])
        
        return max(dp)
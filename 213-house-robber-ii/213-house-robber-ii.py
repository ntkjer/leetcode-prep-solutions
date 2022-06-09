class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def robOne(nums):
            dp = [0] * (len(nums) + 1)
            
            dp[1] = nums[0]
            for i in range(2, len(dp)):
                if i >= 2:
                    dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])
            return dp[-1]
        
        if len(nums) == 1:
            return nums[0]
        res = max(robOne(nums[1:]), robOne(nums[:-1]))
        return res
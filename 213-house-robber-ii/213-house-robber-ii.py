class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def robOne(nums):
            if not nums:
                return 0
            dp = [0 for _ in range(len(nums) + 1)]
            dp[1] = nums[0]
            for i in range(2, len(dp)):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
            return dp[-1]
        
        res = max(robOne(nums[1:]), robOne(nums[:-1]))
        if len(nums) == 1:
            return nums[-1]
        else:
            return res
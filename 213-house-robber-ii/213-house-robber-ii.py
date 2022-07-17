class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def solve(nums):
            dp = [0 for _ in range(len(nums) + 1)]
            dp[0] = 0
            dp[1] = nums[0]
            for i in range(2, len(dp)):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
            return dp[-1]
        if len(nums) == 1:
            return nums[0]
        
        robOne, robTwo = solve(nums[1:]), solve(nums[:-1])
        
        return max(robOne, robTwo)
        
        
    
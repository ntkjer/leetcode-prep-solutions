class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def robOne(nums):
            first = 0
            second = 0
            for num in nums:
                curr = max(second, first + num)
                first = second
                second = curr
            return second
        
        if len(nums) == 1:
            return nums[0]
        res = max(robOne(nums[1:]), robOne(nums[:-1]))
        return res
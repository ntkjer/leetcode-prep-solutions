class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [float('-inf')] * (len(nums) + 1)
        
        res = curr = nums[0]
        for num in nums[1:]:
            curr = max(num, num + curr)
            res = max(res, curr)
        return res
            
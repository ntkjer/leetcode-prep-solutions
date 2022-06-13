class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr = res = nums[0]
        for num in nums[1:]:
            curr = max(curr + num, num)
            res = max(res, curr)
        return res
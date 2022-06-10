class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       
        res = curr = nums[0]
        for num in nums[1:]:
            curr = max(num, num + curr)
            res = max(res, curr)
            
        return res
            
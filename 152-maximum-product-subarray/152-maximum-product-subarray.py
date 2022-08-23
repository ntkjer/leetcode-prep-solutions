class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        curMin = nums[0]
        curMax = nums[0]
        res = nums[0]
        
        for num in nums[1:]:
            tmp = max(num * curMax, num * curMin, num)
            curMin = min(curMin * num, num * curMax, num)
            curMax = tmp
            res = max(res, curMax)
        
        return res
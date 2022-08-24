class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = nums[0]
        curMin = nums[0]
        res = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            newMax = max(curMax * num, num, curMin * num)
            curMin = min(num, curMin * num, curMax * num)
            curMax = newMax
            res = max(curMax, res)
        return res
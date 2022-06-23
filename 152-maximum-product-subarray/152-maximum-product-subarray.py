class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = curMin = res = nums[0]
        for num in nums[1:]:
            tmp = max(num, curMax * num, curMin * num)
            curMin = min(num, curMin * num, curMax * num)
            curMax = tmp
            res = max(res, curMax)
            
        return res
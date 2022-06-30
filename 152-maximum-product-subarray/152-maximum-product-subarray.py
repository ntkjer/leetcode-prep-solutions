class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = res = curMin = nums[0]
        for num in nums[1:]:
            tmp = max(curMax * num, num, curMin * num)
            curMin = min(curMin * num, num, curMax * num)
            curMax = tmp
            res = max(curMax, res)
        return res
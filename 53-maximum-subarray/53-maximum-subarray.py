class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSub = res = nums[0]
        for num in nums[1:]:
            curSub = max(num, num + curSub)
            res = max(res, curSub)
        return res
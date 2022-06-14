class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = currMax = currMin = nums[0]
        
        for num in nums[1:]:
            tmp = max(currMax * num, num, currMin * num)
            currMin = min(currMax * num, num, currMin * num)
            currMax = tmp
            res = max(currMax, res)
        
        return res
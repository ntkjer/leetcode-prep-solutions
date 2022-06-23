class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # -2, 0, -1
        #res, curMin, curMax = -2
        
        # curMax = max(-2, 0, -2 * 0)
        # curMin = min(-2, 0, -2 * 0)
        res = curMin = curMax = nums[0]
        for num in nums[1:]:
            tmp = max(curMax * num, num, curMin * num)
            curMin = min(num, curMin * num, curMax * num)
            curMax = tmp
            res = max(curMax, res)
  
        return res
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        curMax, curMin = 1, 1
        res = max(nums)
        for num in nums:
            if num == 0:
                curMin, curMax = 1, 1
                continue
                
            prevMax = num * curMax
            curMax = max(curMax * num, curMin * num, num)
            curMin = min(prevMax, curMin * num, num)
            
            res = max(res, curMin, curMax)
        return res
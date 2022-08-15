class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0]
        minProd = nums[0]
        maxProd = nums[0]
        
        for num in nums[1:]:
            tmp = max(num, num * minProd, num * maxProd)
            minProd = min(num, num * minProd, num * maxProd)
            maxProd = tmp
            res = max(res, maxProd)
        return res
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [float('-inf')] * (len(nums) + 1)
        
        dp[0] = nums[0]
        
        currMax = currMin = res = nums[0]
        
        for num in nums[1:]:
            tmp = max(num, currMax * num, currMin * num)
            currMin = min(num, currMax * num, currMin * num)
            currMax = tmp
            
            res = max(currMax, res)
        
        return res
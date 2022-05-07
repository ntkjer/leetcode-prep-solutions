class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSub = maxSub = nums[0]
        
        for num in nums[1:]:
            
            currSub = max(num, currSub + num)
            maxSub = max(maxSub, currSub)
        return maxSub
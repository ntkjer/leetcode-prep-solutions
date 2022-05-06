class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        counts = {}
        for i, num in enumerate(nums):
            if (target - num) in counts:
                return [counts[target-num], i]
            
            counts[num] = i
            
        return res
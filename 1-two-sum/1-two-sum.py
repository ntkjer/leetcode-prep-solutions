class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {} # num : idx
        
        for idx, num in enumerate(nums):
            if target - num in d:
                return [idx, d[target - num]]
            d[num] = idx
        return -1
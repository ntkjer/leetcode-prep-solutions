class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        sums = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in sums:
                return [idx, sums[complement]]
            sums[num] = idx
                
        return []
            
        
            
                
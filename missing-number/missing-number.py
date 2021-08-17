class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #nums_set = set(nums)   
        #N = len(nums)
        #nums_inclusive = set([i for i in range(N + 1)])        
        #return set(nums_inclusive - nums_set).pop()
        missing = len(nums) 
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

            
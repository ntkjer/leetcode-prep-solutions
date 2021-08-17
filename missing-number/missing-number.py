class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)   
        res = None 
        N = len(nums)
        nums_inclusive = set([i for i in range(N + 1)])        
        return set(nums_inclusive - nums_set).pop()

            
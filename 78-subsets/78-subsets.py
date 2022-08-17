class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = list()
        stack = list()
        
        def backtrack(start=0):
            if start == len(nums):
                res.append(stack.copy())
                return
            stack.append(nums[start])
            backtrack(start + 1)
            stack.pop()
            backtrack(start + 1)
            
        backtrack()
        return res
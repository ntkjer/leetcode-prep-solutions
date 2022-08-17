class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = list()
        
        def backtrack(i=0, partial=[]):
            if i == len(nums):
                res.append(partial[:])
                return
            partial.append(nums[i])
            backtrack(i + 1, partial)
            partial.pop()
            backtrack(i + 1, partial)
        
        backtrack()
        return res
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = list()
        nums.sort()
        
        def backtrack(i=0, partial=[]):
            if i == len(nums):
                res.append(partial[:])
                return
            
            partial.append(nums[i])
            backtrack(i + 1, partial)
            partial.pop()
            while (i + 1 < len(nums) and nums[i] == nums[i + 1]):
                i += 1
            
            backtrack(i + 1, partial)
            
        backtrack()
        return res
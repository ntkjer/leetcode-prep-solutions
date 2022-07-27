class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = list()
        nums.sort()
        
        def backtrack(i, partial):
            if i == len(nums):
                res.append(partial[:])
                return
            
            partial.append(nums[i])
            backtrack(i + 1, partial)
            partial.pop()
            
            # remove duplicate entries
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            backtrack(i + 1, partial)
        
        backtrack(0, [])
        return res
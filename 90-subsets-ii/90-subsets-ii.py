class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = list()
    
        def backtrack(i, partial):
            if i == len(nums):
                res.append(partial[:])
                return
        
            partial.append(nums[i])
            backtrack(i + 1, partial)
            partial.pop()
            
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
                
            backtrack(i + 1, partial)
            
        backtrack(0, [])
        return res
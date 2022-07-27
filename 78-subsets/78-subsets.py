class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # can't repeat itself, so 1,1,1 is invalid
        target = sum(nums)
        res = list()
        def backtrack(start, partial):
            if start == len(nums):
                res.append(partial[:])
                return 
            partial.append(nums[start])
            backtrack(start + 1, partial)
            partial.pop()
            backtrack(start + 1, partial)
        
        backtrack(0, [])
        return res
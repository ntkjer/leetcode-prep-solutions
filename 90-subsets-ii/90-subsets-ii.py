class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = set()
        def backtrack(start=0, partial=[]):
            if start == len(nums):
                res.add(tuple(partial.copy()))
                return
            partial.append(nums[start])
            backtrack(start + 1, partial)
            partial.pop()
            backtrack(start + 1, partial)
        backtrack()
        return res
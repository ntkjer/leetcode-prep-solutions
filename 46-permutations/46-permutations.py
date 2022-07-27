class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = list()
        n = len(nums)
        def backtrack(start=0):
            if start == len(nums):
                res.append(nums[:])
            
            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[i], nums[start] = nums[start], nums[i]
                
                
        backtrack()
        return res
            
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = list()
        
        def backtrack(start):
            if start == len(nums):
                res.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                backtrack(start + 1)
                nums[i], nums[start] = nums[start], nums[i]
                
                
        backtrack(0)
        return res
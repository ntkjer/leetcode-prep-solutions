class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def solve(first=0):
            if first == len(nums):
                res.append(nums[:])
                return
            
            for i in range(first, len(nums)):
                nums[i], nums[first] = nums[first], nums[i]
                solve(first + 1)
                nums[i], nums[first] = nums[first], nums[i]
            
        res = list()
        solve(0)
        return res
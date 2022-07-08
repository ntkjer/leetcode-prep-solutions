class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)
        cumulative = 1
        for i in range(len(nums) - 2, -1, -1):
            cumulative *= nums[i + 1]
            res[i] *= cumulative
        
        cumulative = 1
        for i in range(1, len(nums)):
            cumulative *= nums[i - 1]
            res[i] = res[i] * cumulative
                
            
        return res
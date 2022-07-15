class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        last_idx = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= last_idx:
                last_idx = i
            
        return last_idx == 0        
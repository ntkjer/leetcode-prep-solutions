class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums) - 1
        last_idx = n
        for i in range(n, -1, -1):
            if nums[i] + i >= last_idx:
                last_idx = i
        
        return last_idx == 0
                
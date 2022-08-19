class Solution:
    def jump(self, nums: List[int]) -> int:
        
        furthest = 0
        jumps = 0
        end = 0
        
        for i in range(len(nums) - 1):
            furthest = max(furthest, nums[i] + i)
            
            if i == end:
                jumps += 1
                end = furthest
            
        return jumps
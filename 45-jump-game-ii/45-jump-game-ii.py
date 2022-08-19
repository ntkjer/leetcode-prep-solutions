class Solution:
    def jump(self, nums: List[int]) -> int:
        
        end = 0
        jumps = 0
        furthest = 0
        
        
        for i in range(len(nums) - 1):
            furthest = max(furthest, nums[i] + i)
            
            if end == i:
                end = furthest
                jumps += 1
                
        
        return jumps
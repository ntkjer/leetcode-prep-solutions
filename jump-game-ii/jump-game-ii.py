class Solution:
    def jump(self, nums: List[int]) -> int:
        
        distance = 0
        jumps = 0
        position = 0  
        
        for i in range(len(nums) - 1):
            distance = max(distance, i + nums[i])
            
            if position == i:
                jumps += 1
                position = distance
                
        return jumps
            
       
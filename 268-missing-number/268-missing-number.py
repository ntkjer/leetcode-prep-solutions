class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_sum = 0
        for i in range(len(nums) + 1):
            total_sum += i    
        
        cur_sum = 0
        for num in nums: 
            cur_sum += num
            
        return total_sum - cur_sum
        
            
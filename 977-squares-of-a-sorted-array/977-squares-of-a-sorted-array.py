class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
    
        
        n = len(nums)
        res = [0] * n
        
        l = 0
        r = n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[l]) < abs(nums[r]):
                square = nums[r]
                r -= 1
            else:
                square = nums[l]
                l += 1
                
            res[i] = square * square
            
        return res
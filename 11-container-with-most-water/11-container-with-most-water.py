class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) - 1
        res = 0
        
        while l < r:
            left, right = height[l], height[r]
            min_height = min(left, right)
            cur_area = (r - l) * min_height
            
            res = max(cur_area, res)
            
            if left < right:
                l += 1
            else:
                r -= 1
                
        return res
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l, r = 0, len(height) - 1
        max_area = float('-inf')
        
        while l <= r:
            length = r - l
            curr = min(height[l], height[r])
            max_area = max(curr * length, max_area)
            
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
                
        return max_area
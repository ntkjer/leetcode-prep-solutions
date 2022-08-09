class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = float('-inf')
        
        for i, h in enumerate(heights):

            start = i
            while stack and stack[-1][1] > h:
                j, prev = stack.pop()
                start = j
                maxArea = max(maxArea, prev * (i - j))
                
            stack.append((start, h))
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
            
        return maxArea
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        stack = [-1]
        max_area = 0
        
        for i, h in enumerate(heights):
            while stack[-1] != -1 and h < heights[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break

                curr_h = heights[top]
                curr_w = i - stack[-1] - 1
                  
                max_area = max(max_area, curr_h * curr_w)
            stack.append(i)
        
        while stack[-1] != -1:
            curr_h = heights[stack.pop()]
            curr_w = len(heights) - stack[-1] - 1
            max_area = max(max_area, curr_h * curr_w)

        return max_area
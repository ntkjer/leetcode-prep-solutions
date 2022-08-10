class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # cut a rectangle with stack indices? 
        stack = []
        res = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                j, prevH = stack.pop()
                res = max(res, (i - j) * prevH)
                start = j
            
            stack.append((start, h))
        
        for i, h in stack:
            res = max(res, (len(heights) - i) * h)
            
        return res
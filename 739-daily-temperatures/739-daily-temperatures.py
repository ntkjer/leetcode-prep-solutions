class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [] # idx, temp? 
        res = [0] * len(temperatures)
        
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                prevTemp, prevIdx = stack.pop()
                res[prevIdx] = i - prevIdx
                
            stack.append([t, i])
        return res
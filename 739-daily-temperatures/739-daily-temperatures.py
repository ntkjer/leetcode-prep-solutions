class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [] # idx, prevtemp
        res = [0] * len(temperatures)
        
        for i, t in enumerate(temperatures):
            
            while stack and stack[-1][1] < t:
                j, prevTemp = stack.pop()
                res[j] = i - j
            
            stack.append([i, t])
            
        return res
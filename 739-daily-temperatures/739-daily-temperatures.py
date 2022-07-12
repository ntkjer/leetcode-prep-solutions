class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # idx, temp
        
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                stackIdx, stackTmp = stack.pop()
                res[stackIdx] = i - stackIdx
            stack.append([i, t])
        return res
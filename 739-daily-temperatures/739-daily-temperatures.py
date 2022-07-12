class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stackIdx, stackTmp = stack.pop()
                result[stackIdx] = (idx - stackIdx)
            stack.append([idx, temp])
        return result
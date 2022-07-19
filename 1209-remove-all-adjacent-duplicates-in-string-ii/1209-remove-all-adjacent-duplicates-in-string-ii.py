class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if not s: return s
        if not k: return s
        
        stack = [] # [char, idx]
        for idx, char in enumerate(s):
            if not stack or stack[-1][0] != char:
                stack.append([char, 1])
                continue
            if stack[-1][0] == char:
                prevChar, freq = stack.pop()
                if freq + 1 == k: # found the kth element, delete
                    continue
                stack.append([char, freq + 1])
        res = list()
       
        while stack:
            char, freq = stack.pop()
            res += (char) * freq
            
        res.reverse() # stack is reversed
        return "".join(res)
                
                    
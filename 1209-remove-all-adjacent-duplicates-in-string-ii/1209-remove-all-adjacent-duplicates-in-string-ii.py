class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # character, freq
        
        
        for c in s:
            if not stack or stack[-1][0] != c:
                stack.append([c, 1])
                continue
                
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] >= k:
                    stack.pop()
                  
        res = ""
        for i in range(len(stack)):
            res += stack[i][0] * int(stack[i][1])
        
        return res
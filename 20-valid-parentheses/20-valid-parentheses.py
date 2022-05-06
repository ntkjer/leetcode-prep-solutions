class Solution:
    def isValid(self, s: str) -> bool:
        parens = {'}': '{', 
                 ')': '(',
                 ']': '['}
        
        stack = []
        
        for c in s:
            if c in parens:
                if not stack:
                    return False
                prev = stack.pop()
                if prev != parens[c]:
                    return False
                
            else:
                stack.append(c)
                
        return True if not stack else False
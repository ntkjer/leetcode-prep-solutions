class Solution:
    def isValid(self, s: str) -> bool:
        parens = { ')': '(', '}': '{', ']': '['}
        
        stack = []
        for c in s:
            if c not in parens:
                stack.append(c)
            else:
                if not stack:
                    return False
                if parens[c] != stack[-1]:
                    return False
                stack.pop()
                
        if stack:
            return False
        
        return True
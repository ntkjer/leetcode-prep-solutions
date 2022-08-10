class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        removal = set()
        stack = [] # c, i
        
        for i, c in enumerate(s):
            if c.isalpha():
                continue
            elif not stack and c == ")":
                removal.add(i)
            elif stack and c == ")":
                stack.pop()
            elif c == "(":
                stack.append((c, i))
        
       
        while stack:
            c, i = stack.pop()
            removal.add(i)
        
        res = list()
        
        
        for i in range(len(s)):
            if i in removal:
                continue
            res.append(s[i])
            
        return "".join(res)
        
        
        
        
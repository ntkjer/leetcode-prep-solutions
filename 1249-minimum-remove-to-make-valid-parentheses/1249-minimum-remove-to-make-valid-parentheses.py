class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        indices = set()
        stack = []
        
        parens = set()
        parens.add(")")
        parens.add("(")
        
        for i, c in enumerate(s):
            if c not in parens:
                continue
                
            if c == "(":
                stack.append(i)
                
            elif not stack:
                indices.add(i)
            else:
                stack.pop()
                
        for i in stack:
            indices.add(i)
            
        res = list()
        for i in range(len(s)):
            if i not in indices:
                res.append(s[i])
            
        return "".join(res)
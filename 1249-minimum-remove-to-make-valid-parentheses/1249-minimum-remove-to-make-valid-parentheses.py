class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []
        indices = set()
        parens = set()
        parens.add("(")
        parens.add(")")
        
        for i, ch in enumerate(s):
            if ch not in parens:
                continue
            
            if ch == "(":
                stack.append(i)
            elif not stack:
                indices.add(i) # found a matching char but no space for 'validity'
            else: 
                stack.pop() # ) and matching (
            
        for i in stack:
            indices.add(i)
        
        res = list()
        for i in range(len(s)):
            if i not in indices:
                res.append(s[i])
                
        return "".join(res)
    
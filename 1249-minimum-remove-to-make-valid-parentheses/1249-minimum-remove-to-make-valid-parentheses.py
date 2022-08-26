class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = [] # this will keep track of current balance ( , )
        remove = set()
        
        for i, c in enumerate(s):
            if c == ")" and not stack:
                remove.add(i)
            elif c == "(":
                stack.append((c, i))
            elif c == ")":
                stack.pop()
        
      
        while stack:
            c, i = stack.pop()
            remove.add(i)
            
        res = list()
        for i in range(len(s)):
            if i in remove:
                continue
            res.append(s[i])
        
        return "".join(res)
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # abcd 
        
        stack = [] # c, freq
        
        
        for c in s:
            while stack and stack[-1][1] >= k:
                stack.pop()    
                
            if stack and c == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
        
        res = list()
        for c, f in stack:
            if f < k:
                res.append(c * f)
            
        return "".join(res)
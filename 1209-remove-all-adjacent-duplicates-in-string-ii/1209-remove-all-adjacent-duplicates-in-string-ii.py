class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        # use a stack and have each item as (c, freq)
        
        # pop last item when freq >= k
        
        stack = []
        
        for c in s:
            if not stack or stack[-1][0] != c:
                stack.append([c, 1])
            else:
                if stack[-1][0] == c:
                    stack[-1][1] += 1
                    if stack[-1][1] >= k:
                        stack.pop()
                        
        res = list()
        for char, freq in stack:
            
            res.append(freq * char)
        
        return "".join(res)
            
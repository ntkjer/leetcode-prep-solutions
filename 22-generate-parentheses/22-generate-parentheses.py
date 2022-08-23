class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = list()
        def backtrack(l, r, partial):
            if l == n == r:
                res.append("".join(partial[:]))
                return
            
            if l < n:
                partial.append("(")
                backtrack(l + 1, r, partial)
                partial.pop()
                
            if r < l:
                partial.append(")")
                backtrack(l, r + 1, partial)
                partial.pop()
                
        backtrack(0, 0, [])
        return res
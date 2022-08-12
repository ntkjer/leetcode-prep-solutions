class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = list()
        partial = []
        def backtrack(left=0, right=0):
            if left == right == n:
                res.append("".join(partial))
                return
            
            if left < n:
                partial.append("(")
                backtrack(left + 1, right)
                partial.pop()
            
            if right < left:
                partial.append(")")
                backtrack(left, right + 1)
                partial.pop()
                
                
        backtrack(0, 0)
        return res

        
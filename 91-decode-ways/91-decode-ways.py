class Solution:
    def numDecodings(self, s: str) -> int:
        
        
        @cache
        def backtrack(i=0):

            if i == len(s):
                return 1
            
            cur = s[i] 
            
            if not (1 <= int(cur) <= 26):
                return 0
            
            if i == len(s) - 1:
                return 1
            
            res = backtrack(i + 1)
            if int(s[i: i + 2]) <= 26:
                res += backtrack(i + 2)
                
            return res
        
        
        return backtrack()
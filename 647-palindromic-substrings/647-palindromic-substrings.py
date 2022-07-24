class Solution:
    def countSubstrings(self, s: str) -> int:
        
        
        
        def build_pal(i, j):
            res = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -=1
                j += 1
                res += 1
            return res
        
        res = 0
        for i in range(len(s)):
            res += build_pal(i, i) + build_pal(i, i + 1)
            
        return res
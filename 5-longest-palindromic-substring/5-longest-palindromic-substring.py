class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def build_pal(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i, j = i - 1, j + 1
                
            return s[i + 1: j]
        res = ""
        for i in range(len(s)):
            even, odd = build_pal(i, i), build_pal(i, i + 1)
            if len(even) > len(res):
                res = even
            if len(odd) > len(res):
                res = odd
        return res
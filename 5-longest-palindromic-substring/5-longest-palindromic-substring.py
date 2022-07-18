class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def makePalindrome(i, j):
            # given two indices i,j create the shortest palindrome and return it.
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
                
            return s[i + 1: j]
        
        res = ""
        for i in range(len(s)):
            palA, palB = makePalindrome(i, i), makePalindrome(i, i + 1)
            if len(palA) > len(res):
                res = palA
            if len(palB) > len(res):
                res = palB
                
        return res
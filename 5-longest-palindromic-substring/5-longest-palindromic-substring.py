class Solution:
    def longestPalindrome(self, s: str) -> str:
        def build(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
                
            return s[i + 1: j]
        
        longest = ""
        for i in range(len(s)):
            even, odd = build(i, i), build(i, i + 1)
            if len(even) > len(longest):
                longest = even
            if len(odd) > len(longest):
                longest = odd
                
        return longest
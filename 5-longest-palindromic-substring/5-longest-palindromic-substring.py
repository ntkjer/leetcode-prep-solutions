class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getLongest(i,j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                j += 1
                i -= 1
            return s[i + 1: j]
        
        longest = ""
        for i in range(len(s)):
            even, odd = getLongest(i, i), getLongest(i, i + 1)
            if len(even) > len(longest):
                longest = even
            if len(odd) > len(longest):
                longest = odd
                
        return longest
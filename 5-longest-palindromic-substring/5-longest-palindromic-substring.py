class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s[::-1] == s:
            return s
        
        longest = ""
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        
        for i in range(len(s)):
            dp[i][i] = True
            longest = s[i]
            
        
        for i in range(len(dp) - 1, -1, -1):
            for j in range(i + 1, len(dp)):
                if s[i] == s[j] and (dp[i + 1][j - 1] or j - i == 1):
                    dp[i][j] = True
                    if (j - i + 1) > len(longest): 
                        longest = s[i: j + 1]
                        
        return longest
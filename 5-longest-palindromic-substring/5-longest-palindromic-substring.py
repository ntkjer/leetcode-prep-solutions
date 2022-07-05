class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1 or s[::-1] == s:
            return s
        
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        res = ""
        for i in range(len(s)):
            dp[i][i] = 1
            res = s[i]
        
        for i in range(len(dp) - 1, -1, -1):
            for j in range(i + 1, len(dp)):
                if s[i] == s[j] and (dp[i + 1][j - 1] or j - i < 3):
                    dp[i][j] = 1
                    if (j - i + 1) > len(res):
                        res = s[i: j + 1]
                        
        return res
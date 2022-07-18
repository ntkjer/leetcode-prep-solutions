class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        res = ""
        
        for i in range(len(dp)):
            dp[i][i] = True
            res = s[i]
            
        for i in range(len(dp) - 1, -1, -1):
            for j in range(i + 1, len(dp)):
                if s[i] == s[j] and (dp[i + 1][j - 1] or j - i == 1):
                    dp[i][j] = True
                    if (j - i + 1) > len(res):
                        res = s[i: j + 1]
                    
        return res
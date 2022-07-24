class Solution:
    def countSubstrings(self, s: str) -> int:
        
        
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        res = 0
        
        for i in range(len(s)):
            dp[i][i] = True
            res += 1
        
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j] and (dp[i + 1][j - 1] or j - i == 1):
                    dp[i][j] = True
                    res += 1
        
        return res
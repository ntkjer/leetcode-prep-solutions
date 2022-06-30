class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0
        
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        
        for i in range(len(dp)):
            dp[i][i] = True
            res += 1
        
        for i in range(len(dp) - 1, -1, -1):
            for j in range(i + 1, len(dp)):
                if s[i] == s[j] and (dp[i + 1][j - 1] or j - i == 1):
                    dp[i][j] = True
                    res += 1
                        
        return res
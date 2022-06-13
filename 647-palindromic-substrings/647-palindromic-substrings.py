class Solution:
    def countSubstrings(self, s: str) -> int:
        
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        
        count  = 0
        for i in range(len(dp)):
            dp[i][i] = 1
            count += 1
            
        for i in range(len(dp) - 1, -1, -1):
            for j in range(i + 1, len(dp)):
                if s[i] == s[j]:
                    if dp[i + 1][j - 1] or j - i == 1:
                        dp[i][j] = 1
                        count += 1
                        
        
        return count
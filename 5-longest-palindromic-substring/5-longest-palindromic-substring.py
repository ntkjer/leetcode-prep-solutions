class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        
        for i in range(len(dp)):
            dp[i][i] = True
            res = s[i]
        n = len(dp)
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if dp[i + 1][j - 1] or j - i == 1:
                        dp[i][j] = True
                        if j - i + 1 > len(res):
                            res = s[i: j + 1]
                        
        return res
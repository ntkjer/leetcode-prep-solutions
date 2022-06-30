class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1] or len(s) < 2:
            return s
        
        res = ""
        
        #   c b b d
        # c 1 0 0 0
        # b   1 1 0
        # b   1 1 0
        # d       1
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        
        for i in range(len(s)):
            res = s[i]
            dp[i][i] = True
        
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j] and (dp[i + 1][j - 1] or j - i < 3):
                    dp[i][j] = True
                    if (j - i + 1) > len(res):
                        res = s[i: j + 1]
                    
        return res
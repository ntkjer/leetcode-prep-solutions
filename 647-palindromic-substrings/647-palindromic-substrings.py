class Solution:
    def countSubstrings(self, s: str) -> int:
        #   a b c
        # a 1 2 3
        # b   1
        # c     1
        
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        res = 0
        for i in range(len(s)):
            dp[i][i] = 1
            res += 1
        
        for i in range(len(dp) - 1, -1, -1):
            for j in range(i + 1, len(dp)):
                if i != j and s[i] == s[j] and (dp[i + 1][j - 1] or j - i == 1):
                    dp[i][j] = True
                    res += 1
                    
                    
        return res
        
class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # s = "abc"
        # a, b, c = 1 * 3
        
        
        # "aaa", res = 6
        # aaa = 1, a = 1 * 3, aa = 1 * 2
        
        
        #   a  a  a 
        # a 1  2  3
        # a    1  
        # a       1
        
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        res = 0
        for i in range(len(s)):
            dp[i][i] = 1
            res += 1
            
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[j] == s[i] and (dp[i + 1][j - 1] or j - i < 3):
                    res += 1
                    dp[i][j] = 1
        return res
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        res = "" 
        for i in range(len(s) - 1, -1, -1):
        
            dp[i][i] = 1
            if len(res) < 1:
                res = s[i]
            for j in range(i + 1, len(s)):
                # check if we match chars and prev palindrome
                if s[i] == s[j] and (dp[i + 1][j - 1] == 1 or j - i == 1):
                    dp[i][j] = 1
                    if len(res) < len(s[i: j + 1]):
                        res = s[i: j + 1]

        return res
                    
                    
                
            
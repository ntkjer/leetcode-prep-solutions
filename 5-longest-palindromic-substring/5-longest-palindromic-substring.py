class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s[::-1] == s:
            return s
        longest = ""
        
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        
        for i in range(len(dp)):
            longest = s[i]
            dp[i][i] = 1
        
        
        for i in range(len(dp) - 1, -1, -1):
            for j in range(i + 1, len(dp)):
                if s[i] == s[j]:
                    if dp[i + 1][j - 1] or j - i == 1:
                        dp[i][j] = True
                        if len(longest) < j - i + 1:
                            longest = s[i: j + 1]
                            
        return longest
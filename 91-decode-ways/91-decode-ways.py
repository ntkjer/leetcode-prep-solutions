class Solution:
    def numDecodings(self, s: str) -> int:
        
        
        @cache
        def backtrack(i=0):

            if i == len(s):
                return 1
            
            cur = s[i] 
            
            if not (1 <= int(cur) <= 26):
                return 0
            
            if i == len(s) - 1:
                return 1
            
            res = backtrack(i + 1)
            if int(s[i: i + 2]) <= 26:
                res += backtrack(i + 2)
                
            return res
        
        if s[0] == "0" or len(s) == 0:
            return 0
        
        dp = [0] * (len(s) + 1)
        dp[0] = 1 
        dp[1] = 1 if s[0] != "0" else 0
        for i in range(2, len(dp)):
            if int(s[i - 1]) != 0:
                dp[i] += dp[i - 1]
            take_two = int(s[i - 2: i])
            if 10 <= take_two <= 26:
                dp[i] += dp[i - 2]
            
                
        return dp[-1]
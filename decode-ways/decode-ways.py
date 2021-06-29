class Solution:
    def numDecodings(self, s: str) -> int:

        @cache
        def solve(idx=0):
            if idx == len(s):
                return 1
            if idx == len(s) - 1:
                return 1
            if s[idx] == "0":
                return 0
            
            res = solve(idx + 1) 

            two = int(s[idx: idx + 2])
            if two >= 10 and two <= 26:
                res += solve(idx + 2)                

            return res

        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1 if s[0] != "0" else 0
        
        for i in range(2, len(dp)):
            if s[i - 1] != "0":
                dp[i] = dp[i - 1]

            x = int(s[i - 2: i])
            if 10 <= x <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]
        
            
        
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1 # ""
        
        dp[1] = 1 if s[0] != "0" else 0
        
        for i in range(2, len(dp)):
            pick_one = s[i - 1: i]
            if 1 <= int(pick_one) <= 10:
                dp[i] += dp[i - 1]
            
            pick_two = s[i - 2: i]
            
            if 10 <= int(pick_two) <= 26:
                dp[i] += dp[i - 2]

            
        return dp[-1]
class Solution:
    def numDecodings(self, s: str) -> int:
        
        # s = "12", 12 and 1,2
        #           L      A,B
        
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        
        dp[1] = 1 if s[0] != "0" else 0
        
        for i in range(2, len(dp)):
            pick_one = s[i - 1]
            if 1 <= int(pick_one) <= 26:
                dp[i] += dp[i - 1]
                
            pick_two = int(s[i - 2: i])
            if 10 <= pick_two <= 26:
                dp[i] += dp[i - 2]
            
        return dp[-1]
                
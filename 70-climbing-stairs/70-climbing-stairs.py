class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, len(dp)):
            if i >= 2:
                dp[i] += dp[i - 2] + dp[i - 1]
            else:
                dp[i] += dp[i - 1]
                
        return dp[-1]
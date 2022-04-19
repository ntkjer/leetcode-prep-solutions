class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n > m:
            n,m = m, n
            
        dp = [1] * n
        for _ in range(1, m):
            for i in range(1, n):
                dp[i] += dp[i - 1]
                    
        return dp[-1]
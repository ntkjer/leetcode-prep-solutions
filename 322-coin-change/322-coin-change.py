class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for amt in range(coin, amount + 1):
                dp[amt] = min(dp[amt - coin] + 1, dp[amt])
                
        return dp[-1] if dp[-1] != float('inf') else -1
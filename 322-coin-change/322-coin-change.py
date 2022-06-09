class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0
        
        for coin in coins:
            for amt in range(len(dp)):
                if amt >= coin:
                    dp[amt] = min(1 + dp[amt - coin], dp[amt])
            
        return dp[-1] if dp[-1] != float('inf') else -1
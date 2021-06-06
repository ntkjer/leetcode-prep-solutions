class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        top down and bottom up solutions to the unbounded knapsack problem.
        
        both represent a 0 amount with 0 ways to make 'change'.
        both are pseudo polynomial time Tn = O(N * w) 
            where w is each representative weight 0..amount
            where N is num coins considered 
        
        
        Bottom up better for space, we only use O(w) and its assumed that w << N
        """
        @lru_cache(maxsize=None)
        def solve(amount):
            if amount < 0:
                return float('inf')
            if amount == 0:
                return 0
            res = float('inf')
            for coin_val in coins:
                res = min(res, 1 + solve(amount - coin_val))

            return res 

        N = len(coins) 
        dp = [float('inf') for _ in range(amount + 1)]

        dp[0] = 0 # ways to make change for 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
            
        res = dp[-1]
        return res if dp[-1] != float('inf') else -1
                

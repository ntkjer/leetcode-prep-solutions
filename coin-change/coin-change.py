class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        seen = {} 
        
        @lru_cache(None)
        def solve(amount):
            if amount < 0:
                return float('inf') 
            
            if amount == 0:
                return 0

            res = float('inf')
            for coin in coins:
                replacement = 1 + solve(amount-coin)
                res = min(res, replacement)
                
            return res
        
        res = solve(amount)
        return res if res != float('inf') else -1
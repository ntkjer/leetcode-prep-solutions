class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

#         @cache #3.9 decorator
#         def solve(amt, idx):
#             if amt == 0:
#                 return 1
# 
#             if amt < 0 or idx < 0:
#                 return 0 
#             
#             return solve(amt - coins[idx], idx) + solve(amt, idx - 1)
#         
# 
        #res = solve(amount, len(coins) - 1)

        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[-1] 

        
        
                   
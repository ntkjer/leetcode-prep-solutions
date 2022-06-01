class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = float('-inf')
        buy = prices[0]
        
        for price in prices[1:]:
            curr = price - buy
            
            profit = max(profit, curr)
            
            if price < buy:
                buy = price
        
        return profit if profit >= 0 else 0
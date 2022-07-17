class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        buy = prices[0]
        res = float('-inf')
        
        for price in prices[1:]:
            res = max(res, price - buy)
            if price < buy:
                buy = price
                
        return res if res > 0 else 0
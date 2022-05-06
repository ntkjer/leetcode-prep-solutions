class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy_idx = 0
        
        for i in range(1, len(prices)):
            if prices[buy_idx] < prices[i]:
                res = max(res, prices[i] - prices[buy_idx])
            else:
                buy_idx = i
                
        return res
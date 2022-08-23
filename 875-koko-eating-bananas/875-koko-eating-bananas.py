class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        lo, hi = 1, max(piles)
        res = float('inf')
        while lo <= hi:
            k = (hi + lo) // 2
            bananas = 0
            
            for pile in piles:
                bananas += math.ceil(pile / k)
            
            if bananas <= h:
                res = min(res, k)
                hi = k - 1
            else:    
                lo = k + 1
        return res
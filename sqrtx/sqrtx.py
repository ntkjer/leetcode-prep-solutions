class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x // 2
        if x < 2:
            return x
        
        while start <= end:
            mid = start + (end - start) // 2
            k = mid * mid
            if k == x:
                return mid
            elif k > x:
                end = mid - 1
            else:
                start = mid + 1
                
        return end
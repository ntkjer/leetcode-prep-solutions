class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        
        right = [0] * (len(ranges))
        
        for i, dist in enumerate(ranges):
            left = max(0, i - dist)
            right[left] = max(right[left], dist + i)
        
   
        
        end = 0
        taps = 0
        start = 0
        while end < n:
            start, end = end + 1, max(right[start: end + 1])
            
            if start > end: 
                return - 1
            
            taps += 1
            
        return taps
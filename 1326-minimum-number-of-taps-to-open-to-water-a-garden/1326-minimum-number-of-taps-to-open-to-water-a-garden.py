class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        
        maxRanges = [0] * len(ranges)
        
        for i, r in enumerate(ranges):
            leftMost = max(0, i - r)
            rightMost = max(maxRanges[leftMost], i + r)
        
            maxRanges[leftMost] = rightMost
        
               
        end = 0
        taps = 0
        furthest = 0
        
        for i, r in enumerate(maxRanges):
            if end == n:
                break
            
            if i > end:
                return -1
            
            furthest = max(r, furthest)
            
            if end == i:
                taps += 1
                end = furthest
        
        return taps
        
        
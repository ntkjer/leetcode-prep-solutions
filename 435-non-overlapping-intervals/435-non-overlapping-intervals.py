class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        res = 0
        intervals.sort()
        prev = intervals[0]
        for interval in intervals[1:]:
            
            start, end = interval
            if start >= prev[1]:   
                prev = interval
            else:
                res += 1    
                prev = [max(start, prev[0]), min(end, prev[1])]
            
        return res
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        
        intervals.sort()
        prev = intervals[0]
        for start, end in intervals[1:]:
            # 1,2 
            # 1,3
            # 2,3
            
            if start >= prev[1]:
                prev = [start, end]
            else:
                res += 1
                prev = [max(start, prev[0]), min(end, prev[1])]
            
        return res
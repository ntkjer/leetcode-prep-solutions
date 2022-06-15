class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort()
        prev = intervals[0][1]
        
        for interval in intervals[1:]:
            if interval[0] >= prev:
                prev = interval[1]
            else:
                count += 1
                prev = min(prev, interval[1])
        return count
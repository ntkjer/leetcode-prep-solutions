class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = intervals[0]
        count = 0
        for interval in intervals[1:]:
            if interval[0] >= prev[1]:
                prev = interval
            else:
                count += 1
                prev = [min(interval[0], prev[0]), min(interval[1], prev[1])]
                
        return count
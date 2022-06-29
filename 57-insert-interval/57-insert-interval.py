class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx = 0
        res = []
        while idx < len(intervals) and intervals[idx][1] < newInterval[0]:
            res.append(intervals[idx])
            idx += 1
        
        while idx < len(intervals):
            if intervals[idx][1] <= newInterval[1] or intervals[idx][0] <= newInterval[1]:
                newInterval = [min(intervals[idx][0], newInterval[0]), max(intervals[idx][1], newInterval[1])]
                idx += 1
            else:
                break
        
        return res + [newInterval] + intervals[idx:]
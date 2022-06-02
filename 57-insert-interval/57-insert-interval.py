class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort()
        
        i = 0
        n = len(intervals)
        res = list()
        
        while i < n and newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
            i += 1

        
        while i < n:
            if intervals[i][0] <= newInterval[0] <= intervals[i][1] or newInterval[0] <= intervals[i][0] <= newInterval[1]:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                i += 1
            else:
                break
        
        return res + [newInterval] + intervals[i:] 
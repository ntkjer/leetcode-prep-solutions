class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx = 0
        N = len(intervals)
        res = list()
        while idx < N and newInterval[0] > intervals[idx][1]:
            res.append(intervals[idx])
            idx += 1
        
        while idx < N:
            if (intervals[idx][1] <= newInterval[1] or intervals[idx][0] <= newInterval[1]):
                newInterval = min(newInterval[0], intervals[idx][0]), max(newInterval[1], intervals[idx][1])
                idx += 1
            else:
                break
        
        return res + [newInterval] + intervals[idx:]
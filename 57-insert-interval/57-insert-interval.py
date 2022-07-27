class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        N = len(intervals)
        res = list()
        idx = 0
        
        while idx < N and newInterval[0] > intervals[idx][1]:
            res.append(intervals[idx])
            idx += 1
            
        # intervals are now intersecting
        while idx < N and newInterval[1] >= intervals[idx][0]:
            newInterval = [min(newInterval[0], intervals[idx][0]), max(newInterval[1], intervals[idx][1])]
            idx += 1
        
        
        
        return res + [newInterval] + intervals[idx:]
        
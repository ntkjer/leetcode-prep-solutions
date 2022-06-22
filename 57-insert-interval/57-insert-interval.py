class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        idx = 0
        while idx < len(intervals) and newInterval[0] > intervals[idx][1]:
            res.append(intervals[idx])
            idx += 1
            
        
        while idx < len(intervals):
            if intervals[idx][0] > newInterval[1]:
                break
            else:
                newInterval = [min(newInterval[0], intervals[idx][0]), max(newInterval[1], intervals[idx][1])]
                idx += 1
            
        return res + [newInterval] + intervals[idx:]
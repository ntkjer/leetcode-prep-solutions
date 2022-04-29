class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        N = len(intervals)
        idx = 0
        result = list()
        
        while idx < N and newInterval[0] > intervals[idx][1]:
            result.append(intervals[idx])
            idx += 1
        
        while idx < N and newInterval[1] >= intervals[idx][0]:
            newInterval[0] = min(intervals[idx][0], newInterval[0])
            newInterval[1] = max(intervals[idx][1], newInterval[1])
            idx += 1
            
        return result + [newInterval] + intervals[idx:] 
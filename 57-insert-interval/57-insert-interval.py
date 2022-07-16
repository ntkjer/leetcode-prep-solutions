class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx = 0
        N = len(intervals)
        
        res = list()
        while idx < N and newInterval[0] > intervals[idx][1]:
            res.append(intervals[idx])
            idx += 1
        
        # intervals at the intersection point
        # new = [2, 5], curr = [1, 3]
        # intervals[idx][0] <= newInterval[0] <= intervals[idx][1]
        # new  = [4, 8]
        # rest = [3, 5], [6, 7], [8, 10]
        # new'  = [3, 8] -> (min_x, max_y)
        # new'' = [3, 8] because newY > intervals[idx][1], skip that last we already overlap
        # new''' = [3, 10] necause newY >= intervals[idx][0]
        
        while idx < N and (newInterval[1] >= intervals[idx][0]):
            newInterval = [min(newInterval[0], intervals[idx][0]), max(newInterval[1], intervals[idx][1])]
            idx += 1
       
        return res + [newInterval] + intervals[idx:]
        
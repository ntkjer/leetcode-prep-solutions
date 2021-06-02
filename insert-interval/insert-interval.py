class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
         
        intervals.append(newInterval)
        intervals.sort()

        res = [intervals[0]]

        for interval in intervals[1:]:
            if res[-1][1] >= interval[0]:
                res[-1][1] = max(interval[1], res[-1][1])
            else:
                res.append(interval)
                
        return res
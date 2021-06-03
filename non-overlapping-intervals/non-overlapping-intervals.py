class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # an overlapping interval 
        num_overlapping = 0
        intervals.sort(key = lambda i: i[1])
        
        last_endpoint = intervals[0][1]
         
        for interval in intervals[1:]:
            if interval[0] >= last_endpoint:
                last_endpoint = interval[1]
                num_overlapping += 1
                
        return len(intervals) - num_overlapping - 1
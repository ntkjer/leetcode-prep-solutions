class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        
        intervals.sort(key = lambda x: x[0])    
        
        count = 1 #we can attend at least one to start!
        res = [intervals[0]]
    
        for interval in intervals[1:]:
            if res[-1][1] > interval[0]:
                return False
            res.append(interval)
        return True
        
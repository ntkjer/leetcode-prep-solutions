class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda interval: interval[0])
        
        start, end = intervals[0]
        for i in range(1, len(intervals)):

            start = intervals[i][0]
            if end > start:
                return False
            end = intervals[i][1] 
            
        return True
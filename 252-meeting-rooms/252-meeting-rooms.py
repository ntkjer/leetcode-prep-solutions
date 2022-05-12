class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort()
        prevStart, prevEnd = intervals[0]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevStart, prevEnd = start, end 
            else:
                return False
        return True
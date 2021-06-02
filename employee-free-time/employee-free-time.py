"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        events = []
        OPEN, CLOSED = 0, 1

        for emp in schedule:
            for interval in emp:
                events.append([interval.start, OPEN])
                events.append([interval.end, CLOSED])
        
        events.sort()
        bal = 0
        result = []
        prev_time = None

        for time, status in events:
            if prev_time and bal == 0:
                result.append(Interval(prev_time, time))

            if status is OPEN:
                bal += 1
            elif status is CLOSED:
                bal -= 1
            
            prev_time = time

        return result
            
            
        
        
            
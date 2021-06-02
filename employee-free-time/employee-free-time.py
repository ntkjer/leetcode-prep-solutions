"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        """

        Two solutions:
        >First is the interval line sweep approach:
            Tn = O(nlgn)  -> runtime dominated by sorting and greedy approach
            Sn = O(n)     -> we store all employee intervals N
        
        > Second solution is optimal and utilizes a min-heap
            Tn = O(n lg k) -> where n is num of employees, k is the number of events
            Sn = O(n)
        """
#         events = []
#         OPEN, CLOSED = 0, 1
# 
#         for emp in schedule:
#             for interval in emp:
#                 events.append([interval.start, OPEN])
#                 events.append([interval.end, CLOSED])
#         
#         events.sort()
#         bal = 0
#         result = []
#         prev_time = None
# 
#         for time, status in events:
#             if prev_time and bal == 0:
#                 result.append(Interval(prev_time, time))
# 
#             if status is OPEN:
#                 bal += 1
#             elif status is CLOSED:
#                 bal -= 1
#             
#             prev_time = time
# 
        heap = [(i.start, i.end) for emp in schedule for i in emp] 
        heapq.heapify(heap)

        res = []
        prev = None

        while heap:
            time = heappop(heap)
            if prev: 
                if prev < time[0]:
                    res.append(Interval(prev, time[0]))

                prev = max(time[1], prev)

            else:
                prev = time[1]
            
        return res
            
            
        
        
            
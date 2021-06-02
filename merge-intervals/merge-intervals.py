class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Solutions overview:
            1. Interval line sweep, same approach as employee free time.

               We reverse the logic and merge all occupied time.
               O(n lg k)

            2. Direct solve
               Simple but tricky edge-cases. 
               O(n)

            3. Heap, O(n lg k).
               
        """
#       # Solution 1.
#        balance = 0
#        OPEN, CLOSED = 0, 1
#        events = list() 
#        res = list()
#
#        for interval in intervals:
#            start, end = interval[0], interval[1]
#            events.append([start, OPEN])
#            events.append([end, CLOSED])
#        
#        events.sort()
#        prev = None 
#
#        start, end = None, None
#
#        for time, state in events:
#            if balance == 0:
#                prev = time
#
#            balance += 1 if state is OPEN else -1
#
#            if balance == 0:
#                res.append([prev, time])
#    
        
#        # solution 3.
#        if len(intervals) <= 1:
#            return intervals
#
#        heapify(intervals)
#        current = heappop(intervals)
#        res = [current]
#        
#        while intervals:
#            next_interval = heappop(intervals) 
#            current = res[-1] 
#            if next_interval[1] <= current[1] or next_interval[0] <= current[1]:
#                current[1] = max(next_interval[1], current[1])
#            else:
#                current = next_interval
#                res.append(current)
#
        # sol 2 -> direct
        
        intervals.sort(key=lambda i:i[0])
        result = list()
        result.append(intervals[0])
        
        for interval in intervals[1:]:
            if result[-1][1] >= interval[0] or result[-1][1] >= interval[1]:
                result[-1][1] = max(interval[1], result[-1][1])
            else:
                result.append(interval)

        return result
            
                

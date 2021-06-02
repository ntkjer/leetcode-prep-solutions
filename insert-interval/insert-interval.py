class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Solution 1:
            Tn = O(n lg n), dominated by sorting.
            Sn = O(n) 
            
            Convenient but too much work for inserting one interval. 

        Solution 2, optimal:
            Tn = O(n)
            Sn = O(n)
            
            Iterate through intervals with idx, where newInterval.start > intervals[i][1]
                append interval[i] to res
                idx += 1

            Insert new at idx
            Insert remaining intervals from idx < N 
           
        Solution 3: Interval line sweep/min-heap

        Solution 4: Binary Search to find location of s,e for newInterval in all intervals
                    Return intervals[:s] + newInterval + intervals[e:]

                    Tn = O(lg n)
        """  
#        
#        # (1.)
#        intervals.append(newInterval)
#        intervals.sort()
#
#        res = [intervals[0]]
#
#        for interval in intervals[1:]:
#            if res[-1][1] >= interval[0]:
#                res[-1][1] = max(interval[1], res[-1][1])
#            else:
#                res.append(interval)
#        
#       # (3.)
#        pq, res = list(), list()
#        for start, end in intervals + [newInterval]:
#            heapq.heappush(pq, (start, -1))
#            heapq.heappush(pq, (end, 1))
#        
#        bal, prev = 0, None
#        while pq:
#            time, status = heapq.heappop(pq)
#            if not prev:
#                prev = time
#
#            bal += status
#            if not bal:
#                res.append([prev, time])
#                prev = None
#        return res     

        # (2.)
        idx = 0
        N = len(intervals)
        res = list() 

        while idx < N and newInterval[0] > intervals[idx][1]:
            res.append(intervals[idx])
            idx += 1
        
        #merge overlapping
        while idx < N and (newInterval[1] >= intervals[idx][0]):
            newInterval[0] = min(newInterval[0], intervals[idx][0])
            newInterval[1] = max(newInterval[1], intervals[idx][1])
            idx += 1

        return res + [newInterval] + intervals[idx:]

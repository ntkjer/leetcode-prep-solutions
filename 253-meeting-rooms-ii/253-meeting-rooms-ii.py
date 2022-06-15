import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        heap = []        
        
        for interval in sorted(intervals):
            if heap and interval[0] >= heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, interval[1])
            else:
                heapq.heappush(heap, interval[1])
        
        

        return len(heap)
            
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        for start, end in sorted(intervals):
            if not heap:
                heappush(heap, end)
                continue
            elif start >= heap[0]:
                heappop(heap)
                
            heappush(heap, end)
            
        
        return len(heap)
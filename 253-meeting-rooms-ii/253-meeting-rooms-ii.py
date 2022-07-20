class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        intervals.sort()
        for start, end in intervals:
            if not heap:
                heappush(heap, end)
                continue
            if start >= heap[0]:
                heappop(heap)
            heappush(heap, end)
            
        return len(heap)
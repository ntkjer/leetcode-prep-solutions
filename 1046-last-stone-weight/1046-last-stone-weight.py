class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            x, y = -heapq.heappop(heap), -heapq.heappop(heap)
            if x == y:
                continue
            else:
                curr = x - y
                heapq.heappush(heap, -curr)
        
        return -heap[0] if heap else 0
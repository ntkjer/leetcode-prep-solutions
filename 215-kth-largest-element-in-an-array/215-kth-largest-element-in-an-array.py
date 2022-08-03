class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        
        heap = [] # max_heap, nums are negated
        
        for num in nums:
            heappush(heap, -num)
        
        res = None
        while heap and k:
            res = -1 * heapq.heappop(heap)
            k -= 1
        
        return res
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or not k:
            return []
            
        heap = [] # max-heap (negative magnitude)
        
        res = list()
        counts = {}
        # [1, 1, 1, 2, 2, 3] 
        # 3: 1
        # 2: 2
        # 1: 3
        
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for num, freq in counts.items():

            heapq.heappush(heap, (-freq, num))
        
        
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
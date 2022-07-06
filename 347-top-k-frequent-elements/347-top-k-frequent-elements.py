class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        for num in counter:
            heappush(heap, (-counter[num], num))
        
        
        res = list()
        while len(res) < k:
            res.append(heappop(heap)[1])
        
        return res
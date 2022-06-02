class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        nums = collections.Counter(nums)
        
        for num in nums:
            heapq.heappush(heap, (-nums[num], num))
    
        result = []
        
        while k != 0:
            curr = heapq.heappop(heap)
            result.append(curr[1])    
            k -= 1
        
        return result
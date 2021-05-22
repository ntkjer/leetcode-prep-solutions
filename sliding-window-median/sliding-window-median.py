class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small = [] #maxheap
        large = [] #minheap
        
        for i in range(k):
            if len(small) == len(large):
                heappush(large, -heappushpop(small, -nums[i]))
            else:
                heappush(small, -heappushpop(large, nums[i]))
        
        res = [float(large[0])] if k & 1 else [(large[0] - small[0])/2]

        to_remove = {}
        
        for i in range(len(nums)):
            to_remove[nums[i]] = 0

        for i in range(k, len(nums)):
            heappush(small, -heappushpop(large, nums[i]))

            evict = nums[i - k]
            
            to_remove[evict] += 1

            if evict > -small[0]:
                # check if item to remove is in large and if so
                # we pop an element from small to maintain at balanced heaps 
                # or in the worst case, large has +1 elems
                heappush(large, -heappop(small))
            
            while small and to_remove[-small[0]]:
                to_remove[-small[0]] -= 1
                heappop(small)
            
            while large and to_remove[large[0]]:
                to_remove[large[0]] -= 1
                heappop(large)
            
            res.append(float(large[0]) if k & 1 else ((large[0]) - small[0]) / 2)
            
        return res
        
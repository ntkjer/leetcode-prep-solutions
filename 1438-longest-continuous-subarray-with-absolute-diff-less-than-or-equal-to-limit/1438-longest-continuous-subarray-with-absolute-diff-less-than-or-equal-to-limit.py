class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        max_d = collections.deque()
        min_d = collections.deque()
        res = 0
        l = 0
        
        for r in range(len(nums)):
            curr = nums[r]
            
            while max_d and curr > max_d[-1]:
                max_d.pop()
            while min_d and curr < min_d[-1]:
                min_d.pop()
                
            max_d.append(curr)
            min_d.append(curr)
            
            
            while max_d[0] - min_d[0] > limit:
                start = nums[l]
                
                if max_d[0] == start:
                    max_d.popleft()
                if min_d[0] == start:
                    min_d.popleft()
                
                l += 1
                
                
            res = max(res, r - l + 1)
        return res
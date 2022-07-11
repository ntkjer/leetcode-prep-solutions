class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        q = collections.deque()
        res = list()
        r = 0
        l = 0
        n = len(nums)
        while r < n:
            
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)
            
            if l > q[0]:
                q.popleft()
            
            if (r - l + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            
            r += 1
        return res 
class Solution:
    def minDays(self, n: int) -> int:
    
        q = collections.deque()
        seen = set()
        
        q.append(n)
        
        days = 0
        
        while q:
            levels = len(q)
            days += 1
            for _ in range(levels):
                curr = q.popleft()
                if curr % 2 == 0 and curr // 2 not in seen:
                    q.append(curr // 2)
                    seen.add(curr // 2)
                if curr % 3 == 0 and curr // 3 not in seen:
                    q.append(curr // 3)
                    seen.add(curr // 3)
                if curr - 1 not in seen:
                    q.append(curr - 1)
                    seen.add(curr - 1)
                if curr - 1 == 0:
                    return days
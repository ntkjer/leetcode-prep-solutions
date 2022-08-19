class Solution:
    def minDays(self, n: int) -> int:
        q = collections.deque()
        
        q.append(n)
        days = 0
        seen = set()
        while q:
            levels = len(q)
            days += 1
            for _ in range(levels):
                oranges = q.popleft()
                
                if oranges % 2 == 0 and oranges % 2 not in seen:
                    q.append(oranges // 2)
                    seen.add(oranges // 2)
                    
                if oranges % 3 == 0 and oranges % 3 not in seen:
                    q.append(oranges // 3)
                    seen.add(oranges // 3)
                    
                if oranges - 1 not in seen:
                    q.append(oranges - 1)
                    
                if oranges - 1 == 0:
                    return days
                
        
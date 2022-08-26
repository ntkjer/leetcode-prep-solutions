class Solution:
    def minDays(self, n: int) -> int:
    
        days = 0
        seen = set()
        
        q = collections.deque()
        q.append(n)
        
        while q:
            days += 1
                        
            for _ in range(len(q)):
                oranges = q.popleft()
                if not oranges - 1:
                    return days
                if (oranges - 1 > 0) and (oranges - 1) not in seen:
                    q.append(oranges - 1)
                    seen.add(oranges - 1)

                if (oranges % 2 == 0) and (oranges % 2) not in seen:
                    q.append(oranges // 2)
                    seen.add(oranges // 2)
                if (oranges % 3 == 0) and (oranges % 3) not in seen:
                    q.append(oranges // 3)
                    seen.add(oranges // 3)



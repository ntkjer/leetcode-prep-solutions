class Solution:
    def minDays(self, n: int) -> int:
        
        
        q = collections.deque()
        q.append(n)
        days = 0
        seen = set()
        
        
        while q:
            days += 1
            for _ in range(len(q)):
                num = q.popleft()
                
                if num - 1 == 0:
                    return days
                
                if num % 3 == 0 and num // 3 not in seen:
                    seen.add(num // 3)
                    q.append(num // 3)
                    
                if num % 2 == 0 and num // 2 not in seen:
                    seen.add(num // 2)
                    q.append(num // 2)
                
                if num - 1 > 0 and num - 1 not in seen:
                    seen.add(num - 1)
                    q.append(num - 1)
            
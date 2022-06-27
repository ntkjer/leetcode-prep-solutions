class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        target = collections.Counter(t)
        
        l = 0
        found, desired = 0, len(target)
        res = float('inf'), 0, 0
        
        for r in range(len(s)):
            curr = s[r]
            window[curr] = window.get(curr, 0) + 1
            
            if window[curr] == target[curr]:
                found += 1
            
            while found == desired and l <= r:
                if (r - l + 1) < res[0]:
                    res = (r - l + 1), l, r
                    
                start = s[l]
                window[start] -= 1
                
                if window[start] < target[start]:
                    found -= 1
                
                l += 1
                
        return "" if res[0] == float('inf') else s[res[1]: res[2] + 1]
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        target = collections.Counter(t)
        
        window = {}
        res = [float('inf'), 0, 0] # len(s'), i, j
        desired = len(target)
        found = 0
        l = 0
        max_freq = float('-inf')
        
        for r in range(len(s)):
            curr = s[r]
            window[curr] = window.get(curr, 0) + 1
            
            if curr in target and window[curr] == target[curr]:
                found += 1
            
            while found == desired:
                if (r - l + 1) < res[0]:
                    res = [r - l + 1, l, r]
                
                start = s[l]
                window[start] -= 1
                
                if start in target and window[start] < target[start]:
                    found -= 1
                
                l += 1
                 
        return s[res[1]: res[2] + 1] if res[0] != float('inf') else ""
        
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = collections.Counter(t)
        window = {}
        found = 0
        desired = len(target)
        
        res = [float('inf'), 0, 0]
        l = 0
        for r in range(len(s)):
            curr = s[r]
            window[curr] = window.get(curr, 0) + 1
            
            if curr in target and window[curr] == target[curr]:
                found += 1
            
            while l < len(s) and found == desired:
                if (r - l + 1) < res[0]:
                    res = [(r - l + 1), l, r]
                
                start = s[l]
                window[start] -= 1
                if start in target and window[start] < target[start]:
                    found -= 1
                
                l += 1
        
        
        return "" if res[0] == float('inf') else s[res[1]: res[2] + 1]
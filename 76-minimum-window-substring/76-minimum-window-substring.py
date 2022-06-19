class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        window = {}
        target = Counter(t)
        l = 0
        res = float('inf'), 0, 0
        found, desired = 0, len(target)
        
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1
            
            if char in target and window[char] == target[char]:
                found += 1

            while l <= r and found == desired:

                if (r - l + 1) < res[0]:
                    res = (r - l + 1), l, r
                    
                start = s[l]
                window[start] -= 1
                
                if start in target and window[start] < target[start]:
                    found -= 1
                    
                l += 1
    
        return "" if res[0] == float('inf') else s[res[1]: res[2] + 1]                
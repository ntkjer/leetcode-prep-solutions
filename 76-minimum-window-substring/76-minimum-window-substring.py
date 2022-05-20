class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        window = {}
        target = Counter(t)
        result = float('inf'), 0, 0
        desired, found = len(target), 0
        
        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) +  1
            
            if char in target and window[char] == target[char]:
                found += 1
            
            while l <= r and found == desired:
                if (r - l + 1) < result[0]:
                    result = (r - l + 1), l, r
                    
                start_char = s[l]
                window[start_char] -= 1
                
                if start_char in target and window[start_char] < target[start_char]:
                    found -= 1
                    
                l += 1
        
        return "" if result[0] == float('inf') else s[result[1] : result[2] + 1]
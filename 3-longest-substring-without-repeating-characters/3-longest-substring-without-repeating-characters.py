class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        window = {}
        
        res = 0
        l = 0
        
        for r in range(len(s)):
            curr = s[r]
            window[curr] = window.get(curr, 0) + 1
            while window[curr] > 1:
                start = s[l]
                window[start] -= 1
                
                l += 1
            
            res = max(r - l + 1, res)
        return res
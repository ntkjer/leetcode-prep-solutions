class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        l = 0
        res = 0
        
        for r in range(len(s)):
            curr = s[r]
            window[curr] = window.get(curr, 0) + 1
            
            while l < r and window[curr] > 1:
                start = s[l]
                window[start] -= 1
                l += 1
                
            res = max(res, r - l + 1)
            
        return res
    
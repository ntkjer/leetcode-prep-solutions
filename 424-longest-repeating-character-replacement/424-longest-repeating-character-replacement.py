class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        window = {}
        l = 0
        maxFreq = 0
        res = 0
        
        for r in range(len(s)):
            curr = s[r]
            window[curr] = window.get(curr, 0) + 1
            
            maxFreq = max(maxFreq, window[curr])
            
            while (r - l + 1) - maxFreq > k:
                window[s[l]] -= 1
                l += 1
                
            res = max(res, r - l + 1)
                
        return res
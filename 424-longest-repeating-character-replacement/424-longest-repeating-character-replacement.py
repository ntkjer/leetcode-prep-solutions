class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        window = {}
        maxFreq = 0
        l = 0
        res = 0
        for r in range(len(s)):
            curr = s[r]
            window[curr] = window.get(curr, 0) + 1
            
            maxFreq = max(maxFreq, window[curr])
            
            while l < r and (r - l + 1) - maxFreq > k: 
                start = s[l]
                window[start] -= 1
                l += 1
            
            res = max(r - l + 1, res)
        return res
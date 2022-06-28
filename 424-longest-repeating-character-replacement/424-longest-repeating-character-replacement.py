class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        res = float('-inf')
        
        window = {}
        maxFreq = 0
        
        for r in range(len(s)):
            curr = s[r]
            window[curr] = window.get(curr, 0) + 1
            maxFreq = max(window[curr], maxFreq)
            
            while (r - l + 1) - maxFreq > k:
                start = s[l]
                window[start] -= 1
                l += 1
                
            res = max(res, (r - l + 1))
            
        return res
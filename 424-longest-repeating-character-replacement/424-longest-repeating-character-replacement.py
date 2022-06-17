class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        counts = {}
        res = 0
        maxFreq = 0
        
        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            
            maxFreq = max(maxFreq, counts[s[r]])
            
            while (r - l + 1) - maxFreq > k:
                counts[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
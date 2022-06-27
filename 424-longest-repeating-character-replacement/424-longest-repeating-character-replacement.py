class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        maxFreq = float('-inf')
        res = 0
        l = 0
        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            
            maxFreq = max(maxFreq, counts[s[r]])
            while (r - l + 1 - maxFreq) > k:
                counts[s[l]] -= 1
                l += 1
                
            res = max(res, r - l + 1)
            
        return res
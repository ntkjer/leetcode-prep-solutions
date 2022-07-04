class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        window = {}
        maxFreq = 0
        left = 0
        res = 0
        for right in range(len(s)):
            
            curr = s[right]
            window[curr] = window.get(curr, 0) + 1
            
            maxFreq = max(maxFreq, window[curr])
            
            while left < len(s) and (right - left + 1) - maxFreq > k:
                start = s[left]
                window[start] -= 1
                left += 1
                
            res = max(res, (right - left + 1))
            
        return res
                
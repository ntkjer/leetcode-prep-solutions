class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        d = {}  
        longest = 0
        result = 0

        for i, c in enumerate(s):
            if c in d:
                dup_idx = d[c]
                if dup_idx >= longest:
                    result = max(result, i - longest)   
                    longest = dup_idx + 1
            d[c] = i

        return max(result, len(s) - longest)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        l = 0
        longest = 0
        
        for r in range(len(s)):
            curr = s[r]
            window[curr] = window.get(curr, 0) + 1
            
            while window[curr] > 1:
                window[s[l]] -= 1
                l += 1
                
            longest = max(longest, (r - l + 1))
            
        return longest
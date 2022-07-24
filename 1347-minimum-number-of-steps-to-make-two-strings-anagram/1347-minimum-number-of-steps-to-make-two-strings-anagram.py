class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        freq = [0] * 26
        remove = 0
        
        for c in s:
            freq[ord(c) - ord('a')] += 1
        
        for c in t:
            if freq[ord(c) - ord('a')] > 0:
                freq[ord(c) - ord('a')] -= 1
            else:
                remove += 1
                
        return remove
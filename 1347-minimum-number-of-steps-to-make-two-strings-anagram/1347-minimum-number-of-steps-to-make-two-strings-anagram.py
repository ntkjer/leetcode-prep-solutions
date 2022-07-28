class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        freq = [0] * 26
        
        for c in s:
            freq[ord(c) - ord('a')] += 1
        
        steps = 0
        for c in t:
            if freq[ord(c) - ord('a')] > 0:
                freq[ord(c) - ord('a')] -= 1
            
            else:
                steps += 1
        
        return steps
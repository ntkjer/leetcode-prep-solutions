class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        freq = [0] * 26
        
        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
        steps = 0
        for i in range(len(t)):
            if freq[ord(t[i]) - ord('a')] > 0:
                freq[ord(t[i]) - ord('a')] -= 1
            else:
                steps += 1
        return steps
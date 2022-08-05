class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False
        s1Freq = [0] * 26
        s2Freq = [0] * 26
        
        
        for i in range(len(s1)):
            s1Freq[ord(s1[i]) - ord('a')] += 1
            s2Freq[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(len(s1Freq)):
            if s1Freq[i] == s2Freq[i]:
                matches += 1
                
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            idx = ord(s2[r]) - ord('a')
            s2Freq[idx] += 1
            if s2Freq[idx] == s1Freq[idx]:
                matches += 1
            elif s2Freq[idx] == s1Freq[idx] + 1:
                matches -= 1
            
            
            idx = ord(s2[l]) - ord('a')
            s2Freq[idx] -= 1
            if s2Freq[idx] == s1Freq[idx]:
                matches += 1
            elif s2Freq[idx] == s1Freq[idx] - 1:
                matches -= 1
            
            l += 1
        return matches == 26
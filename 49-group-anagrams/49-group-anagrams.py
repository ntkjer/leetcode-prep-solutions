class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}
        for word in strs:
            freqs = [0] * 26
            for ch in word:
                freqs[ord(ch) - ord('a')] += 1
                
            groups[tuple(freqs)] = groups.get(tuple(freqs), []) + [word]
        
        return groups.values()
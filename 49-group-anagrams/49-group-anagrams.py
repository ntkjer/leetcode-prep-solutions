class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        chars = [0] * 26
        anagrams = {}
        
        for word in strs:
            chars = [0] * 26
            for ch in word:
                chars[ord(ch) - ord('a')] += 1
            anagrams[tuple(chars)] = anagrams.get(tuple(chars), []) + [word]
        
        return anagrams.values()
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        
        
        for word in strs:
            chars = [0] * 26
            for ch in word:
                chars[ord('a') - ord(ch)] += 1
            key = "".join(str(chars))
            if key not in res:
                res[key] = [word]
            else:
                res[key].append(word)
        
        return res.values()
                
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        chars = Counter(s)
        target = Counter(t)
        
        for c in chars:
            if c not in target or target[c] != chars[c]:
                return False
        
        if len(chars) != len(target):
            return False
        
        return True
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) < len(t):
            return self.isAnagram(t, s)
        
        chars = {}
        for c in s:
            chars[c] = chars.get(c, 0) + 1
        
        for c in t:
            if c in chars:
                if chars[c] == 1:
                    chars.pop(c)
                else:
                    chars[c] -= 1
        
        return True if not chars else False
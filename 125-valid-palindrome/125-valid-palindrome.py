class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        pal = []
        for c in s:
            if c.isalnum():
                pal.append(c.lower())
                
 
        l = 0
        r = len(pal) - 1
        while l <= r:
            if pal[l] != pal[r]:
                return False
            l, r = l + 1, r - 1
            
        return True
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def check_pal(s):
            lo, hi = 0, len(s) - 1
         
            while lo < hi:
                if s[lo] != s[hi]:
                    return False
                else:
                    lo = lo + 1
                    hi = hi - 1
            return True
        
        if not s:
            return 0
        elif check_pal(s):
            return 1
        else:
            return 2